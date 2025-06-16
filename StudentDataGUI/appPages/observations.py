#!/usr/bin/env python3

"""
Observation Notes Page (Updated for Normalized SQL Schema)
- Uses new schema from updated_sql_bestpractice.py
- Uploads and downloads observation notes using normalized tables and foreign keys
"""

import sqlite3
from pathlib import Path
import datetime
import pandas as pd
from nicegui import ui

# --- CONFIGURATION ---
DATABASE_PATH = "/home/ryhunsaker/Documents/StudentDatabase/students20252026.db"
OBSERVATION_TYPE = "Observation"  # Must match ProgressType.name in DB

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
    cur.execute("INSERT INTO ProgressType (name, description) VALUES (?, ?)", (name, "Observation notes"))
    conn.commit()
    return cur.lastrowid

def create_observation_session(conn, student_id, progress_type_id, date, notes=None):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes)
    )
    conn.commit()
    return cur.lastrowid

def fetch_observations_for_student(conn, student_id, progress_type_id):
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
    with ui.card():
        ui.label("Observation Notes (Normalized DB)").classes("text-h4 text-grey-8")
        student_name = ui.input("Student Name", placeholder="Enter student name")
        ui.label("Date")
        date_input = ui.date(value=datetime.date.today())
        notes_input = ui.textarea("Observation Notes", placeholder="Type observation notes here...")

        def save_observation():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
            if not name or not date_val or not notes:
                ui.notify("Student name, date, and notes are required.", type="negative")
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
                # Display as a simple table (could be enhanced to timeline, etc.)
                with ui.dialog() as dialog, ui.card():
                    ui.label(f"Observation Notes for {name}").classes("text-h5")
                    for _, row in df.iterrows():
                        ui.markdown(f"**{row['date'].strftime('%Y-%m-%d')}**: {row['notes']}")
                    ui.button("Close", on_click=dialog.close)
                dialog.open()
            except Exception as e:
                ui.notify(f"Error fetching observations: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Show All Observations", on_click=plot_observations, color="secondary")

# --- PAGE ENTRY POINT ---
@ui.page("/observations_ui")
def create():
    observations_ui()

# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app
    create()
    app.run()
