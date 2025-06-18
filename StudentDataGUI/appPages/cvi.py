#!/usr/bin/env python3

"""
CVI Progress Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads CVI data using normalized tables and foreign keys
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
CVI_PROGRESS_TYPE = "CVI"  # Must match ProgressType.name in DB


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
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "CVI skills progression"))
    conn.commit()
    return cur.lastrowid

def get_cvi_parts(conn, progress_type_id):
    """
    Returns a dict mapping code (e.g. 'P1_1') to part_id for CVI assessment.
    If not present, creates the standard set.
    """
    cur = conn.cursor()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    rows = cur.fetchall()
    if rows and len(rows) >= 10:
        return {code: pid for code, pid in rows}
    # If not present, create standard CVI parts
    cvi_parts = [
        ("P1_1", "Color Preference"),
        ("P1_2", "Need for Movement"),
        ("P1_3", "Latency"),
        ("P1_4", "Field Preference"),
        ("P1_5", "Visual Complexity"),
        ("P1_6", "Nonpurposeful Gaze"),
        ("P2_1", "Distance Viewing"),
        ("P2_2", "Atypical Reflexes"),
        ("P2_3", "Visual Novelty"),
        ("P2_4", "Visual Reach"),
    ]
    for code, desc in cvi_parts:
        cur.execute(
            "INSERT OR IGNORE INTO AssessmentPart (progress_type_id, code, description) VALUES (?, ?, ?)",
            (progress_type_id, code, desc)
        )
    conn.commit()
    cur.execute("SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?", (progress_type_id,))
    return {code: pid for code, pid in cur.fetchall()}

def create_cvi_session(conn, student_id, progress_type_id, date, notes=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_cvi_results(conn, session_id, part_scores, student_name, date_val, notes=None):
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

    # Append data to CVIProgression.csv
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    import csv
    cvi_csv_path = Path(DATA_ROOT) / "StudentDataFiles" / student_name / "CVIProgression.csv"
    cvi_csv_path.parent.mkdir(parents=True, exist_ok=True)
    # Prepare data for horizontal writing
    header = ["date"] + list(part_scores.keys())
    row = [date_val] + [score for _, score in part_scores.values()]

    # Write data horizontally
    write_header = not cvi_csv_path.exists()  # Write header only if file doesn't exist
    with open(cvi_csv_path, mode="a", newline="") as csvfile:
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
    json_path = student_dir / f"cvi_{now}.json"
    json_data = {
        "student_name": student_name,
        "date": date_val,
        "notes": notes,
        "part_scores": {code: score for code, (part_id, score) in part_scores.items()}
    }
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)

def fetch_cvi_data_for_student(conn, student_id, progress_type_id, part_codes):
    """
    Returns a DataFrame with columns: date, code1, code2, ..., codeN
    """
    # Get all sessions for this student and CVI
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
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')  # Convert datetime to string for JSON serialization
    return df

# --- UI LOGIC ---

def cvi_skills_ui():
    with ui.card():
        ui.label("CVI Progression (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
        # CVI part codes and labels
        cvi_parts = [
            ("P1_1", "Color Preference"),
            ("P1_2", "Need for Movement"),
            ("P1_3", "Latency"),
            ("P1_4", "Field Preference"),
            ("P1_5", "Visual Complexity"),
            ("P1_6", "Nonpurposeful Gaze"),
            ("P2_1", "Distance Viewing"),
            ("P2_2", "Atypical Reflexes"),
            ("P2_3", "Visual Novelty"),
            ("P2_4", "Visual Reach"),
        ]
        part_inputs = {}
        for code, label in cvi_parts:
            part_inputs[code] = ui.number(label=label, value=0, min=0, max=3, step=1)
        notes_input = ui.textarea("Notes (optional)")

        def save_cvi_data():
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
                progress_type_id = get_progress_type_id(conn, CVI_PROGRESS_TYPE)
                part_ids = get_cvi_parts(conn, progress_type_id)
                session_id = create_cvi_session(conn, student_id, progress_type_id, date_val, notes)
                part_scores = {}
                for code in part_inputs:
                    score = part_inputs[code].value
                    part_scores[code] = (part_ids[code], score)
                insert_cvi_results(conn, session_id, part_scores)

                # Append data to CVIProgression.csv
                from StudentDataGUI.appHelpers.helpers import DATA_ROOT
                import csv
                cvi_csv_path = Path(DATA_ROOT) / "StudentDataFiles" / name / "CVIProgression.csv"
                cvi_csv_path.parent.mkdir(parents=True, exist_ok=True)
                # Prepare data for horizontal writing
                header = ["date"] + list(part_scores.keys())
                row = [date_val] + [score for _, score in part_scores.values()]

                # Write data horizontally
                write_header = not cvi_csv_path.exists()  # Write header only if file doesn't exist
                with open(cvi_csv_path, mode="a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    if write_header:
                        writer.writerow(header)
                    writer.writerow(row)

                # Save JSON snapshot of the inserted data
                import json
                from datetime import datetime
                json_path = Path(DATA_ROOT) / "StudentDataFiles" / name / f"cvi_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
                json_data = {
                    "student_name": name,
                    "date": date_val.strftime('%Y-%m-%d'),  # Convert datetime to string
                    "notes": notes,
                    "part_scores": {code: score for code, (part_id, score) in part_scores.items()}
                }
                with open(json_path, "w") as f:
                    json.dump(json_data, f, indent=2)

                ui.notify("CVI data saved successfully and appended to CSV!", type="positive")
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save CVI Data", on_click=save_cvi_data, color="primary")

        def plot_cvi_data():
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
                progress_type_id = get_progress_type_id(conn, CVI_PROGRESS_TYPE)
                part_ids = get_cvi_parts(conn, progress_type_id)
                part_codes = list(part_ids.keys())
                df = fetch_cvi_data_for_student(conn, student_id, progress_type_id, part_codes)
                if df.empty:
                    ui.notify("No CVI data for this student.", type="warning")
                    return

                # Print dataframe to terminal for debugging
                print(f"Data plotted for student: {name}")
                print(df.to_string())
                # Plotting
                fig = make_subplots(
                    rows=5, cols=2,
                    subplot_titles=[
                        "Color Preference", "Need for Movement",
                        "Latency", "Field Preference",
                        "Visual Complexity", "Nonpurposeful Gaze",
                        "Distance Viewing", "Atypical Reflexes",
                        "Visual Novelty", "Visual Reach"
                    ]
                )
                # Map codes to subplot positions
                code_to_subplot = {
                    "P1_1": (1, 1), "P1_2": (1, 2),
                    "P1_3": (2, 1), "P1_4": (2, 2),
                    "P1_5": (3, 1), "P1_6": (3, 2),
                    "P2_1": (4, 1), "P2_2": (4, 2),
                    "P2_3": (5, 1), "P2_4": (5, 2),
                }
                for code, (row, col) in code_to_subplot.items():
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
                    title_text=f"{name}: CVI Progression",
                    hovermode="x unified"
                )
                # Save HTML to student folder with timestamp
                from datetime import datetime
                from StudentDataGUI.appHelpers.helpers import DATA_ROOT
                now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                student_dir = Path(DATA_ROOT) / "StudentDataFiles" / name
                student_dir.mkdir(parents=True, exist_ok=True)
                html_path = student_dir / f"cvi_{now}.html"
                fig.write_html(str(html_path), auto_open=False)
                ui.notify(f"Graph saved to {html_path}", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot CVI Data", on_click=plot_cvi_data, color="secondary")

# --- PAGE ENTRY POINT ---
@ui.page("/cvi_skills_ui")
def create():
    cvi_skills_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
