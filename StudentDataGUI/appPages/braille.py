StudentDataGUI/StudentDataGUI/appPages/braille_updated.py
#!/usr/bin/env python3

"""
Braille Skills Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads braille data using normalized tables and foreign keys
"""

import sqlite3
from pathlib import Path
import datetime
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from nicegui import ui

# --- CONFIGURATION ---
DATABASE_PATH = "/home/ryhunsaker/Documents/StudentDatabase/students_bestpractice.db"
BRAILLE_PROGRESS_TYPE = "Braille"  # Must match ProgressType.name in DB

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
    # If not present, create it
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Braille skills progression"))
    conn.commit()
    return cur.lastrowid

def get_braille_parts(conn, progress_type_id):
    """
    Returns a dict mapping code (e.g. 'P1_1') to part_id for Braille assessment.
    If not present, creates the standard set.
    """
    cur = conn.cursor()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    rows = cur.fetchall()
    if rows and len(rows) >= 62:
        return {code: pid for code, pid in rows}
    # If not present, create standard braille parts (based on original schema)
    braille_parts = []
    # Phases 1-8, with variable number of items per phase
    # For brevity, only a subset is shown; expand as needed for your use case
    for phase, count in [
        ("P1", 4), ("P2", 15), ("P3", 15), ("P4", 4), ("P5", 4), ("P6", 7), ("P7", 8), ("P8", 7)
    ]:
        for i in range(1, count+1):
            code = f"{phase}_{i}"
            desc = f"Braille {phase} skill {i}"
            braille_parts.append((code, desc))
    for code, desc in braille_parts:
        cur.execute(
            "INSERT OR IGNORE INTO AssessmentPart (progress_type_id, code, description) VALUES (?, ?, ?)",
            (progress_type_id, code, desc)
        )
    conn.commit()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    return {code: pid for code, pid in cur.fetchall()}

def create_braille_session(conn, student_id, progress_type_id, date, notes=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_braille_results(conn, session_id, part_scores):
    """
    part_scores: dict of {code: score}
    """
    cur = conn.cursor()
    for code, (part_id, score) in part_scores.items():
        cur.execute(
            "INSERT INTO AssessmentResult (session_id, part_id, score) VALUES (?, ?, ?)",
            (session_id, part_id, score)
        )
    conn.commit()

def fetch_braille_data_for_student(conn, student_id, progress_type_id, part_codes):
    """
    Returns a DataFrame with columns: date, code1, code2, ..., codeN
    """
    # Get all sessions for this student and braille
    cur = conn.cursor()
    cur.execute(
        "SELECT id, date FROM ProgressSession WHERE student_id = ? AND progress_type_id = ? ORDER BY date ASC",
        (student_id, progress_type_id)
    )
    sessions = cur.fetchall()
    if not sessions:
        return pd.DataFrame()
    session_ids = [sid for sid, _ in sessions]
    session_dates = {sid: date for sid, date in sessions}
    # Get all results for these sessions
    format_codes = ','.join('?' for _ in part_codes)
    cur.execute(
        f"""
        SELECT ar.session_id, ap.code, ar.score
        FROM AssessmentResult ar
        JOIN AssessmentPart ap ON ar.part_id = ap.id
        WHERE ar.session_id IN ({','.join('?' for _ in session_ids)}) AND ap.code IN ({format_codes})
        """,
        session_ids + list(part_codes)
    )
    rows = cur.fetchall()
    # Build DataFrame
    data = {}
    for sid in session_ids:
        data[sid] = {code: None for code in part_codes}
        data[sid]['date'] = session_dates[sid]
    for sid, code, score in rows:
        data[sid][code] = score
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df['date'])
    return df

# --- UI LOGIC ---

def braille_skills_ui():
    with ui.card():
        ui.label("Braille Skills (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        date_input = ui.date(label="Date", value=datetime.date.today())
        # Braille part codes and labels (expand as needed)
        braille_parts = []
        for phase, count in [
            ("P1", 4), ("P2", 15), ("P3", 15), ("P4", 4), ("P5", 4), ("P6", 7), ("P7", 8), ("P8", 7)
        ]:
            for i in range(1, count+1):
                code = f"{phase}_{i}"
                label = f"{phase} Skill {i}"
                braille_parts.append((code, label))
        part_inputs = {}
        with ui.row():
            for code, label in braille_parts:
                part_inputs[code] = ui.number(label=label, value=0, min=0, max=3, step=1)
        notes_input = ui.input("Notes (optional)", multiline=True)

        def save_braille_data():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
            if not name or not date_val:
                ui.notify("Student name and date are required.", type="negative")
                return
            # Connect and insert
            conn = get_connection()
            try:
                student_id = get_or_create_student(conn, name)
                progress_type_id = get_progress_type_id(conn, BRAILLE_PROGRESS_TYPE)
                part_ids = get_braille_parts(conn, progress_type_id)
                session_id = create_braille_session(conn, student_id, progress_type_id, date_val, notes)
                part_scores = {}
                for code in part_inputs:
                    score = part_inputs[code].value
                    part_scores[code] = (part_ids[code], score)
                insert_braille_results(conn, session_id, part_scores)
                ui.notify("Braille data saved successfully!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save Braille Data", on_click=save_braille_data, color="primary")

        def plot_braille_data():
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
                progress_type_id = get_progress_type_id(conn, BRAILLE_PROGRESS_TYPE)
                part_ids = get_braille_parts(conn, progress_type_id)
                part_codes = list(part_ids.keys())
                df = fetch_braille_data_for_student(conn, student_id, progress_type_id, part_codes)
                if df.empty:
                    ui.notify("No braille data for this student.", type="warning")
                    return
                # Plotting: For demonstration, plot each phase in a subplot
                fig = make_subplots(
                    rows=4, cols=2,
                    subplot_titles=[
                        "Phase 1", "Phase 2", "Phase 3", "Phase 4",
                        "Phase 5", "Phase 6", "Phase 7", "Phase 8"
                    ]
                )
                # Map codes to subplot positions
                phase_map = {
                    "P1": (1, 1), "P2": (1, 2), "P3": (2, 1), "P4": (2, 2),
                    "P5": (3, 1), "P6": (3, 2), "P7": (4, 1), "P8": (4, 2)
                }
                for code in part_codes:
                    phase = code.split("_")[0]
                    row, col = phase_map[phase]
                    fig.add_trace(
                        go.Scatter(
                            x=df['date'],
                            y=df[code],
                            mode="lines+markers",
                            name=code,
                            hovertemplate=f"{code}: "+"%{y}"
                        ),
                        row=row, col=col
                    )
                fig.update_layout(
                    template="simple_white",
                    title_text=f"{name}: Braille Skills Progression",
                    hovermode="x unified"
                )
                # Show in browser or as HTML
                tmp_html = Path.home() / "BrailleSkillsProgression.html"
                fig.write_html(str(tmp_html), auto_open=True)
                ui.notify("Graph generated and opened in browser.", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot Braille Data", on_click=plot_braille_data, color="secondary")

# --- PAGE ENTRY POINT ---
def create():
    braille_skills_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()