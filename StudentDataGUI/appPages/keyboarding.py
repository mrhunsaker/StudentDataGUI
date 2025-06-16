#!/usr/bin/env python3

"""
Keyboarding Skills Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads keyboarding data using normalized tables and foreign keys
"""

import sqlite3
from pathlib import Path
import datetime
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from nicegui import ui

# --- CONFIGURATION ---
DATABASE_PATH = "/home/ryhunsaker/Documents/StudentDatabase/students20252026.db"
KEYBOARDING_PROGRESS_TYPE = "Keyboarding"  # Must match ProgressType.name in DB

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
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Keyboarding skills progression"))
    conn.commit()
    return cur.lastrowid

def create_keyboarding_session(conn, student_id, progress_type_id, date, notes=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def insert_keyboarding_result(conn, session_id, program, topic, speed, accuracy):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO KeyboardingResult (session_id, program, topic, speed, accuracy) VALUES (?, ?, ?, ?, ?)",
        (session_id, program, topic, speed, accuracy)
    )
    conn.commit()

def fetch_keyboarding_data_for_student(conn, student_id, progress_type_id):
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

def keyboarding_skills_ui():
    with ui.card():
        ui.label("Keyboarding Skills (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
        program_input = ui.select(
            options=[
                "Typio", "TypeAbility", "APH Typer", "Typing Club", "MonkeyType", "Custom Assignment"
            ],
            label="Keyboarding Program"
        )
        topic_input = ui.select(
            options=[
                "Home Row", "Top Row", "Bottom Row", "Numbers", "Modifier Keys", "F-Keys", "Shortcut Keystrokes"
            ],
            label="Topic Covered"
        )
        speed_input = ui.number(label="Typing Speed (WPM)", value=0, min=0, max=200, step=1)
        accuracy_input = ui.number(label="Typing Accuracy (%)", value=0, min=0, max=100, step=1)
        notes_input = ui.textarea("Notes (optional)")

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
                insert_keyboarding_result(conn, session_id, program, topic, speed, accuracy)
                ui.notify("Keyboarding data saved successfully!", type="positive")
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
