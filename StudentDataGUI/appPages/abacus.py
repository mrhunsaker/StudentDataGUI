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
from ..appTheming import theme

from StudentDataGUI.appHelpers.helpers import dataBasePath
from StudentDataGUI.appHelpers.artifacts import write_session_artifacts

# Database is now stored in /app_home at the project root
DATABASE_PATH = dataBasePath
ABACUS_PROGRESS_TYPE = "Abacus"  # Must match ProgressType.name in DB

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
    # If not present, create it
    cur.execute(
        "INSERT INTO ProgressType (name, description) VALUES (?, ?)",
        (name, "Abacus skills progression"),
    )
    conn.commit()
    return cur.lastrowid


def get_abacus_parts(conn: sqlite3.Connection, progress_type_id: int) -> dict[str, int]:
    """
    Retrieve or create Abacus assessment parts.

    Parameters
    ----------
    conn : sqlite3.Connection
        The database connection object.
    progress_type_id : int
        The ID of the progress type for Abacus.

    Returns
    -------
    dict[str, int]
        A dictionary mapping part codes (e.g., 'P1_1') to their corresponding IDs.
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?",
        (progress_type_id,),
    )
    rows = cur.fetchall()
    if rows and len(rows) >= 26:
        return {code: pid for code, pid in rows}
    # If not present, create standard abacus parts
    abacus_parts = [
        # Phase 1
        ("P1_1", "Setting Numbers"),
        ("P1_2", "Clearing Beads"),
        ("P1_3", "Place Value"),
        ("P1_4", "Vocabulary"),
        # Phase 2
        ("P2_1", "Setting Numbers"),
        ("P2_2", "Clearing Beads"),
        ("P2_3", "Place Value"),
        # Phase 3
        ("P3_1", "Setting Numbers"),
        ("P3_2", "Clearing Beads"),
        ("P3_3", "Place Value"),
        # Phase 4
        ("P4_1", "Setting Numbers"),
        ("P4_2", "Clearing Beads"),
        # Phase 5
        ("P5_1", "Place Value"),
        ("P5_2", "Vocabulary"),
        # Phase 6
        ("P6_1", "Setting Numbers"),
        ("P6_2", "Clearing Beads"),
        ("P6_3", "Place Value"),
        ("P6_4", "Vocabulary"),
        # Phase 7
        ("P7_1", "Setting Numbers"),
        ("P7_2", "Clearing Beads"),
        ("P7_3", "Place Value"),
        ("P7_4", "Vocabulary"),
        # Phase 8
        ("P8_1", "Setting Numbers"),
        ("P8_2", "Clearing Beads"),
    ]
    for code, desc in abacus_parts:
        cur.execute(
            "INSERT OR IGNORE INTO AssessmentPart (progress_type_id, code, description) VALUES (?, ?, ?)",
            (progress_type_id, code, desc),
        )
    conn.commit()
    cur.execute(
        "SELECT code, id FROM AssessmentPart WHERE progress_type_id = ?",
        (progress_type_id,),
    )
    return {code: pid for code, pid in cur.fetchall()}


def create_abacus_session(
    conn: sqlite3.Connection,
    student_id: int,
    progress_type_id: int,
    date: str,
    notes: str = None,
) -> int:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ProgressSession (student_id, progress_type_id, date, notes) VALUES (?, ?, ?, ?)",
        (student_id, progress_type_id, date, notes),
    )
    conn.commit()
    return cur.lastrowid


def insert_abacus_results(
    conn: sqlite3.Connection,
    session_id: int,
    part_scores: dict[str, tuple[int, int]],
    student_name: str,
    date_val: str,
    notes: str = None,
) -> None:
    """
    part_scores: dict of {code: score}
    """
    cur = conn.cursor()
    for code, (part_id, score) in part_scores.items():
        cur.execute(
            "INSERT INTO AssessmentResult (session_id, part_id, score) VALUES (?, ?, ?)",
            (session_id, part_id, score),
        )
    conn.commit()

    # Write artifacts (CSV horizontal + JSON snapshot) using shared helper
    from StudentDataGUI.appHelpers.helpers import DATA_ROOT

    normalized_scores = {code: score for code, (part_id, score) in part_scores.items()}
    write_session_artifacts(
        base_dir=DATA_ROOT,
        student_name=student_name,
        date_val=date_val,
        part_scores=normalized_scores,  # already normalized to code->score
        notes=notes,
        prefix="Abacus",
        layout="horizontal",
        include_json=True,
    )


def fetch_abacus_data_for_student(
    conn: sqlite3.Connection,
    student_id: int,
    progress_type_id: int,
    part_codes: list[str],
) -> pd.DataFrame:
    """
    Returns a DataFrame with columns: date, code1, code2, ..., codeN
    """
    # Get all sessions for this student and abacus
    cur = conn.cursor()
    cur.execute(
        "SELECT id, date FROM ProgressSession WHERE student_id = ? AND progress_type_id = ? ORDER BY date ASC",
        (student_id, progress_type_id),
    )
    sessions = cur.fetchall()
    if not sessions:
        return pd.DataFrame()
    session_ids = [sid for sid, _ in sessions]
    session_dates = {sid: date for sid, date in sessions}
    # Get all results for these sessions
    format_codes = ",".join("?" for _ in part_codes)
    cur.execute(
        f"""
        SELECT ar.session_id, ap.code, ar.score
        FROM AssessmentResult ar
        JOIN AssessmentPart ap ON ar.part_id = ap.id
        WHERE ar.session_id IN ({",".join("?" for _ in session_ids)}) AND ap.code IN ({format_codes})
        """,
        session_ids + list(part_codes),
    )
    rows = cur.fetchall()
    # Build DataFrame
    data = {}
    for sid in session_ids:
        data[sid] = {code: None for code in part_codes}
        data[sid]["date"] = session_dates[sid]
    for sid, code, score in rows:
        data[sid][code] = score
    df = pd.DataFrame.from_dict(data, orient="index")
    df = df.sort_values("date")
    df["date"] = pd.to_datetime(df["date"])
    return df


# --- UI LOGIC ---


def abacus_skills_ui() -> None:
    # Consistent page title (outside card)
    ui.label("Abacus Skills").classes("text-h4 text-grey-8")
    with theme.card():
        from StudentDataGUI.appHelpers.helpers import students

        student_name = (
            ui.select(options=students, label="Student Name")
            .props("aria-describedby=student_name_error")
            .style("width: 500px;")
        )
        student_name_error = (
            ui.label("Student name is required.")
            .props("id=student_name_error")
            .classes("text-red-700")
            .style("display:none")
        )
        ui.label("Date")
        date_input = (
            ui.date(value=datetime.date.today())
            .props("aria-describedby=date_error")
            .style("width: 500px;")
        )
        date_error = (
            ui.label("Date is required.")
            .props("id=date_error")
            .classes("text-red-700")
            .style("display:none")
        )
        # Abacus part codes and labels
        abacus_parts = [
            ("P1_1", "Phase 1: Setting Numbers"),
            ("P1_2", "Phase 1: Clearing Beads"),
            ("P1_3", "Phase 1: Place Value"),
            ("P1_4", "Phase 1: Vocabulary"),
            ("P2_1", "Phase 2: Setting Numbers"),
            ("P2_2", "Phase 2: Clearing Beads"),
            ("P2_3", "Phase 2: Place Value"),
            ("P3_1", "Phase 3: Setting Numbers"),
            ("P3_2", "Phase 3: Clearing Beads"),
            ("P3_3", "Phase 3: Place Value"),
            ("P4_1", "Phase 4: Setting Numbers"),
            ("P4_2", "Phase 4: Clearing Beads"),
            ("P5_1", "Phase 5: Place Value"),
            ("P5_2", "Phase 5: Vocabulary"),
            ("P6_1", "Phase 6: Setting Numbers"),
            ("P6_2", "Phase 6: Clearing Beads"),
            ("P6_3", "Phase 6: Place Value"),
            ("P6_4", "Phase 6: Vocabulary"),
            ("P7_1", "Phase 7: Setting Numbers"),
            ("P7_2", "Phase 7: Clearing Beads"),
            ("P7_3", "Phase 7: Place Value"),
            ("P7_4", "Phase 7: Vocabulary"),
            ("P8_1", "Phase 8: Setting Numbers"),
            ("P8_2", "Phase 8: Clearing Beads"),
        ]
        part_inputs = {}
        for code, label in abacus_parts:
            part_inputs[code] = ui.number(
                label=label, value=0, min=0, max=3, step=1
            ).style("width: 500px;")
        notes_input = ui.textarea("Notes (optional)").style("width: 500px;")

        def save_abacus_data():
            name = student_name.value.strip()
            date_val = date_input.value
            notes = notes_input.value.strip()
            error_found = False
            if not name:
                student_name_error.style("display:block")
                student_name.props("aria-invalid=true")
                student_name.run_javascript("this.focus()")
                error_found = True
            else:
                student_name_error.style("display:none")
                student_name.props("aria-invalid=false")
            if not date_val:
                date_error.style("display:block")
                date_input.props("aria-invalid=true")
                if not error_found:
                    date_input.run_javascript("this.focus()")
                error_found = True
            else:
                date_error.style("display:none")
                date_input.props("aria-invalid=false")
            if error_found:
                return
            # Connect and insert
            conn = get_connection()
            try:
                student_id = get_or_create_student(conn, name)
                progress_type_id = get_progress_type_id(conn, ABACUS_PROGRESS_TYPE)
                part_ids = get_abacus_parts(conn, progress_type_id)
                session_id = create_abacus_session(
                    conn, student_id, progress_type_id, date_val, notes
                )
                part_scores = {}
                for code in part_inputs:
                    score = part_inputs[code].value
                    part_scores[code] = (part_ids[code], score)
                insert_abacus_results(
                    conn, session_id, part_scores, name, date_val, notes
                )

                # CSV/JSON artifact writing is already performed inside insert_abacus_results().
                # Removed duplicate CSV and JSON generation to avoid double writes.

                ui.notify(
                    "Abacus data saved successfully and appended to CSV!",
                    type="positive",
                )
            except Exception as e:
                ui.notify(f"Error saving data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Save Abacus Data", on_click=save_abacus_data, color="primary")

        def plot_abacus_data():
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
                progress_type_id = get_progress_type_id(conn, ABACUS_PROGRESS_TYPE)
                part_ids = get_abacus_parts(conn, progress_type_id)
                part_codes = list(part_ids.keys())
                df = fetch_abacus_data_for_student(
                    conn, student_id, progress_type_id, part_codes
                )
                df["date"] = df["date"].astype(
                    str
                )  # Convert date column to string for JSON serialization
                if df.empty:
                    ui.notify("No abacus data for this student.", type="warning")
                    return

                # Print dataframe to terminal for debugging
                print(f"Data plotted for student: {name}")
                print(df.to_string())
                # Plotting
                fig = make_subplots(
                    rows=4,
                    cols=2,
                    subplot_titles=[
                        "Phase 1",
                        "Phase 2",
                        "Phase 3",
                        "Phase 4",
                        "Phase 5",
                        "Phase 6",
                        "Phase 7",
                        "Phase 8",
                    ],
                )
                # Map codes to subplot positions
                phase_map = {
                    "P1": (1, 1),
                    "P2": (1, 2),
                    "P3": (2, 1),
                    "P4": (2, 2),
                    "P5": (3, 1),
                    "P6": (3, 2),
                    "P7": (4, 1),
                    "P8": (4, 2),
                }
                for code in part_codes:
                    phase = code.split("_")[0]
                    row, col = phase_map[phase]
                    fig.add_trace(
                        go.Scatter(
                            x=df["date"],
                            y=df[code],
                            mode="lines+markers",
                            name=code,
                            hovertemplate=f"{code}: " + "%{y}",
                        ),
                        row=row,
                        col=col,
                    )
                fig.update_layout(
                    template="simple_white",
                    title_text=f"{name}: Abacus Skills Progression",
                    hovermode="x unified",
                )
                # Save HTML to student folder with timestamp
                from datetime import datetime
                from StudentDataGUI.appHelpers.helpers import DATA_ROOT

                now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                student_dir = Path(DATA_ROOT) / "StudentDataFiles" / name
                student_dir.mkdir(parents=True, exist_ok=True)
                html_path = student_dir / f"abacus_{now}.html"
                fig.write_html(str(html_path), auto_open=False)
                ui.notify(f"Graph saved to {html_path}", type="positive")
            except Exception as e:
                ui.notify(f"Error plotting data: {e}", type="negative")
            finally:
                conn.close()

        ui.button("Plot Abacus Data", on_click=plot_abacus_data, color="secondary")


# --- PAGE ENTRY POINT ---
def create():
    with theme.frame("- ABACUS SKILLS -"):
        abacus_skills_ui()


# If running standalone for testing
if __name__ == "__main__":
    from nicegui import app

    create()
    app.run()
