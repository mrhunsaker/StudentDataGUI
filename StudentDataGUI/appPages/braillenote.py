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
from StudentDataGUI.appHelpers.helpers import students
from ..appTheming import theme

from StudentDataGUI.appHelpers.helpers import dataBasePath
# Database is now stored in /app_home at the project root
DATABASE_PATH = dataBasePath
BRAILLENOTE_PROGRESS_TYPE = "BrailleNote"  # Must match ProgressType.name in DB


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
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "BrailleNote skills progression"))
    conn.commit()
    return cur.lastrowid

def get_braillenote_parts(conn: sqlite3.Connection, progress_type_id: int) -> dict[str, int]:
    """
    Returns a dict mapping code (e.g. 'P1_1') to part_id for BrailleNote assessment.
    If not present, creates the standard set.
    """
    cur = conn.cursor()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    rows = cur.fetchall()
    if rows and len(rows) >= 60:
        return {code: pid for code, pid in rows}
    # If not present, create standard BrailleNote parts (abbreviated for demo, expand as needed)
    braillenote_parts = [
        # Phase 1
        ("P1_1", "Physical Layout"), ("P1_2", "Setup/Universal Commands"), ("P1_3", "BNT+ Navigation"),
        ("P1_4", "File Management"), ("P1_5", "Word Processor"), ("P1_6", "Email"), ("P1_7", "Internet"),
        ("P1_8", "Calculator"), ("P1_9", "KeyMath"),
        # Phase 2
        ("P2_1", "Calendar"), ("P2_2", "KeyBRF"), ("P2_3", "KeyFiles"), ("P2_4", "KeyMail"),
        ("P2_5", "KeyWeb"), ("P2_6", "KeyCalc"), ("P2_7", "KeyWord"),
        # Phase 3
        ("P3_1", "KeySlides"), ("P3_2", "KeyCode"), ("P3_3", "Third Party Apps"), ("P3_4", "Braille Input"),
        ("P3_5", "Braille Output"), ("P3_6", "Settings"), ("P3_7", "Accessibility"),
        # Phase 4
        ("P4_1", "Advanced File Management"), ("P4_2", "Cloud Integration"), ("P4_3", "Device Maintenance"),
        # Phase 5
        ("P5_1", "Collaboration"), ("P5_2", "Export/Import"), ("P5_3", "Printing"), ("P5_4", "Backup"),
        # Phase 6
        ("P6_1", "App Installation"), ("P6_2", "App Updates"), ("P6_3", "Troubleshooting"),
        # Phase 7
        ("P7_1", "Custom Shortcuts"), ("P7_2", "Macros"), ("P7_3", "Scripting"), ("P7_4", "Automation"),
        # Phase 8
        ("P8_1", "Bluetooth Devices"), ("P8_2", "USB Devices"), ("P8_3", "External Displays"),
        ("P8_4", "Audio Output"), ("P8_5", "Video Output"),
        # Phase 9
        ("P9_1", "Security"), ("P9_2", "User Accounts"), ("P9_3", "Parental Controls"), ("P9_4", "Network Settings"),
        # Phase 10
        ("P10_1", "Speech Settings"), ("P10_2", "Voice Profiles"), ("P10_3", "Language Support"),
        # Phase 11
        ("P11_1", "Firmware Updates"), ("P11_2", "Diagnostics"), ("P11_3", "Logs"), ("P11_4", "Support"),
        ("P11_5", "Warranty"),
        # Phase 12
        ("P12_1", "Community Resources"), ("P12_2", "Online Help"), ("P12_3", "User Forums"), ("P12_4", "Feedback"),
    ]
    for code, desc in braillenote_parts:
        cur.execute(
            "INSERT OR IGNORE INTO AssessmentPart (progress_type_id, code, description) VALUES (?, ?, ?)",
            (progress_type_id, code, desc)
        )
    conn.commit()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    return {code: pid for code, pid in cur.fetchall()}

def create_braillenote_session(conn: sqlite3.Connection, student_id: int, progress_type_id: int, date: str, notes: str | None = None) -> int:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_braillenote_results(conn, session_id, part_scores, student_name, date_val, notes=None):
    def insert_braillenote_results(conn, session_id, part_scores, student_name, date_val, notes=None):
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

        # Append data to BrailleNoteSkillsProgression.csv
        from StudentDataGUI.appHelpers.helpers import DATA_ROOT
        import csv
        braillenote_csv_path = Path(DATA_ROOT) / "StudentDataFiles" / student_name / "BrailleNoteSkillsProgression.csv"
        braillenote_csv_path.parent.mkdir(parents=True, exist_ok=True)
        # Prepare data for horizontal writing
        header = ["date"] + list(part_scores.keys())
        row = [date_val] + [score for _, score in part_scores.values()]

        # Write data horizontally
        write_header = not braillenote_csv_path.exists()  # Write header only if file doesn't exist
        with open(braillenote_csv_path, mode="a", newline="") as csvfile:
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
        json_path = student_dir / f"braillenote_{now}.json"
        json_data = {
            "student_name": student_name,
            "date": date_val,
            "notes": notes,
            "part_scores": {code: score for code, (part_id, score) in part_scores.items()}
        }
        with open(json_path, "w") as f:
            json.dump(json_data, f, indent=2)
    # Save JSON snapshot of the inserted data
    import json
    from datetime import datetime
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    student_dir = Path(DATA_ROOT) / "StudentDataFiles" / student_name
    student_dir.mkdir(parents=True, exist_ok=True)
    json_path = student_dir / f"braillenote_{now}.json"
    json_data = {
        "student_name": student_name,
        "date": date_val,
        "notes": notes,
        "part_scores": {code: score for code, (part_id, score) in part_scores.items()}
    }
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)

def fetch_braillenote_data_for_student(conn: sqlite3.Connection, student_id: int, progress_type_id: int, part_codes: list[str]) -> pd.DataFrame:
    """
    Returns a DataFrame with columns: date, code1, code2, ..., codeN
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
    for sid, code, score in rows:
        data[sid][code] = score
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df['date']).astype(str)
    df['date'] = df['date'].astype(str)  # Ensure date column is JSON serializable
    return df

# --- UI LOGIC ---

def braillenote_skills_ui():
    with ui.card():
        ui.label("BrailleNote Touch Plus Skills").classes("text-h4 text-grey-8")
        student_name = ui.select(options=students, label="Student Name").props('aria-describedby=student_name_error').style("width: 500px")
        student_name_error = ui.label("Student name is required.").props('id=student_name_error').classes('text-red-700').style('display:none')
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today()).props('aria-describedby=date_error').style("width: 500px")
        date_error = ui.label("Date is required.").props('id=date_error').classes('text-red-700').style('display:none')
        # BrailleNote part codes and labels (abbreviated for demo, expand as needed)
        braillenote_parts = [
            ("P1_1", "Physical Layout"), ("P1_2", "Setup/Universal Commands"), ("P1_3", "BNT+ Navigation"),
            ("P1_4", "File Management"), ("P1_5", "Word Processor"), ("P1_6", "Email"), ("P1_7", "Internet"),
            ("P1_8", "Calculator"), ("P1_9", "KeyMath"),
            ("P2_1", "Calendar"), ("P2_2", "KeyBRF"), ("P2_3", "KeyFiles"), ("P2_4", "KeyMail"),
            ("P2_5", "KeyWeb"), ("P2_6", "KeyCalc"), ("P2_7", "KeyWord"),
            ("P3_1", "KeySlides"), ("P3_2", "KeyCode"), ("P3_3", "Third Party Apps"), ("P3_4", "Braille Input"),
            ("P3_5", "Braille Output"), ("P3_6", "Settings"), ("P3_7", "Accessibility"),
            ("P4_1", "Advanced File Management"), ("P4_2", "Cloud Integration"), ("P4_3", "Device Maintenance"),
            ("P5_1", "Collaboration"), ("P5_2", "Export/Import"), ("P5_3", "Printing"), ("P5_4", "Backup"),
            ("P6_1", "App Installation"), ("P6_2", "App Updates"), ("P6_3", "Troubleshooting"),
            ("P7_1", "Custom Shortcuts"), ("P7_2", "Macros"), ("P7_3", "Scripting"), ("P7_4", "Automation"),
            ("P8_1", "Bluetooth Devices"), ("P8_2", "USB Devices"), ("P8_3", "External Displays"),
            ("P8_4", "Audio Output"), ("P8_5", "Video Output"),
            ("P9_1", "Security"), ("P9_2", "User Accounts"), ("P9_3", "Parental Controls"), ("P9_4", "Network Settings"),
            ("P10_1", "Speech Settings"), ("P10_2", "Voice Profiles"), ("P10_3", "Language Support"),
            ("P11_1", "Firmware Updates"), ("P11_2", "Diagnostics"), ("P11_3", "Logs"), ("P11_4", "Support"),
            ("P11_5", "Warranty"),
            ("P12_1", "Community Resources"), ("P12_2", "Online Help"), ("P12_3", "User Forums"), ("P12_4", "Feedback"),
        ]
        part_inputs = {}
        for code, label in braillenote_parts:
            part_inputs[code] = ui.number(label=label, value=0, min=0, max=3, step=1).style("width: 500px")
        notes_input = ui.textarea("Notes (optional)").style("width: 500px")

        def save_braillenote_data():
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
                progress_type_id = get_progress_type_id(conn, BRAILLENOTE_PROGRESS_TYPE)
                part_ids = get_braillenote_parts(conn, progress_type_id)
                session_id = create_braillenote_session(conn, student_id, progress_type_id, date_val, notes)
                part_scores = {}
                for code in part_inputs:
                    score = part_inputs[code].value
                    part_scores[code] = (part_ids[code], score)
                insert_braillenote_results(conn, session_id, part_scores, name, date_val, notes)

                # Append data to BrailleNoteSkillsProgression.csv
                from StudentDataGUI.appHelpers.helpers import DATA_ROOT
                import csv
                braillenote_csv_path = Path(DATA_ROOT) / "StudentDataFiles" / name / "BrailleNoteSkillsProgression.csv"
                braillenote_csv_path.parent.mkdir(parents=True, exist_ok=True)
                # Prepare data for horizontal writing
                header = ["date"] + list(part_scores.keys())
                row = [date_val] + [score for _, score in part_scores.values()]

                # Write data horizontally
                write_header = not braillenote_csv_path.exists()  # Write header only if file doesn't exist
                with open(braillenote_csv_path, mode="a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    if write_header:
                        writer.writerow(header)
                    writer.writerow(row)

                # Save JSON snapshot of the inserted data
                import json
                from datetime import datetime
                json_path = Path(DATA_ROOT) / "StudentDataFiles" / name / f"braillenote_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
                json_data = {
                    "student_name": name,
                    "date": date_val,
                    "notes": notes,
                    "part_scores": {code: score for code, (part_id, score) in part_scores.items()}
                }
                with open(json_path, "w") as f:
                    json.dump(json_data, f, indent=2)

                ui.notify("BrailleNote data saved successfully and appended to CSV!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save BrailleNote Data", on_click=save_braillenote_data, color="primary")

        def plot_braillenote_data():
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
                progress_type_id = get_progress_type_id(conn, BRAILLENOTE_PROGRESS_TYPE)
                part_ids = get_braillenote_parts(conn, progress_type_id)
                part_codes = list(part_ids.keys())
                df = fetch_braillenote_data_for_student(conn, student_id, progress_type_id, part_codes)
                if df.empty:
                    ui.notify("No braillenote data for this student.", type="warning")
                    return

                # Print dataframe to terminal for debugging
                print(f"Data plotted for student: {name}")
                print(df.to_string())
                # Plotting
                # For demo, plot first 12 skills in a 3x4 grid
                fig = make_subplots(
                    rows=3, cols=4,
                    subplot_titles=[label for _, label in braillenote_parts[:12]]
                )
                for idx, code in enumerate(part_codes[:12]):
                    row = idx // 4 + 1
                    col = idx % 4 + 1
                    fig.add_trace(
                        go.Scatter(
                            x=df['date'],  # Ensure date column is JSON serializable
                            y=df[code],
                            mode="lines+markers",
                            name=code,
                            hovertemplate=f"{code}: "+"%{y}"
                        ),
                        row=row, col=col
                    )
                fig.update_layout(
                    template="simple_white",
                    title_text=f"{name}: BrailleNote Touch Plus Skills Progression",
                    hovermode="x unified"
                )
                tmp_html = Path.home() / "BrailleNoteSkillsProgression.html"
                fig.write_html(str(tmp_html), auto_open=True)
                ui.notify("Graph generated and opened in browser.", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot BrailleNote Data", on_click=plot_braillenote_data, color="secondary")

# --- PAGE ENTRY POINT ---
def create():
    with theme.frame("- BRAILLENOTE SKILLS -"):
        braillenote_skills_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
