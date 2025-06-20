<file_path>
StudentDataGUI/StudentDataGUI/test/test_abacus.py
</file_path>

<edit_description>
Write tests for abacus module.
</edit_description>
```

```StudentDataGUI/StudentDataGUI/test/test_abacus.py
import sqlite3
import pytest
from StudentDataGUI.appPages.abacus import (
    get_connection,
    get_or_create_student,
    get_progress_type_id,
    get_abacus_parts,
    create_abacus_session,
    insert_abacus_results,
    fetch_abacus_data_for_student,
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
    progress_type_id = get_progress_type_id(conn, "Abacus")
    assert progress_type_id is not None

    # Test that the same progress type is not duplicated
    same_progress_type_id = get_progress_type_id(conn, "Abacus")
    assert progress_type_id == same_progress_type_id


def test_get_abacus_parts(db_connection):
    conn = db_connection
    progress_type_id = get_progress_type_id(conn, "Abacus")
    abacus_parts = get_abacus_parts(conn, progress_type_id)
    assert isinstance(abacus_parts, dict)
    assert len(abacus_parts) > 0


def test_create_abacus_session(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Abacus")
    session_id = create_abacus_session(conn, student_id, progress_type_id, "2023-10-01", "Test notes")
    assert session_id is not None


def test_insert_abacus_results(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Abacus")
    abacus_parts = get_abacus_parts(conn, progress_type_id)
    session_id = create_abacus_session(conn, student_id, progress_type_id, "2023-10-01", "Test notes")

    part_scores = {code: (part_id, 3) for code, part_id in abacus_parts.items()}
    insert_abacus_results(conn, session_id, part_scores, "John Doe", "2023-10-01", "Test notes")

    # Verify that results were inserted
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM AssessmentResult WHERE session_id = ?", (session_id,))
    result_count = cur.fetchone()[0]
    assert result_count == len(part_scores)


def test_fetch_abacus_data_for_student(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Abacus")
    abacus_parts = get_abacus_parts(conn, progress_type_id)
    session_id = create_abacus_session(conn, student_id, progress_type_id, "2023-10-01", "Test notes")

    part_scores = {code: (part_id, 3) for code, part_id in abacus_parts.items()}
    insert_abacus_results(conn, session_id, part_scores, "John Doe", "2023-10-01", "Test notes")

    df = fetch_abacus_data_for_student(conn, student_id, progress_type_id, list(abacus_parts.keys()))
    assert not df.empty
    assert "date" in df.columns
    assert all(code in df.columns for code in abacus_parts.keys())
