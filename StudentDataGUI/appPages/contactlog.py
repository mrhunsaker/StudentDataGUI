#!/usr/bin/env python3

"""
Contact Log Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads contact log data using normalized tables and foreign keys
"""

import sqlite3
from pathlib import Path
import datetime
import pandas as pd
import plotly.graph_objs as go
from nicegui import ui

# --- CONFIGURATION ---
DATABASE_PATH = "/home/ryhunsaker/Documents/StudentDatabase/students20252026.db"
CONTACTLOG_PROGRESS_TYPE = "ContactLog"  # Must match ProgressType.name in DB

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
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Contact log entries"))
    conn.commit()
    return cur.lastrowid

def get_contactlog_parts(conn, progress_type_id):
    """
    Returns a dict mapping code (e.g. 'CONTACT_METHOD') to part_id for ContactLog assessment.
    If not present, creates the standard set.
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

def create_contactlog_session(conn, student_id, progress_type_id, date, notes=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_contactlog_results(conn, session_id, part_values):
    """
    part_values: dict of {code: value}
    """
    cur = conn.cursor()
    for code, (part_id, value) in part_values.items():
        cur.execute(
            "INSERT INTO AssessmentResult (session_id, part_id, score) VALUES (?, ?, ?)",
            (session_id, part_id, value)
        )
    conn.commit()

def fetch_contactlog_data_for_student(conn, student_id, progress_type_id, part_codes):
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
    df['date'] = pd.to_datetime(df['date'])
    return df

# --- UI LOGIC ---

def contactlog_ui():
    with ui.card():
        ui.label("Contact Log (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
        guardian_name = ui.input("Guardian Name")
        contact_method = ui.select(["Phone", "Text", "In-Person", "Email"], label="Contact Method")
        phone_number = ui.input("Phone Number")
        email_address = ui.input("Email Address")
        contact_response = ui.select(["Answered", "Left Message", "Unable to Leave Message", "Disconnected"], label="Contact Response")
        contact_general = ui.select(["IEP Related", "Discipline Related", "Student Requested"], label="General Topic")
        contact_specific = ui.select(["Schedule IEP Meeting", "IEP Team Follow-Up", "Collaborate on Student IEP Goals", "Progress Monitoring Update"], label="Specific Topic")
        notes_input = ui.textarea("Contact Notes (if email, please copy/paste email here)")

        def save_contactlog_data():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
            if not name or not date_val:
                ui.notify("Student name and date are required.", type="negative")
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
                ui.notify("Contact log entry saved successfully!", type="positive")
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
                df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')
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
@ui.page("/contactlog_ui")
def create():
    contactlog_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
