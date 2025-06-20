<file_path>
StudentDataGUI/StudentDataGUI/test/test_keyboarding.py
</file_path>

<edit_description>
Write tests for keyboarding module.
</edit_description>
```

```python
import sqlite3
import pytest
from StudentDataGUI.appPages.keyboarding import (
    get_connection,
    get_or_create_student,
    get_progress_type_id,
    create_keyboarding_session,
    insert_keyboarding_result,
    fetch_keyboarding_data_for_student,
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
        "CREATE TABLE ProgressSession (id INTEGER PRIMARY KEY, student_id INTEGER, progress_type_id INTEGER, date TEXT, notes TEXT)"
    )
    conn.execute(
        "CREATE TABLE KeyboardingResult (id INTEGER PRIMARY KEY, session_id INTEGER, program TEXT, topic TEXT, speed INTEGER, accuracy INTEGER)"
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
    progress_type_id = get_progress_type_id(conn, "Keyboarding")
    assert progress_type_id is not None

    # Test that the same progress type is not duplicated
    same_progress_type_id = get_progress_type_id(conn, "Keyboarding")
    assert progress_type_id == same_progress_type_id


def test_create_keyboarding_session(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Keyboarding")
    session_id = create_keyboarding_session(
        conn, student_id, progress_type_id, "2023-10-01", "Test notes"
    )
    assert session_id is not None


def test_insert_keyboarding_result(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Keyboarding")
    session_id = create_keyboarding_session(
        conn, student_id, progress_type_id, "2023-10-01", "Test notes"
    )

    insert_keyboarding_result(
        conn,
        session_id,
        "Typing Club",
        "Home Row",
        50,
        95,
        "John Doe",
        "2023-10-01",
        "Test notes",
    )

    # Verify that the result was inserted
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM KeyboardingResult WHERE session_id = ?", (session_id,))
    result_count = cur.fetchone()[0]
    assert result_count == 1


def test_fetch_keyboarding_data_for_student(db_connection):
    conn = db_connection
    student_id = get_or_create_student(conn, "John Doe")
    progress_type_id = get_progress_type_id(conn, "Keyboarding")
    session_id = create_keyboarding_session(
        conn, student_id, progress_type_id, "2023-10-01", "Test notes"
    )

    insert_keyboarding_result(
        conn,
        session_id,
        "Typing Club",
        "Home Row",
        50,
        95,
        "John Doe",
        "2023-10-01",
        "Test notes",
    )

    df = fetch_keyboarding_data_for_student(conn, student_id, progress_type_id)
    assert not df.empty
    assert "date" in df.columns
    assert "program" in df.columns
    assert "topic" in df.columns
    assert "speed" in df.columns
    assert "accuracy" in df.columns
