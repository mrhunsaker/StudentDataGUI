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
from nicegui import ui
from ..appTheming import theme

from StudentDataGUI.appHelpers.helpers import dataBasePath
# Database is now stored in /app_home at the project root
DATABASE_PATH = dataBasePath
CONTACTLOG_PROGRESS_TYPE = "ContactLog"  # Must match ProgressType.name in DB

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
    Retrieve the student ID for a given name, or create a new student entry if not found.

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
    Retrieve the progress type ID for a given name, or create a new entry if not found.

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
    # If not present, create it
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Contact log entries"))
    conn.commit()
    return cur.lastrowid

def get_contactlog_parts(conn: sqlite3.Connection, progress_type_id: int) -> dict[str, int]:
    """
    Retrieve or create the standard set of contact log parts for a given progress type.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    progress_type_id : int
        The ID of the progress type.

    Returns
    -------
    dict[str, int]
        A dictionary mapping part codes (e.g., 'CONTACT_METHOD') to their corresponding IDs.
    """
    cur = conn.cursor()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    rows = cur.fetchall()
    if rows and len(rows) >= 7:
        return {code: pid for code, pid in rows}
    # If not present, create standard contact log parts
    contactlog_parts = [
        ("CONTACT_METHOD", "Contact Method"),
        ("CONTACT_RESPONSE", "Contact Response"),
        ("CONTACT_GENERAL", "General Topic"),
        ("CONTACT_SPECIFIC", "Specific Topic"),
        ("GUARDIAN_NAME", "Guardian Name"),
        ("PHONE_NUMBER", "Phone Number"),
        ("EMAIL_ADDRESS", "Email Address"),
    ]
    for code, desc in contactlog_parts:
        cur.execute(
            "INSERT OR IGNORE INTO AssessmentPart (progress_type_id, code, description) VALUES (?, ?, ?)",
            (progress_type_id, code, desc)
        )
    conn.commit()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    return {code: pid for code, pid in cur.fetchall()}

def create_contactlog_session(conn: sqlite3.Connection, student_id: int, progress_type_id: int, date: str, notes: str = None) -> int:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_contactlog_results(conn: sqlite3.Connection, session_id: int, part_scores: dict[str, tuple[int, str]], student_name: str, date_val: str, notes: str = None) -> None:
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

    # Append data to ContactLog.csv
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    import csv
    contactlog_csv_path = Path(DATA_ROOT) / "StudentDataFiles" / student_name / "ContactLog.csv"
    contactlog_csv_path.parent.mkdir(parents=True, exist_ok=True)
    # Prepare data for horizontal writing
    header = ["date"] + list(part_scores.keys())
    row = [date_val] + [score for _, score in part_scores.values()]

    # Write data horizontally
    write_header = not contactlog_csv_path.exists()  # Write header only if file doesn't exist
    with open(contactlog_csv_path, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(header)
        writer.writerow(row)
    # Save JSON snapshot of the inserted data
    import json
    from datetime import datetime
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    student_dir = Path(DATA_ROOT) / "StudentDataFiles" / student_name
    student_dir.mkdir(parents=True, exist_ok=True)
    json_path = student_dir / f"contactlog_{now}.json"
    json_path = Path(DATA_ROOT) / "StudentDataFiles" / student_name / f"contactlog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    json_data = {
        "student_name": student_name,
        "date": str(date_val),
        "notes": notes,
        "part_scores": {code: score for code, (part_id, score) in part_scores.items()}
    }
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)

def fetch_contactlog_data_for_student(conn: sqlite3.Connection, student_id: int, progress_type_id: int, part_codes: list[str]) -> pd.DataFrame:
    """
    Returns a DataFrame with columns: date, code1, code2, ..., codeN, notes
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
    data = {}
    for sid in session_ids:
        data[sid] = {code: None for code in part_codes}
        data[sid]['date'] = session_dates[sid]
        data[sid]['notes'] = session_notes[sid]
    for sid, code, value in rows:
        data[sid][code] = value
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df['date']).astype(str)  # Ensure date column is JSON serializable
    return df

# --- UI LOGIC ---

def contactlog_ui():
    with theme.frame("- CONTACT LOG -"):
        ui.label("Contact Log").classes("text-h4 text-grey-8")
        from StudentDataGUI.appHelpers.helpers import students
        student_name = ui.select(options=students, label="Student Name").props('aria-describedby=student_name_error').style("width: 500px;")
        student_name_error = ui.label("Student name is required.").props('id=student_name_error').classes('text-red-700').style('display:none')
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today()).props('aria-describedby=date_error').style("width: 500px;")
        date_error = ui.label("Date is required.").props('id=date_error').classes('text-red-700').style('display:none')
        guardian_name = ui.input("Guardian Name").style("width: 500px;")
        contact_method = ui.select(["Phone", "Text", "In-Person", "Email"], label="Contact Method").style("width: 500px;")
        phone_number = ui.input("Phone Number").style("width: 500px;")
        email_address = ui.input("Email Address").style("width: 500px;")
        contact_response = ui.select(["Answered", "Left Message", "Unable to Leave Message", "Disconnected"], label="Contact Response").style("width: 500px;")
        contact_general = ui.select(["IEP Related", "Discipline Related", "Student Requested"], label="General Topic").style("width: 500px;")
        contact_specific = ui.select(["Schedule IEP Meeting", "IEP Team Follow-Up", "Collaborate on Student IEP Goals", "Progress Monitoring Update"], label="Specific Topic").style("width: 500px;")
        notes_input = ui.textarea("Contact Notes (if email, please copy/paste email here)").style("width: 500px;")

        def save_contactlog_data():
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
            if error_found:
                return
            conn = get_connection()
            try:
                student_id = get_or_create_student(conn, name)
                progress_type_id = get_progress_type_id(conn, CONTACTLOG_PROGRESS_TYPE)
                part_ids = get_contactlog_parts(conn, progress_type_id)
                session_id = create_contactlog_session(conn, student_id, progress_type_id, date_val, notes)
                part_values = {
                    "CONTACT_METHOD": (part_ids["CONTACT_METHOD"], contact_method.value),
                    "CONTACT_RESPONSE": (part_ids["CONTACT_RESPONSE"], contact_response.value),
                    "CONTACT_GENERAL": (part_ids["CONTACT_GENERAL"], contact_general.value),
                    "CONTACT_SPECIFIC": (part_ids["CONTACT_SPECIFIC"], contact_specific.value),
                    "GUARDIAN_NAME": (part_ids["GUARDIAN_NAME"], guardian_name.value),
                    "PHONE_NUMBER": (part_ids["PHONE_NUMBER"], phone_number.value),
                    "EMAIL_ADDRESS": (part_ids["EMAIL_ADDRESS"], email_address.value),
                }
                insert_contactlog_results(conn, session_id, part_values)

                # Append data to ContactLog.csv
                from StudentDataGUI.appHelpers.helpers import DATA_ROOT
                import csv
                contactlog_csv_path = Path(DATA_ROOT) / "StudentDataFiles" / name / "ContactLog.csv"
                contactlog_csv_path.parent.mkdir(parents=True, exist_ok=True)
                # Prepare data for horizontal writing
                header = ["date"] + list(part_values.keys())
                row = [date_val] + [value for _, value in part_values.values()]

                # Write data horizontally
                write_header = not contactlog_csv_path.exists()  # Write header only if file doesn't exist
                with open(contactlog_csv_path, mode="a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    if write_header:
                        writer.writerow(header)
                    writer.writerow(row)

                # Save JSON snapshot of the inserted data
                import json
                from datetime import datetime
                json_path = Path(DATA_ROOT) / "StudentDataFiles" / name / f"contactlog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
                json_data = {
                    "student_name": name,
                    "date": date_val,
                    "notes": notes,
                    "contact_details": {key: value for key, (part_id, value) in part_values.items()}
                }
                with open(json_path, "w") as f:
                    json.dump(json_data, f, indent=2)

                ui.notify("Contact log entry saved successfully and appended to CSV!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save Contact Log Entry", on_click=save_contactlog_data, color="primary")

        def plot_contactlog_data():
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
                progress_type_id = get_progress_type_id(conn, CONTACTLOG_PROGRESS_TYPE)
                part_ids = get_contactlog_parts(conn, progress_type_id)
                part_codes = list(part_ids.keys())
                df = fetch_contactlog_data_for_student(conn, student_id, progress_type_id, part_codes)
                if df.empty:
                    ui.notify("No contact log data for this student.", type="warning")
                    return

                # Print dataframe to terminal for debugging
                print(f"Data plotted for student: {name}")
                print(df.to_string())
                # Plotting: show count of contact methods over time
                df['date_str'] = df['date']  # Use already serialized date column
                method_counts = df.groupby(['date_str', 'CONTACT_METHOD']).size().unstack(fill_value=0)
                fig = go.Figure()
                for method in method_counts.columns:
                    fig.add_trace(go.Bar(
                        x=method_counts.index,
                        y=method_counts[method],
                        name=method
                    ))
                fig.update_layout(
                    barmode='stack',
                    title=f"{name}: Contact Methods Over Time",
                    xaxis_title="Date",
                    yaxis_title="Number of Contacts",
                    template="simple_white"
                )
                tmp_html = Path.home() / "ContactLogPlot.html"
                fig.write_html(str(tmp_html), auto_open=True)
                ui.notify("Contact log plot generated and opened in browser.", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot Contact Log Data", on_click=plot_contactlog_data, color="secondary")

# --- PAGE ENTRY POINT ---
def create():
    contactlog_ui()


# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app

    create()
    app.run()
