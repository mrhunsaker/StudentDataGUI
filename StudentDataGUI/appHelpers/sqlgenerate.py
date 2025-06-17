#!/usr/bin/env python3

"""
Redesigned SQL schema for Student Data Application
- Normalized, avoids data duplication
- Uses foreign keys for relationships
- Suitable for tracking multiple types of student progress
- Start a new database with this schema
"""

import sqlite3
from sqlite3 import Error
import os

##############################################################################
# Database Path (now uses helpers logic for container compatibility)
##############################################################################
from .helpers import database_dir
DATABASE_PATH = database_dir
import logging

logging.debug(f"Resolved DATABASE_PATH: {DATABASE_PATH}")
##############################################################################
# Schema Definition
##############################################################################

SCHEMA = [
    # Core student table
    """
    CREATE TABLE IF NOT EXISTS Student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthdate TEXT,
        notes TEXT
    );
    """,

    # Table for different types of progress/tasks
    """
    CREATE TABLE IF NOT EXISTS ProgressType (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    );
    """,

    # Table for a session of progress (date, student, type)
    """
    CREATE TABLE IF NOT EXISTS ProgressSession (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        progress_type_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        notes TEXT,
        FOREIGN KEY(student_id) REFERENCES Student(id) ON DELETE CASCADE,
        FOREIGN KEY(progress_type_id) REFERENCES ProgressType(id) ON DELETE CASCADE
    );
    """,

    # Table for keyboarding results (example of a simple progress type)
    """
    CREATE TABLE IF NOT EXISTS KeyboardingResult (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER NOT NULL,
        program TEXT NOT NULL,
        topic TEXT NOT NULL,
        speed INTEGER NOT NULL,
        accuracy INTEGER NOT NULL,
        FOREIGN KEY(session_id) REFERENCES ProgressSession(id) ON DELETE CASCADE
    );
    """,

    # Table for generic trial-based progress (for tasks with multiple trials)
    """
    CREATE TABLE IF NOT EXISTS TrialResult (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER NOT NULL,
        task TEXT NOT NULL,
        lesson TEXT,
        session_label TEXT,
        trial_number INTEGER NOT NULL,
        score INTEGER,
        FOREIGN KEY(session_id) REFERENCES ProgressSession(id) ON DELETE CASCADE
    );
    """,

    # Table for storing median and notes for trial-based sessions
    """
    CREATE TABLE IF NOT EXISTS TrialSessionSummary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER NOT NULL UNIQUE,
        median FLOAT,
        notes TEXT,
        FOREIGN KEY(session_id) REFERENCES ProgressSession(id) ON DELETE CASCADE
    );
    """,

    # Table for storing progress on multi-part assessments (e.g., Braille, Screen Reader, etc.)
    """
    CREATE TABLE IF NOT EXISTS AssessmentPart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        progress_type_id INTEGER NOT NULL,
        code TEXT NOT NULL,
        description TEXT,
        UNIQUE(progress_type_id, code),
        FOREIGN KEY(progress_type_id) REFERENCES ProgressType(id) ON DELETE CASCADE
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS AssessmentResult (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER NOT NULL,
        part_id INTEGER NOT NULL,
        score INTEGER,
        FOREIGN KEY(session_id) REFERENCES ProgressSession(id) ON DELETE CASCADE,
        FOREIGN KEY(part_id) REFERENCES AssessmentPart(id) ON DELETE CASCADE
    );
    """
]

##############################################################################
# Schema Setup Functions
##############################################################################

def create_connection(db_file):
    """Create a SQLite database connection."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_tables(conn):
    """Create all tables defined in SCHEMA."""
    try:
        cursor = conn.cursor()
        for sql in SCHEMA:
            cursor.execute(sql)
        conn.commit()
        print("All tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

def initialize_database():
    """Initialize the database with the new schema."""
    try:
        if os.path.exists(DATABASE_PATH):
            logging.info(f"Database already exists at {DATABASE_PATH}.")
        else:
            logging.info(f"Creating new database at {DATABASE_PATH}.")
            conn = create_connection(DATABASE_PATH)
            if conn:
                create_tables(conn)
                conn.close()
                logging.info(f"Database initialized successfully at {DATABASE_PATH}.")
    except Exception as e:
        logging.error(f"Failed to initialize database at {DATABASE_PATH}: {e}")

##############################################################################
# Example Usage
##############################################################################

if __name__ == "__main__":
    initialize_database()

"""
SCHEMA DESIGN NOTES:

- Student: Each student is stored once.
- ProgressType: Each type of progress/assessment is stored once (e.g., 'Keyboarding', 'Braille', etc.).
- ProgressSession: Each session (date, student, type) is stored once, linking a student and a progress type on a date.
- KeyboardingResult: Stores keyboarding-specific results for a session.
- TrialResult: Stores individual trial results for a session (for tasks with multiple trials).
- TrialSessionSummary: Stores summary data (median, notes) for a trial-based session.
- AssessmentPart: Defines the parts for each assessment type (e.g., 'P1_1', 'P2_3' for Braille, etc.).
- AssessmentResult: Stores the score for each part of an assessment for a session.

To add a new assessment type (e.g., 'Braille', 'Screen Reader'), insert a row into ProgressType, then define its parts in AssessmentPart.
To record a student's progress, create a ProgressSession, then add results to the appropriate result table(s).

This schema is normalized, avoids data duplication, and supports extensibility for new assessment types.
"""
