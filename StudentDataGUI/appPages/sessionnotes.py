#!/usr/bin/env python3

"""
Session Notes Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads session notes using normalized tables and foreign keys
"""

import sqlite3
from pathlib import Path
import datetime
import pandas as pd
from nicegui import ui

# --- CONFIGURATION ---
DATABASE_PATH = "/home/ryhunsaker/Documents/StudentDatabase/students20252026.db"
SESSION_NOTES_TYPE = "SessionNotes"  # Must match ProgressType.name in DB

# --- UTILITY FUNCTIONS ---

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def get_or_create_student(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT id FROM Student WHERE name = ?", (name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO Student (name) VALUES (?)", (name,))
    conn.commit()
    return cur.lastrowid

def get_progress_type_id(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT id FROM ProgressType WHERE name = ?", (name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Session notes and anecdotal observations"))
    conn.commit()
    return cur.lastrowid

def create_session(conn, student_id, progress_type_id, date, notes=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_trial_results(conn, session_id, task, lesson, session_label, trials):
    """
    trials: list of (trial_number, score)
    """
    cur = conn.cursor()
    for trial_number, score in trials:
        cur.execute(
            "INSERT INTO TrialResult (session_id, task, lesson, session_label, trial_number, score) VALUES (?, ?, ?, ?, ?, ?)",
            (session_id, task, lesson, session_label, trial_number, score)
        )
    conn.commit()

def insert_session_summary(conn, session_id, median, notes):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO TrialSessionSummary (session_id, median, notes) VALUES (?, ?, ?)",
        (session_id, median, notes)
    )
    conn.commit()

def fetch_session_notes_for_student(conn, student_id, progress_type_id):
    """
    Returns a DataFrame with columns: date, notes, median, trial_1, ..., trial_11
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT id, date, notes FROM ProgressSession WHERE student_id = ? AND progress_type_id = ? ORDER BY date ASC",
        (student_id, progress_type_id)
    )
    sessions = cur.fetchall()
    if not sessions:
        return pd.DataFrame()
    session_ids = [sid for sid, _, _ in sessions]
    session_dates = {sid: date for sid, date, _ in sessions}
    session_notes = {sid: notes for sid, _, notes in sessions}
    # Get all trial results for these sessions
    cur.execute(
        f"""
        SELECT session_id, trial_number, score
        FROM TrialResult
        WHERE session_id IN ({','.join('?' for _ in session_ids)})
        """,
        session_ids
    )
    rows = cur.fetchall()
    # Get session summaries
    cur.execute(
        f"""
        SELECT session_id, median, notes
        FROM TrialSessionSummary
        WHERE session_id IN ({','.join('?' for _ in session_ids)})
        """,
        session_ids
    )
    summaries = {sid: (median, notes) for sid, median, notes in cur.fetchall()}
    # Build DataFrame
    data = {}
    for sid in session_ids:
        data[sid] = {'date': session_dates[sid], 'notes': session_notes[sid]}
        # Add summary if present
        if sid in summaries:
            data[sid]['median'] = summaries[sid][0]
            data[sid]['summary_notes'] = summaries[sid][1]
        else:
            data[sid]['median'] = None
            data[sid]['summary_notes'] = None
        # Add trials
        for t in range(1, 12):
            data[sid][f"trial_{t}"] = None
    for sid, trial_number, score in rows:
        data[sid][f"trial_{trial_number}"] = score
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df['date'])
    return df

# --- UI LOGIC ---

def session_notes_ui():
    with ui.card():
        ui.label("Session Notes (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
        task_input = ui.input("Task", placeholder="Task or activity (optional)")
        lesson_input = ui.input("Lesson", placeholder="Lesson (optional)")
        session_label_input = ui.input("Session Label", placeholder="Session label (optional)")
        notes_input = ui.textarea("Anecdotal Notes", placeholder="Enter session notes here")
        trial_inputs = []
        for i in range(1, 12):
            trial_inputs.append(ui.number(label=f"Trial {i}", value=0, min=0, max=3, step=1))
        median_input = ui.number("Median (optional)", value=None)
        summary_notes_input = ui.textarea("Summary Notes (optional)", placeholder="Enter summary notes here")

        def save_session_notes():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
            task = task_input.value.strip()
            lesson = lesson_input.value.strip()
            session_label = session_label_input.value.strip()
            median = median_input.value
            summary_notes = summary_notes_input.value.strip()
            if not name or not date_val:
                ui.notify("Student name and date are required.", type="negative")
                return
            # Connect and insert
            conn = get_connection()
            try:
                student_id = get_or_create_student(conn, name)
                progress_type_id = get_progress_type_id(conn, SESSION_NOTES_TYPE)
                session_id = create_session(conn, student_id, progress_type_id, date_val, notes)
                trials = []
                for idx, inp in enumerate(trial_inputs, 1):
                    score = inp.value
                    trials.append((idx, score))
                insert_trial_results(conn, session_id, task, lesson, session_label, trials)
                if median is not None or summary_notes:
                    insert_session_summary(conn, session_id, median, summary_notes)
                ui.notify("Session notes saved successfully!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save Session Notes", on_click=save_session_notes, color="primary")

        def plot_session_notes():
            name = student_name.value.strip()
            if not name:
                ui.notify("Enter student name to plot.", type="negative")
                return
            conn = get_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT id FROM Student WHERE name = ?", (name,))
                row = cur.fetchone()
                if not row:
                    ui.notify("Student not found.", type="negative")
                    return
                student_id = row[0]
                progress_type_id = get_progress_type_id(conn, SESSION_NOTES_TYPE)
                df = fetch_session_notes_for_student(conn, student_id, progress_type_id)
                if df.empty:
                    ui.notify("No session notes for this student.", type="warning")
                    return

                # Print dataframe to terminal for debugging
                print(f"Data plotted for student: {name}")
                print(df.to_string())
                # Plotting: show trial scores over time
                import plotly.graph_objs as go
                from plotly.subplots import make_subplots
                fig = make_subplots(rows=1, cols=1)
                for t in range(1, 12):
                    col = f"trial_{t}"
                    if col in df.columns:
                        fig.add_trace(
                            go.Scatter(
                                x=df['date'],
                                y=df[col],
                                mode="lines+markers",
                                name=col,
                                hovertemplate=f"{col}: "+"%{y}"
                            )
                        )
                fig.update_layout(
                    template="simple_white",
                    title_text=f"{name}: Session Notes Trials Over Time",
                    hovermode="x unified"
                )
                tmp_html = Path.home() / "SessionNotesProgression.html"
                fig.write_html(str(tmp_html), auto_open=True)
                ui.notify("Graph generated and opened in browser.", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot Session Notes", on_click=plot_session_notes, color="secondary")

# --- PAGE ENTRY POINT ---
@ui.page("/sessionnotes_ui")
def create():
    session_notes_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
