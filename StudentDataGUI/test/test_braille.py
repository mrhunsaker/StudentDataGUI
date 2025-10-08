import sqlite3
import pytest
from StudentDataGUI.appPages.braille import (
    get_or_create_student,
    get_progress_type_id,
    get_braille_parts,
    create_braille_session,
    insert_braille_results,
    fetch_braille_data_for_student,
)

DATABASE_PATH = ":memory:"  # Use an in-memory database for testing


@pytest.fixture
def db_connection():
    """Fixture to set up and tear down an in-memory SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("CREATE TABLE Student (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    conn.execute(
        "CREATE TABLE ProgressType (id INTEGER PRIMARY KEY, name TEXT UNIQUE, description TEXT)"
    )
    conn.execute(
        "CREATE TABLE AssessmentPart (id INTEGER PRIMARY KEY, progress_type_id INTEGER, code TEXT, description TEXT)"
    )
    conn.execute(
        "CREATE TABLE ProgressSession (id INTEGER PRIMARY KEY, student_id INTEGER, progress_type_id INTEGER, date TEXT, notes TEXT)"
    )
    conn.execute(
        "CREATE TABLE AssessmentResult (id INTEGER PRIMARY KEY, session_id INTEGER, part_id INTEGER, score INTEGER)"
    )
    yield conn
    conn.close()


def test_get_or_create_student(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    assert student_id is not None

    # Test that the same student is not duplicated
    same_student_id = get_or_create_student(conn, "John Doe")
    assert student_id == same_student_id


def test_get_progress_type_id(db_connection):
    conn = db_connection
    progress_type_id = get_progress_type_id(conn, "Braille")
    assert progress_type_id is not None

    # Test that the same progress type is not duplicated
    same_progress_type_id = get_progress_type_id(conn, "Braille")
    assert progress_type_id == same_progress_type_id


def test_get_braille_parts(db_connection):
    conn = db_connection
    progress_type_id = get_progress_type_id(conn, "Braille")
    braille_parts = get_braille_parts(conn, progress_type_id)
    assert isinstance(braille_parts, dict)
    assert len(braille_parts) > 0


def test_create_braille_session(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Braille")
    session_id = create_braille_session(conn, student_id, progress_type_id, "2023-10-01", "Test notes")
    assert session_id is not None


def test_insert_braille_results(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Braille")
    braille_parts = get_braille_parts(conn, progress_type_id)
    session_id = create_braille_session(conn, student_id, progress_type_id, "2023-10-01", "Test notes")

    part_scores = {code: (part_id, 3) for code, part_id in braille_parts.items()}
    insert_braille_results(conn, session_id, part_scores, "John Doe", "2023-10-01", "Test notes")

    # Verify that results were inserted
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM AssessmentResult WHERE session_id = ?", (session_id,))
    result_count = cur.fetchone()[0]
    assert result_count == len(part_scores)


def test_fetch_braille_data_for_student(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Braille")
    braille_parts = get_braille_parts(conn, progress_type_id)
    session_id = create_braille_session(conn, student_id, progress_type_id, "2023-10-01", "Test notes")

    part_scores = {code: (part_id, 3) for code, part_id in braille_parts.items()}
    insert_braille_results(conn, session_id, part_scores, "John Doe", "2023-10-01", "Test notes")

    df = fetch_braille_data_for_student(conn, student_id, progress_type_id, list(braille_parts.keys()))
    assert not df.empty
    assert "date" in df.columns
    assert all(code in df.columns for code in braille_parts.keys())
