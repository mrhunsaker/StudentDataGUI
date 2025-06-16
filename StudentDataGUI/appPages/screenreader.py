StudentDataGUI/StudentDataGUI/appPages/screenreader_updated.py
#!/usr/bin/env python3

"""
Screen Reader Skills Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads screen reader data using normalized tables and foreign keys
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
SCREENREADER_PROGRESS_TYPE = "ScreenReader"  # Must match ProgressType.name in DB

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
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Screen Reader skills progression"))
    conn.commit()
    return cur.lastrowid

def get_screenreader_parts(conn, progress_type_id):
    """
    Returns a dict mapping code (e.g. 'P1_1') to part_id for ScreenReader assessment.
    If not present, creates the standard set.
    """
    cur = conn.cursor()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    rows = cur.fetchall()
    if rows and len(rows) >= 30:
        return {code: pid for code, pid in rows}
    # If not present, create standard screenreader parts
    screenreader_parts = [
        # Phase 1
        ("P1_1", "Turn ON/OFF"), ("P1_2", "Use Modifier Keys"), ("P1_3", "Use Reading Commands"), ("P1_4", "ID Titles"),
        ("P1_5", "Access Documents"), ("P1_6", "Switch Program Focus"),
        # Phase 2
        ("P2_1", "Type with all keys"), ("P2_2", "Change Screen Reader Settings"),
        ("P2_3", "Write documents"), ("P2_4", "Copy/Paste Text"),
        # Phase 3
        ("P3_1", "Define HTML Elements"), ("P3_2", "ID HTML Elements"), ("P3_3", "Navigate to Address Bar"),
        ("P3_4", "TAB Navigation"), ("P3_5", "Quick Key Navigation"), ("P3_6", "Elements List Navigation"),
        ("P3_7", "Justify Navigation Method"), ("P3_8", "ALT-TAB Focus"), ("P3_9", "Toggle Screen Reader Mode"),
        ("P3_10", "Navigate a Table"), ("P3_11", "Navigation Sequence"),
        # Phase 4
        ("P4_1", "Save and Open Files"), ("P4_2", "Create Folders"), ("P4_3", "Navigate Cloud Storage"),
        ("P4_4", "Download from Internet"), ("P4_5", "UNZIP Folders"), ("P4_6", "Use Virtual Cursor"),
        ("P4_7", "Use Built-In OCR"),
    ]
    for code, desc in screenreader_parts:
        cur.execute(
            "INSERT OR IGNORE INTO AssessmentPart (progress_type_id, code, description) VALUES (?, ?, ?)",
            (progress_type_id, code, desc)
        )
    conn.commit()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    return {code: pid for code, pid in cur.fetchall()}

def create_screenreader_session(conn, student_id, progress_type_id, date, notes=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_screenreader_results(conn, session_id, part_scores):
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

def fetch_screenreader_data_for_student(conn, student_id, progress_type_id, part_codes):
    """
    Returns a DataFrame with columns: date, code1, code2, ..., codeN
    """
    # Get all sessions for this student and screenreader
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

def screenreader_skills_ui():
    with ui.card():
        ui.label("Screen Reader Skills (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        date_input = ui.date(label="Date", value=datetime.date.today())
        # ScreenReader part codes and labels
        screenreader_parts = [
            ("P1_1", "Turn ON/OFF"), ("P1_2", "Use Modifier Keys"), ("P1_3", "Use Reading Commands"), ("P1_4", "ID Titles"),
            ("P1_5", "Access Documents"), ("P1_6", "Switch Program Focus"),
            ("P2_1", "Type with all keys"), ("P2_2", "Change Screen Reader Settings"),
            ("P2_3", "Write documents"), ("P2_4", "Copy/Paste Text"),
            ("P3_1", "Define HTML Elements"), ("P3_2", "ID HTML Elements"), ("P3_3", "Navigate to Address Bar"),
            ("P3_4", "TAB Navigation"), ("P3_5", "Quick Key Navigation"), ("P3_6", "Elements List Navigation"),
            ("P3_7", "Justify Navigation Method"), ("P3_8", "ALT-TAB Focus"), ("P3_9", "Toggle Screen Reader Mode"),
            ("P3_10", "Navigate a Table"), ("P3_11", "Navigation Sequence"),
            ("P4_1", "Save and Open Files"), ("P4_2", "Create Folders"), ("P4_3", "Navigate Cloud Storage"),
            ("P4_4", "Download from Internet"), ("P4_5", "UNZIP Folders"), ("P4_6", "Use Virtual Cursor"),
            ("P4_7", "Use Built-In OCR"),
        ]
        part_inputs = {}
        with ui.row():
            for code, label in screenreader_parts:
                part_inputs[code] = ui.number(label=label, value=0, min=0, max=3, step=1)
        notes_input = ui.input("Notes (optional)", multiline=True)

        def save_screenreader_data():
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
                progress_type_id = get_progress_type_id(conn, SCREENREADER_PROGRESS_TYPE)
                part_ids = get_screenreader_parts(conn, progress_type_id)
                session_id = create_screenreader_session(conn, student_id, progress_type_id, date_val, notes)
                part_scores = {}
                for code in part_inputs:
                    score = part_inputs[code].value
                    part_scores[code] = (part_ids[code], score)
                insert_screenreader_results(conn, session_id, part_scores)
                ui.notify("Screen Reader data saved successfully!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save Screen Reader Data", on_click=save_screenreader_data, color="primary")

        def plot_screenreader_data():
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
                progress_type_id = get_progress_type_id(conn, SCREENREADER_PROGRESS_TYPE)
                part_ids = get_screenreader_parts(conn, progress_type_id)
                part_codes = list(part_ids.keys())
                df = fetch_screenreader_data_for_student(conn, student_id, progress_type_id, part_codes)
                if df.empty:
                    ui.notify("No screen reader data for this student.", type="warning")
                    return
                # Plotting
                fig = make_subplots(
                    rows=5, cols=2,
                    subplot_titles=[
                        "Phase 1a: Reading", "Phase 2: Writing",
                        "Phase 1b: Reading", "Phase 3a: Internet",
                        "Phase 3b: Internet", "Phase 3c: Internet",
                        "Phase 4a: File Management", "Phase 4b: File Management",
                        "", ""
                    ]
                )
                # Map codes to subplot positions (simplified for demonstration)
                phase_map = {
                    "P1": (1, 1), "P2": (1, 2), "P3": (2, 1), "P4": (2, 2)
                }
                # For more granular mapping, you can expand this dictionary
                for code in part_codes:
                    # Assign to subplots based on code prefix
                    if code.startswith("P1_"):
                        row, col = 1, 1
                    elif code.startswith("P2_"):
                        row, col = 1, 2
                    elif code.startswith("P3_"):
                        row, col = 2, 1
                    elif code.startswith("P4_"):
                        row, col = 2, 2
                    else:
                        row, col = 5, 2
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
                    title_text=f"{name}: Screen Reader Skills Progression",
                    hovermode="x unified"
                )
                # Show in browser or as HTML
                tmp_html = Path.home() / "ScreenReaderSkillsProgression.html"
                fig.write_html(str(tmp_html), auto_open=True)
                ui.notify("Graph generated and opened in browser.", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot Screen Reader Data", on_click=plot_screenreader_data, color="secondary")

# --- PAGE ENTRY POINT ---
def create():
    screenreader_skills_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()