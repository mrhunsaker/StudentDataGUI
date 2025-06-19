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
from StudentDataGUI.appHelpers.roster import students
from ..appTheming import theme

# --- CONFIGURATION ---
from StudentDataGUI.appHelpers.helpers import dataBasePath
DATABASE_PATH = dataBasePath
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

def insert_braille_results(conn, session_id, part_scores, student_name, date_val, notes=None):
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

    # Append data to BrailleSkillsProgression.csv
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    import csv
    braille_csv_path = Path(DATA_ROOT) / "StudentDataFiles" / student_name / "BrailleSkillsProgression.csv"
    braille_csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(braille_csv_path, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for code, (part_id, score) in part_scores.items():
            writer.writerow([student_name, date_val, code, score, notes])
    # Save JSON snapshot of the inserted data
    import json
    from datetime import datetime
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    student_dir = Path(DATA_ROOT) / "StudentDataFiles" / student_name
    student_dir.mkdir(parents=True, exist_ok=True)
    json_path = student_dir / f"braille_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    json_data = {
        "student_name": student_name,
        "date": date_val,
        "notes": notes,
        "part_scores": {code: score for code, (part_id, score) in part_scores.items()}
    }
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)

    # Append data to BrailleSkillsProgression.csv
    import csv
    braille_csv_path = student_dir / "BrailleSkillsProgression.csv"
    with open(braille_csv_path, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for code, (part_id, score) in part_scores.items():
            writer.writerow([student_name, date_val, code, score, notes])

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
    df['date'] = pd.to_datetime(df['date']).astype(str)
    df['date'] = df['date'].astype(str)  # Ensure date column is JSON serializable
    return df

# --- UI LOGIC ---

def braille_skills_ui():
    with theme.frame("- BRAILLE SKILLS -"):
        with ui.card():
            ui.label("Braille Skills (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.select(options=students, label="Student Name").style("width: 500px")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
        # Braille part codes and labels
        braille_parts = [
            ("P1_1", "1.1. Track left to right"), ("P1_2", "1.2. Track top to bottom"),
            ("P1_3", "1.3. Discriminate shapes"), ("P1_4", "1.4. Discriminate braille characters"),
            ("P2_1", "2.1. Mangold Progression: G C L"), ("P2_2", "2.2. Mangold Progression: D Y"),
            ("P2_3", "2.3. Mangold Progression: A B"), ("P2_4", "2.4. Mangold Progression: S"),
            ("P2_5", "2.5. Mangold Progression: W"), ("P2_6", "2.6. Mangold Progression: P O"),
            ("P2_7", "2.7. Mangold Progression: K"), ("P2_8", "2.8. Mangold Progression: R"),
            ("P2_9", "2.9. Mangold Progression: M E"), ("P2_10", "2.10. Mangold Progression: H"),
            ("P2_11", "2.11. Mangold Progression: N X"), ("P2_12", "2.12. Mangold Progression: Z F"),
            ("P2_13", "2.13. Mangold Progression: U T"), ("P2_14", "2.14. Mangold Progression: Q I"),
            ("P2_15", "2.15. Mangold Progression: V J"),
            ("P3_1", "3.1. Alphabetic Wordsigns"), ("P3_2", "3.2. Braille Numbers"),
            ("P3_3", "3.3. Punctuation"), ("P3_4", "3.4. Strong Contractions (AND OF FOR WITH THE)"),
            ("P3_5", "3.5. Strong Groupsigns (CH GH SH TH WH ED ER OU OW ST AR ING)"),
            ("P3_6", "3.6. Strong Wordsigns (CH SH TH WH OU ST)"),
            ("P3_7", "3.7. Lower Groupsigns (BE CON DIS)"), ("P3_8", "3.8. Lower Groupsigns (EA BB CC FF GG)"),
            ("P3_9", "3.9. Lower Groupsigns/Wordsigns (EN IN)"), ("P3_10", "3.10. Lower Wordsigns (BE HIS WAS WERE)"),
            ("P3_11", "3.11. Dot 5 Contractions"), ("P3_12", "3.12. Dot 45 Contractions"),
            ("P3_13", "3.13. Dot 456 Contractions"), ("P3_14", "3.14. Final Letter Groupsigns"),
            ("P3_15", "3.15. Shortform Words"),
            ("P4_1", "4.1. Grade 1 Indicators"), ("P4_2", "4.2. Capitals Indicators"),
            ("P4_3", "4.3. Numeric Mode and Spatial math"),
            ("P4_4", "4.4. Typeform Indicators (ITALIC  SCRIPT  UNDERLINE  BOLDFACE)"),
            ("P5_1", "5.1. Page Numbering"), ("P5_2", "5.2. Headings"),
            ("P5_3", "5.3. Lists"), ("P5_4", "5.4. Poety / Drama"),
            ("P6_1", "6.1. Operation and Comparison Signs"), ("P6_2", "6.2. Grade 1 Mode"),
            ("P6_3", "6.3. Special Print Symbols"), ("P6_4", "6.4. Omission Marks"),
            ("P6_5", "6.5. Shape Indicators"), ("P6_6", "6.6. Roman Numerals"),
            ("P6_7", "6.7. Fractions"),
            ("P7_1", "7.1. Grade 1 Mode and Algebra"), ("P7_2", "7.2. Grade 1 Mode and Fractions"),
            ("P7_3", "7.3. Advanced Operation and Comparison Signs"), ("P7_4", "7.4. Indices"),
            ("P7_5", "7.5. Roots and Radicals"), ("P7_6", "7.6. Miscellaneous Shape Indicators"),
            ("P7_7", "7.7. Functions"), ("P7_8", "7.8. Greek letters"),
            ("P8_1", "8.1. Functions"), ("P8_2", "8.2. Modifiers  Bars  and Dots"),
            ("P8_3", "8.3. Modifiers  Arrows  and Limits"), ("P8_4", "8.4. Probability"),
            ("P8_5", "8.5. Calculus: Differentiation"), ("P8_6", "8.6. Calculus: Integration"),
            ("P8_7", "8.7. Vertical Bars")
        ]
        part_inputs = {}
        for code, label in braille_parts:
            part_inputs[code] = ui.number(label=label, value=0, min=0, max=3, step=1).style("width: 500px")
        notes_input = ui.textarea("Notes (optional)").style("width: 500px")

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
                insert_braille_results(conn, session_id, part_scores, name, date_val, notes)
                ui.notify("Braille data saved successfully and appended to CSV!", type="positive")
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

                # Print dataframe to terminal for debugging
                print(f"Data plotted for student: {name}")
                print(df.to_string())
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
                    title_text=f"{name}: Braille Skills Progression",
                    hovermode="x unified"
                )
                # Save HTML to student folder with timestamp
                from datetime import datetime
                from StudentDataGUI.appHelpers.helpers import DATA_ROOT
                now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                student_dir = Path(DATA_ROOT) / "StudentDataFiles" / name
                student_dir.mkdir(parents=True, exist_ok=True)
                html_path = student_dir / f"braille_{now}.html"
                fig.write_html(str(html_path), auto_open=False)
                ui.notify(f"Graph saved to {html_path}", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot Braille Data", on_click=plot_braille_data, color="secondary")

# --- PAGE ENTRY POINT ---
@ui.page("/braille_skills_ui")
def create():
    braille_skills_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
