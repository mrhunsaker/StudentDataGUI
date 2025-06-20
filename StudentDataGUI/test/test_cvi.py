<file_path>
StudentDataGUI/StudentDataGUI/test/test_cvi.py
</file_path>

<edit_description>
Write tests for cvi module.
</edit_description>
```

```StudentDataGUI/StudentDataGUI/test/test_cvi.py
import sqlite3
import pytest
from StudentDataGUI.appPages.cvi import (
    get_connection,
    get_or_create_student,
    get_progress_type_id,
    get_cvi_parts,
    create_cvi_session,
    insert_cvi_results,
    fetch_cvi_data_for_student,
)

DATABASE_PATH = ":memory:"  # Use an in-memory database for testing


@pytest.fixture
def connection():
    """Fixture to provide a database connection."""
    conn = sqlite3.connect(DATABASE_PATH)
    yield conn
    conn.close()


def test_get_connection():
    """Test the get_connection function."""
    conn = get_connection()
    assert isinstance(conn, sqlite3.Connection)
    conn.close()


def test_get_or_create_student(connection):
    """Test the get_or_create_student function."""
    student_name = "John Doe"
    student_id = get_or_create_student(connection, student_name)
    assert isinstance(student_id, int)

    # Ensure the same student ID is returned for the same name
    same_student_id = get_or_create_student(connection, student_name)
    assert student_id == same_student_id


def test_get_progress_type_id(connection):
    """Test the get_progress_type_id function."""
    progress_type_name = "CVI"
    progress_type_id = get_progress_type_id(connection, progress_type_name)
    assert isinstance(progress_type_id, int)

    # Ensure the same progress type ID is returned for the same name
    same_progress_type_id = get_progress_type_id(connection, progress_type_name)
    assert progress_type_id == same_progress_type_id


def test_get_cvi_parts(connection):
    """Test the get_cvi_parts function."""
    progress_type_name = "CVI"
    progress_type_id = get_progress_type_id(connection, progress_type_name)
    cvi_parts = get_cvi_parts(connection, progress_type_id)

    assert isinstance(cvi_parts, dict)
    assert len(cvi_parts) >= 10  # Ensure at least 10 parts are created


def test_create_cvi_session(connection):
    """Test the create_cvi_session function."""
    student_name = "Jane Doe"
    progress_type_name = "CVI"
    student_id = get_or_create_student(connection, student_name)
    progress_type_id = get_progress_type_id(connection, progress_type_name)

    session_id = create_cvi_session(
        connection, student_id, progress_type_id, "2023-01-01", "Initial session"
    )
    assert isinstance(session_id, int)


def test_insert_cvi_results(connection):
    """Test the insert_cvi_results function."""
    student_name = "Jane Doe"
    progress_type_name = "CVI"
    student_id = get_or_create_student(connection, student_name)
    progress_type_id = get_progress_type_id(connection, progress_type_name)
    cvi_parts = get_cvi_parts(connection, progress_type_id)

    session_id = create_cvi_session(
        connection, student_id, progress_type_id, "2023-01-01", "Initial session"
    )
    part_scores = {code: (part_id, 3) for code, part_id in cvi_parts.items()}

    insert_cvi_results(connection, session_id, part_scores, student_name, "2023-01-01", "Notes")


def test_fetch_cvi_data_for_student(connection):
    """Test the fetch_cvi_data_for_student function."""
    student_name = "Jane Doe"
    progress_type_name = "CVI"
    student_id = get_or_create_student(connection, student_name)
    progress_type_id = get_progress_type_id(connection, progress_type_name)
    cvi_parts = get_cvi_parts(connection, progress_type_id)

    session_id = create_cvi_session(
        connection, student_id, progress_type_id, "2023-01-01", "Initial session"
    )
    part_scores = {code: (part_id, 3) for code, part_id in cvi_parts.items()}
    insert_cvi_results(connection, session_id, part_scores, student_name, "2023-01-01", "Notes")

    df = fetch_cvi_data_for_student(connection, student_id, progress_type_id, list(cvi_parts.keys()))
    assert not df.empty
    assert "date" in df.columns
    assert all(code in df.columns for code in cvi_parts.keys())
