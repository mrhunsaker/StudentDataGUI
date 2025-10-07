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
import pandas as pd
from nicegui import ui
from StudentDataGUI.appHelpers.helpers import students
from ..appTheming import theme

from StudentDataGUI.appHelpers.helpers import dataBasePath
# Database is now stored in /app_home at the project root
DATABASE_PATH = dataBasePath
OBSERVATION_TYPE = "Observation"  # Must match ProgressType.name in DB

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
    # If not present, create it
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Observation notes"))
    conn.commit()
    return cur.lastrowid

def create_observation_session(conn: sqlite3.Connection, student_id: int, progress_type_id: int, date: str, notes: str | None = None, student_name: str | None = None) -> int:
    """
    Create a new observation session record in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    student_id : int
        The ID of the student.
    progress_type_id : int
        The ID of the progress type.
    date : str
        The date of the observation session.
    notes : str, optional
        Additional notes for the session (default is None).
    student_name : str, optional
        The name of the student (default is None).

    Returns
    -------
    int
        The ID of the newly created observation session.
    """
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    session_id = cur.lastrowid

    # Save JSON snapshot of the inserted data
    import json
    from datetime import datetime
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if student_name:
        student_dir = Path(DATA_ROOT) / "StudentDataFiles" / student_name
        student_dir.mkdir(parents=True, exist_ok=True)
        json_path = student_dir / f"observations_{now}.json"
        json_data = {
            "student_name": student_name,
            "date": date,
            "notes": notes,
        }
        with open(json_path, "w") as f:
            json.dump(json_data, f, indent=2)

    return session_id

def fetch_observations_for_student(conn: sqlite3.Connection, student_id: int, progress_type_id: int) -> pd.DataFrame:
    """
    Fetch observation notes for a specific student.

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
        A DataFrame containing observation notes with columns: date, notes.
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT date, notes FROM ProgressSession WHERE student_id = ? AND progress_type_id = ? ORDER BY date ASC",
        (student_id, progress_type_id)
    )
    rows = cur.fetchall()
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows, columns=["date", "notes"])
    df["date"] = pd.to_datetime(df["date"])
    return df

# --- UI LOGIC ---

def observations_ui():
    with theme.frame("- OBSERVATION NOTES -"):
        ui.label("Observation Notes").classes("text-h4 text-grey-8")
        student_name = ui.select(options=students, label="Student Name").props('aria-describedby=student_name_error').style("width: 500px")
        student_name_error = ui.label("Student name is required.").props('id=student_name_error').classes('text-red-700').style('display:none')
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today()).props('aria-describedby=date_error').style("width: 500px")
        date_error = ui.label("Date is required.").props('id=date_error').classes('text-red-700').style('display:none')
        notes_input = ui.textarea("Observation Notes", placeholder="Type observation notes here...").props('aria-describedby=notes_error').style("width: 500px")
        notes_error = ui.label("Observation notes are required.").props('id=notes_error').classes('text-red-700').style('display:none')

        def save_observation():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
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
            if not notes:
                notes_error.style('display:block')
                notes_input.props('aria-invalid=true')
                if not error_found:
                    notes_input.run_javascript('this.focus()')
                error_found = True
            else:
                notes_error.style('display:none')
                notes_input.props('aria-invalid=false')
            if error_found:
                return
            conn = get_connection()
            try:
                student_id = get_or_create_student(conn, name)
                progress_type_id = get_progress_type_id(conn, OBSERVATION_TYPE)
                create_observation_session(conn, student_id, progress_type_id, date_val, notes)
                ui.notify("Observation note saved successfully!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving observation: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save Observation", on_click=save_observation, color="primary")

        def plot_observations():
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
                progress_type_id = get_progress_type_id(conn, OBSERVATION_TYPE)
                df = fetch_observations_for_student(conn, student_id, progress_type_id)
                if df.empty:
                    ui.notify("No observation notes for this student.", type="warning")
                    return

                # Save the triggering button for focus restoration
                import uuid
                trigger_id = f"trigger-btn-{uuid.uuid4().hex}"
                trigger_btn = ui.query(f'#{trigger_id}')
                # Display as a simple table (could be enhanced to timeline, etc.)
                with ui.dialog().props('role=dialog aria-modal=true').classes('focus:outline-none') as dialog, ui.card():
                    heading = ui.label(f"Observation Notes for {name}").classes("text-h5").props('tabindex=0 id=dialog-heading')
                    for _, row in df.iterrows():
                        ui.markdown(f"**{row['date'].strftime('%Y-%m-%d')}**: {row['notes']}")
                    close_btn = ui.button("Close", on_click=lambda: (dialog.close(), ui.run_javascript(f'document.getElementById("{trigger_id}").focus()')))
                    # Move focus to heading when dialog opens
                    dialog.on('open', lambda: heading.run_javascript('this.focus()'))
                dialog.open()
            except Exception as e:
                ui.notify(f"Error fetching observations: {e}", type="negative")
            finally:
                conn.close()

        # Add an id to the trigger button for focus restoration
        ui.button("Show All Observations", on_click=plot_observations, color="secondary").props('id=trigger-btn-observations')

# --- PAGE ENTRY POINT ---
def create():
    observations_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
