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
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from nicegui import ui
from StudentDataGUI.appHelpers.roster import students
from ..appTheming import theme

# --- CONFIGURATION ---
from StudentDataGUI.appHelpers.helpers import dataBasePath
DATABASE_PATH = dataBasePath
KEYBOARDING_PROGRESS_TYPE = "Keyboarding"  # Must match ProgressType.name in DB

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
    """
    Retrieve or create a progress type record in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    name : str
        The name of the progress type.

    Returns
    -------
    int
        The ID of the progress type in the database.
    """
    cur = conn.cursor()
    cur.execute("SELECT id FROM ProgressType WHERE name = ?", (name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Keyboarding skills progression"))
    conn.commit()
    return cur.lastrowid

def create_keyboarding_session(conn: sqlite3.Connection, student_id: int, progress_type_id: int, date: datetime.date, notes: str = None) -> int:
    """
    Create a new keyboarding session record in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    student_id : int
        The ID of the student.
    progress_type_id : int
        The ID of the progress type.
    date : datetime.date
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

def insert_keyboarding_result(conn: sqlite3.Connection, session_id: int, program: str, topic: str, speed: int, accuracy: int, student_name: str, date_val: datetime.date, notes: str = None) -> None:
    """
    Insert a keyboarding result into the database and save a JSON snapshot.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    session_id : int
        The ID of the session.
    program : str
        The keyboarding program used.
    topic : str
        The topic covered during the session.
    speed : int
        The typing speed in words per minute (WPM).
    accuracy : int
        The typing accuracy as a percentage.
    student_name : str
        The name of the student.
    date_val : datetime.date
        The date of the session.
    notes : str, optional
        Additional notes for the session (default is None).

    Returns
    -------
    None
    """
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO KeyboardingResult (session_id, program, topic, speed, accuracy) VALUES (?, ?, ?, ?, ?)",
        (session_id, program, topic, speed, accuracy)
    )
    conn.commit()
    # Save JSON snapshot of the inserted data
    import json
    from datetime import datetime
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    student_dir = Path(DATA_ROOT) / "StudentDataFiles" / student_name
    student_dir.mkdir(parents=True, exist_ok=True)
    json_path = student_dir / f"keyboarding_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    json_data = {
        "student_name": student_name,
        "date": str(date_val),
        "program": program,
        "topic": topic,
        "speed": speed,
        "accuracy": accuracy,
        "notes": notes,
    }
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)

    # Append data to KeyboardingSkillsProgression.csv
    import csv
    keyboarding_csv_path = student_dir / "KeyboardingSkillsProgression.csv"
    header = ["date", "program", "topic", "speed", "accuracy", "notes"]
    row = [date_val, program, topic, speed, accuracy, notes]
    write_header = not keyboarding_csv_path.exists()  # Write header only if file doesn't exist
    with open(keyboarding_csv_path, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(header)
        writer.writerow(row)

def fetch_keyboarding_data_for_student(conn: sqlite3.Connection, student_id: int, progress_type_id: int) -> pd.DataFrame:
    """
    Returns a DataFrame with columns: date, program, topic, speed, accuracy
    """
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
    format_ids = ','.join('?' for _ in session_ids)
    cur.execute(
        f"""
        SELECT kr.session_id, kr.program, kr.topic, kr.speed, kr.accuracy
        FROM KeyboardingResult kr
        WHERE kr.session_id IN ({format_ids})
        """,
        session_ids
    )
    rows = cur.fetchall()
    # Build DataFrame
    data = []
    for row in rows:
        session_id, program, topic, speed, accuracy = row
        data.append({
            "date": session_dates[session_id],
            "program": program,
            "topic": topic,
            "speed": speed,
            "accuracy": accuracy
        })
    df = pd.DataFrame(data)
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
    return df

# --- UI LOGIC ---

def keyboarding_skills_ui() -> None:
    with theme.frame("- KEYBOARDING SKILLS -"):
        with ui.card():
            ui.label("Keyboarding Skills (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.select(options=students, label="Student Name").style("width: 500px")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
        program_input = ui.select(
            options=[
                "Typio", "TypeAbility", "APH Typer", "Typing Club", "MonkeyType", "Custom Assignment"
            ],
            label="Keyboarding Program"
        ).style("width: 500px;")
        topic_input = ui.select(
            options=[
                "Home Row", "Top Row", "Bottom Row", "Numbers", "Modifier Keys", "F-Keys", "Shortcut Keystrokes"
            ],
            label="Topic Covered"
        ).style("width: 500px;")
        speed_input = ui.number(label="Typing Speed (WPM)", value=0, min=0, max=200, step=1).style("width: 500px;")
        accuracy_input = ui.number(label="Typing Accuracy (%)", value=0, min=0, max=100, step=1).style("width: 500px;")
        notes_input = ui.textarea("Notes (optional)").style("width: 500px;")

        def save_keyboarding_data():
            name = student_name.value.strip()
            date_val = date_input.value
            program = program_input.value
            topic = topic_input.value
            speed = speed_input.value
            accuracy = accuracy_input.value
            notes = notes_input.value.strip()
            if not name or not date_val or not program or not topic:
                ui.notify("Student name, date, program, and topic are required.", type="negative")
                return
            # Connect and insert
            conn = get_connection()
            try:
                student_id = get_or_create_student(conn, name)
                progress_type_id = get_progress_type_id(conn, KEYBOARDING_PROGRESS_TYPE)
                session_id = create_keyboarding_session(conn, student_id, progress_type_id, date_val, notes)
                insert_keyboarding_result(conn, session_id, program, topic, speed, accuracy, name, date_val, notes)
                ui.notify("Keyboarding data saved successfully and appended to CSV!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save Keyboarding Data", on_click=save_keyboarding_data, color="primary")

        def plot_keyboarding_data():
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
                progress_type_id = get_progress_type_id(conn, KEYBOARDING_PROGRESS_TYPE)
                df = fetch_keyboarding_data_for_student(conn, student_id, progress_type_id)
                if df.empty:
                    ui.notify("No keyboarding data for this student.", type="warning")
                    return

                # Print dataframe to terminal for debugging
                print(f"Data plotted for student: {name}")
                print(df.to_string())
                # Plotting
                fig = make_subplots(
                    rows=2, cols=1,
                    subplot_titles=["Typing Speed (WPM)", "Typing Accuracy (%)"]
                )
                fig.add_trace(
                    go.Scatter(
                        x=df['date'],
                        y=df['speed'],
                        mode="lines+markers",
                        name="Speed (WPM)",
                        text=df['program'] + " - " + df['topic'],
                        hovertemplate="Date: %{x}<br>Speed: %{y} WPM<br>%{text}"
                    ),
                    row=1, col=1
                )
                fig.add_trace(
                    go.Scatter(
                        x=df['date'],
                        y=df['accuracy'],
                        mode="lines+markers",
                        name="Accuracy (%)",
                        text=df['program'] + " - " + df['topic'],
                        hovertemplate="Date: %{x}<br>Accuracy: %{y}%<br>%{text}"
                    ),
                    row=2, col=1
                )
                fig.update_layout(
                    template="simple_white",
                    title_text=f"{name}: Keyboarding Progression",
                    hovermode="x unified"
                )
                tmp_html = Path.home() / "KeyboardingProgression.html"
                fig.write_html(str(tmp_html), auto_open=True)
                ui.notify("Graph generated and opened in browser.", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot Keyboarding Data", on_click=plot_keyboarding_data, color="secondary")

# --- PAGE ENTRY POINT ---
@ui.page("/keyboarding_skills_ui")
def create():
    keyboarding_skills_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
