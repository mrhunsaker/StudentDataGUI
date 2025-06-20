<file_path>
StudentDataGUI/StudentDataGUI/test/test_contactlog.py
</file_path>

<edit_description>
Write tests for contactlog module.
</edit_description>
```

```python
import sqlite3
import pytest
from StudentDataGUI.appPages.contactlog import (
    get_connection,
    get_or_create_student,
    get_progress_type_id,
    get_contactlog_parts,
    create_contactlog_session,
    insert_contactlog_results,
    fetch_contactlog_data_for_student,
)

# Mock database path for testing
TEST_DATABASE_PATH = "test_contactlog.db"

@pytest.fixture
def setup_database():
    """Fixture to set up and tear down a test database."""
    conn = sqlite3.connect(TEST_DATABASE_PATH)
    cursor = conn.cursor()
    # Create mock tables
    cursor.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS ProgressType (id INTEGER PRIMARY KEY, name TEXT UNIQUE, description TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS AssessmentPart (id INTEGER PRIMARY KEY, progress_type_id INTEGER, code TEXT, description TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS ProgressSession (id INTEGER PRIMARY KEY, student_id INTEGER, progress_type_id INTEGER, date TEXT, notes TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS AssessmentResult (id INTEGER PRIMARY KEY, session_id INTEGER, part_id INTEGER, score TEXT)")
    conn.commit()
    yield conn
    conn.close()

def test_get_or_create_student(setup_database):
    conn = setup_database
    student_name = "John Doe"
    student_id = get_or_create_student(conn, student_name)
    assert student_id is not None

    # Ensure the student is not duplicated
    duplicate_id = get_or_create_student(conn, student_name)
    assert student_id == duplicate_id

def test_get_progress_type_id(setup_database):
    conn = setup_database
    progress_type_name = "ContactLog"
    progress_type_id = get_progress_type_id(conn, progress_type_name)
    assert progress_type_id is not None

    # Ensure the progress type is not duplicated
    duplicate_id = get_progress_type_id(conn, progress_type_name)
    assert progress_type_id == duplicate_id

def test_get_contactlog_parts(setup_database):
    conn = setup_database
    progress_type_name = "ContactLog"
    progress_type_id = get_progress_type_id(conn, progress_type_name)
    parts = get_contactlog_parts(conn, progress_type_id)
    assert isinstance(parts, dict)
    assert len(parts) >= 7  # Ensure standard parts are created

def test_create_contactlog_session(setup_database):
    conn = setup_database
    student_name = "Jane Doe"
    progress_type_name = "ContactLog"
    student_id = get_or_create_student(conn, student_name)
    progress_type_id = get_progress_type_id(conn, progress_type_name)
    session_id = create_contactlog_session(conn, student_id, progress_type_id, "2023-01-01", "Initial contact")
    assert session_id is not None

def test_insert_contactlog_results(setup_database):
    conn = setup_database
    student_name = "Jane Doe"
    progress_type_name = "ContactLog"
    student_id = get_or_create_student(conn, student_name)
    progress_type_id = get_progress_type_id(conn, progress_type_name)
    parts = get_contactlog_parts(conn, progress_type_id)
    session_id = create_contactlog_session(conn, student_id, progress_type_id, "2023-01-01", "Initial contact")
    part_scores = {code: (part_id, "Sample Score") for code, part_id in parts.items()}
    insert_contactlog_results(conn, session_id, part_scores, student_name, "2023-01-01", "Notes")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM AssessmentResult WHERE session_id = ?", (session_id,))
    result_count = cursor.fetchone()[0]
    assert result_count == len(parts)

def test_fetch_contactlog_data_for_student(setup_database):
    conn = setup_database
    student_name = "Jane Doe"
    progress_type_name = "ContactLog"
    student_id = get_or_create_student(conn, student_name)
    progress_type_id = get_progress_type_id(conn, progress_type_name)
    parts = get_contactlog_parts(conn, progress_type_id)
    session_id = create_contactlog_session(conn, student_id, progress_type_id, "2023-01-01", "Initial contact")
    part_scores = {code: (part_id, "Sample Score") for code, part_id in parts.items()}
    insert_contactlog_results(conn, session_id, part_scores, student_name, "2023-01-01", "Notes")
    data = fetch_contactlog_data_for_student(conn, student_id, progress_type_id, list(parts.keys()))
    assert not data.empty
    assert "date" in data.columns
    for code in parts.keys():
        assert code in data.columns
