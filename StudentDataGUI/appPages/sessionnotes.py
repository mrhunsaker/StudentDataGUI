#!/usr/bin/env python3

"""
 Copyright 2025  Michael Ryan Hunsaker, M.Ed., Ph.D.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import sqlite3
from pathlib import Path
import datetime
import pandas as pd"""
 Copyright 2025  Michael Ryan Hunsaker, M.Ed., Ph.D.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
from nicegui import ui
from StudentDataGUI.appHelpers.roster import students
from ..appTheming import theme

# --- CONFIGURATION ---
from StudentDataGUI.appHelpers.helpers import dataBasePath
DATABASE_PATH = dataBasePath
SESSION_NOTES_TYPE = "SessionNotes"  # Must match ProgressType.name in DB

# --- UTILITY FUNCTIONS ---

def get_connection() -> sqlite3.Connection:
    """
    Establish a connection to the SQLite database.

    Returns
    -------
    sqlite3.Connection
        A connection object to interact with the SQLite database.
    """
    return sqlite3.connect(DATABASE_PATH)

def get_or_create_student(conn: sqlite3.Connection, name: str) -> int:
    """
    Retrieve or create a student record in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    name : str
        The name of the student.

    Returns
    -------
    int
        The ID of the student in the database.
    """
    cur = conn.cursor()
    cur.execute("SELECT id FROM Student WHERE name = ?", (name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO Student (name) VALUES (?)", (name,))
    conn.commit()
    return cur.lastrowid

def get_progress_type_id(conn: sqlite3.Connection, name: str) -> int:
    cur = conn.cursor()
    cur.execute("SELECT id FROM ProgressType WHERE name = ?", (name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Session notes and anecdotal observations"))
    conn.commit()
    return cur.lastrowid

def create_session(conn: sqlite3.Connection, student_id: int, progress_type_id: int, date: str, notes: str | None = None) -> int:
    """
    Create a new session record in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    student_id : int
        The ID of the student.
    progress_type_id : int
        The ID of the progress type.
    date : str
        The date of the session.
    notes : str, optional
        Additional notes for the session (default is None).

    Returns
    -------
    int
        The ID of the newly created session.
    """
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_trial_results(conn: sqlite3.Connection, session_id: int, task: str, lesson: str, session_label: str, trials: list[tuple[int, int]]) -> None:
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

def insert_session_summary(conn: sqlite3.Connection, session_id: int, median: float, notes: str) -> None:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO TrialSessionSummary (session_id, median, notes) VALUES (?, ?, ?)",
        (session_id, median, notes)
    )
    conn.commit()

def fetch_session_notes_for_student(conn: sqlite3.Connection, student_id: int, progress_type_id: int) -> pd.DataFrame:
    """
    Fetch session notes and trial results for a student.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    student_id : int
        The ID of the student.
    progress_type_id : int
        The ID of the progress type.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns: date, notes, median, trial_1, ..., trial_11.
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

def session_notes_ui() -> None:
    with theme.frame("- SESSION NOTES -"):
        ui.label("Session Notes (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.select(options=students, label="Student Name").props('aria-describedby=student_name_error').style("width: 500px")
        student_name_error = ui.label("Student name is required.").props('id=student_name_error').classes('text-red-700').style('display:none')
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today()).props('aria-describedby=date_error').style("width: 500px")
        date_error = ui.label("Date is required.").props('id=date_error').classes('text-red-700').style('display:none')
        task_input = ui.input("Task", placeholder="Task or activity (optional)").style("width: 500px")
        lesson_input = ui.input("Lesson", placeholder="Lesson (optional)").style("width: 500px")
        session_label_input = ui.input("Session Label", placeholder="Session label (optional)").style("width: 500px")
        notes_input = ui.textarea("Anecdotal Notes", placeholder="Enter session notes here").style("width: 500px")
        trial_inputs = []
        for i in range(1, 12):
            trial_inputs.append(ui.number(label=f"Trial {i}", value=0, min=0, max=3, step=1).style("width: 500px"))
        median_input = ui.number("Median (optional)", value=None).style("width: 500px")
        summary_notes_input = ui.textarea("Summary Notes (optional)", placeholder="Enter summary notes here").style("width: 500px")

        def save_session_notes():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
            task = task_input.value.strip()
            lesson = lesson_input.value.strip()
            session_label = session_label_input.value.strip()
            median = median_input.value
            summary_notes = summary_notes_input.value.strip()
            error_found = False
            if not name:
                student_name_error.style('display:block')
                student_name.props('aria-invalid=true')
                student_name.run_javascript('this.focus()')
                error_found = True
            else:
                student_name_error.style('display:none')
                student_name.props('aria-invalid=false')
            if not date_val:
                date_error.style('display:block')
                date_input.props('aria-invalid=true')
                if not error_found:
                    date_input.run_javascript('this.focus()')
                error_found = True
            else:
                date_error.style('display:none')
                date_input.props('aria-invalid=false')
            if error_found:
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
