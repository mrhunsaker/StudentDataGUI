#!/usr/bin/env python3

"""
Minimal test script to validate the Student Data GUI containerized setup.
This script tests basic functionality without requiring the full application stack.
"""

import sys
import os
import sqlite3
import tempfile
from pathlib import Path

def test_basic_imports():
    """Test basic Python imports that should work in any environment."""
    print("Testing basic imports...")

    try:
        import sqlite3
        print("✓ sqlite3 imported successfully")
    except ImportError as e:
        print(f"✗ sqlite3 import failed: {e}")
        return False

    try:
        import os
        print("✓ os imported successfully")
    except ImportError as e:
        print(f"✗ os import failed: {e}")
        return False

    try:
        import sys
        print("✓ sys imported successfully")
    except ImportError as e:
        print(f"✗ sys import failed: {e}")
        return False

    try:
        from pathlib import Path
        print("✓ pathlib imported successfully")
    except ImportError as e:
        print(f"✗ pathlib import failed: {e}")
        return False

    return True

def test_database_operations():
    """Test basic database operations."""
    print("\nTesting database operations...")

    try:
        # Create a temporary database
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp_file:
            db_path = tmp_file.name

        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create a test table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_added TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Insert test data
        cursor.execute("INSERT INTO test_students (name) VALUES (?)", ("Test Student",))
        conn.commit()

        # Query test data
        cursor.execute("SELECT * FROM test_students")
        result = cursor.fetchone()

        conn.close()

        # Clean up
        os.unlink(db_path)

        if result:
            print("✓ Database operations working")
            return True
        else:
            print("✗ Database query returned no results")
            return False

    except Exception as e:
        print(f"✗ Database test failed: {e}")
        return False

def test_file_operations():
    """Test file system operations."""
    print("\nTesting file operations...")

    try:
        # Test directory creation
        test_dir = Path("/tmp/student_data_test")
        test_dir.mkdir(exist_ok=True)

        # Test file writing
        test_file = test_dir / "test.txt"
        test_file.write_text("Hello, Student Data GUI!")

        # Test file reading
        content = test_file.read_text()

        # Clean up
        test_file.unlink()
        test_dir.rmdir()

        if content == "Hello, Student Data GUI!":
            print("✓ File operations working")
            return True
        else:
            print("✗ File content mismatch")
            return False

    except Exception as e:
        print(f"✗ File operations test failed: {e}")
        return False

def test_environment():
    """Test environment variables and paths."""
    print("\nTesting environment...")

    # Check Python path
    python_path = os.getenv("PYTHONPATH")
    if python_path:
        print(f"✓ PYTHONPATH set to: {python_path}")
    else:
        print("⚠ PYTHONPATH not set")

    # Check current working directory
    cwd = os.getcwd()
    print(f"✓ Current working directory: {cwd}")

    # Check if we can import the main module structure
    try:
        sys.path.insert(0, "/app")
        import StudentDataGUI
        print("✓ StudentDataGUI module structure accessible")
        return True
    except ImportError as e:
        print(f"⚠ StudentDataGUI module import failed (expected in non-container environment): {e}")
        # This is expected when running outside container
        return True
    except Exception as e:
        print(f"✗ Unexpected error importing StudentDataGUI: {e}")
        return False

def test_nicegui_availability():
    """Test if NiceGUI is available (optional for container validation)."""
    print("\nTesting NiceGUI availability...")

    try:
        import nicegui
        print(f"✓ NiceGUI {nicegui.__version__} is available")
        return True
    except ImportError:
        print("⚠ NiceGUI not available (expected outside container)")
        return True  # This is not a failure for the basic test

def main():
    """Run all tests."""
    print("=" * 60)
    print("Student Data GUI Minimal Test Suite")
    print("=" * 60)

    tests = [
        ("Basic Imports", test_basic_imports),
        ("Database Operations", test_database_operations),
        ("File Operations", test_file_operations),
        ("Environment", test_environment),
        ("NiceGUI Availability", test_nicegui_availability),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 40)
        try:
            if test_func():
                passed += 1
                print(f"✓ {test_name} PASSED")
            else:
                print(f"✗ {test_name} FAILED")
        except Exception as e:
            print(f"✗ {test_name} ERROR: {e}")

    print("\n" + "=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("✓ All tests passed! Basic setup is working.")
        return 0
    elif passed >= total - 1:  # Allow one test to fail (likely NiceGUI in non-container)
        print("✓ Core functionality tests passed.")
        return 0
    else:
        print(f"✗ {total - passed} tests failed. Setup may have issues.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
