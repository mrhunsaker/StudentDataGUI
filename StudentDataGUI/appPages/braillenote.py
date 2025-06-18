#!/usr/bin/env python3

"""
BrailleNote Touch Plus Skills Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads BrailleNote data using normalized tables and foreign keys
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
from StudentDataGUI.appHelpers.helpers import dataBasePath
DATABASE_PATH = dataBasePath
BRAILLENOTE_PROGRESS_TYPE = "BrailleNote"  # Must match ProgressType.name in DB


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
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "BrailleNote Touch Plus skills progression"))
    conn.commit()
    return cur.lastrowid

def get_braillenote_parts(conn, progress_type_id):
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

def create_braillenote_session(conn, student_id, progress_type_id, date, notes=None):
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

def fetch_braillenote_data_for_student(conn, student_id, progress_type_id, part_codes):
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
    df['date'] = pd.to_datetime(df['date'])
    return df

# --- UI LOGIC ---

def braillenote_skills_ui():
    with ui.card():
        ui.label("BrailleNote Touch Plus Skills (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
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
            part_inputs[code] = ui.number(label=label, value=0, min=0, max=3, step=1)
        notes_input = ui.textarea("Notes (optional)")

        def save_braillenote_data():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
            if not name or not date_val:
                ui.notify("Student name and date are required.", type="negative")
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
                ui.notify("BrailleNote data saved successfully!", type="positive")
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
@ui.page("/braillenote_skills_ui")
def create():
    braillenote_skills_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
