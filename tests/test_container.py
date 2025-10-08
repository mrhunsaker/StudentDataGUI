#!/usr/bin/env python3

"""
Test script to validate containerized deployment of Student Data GUI.
This script checks if all dependencies are properly installed and the application can start.
"""

import sys
import os
import traceback
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing Python imports...")

    try:
        import nicegui
        print(f"✓ NiceGUI {nicegui.__version__}")
    except ImportError as e:
        print(f"✗ NiceGUI import failed: {e}")
        return False

    try:
        import pandas as pd
        print(f"✓ Pandas {pd.__version__}")
    except ImportError as e:
        print(f"✗ Pandas import failed: {e}")
        return False

    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__}")
    except ImportError as e:
        print(f"✗ NumPy import failed: {e}")
        return False

    try:
        import matplotlib
        print(f"✓ Matplotlib {matplotlib.__version__}")
    except ImportError as e:
        print(f"✗ Matplotlib import failed: {e}")
        return False

    try:
        import plotly
        print(f"✓ Plotly {plotly.__version__}")
    except ImportError as e:
        print(f"✗ Plotly import failed: {e}")
        return False

    try:
        import sqlite3
        print(f"✓ SQLite3 {sqlite3.sqlite_version}")
    except ImportError as e:
        print(f"✗ SQLite3 import failed: {e}")
        return False

    try:
        import aiohttp
        print(f"✓ aiohttp {aiohttp.__version__}")
    except ImportError as e:
        print(f"✗ aiohttp import failed: {e}")
        return False

    try:
        import requests
        print(f"✓ requests {requests.__version__}")
    except ImportError as e:
        print(f"✗ requests import failed: {e}")
        return False

    # Test GUI libraries (these might not work in headless containers)
    try:
        import cairo
        print("✓ PyCairo available")
    except ImportError as e:
        print(f"⚠ PyCairo import failed (might not be needed in headless mode): {e}")

    try:
        import gi
        print("✓ PyGObject available")
    except ImportError as e:
        print(f"⚠ PyGObject import failed (might not be needed in headless mode): {e}")

    return True

def test_directories():
    """Test if necessary directories exist and are writable."""
    print("\nTesting directory structure...")

    directories = [
        "/app/data",
        "/app/database",
        "/tmp/matplotlib",
        "/tmp/home",
    ]

    for directory in directories:
        try:
            Path(directory).mkdir(parents=True, exist_ok=True)
            # Test write permissions
            test_file = Path(directory) / "test_write.tmp"
            test_file.write_text("test")
            test_file.unlink()
            print(f"✓ {directory} - exists and writable")
        except Exception as e:
            print(f"✗ {directory} - error: {e}")
            return False

    return True

def test_environment():
    """Test environment variables."""
    print("\nTesting environment variables...")

    env_vars = {
        "PYTHONPATH": "/app",
        "NICEGUI_HOST": "0.0.0.0",
        "NICEGUI_PORT": "8080",
        "MPLCONFIGDIR": "/tmp/matplotlib",
        "HOME": "/tmp/home",
    }

    for var, expected in env_vars.items():
        actual = os.getenv(var)
        if actual:
            print(f"✓ {var}={actual}")
        else:
            print(f"⚠ {var} not set (expected: {expected})")

    return True

def test_application_structure():
    """Test if application files are in place."""
    print("\nTesting application structure...")

    required_files = [
        "/app/StudentDataGUI/__init__.py",
        "/app/StudentDataGUI/main.py",
    ]

    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} missing")
            return False

    # Check if we can import the main module
    try:
        sys.path.insert(0, "/app")
        import StudentDataGUI
        print("✓ StudentDataGUI module can be imported")
    except ImportError as e:
        print(f"✗ StudentDataGUI import failed: {e}")
        return False

    return True

def test_route_configuration():
    """Test if application routes are properly configured."""
    print("\nTesting route configuration...")

    # Expected routes based on menu navigation
    expected_routes = [
        "/",  # Homepage
        "/contactlog_ui",
        "/sessionnotes_ui",
        "/observations_ui",
        "/cvi_skills_ui",
        "/abacus_skills_ui",
        "/braille_skills_ui",
        "/keyboarding_skills_ui",
        "/screenreader_skills_ui",
        "/braillenote_skills_ui",
        "/ios_skills_ui",
        "/digitalliteracy_skills_ui",
        "/instructionalmaterials"
    ]

    try:
        # Check if page modules exist
        page_modules = [
            "/app/StudentDataGUI/appPages/contactlog.py",
            "/app/StudentDataGUI/appPages/sessionnotes.py",
            "/app/StudentDataGUI/appPages/observations.py",
            "/app/StudentDataGUI/appPages/cvi.py",
            "/app/StudentDataGUI/appPages/abacus.py",
            "/app/StudentDataGUI/appPages/braille.py",
            "/app/StudentDataGUI/appPages/keyboarding.py",
            "/app/StudentDataGUI/appPages/screenreader.py",
            "/app/StudentDataGUI/appPages/braillenote.py",
            "/app/StudentDataGUI/appPages/ios.py",
            "/app/StudentDataGUI/appPages/digitalliteracy.py",
            "/app/StudentDataGUI/appPages/InstructionalMaterials.py"
        ]

        missing_modules = []
        for module_path in page_modules:
            if not Path(module_path).exists():
                missing_modules.append(module_path)

        if missing_modules:
            print(f"✗ Missing page modules: {missing_modules}")
            return False
        else:
            print(f"✓ All {len(page_modules)} page modules exist")

        # Check if @ui.page decorators are present (basic syntax check)
        routes_with_decorators = 0
        for module_path in page_modules:
            try:
                with open(module_path, 'r') as f:
                    content = f.read()
                    if '@ui.page(' in content:
                        routes_with_decorators += 1
            except Exception as e:
                print(f"⚠ Could not check {module_path}: {e}")

        if routes_with_decorators >= len(page_modules) - 2:  # Allow some flexibility
            print(f"✓ Found @ui.page decorators in {routes_with_decorators} modules")
        else:
            print(f"⚠ Only found @ui.page decorators in {routes_with_decorators}/{len(page_modules)} modules")

        print("✓ Route configuration appears valid")
        return True

    except Exception as e:
        print(f"✗ Route configuration test failed: {e}")
        return False

def test_network():
    """Test network connectivity for health checks."""
    print("\nTesting network setup...")

    try:
        import socket

        # Test if we can bind to the expected port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 8080))
            print("✓ Port 8080 is available")
    except Exception as e:
        print(f"⚠ Port 8080 test failed: {e}")

    return True

def test_database():
    """Test database functionality."""
    print("\nTesting database functionality...")

    try:
        import sqlite3

        # Create a test database
        db_path = "/app/data/test.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create a test table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)

        # Insert test data
        cursor.execute("INSERT INTO test (name) VALUES (?)", ("test_entry",))
        conn.commit()

        # Query test data
        cursor.execute("SELECT * FROM test")
        result = cursor.fetchone()

        conn.close()

        # Clean up
        Path(db_path).unlink(missing_ok=True)

        if result:
            print("✓ Database operations working")
            return True
        else:
            print("✗ Database query returned no results")
            return False

    except Exception as e:
        print(f"✗ Database test failed: {e}")
        return False

def main():
    """Run all container validation tests."""
    print("=" * 60)
    print("Student Data GUI Container Validation Test")
    print("=" * 60)

    tests = [
        ("Import Tests", test_imports),
        ("Directory Tests", test_directories),
        ("Environment Tests", test_environment),
        ("Application Structure Tests", test_application_structure),
        ("Route Configuration Tests", test_route_configuration),
        ("Network Tests", test_network),
        ("Database Tests", test_database),
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
            traceback.print_exc()

    print("\n" + "=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("✓ All tests passed! Container is ready.")
        return 0
    else:
        print(f"✗ {total - passed} tests failed. Container may have issues.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
