#!/usr/bin/env python3

"""
 Copyright 2023  Michael Ryan Hunsaker, M.Ed., Ph.D.

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

# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""

import sqlite3
from sqlite3 import Error
from pathlib import Path
import os
from appHelpers.helpers import dataBasePath
from nicegui import ui

##############################################################################
# Create SQL database with SQLite and create data tables
##############################################################################
def create_connection(db_file):
    """
    Create a SQLite database connection.

    Parameters
    ----------
    db_file : str
        The path to the SQLite database file.

    Returns
    -------
    sqlite3.Connection
        A connection object to the SQLite database.

    Raises
    ------
    Error
        If an error occurs while connecting to the database.

    Examples
    --------
    >>> db_connection = create_connection("example.db")
    >>> # Use db_connection for database operations
    >>> # ...

    Note
    ----
    It is recommended to close the database connection after usage by calling the `close` method
    on the returned connection object.
    """
    conn = None
    print(f"Attempting to connect to: {db_file}")
    if os.path.exists(db_file):
        print("Database file exists.")
    else:
        print("Database file does not exist. Attempting to create it.")
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print(f"Connection successful. Database file: {db_file}")
    except Error as e:
        ui.notify(
            e,
            position="center",
            type="negative",
            close_button="OK",
        )
        print(e)
    finally:
        if conn:
            conn.close()
    return conn

dataBasePath = "/home/ryhunsaker/Documents/StudentDatabase/students.db"
create_connection(dataBasePath)
print(dataBasePath)

def create_table(conn, sql_create_sql_table):
    """
    Create a table in the SQLite database.

    Parameters
    ----------
    conn : sqlite3.Connection
        The SQLite database connection.
    sql_create_table : str
        The SQL statement to create the table.

    Returns
    -------
    None

    Raises
    ------
    Error
        If an error occurs while creating the table.

    Examples
    --------
    >>> # Assuming 'conn' is a valid SQLite database connection
    >>> create_table(conn, "CREATE TABLE IF NOT EXISTS example_table (id INTEGER PRIMARY KEY, name TEXT);")
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_sql_table)
    except Error as e:
        ui.notify(
            e,
            position="center",
            type="negative",
            close_button="OK",
        )
    conn.close()


def createTables():
    """
    Create tables within the SQLite database for all projects.

    This function creates multiple tables in the SQLite database, each designed
    to store progress data for different projects such as keyboarding, student data,
    braille progress, screen reader progress, abacus progress, CVI progress, iOS progress,
    braille note progress, and digital literacy progress.

    Returns
    -------
    None

    Examples
    --------
    >>> createTables()
    """
    sql_create_keyboarding_table = """CREATE TABLE IF NOT EXISTS
    KEYBOARDING(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        PROGRAM TEXT NOT NULL,
        TOPIC TEXT NOT NULL,
        SPEED INT NOT NULL,
        ACCURACY INT NOT NULL
    );"""
    sql_create_studentdata_table = """CREATE TABLE IF NOT EXISTS
    STUDENTDATA(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        TASK TEXT NOT NULL,
        LESSON TEXT NOT NULL,
        SESSION TEXT NOT NULL,
        TRIAL01 INTEGER,
        TRIAL02 INTEGER,
        TRIAL03 INTEGER,
        TRIAL04 INTEGER,
        TRIAL05 INTEGER,
        TRIAL06 INTEGER,
        TRIAL07 INTEGER,
        TRIAL08 INTEGER,
        TRIAL09 INTEGER,
        TRIAL10 INTEGER,
        TRIAL11 INTEGER,
        MEDIAN FLOAT,
        NOTES TEXT NOT NULL
    );"""

    sql_create_brailledata_table = """CREATE TABLE IF NOT EXISTS
    BRAILLEPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER,
        P1_2 INTEGER,
        P1_3 INTEGER,
        P1_4 INTEGER,
        P2_1 INTEGER,
        P2_2 INTEGER,
        P2_3 INTEGER,
        P2_4 INTEGER,
        P2_5 INTEGER,
        P2_6 INTEGER,
        P2_7 INTEGER,
        P2_8 INTEGER,
        P2_9 INTEGER,
        P2_10 INTEGER,
        P2_11 INTEGER,
        P2_12 INTEGER,
        P2_13 INTEGER,
        P2_14 INTEGER,
        P2_15 INTEGER,
        P3_1 INTEGER,
        P3_2 INTEGER,
        P3_3 INTEGER,
        P3_4 INTEGER,
        P3_5 INTEGER,
        P3_6 INTEGER,
        P3_7 INTEGER,
        P3_8 INTEGER,
        P3_9 INTEGER,
        P3_10 INTEGER,
        P3_11 INTEGER,
        P3_12 INTEGER,
        P3_13 INTEGER,
        P3_14 INTEGER,
        P3_15 INTEGER,
        P4_1 INTEGER,
        P4_2 INTEGER,
        P4_3 INTEGER,
        P4_4 INTEGER,
        P5_1 INTEGER,
        P5_2 INTEGER,
        P5_3 INTEGER,
        P5_4 INTEGER,
        P6_1 INTEGER,
        P6_2 INTEGER,
        P6_3 INTEGER,
        P6_4 INTEGER,
        P6_5 INTEGER,
        P6_6 INTEGER,
        P6_7 INTEGER,
        P7_1 INTEGER,
        P7_2 INTEGER,
        P7_3 INTEGER,
        P7_4 INTEGER,
        P7_5 INTEGER,
        P7_6 INTEGER,
        P7_7 INTEGER,
        P7_8 INTEGER,
        P8_1 INTEGER,
        P8_2 INTEGER,
        P8_3 INTEGER,
        P8_4 INTEGER,
        P8_5 INTEGER,
        P8_6 INTEGER,
        P8_7 INTEGER
    );"""

    sql_create_screenreaderdata_table = """CREATE TABLE IF NOT EXISTS
    SCREENREADERPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER,
        P1_2 INTEGER,
        P1_3 INTEGER,
        P1_4 INTEGER,
        P1_5 INTEGER,
        P1_6 INTEGER,
        P2_1 INTEGER,
        P2_2 INTEGER,
        P2_3 INTEGER,
        P2_4 INTEGER,
        P3_1 INTEGER,
        P3_2 INTEGER,
        P3_3 INTEGER,
        P3_4 INTEGER,
        P3_5 INTEGER,
        P3_6 INTEGER,
        P3_7 INTEGER,
        P3_8 INTEGER,
        P3_9 INTEGER,
        P3_10 INTEGER,
        P3_11 INTEGER,
        P4_1 INTEGER,
        P4_2 INTEGER,
        P4_3 INTEGER,
        P4_4 INTEGER,
        P4_5 INTEGER,
        P4_6 INTEGER,
        P4_7 INTEGER
    );"""

    sql_create_abacusdata_table = """CREATE TABLE IF NOT EXISTS
    ABACUSPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER,
        P1_2 INTEGER,
        P1_3 INTEGER,
        P1_4 INTEGER,
        P2_1 INTEGER,
        P2_2 INTEGER,
        P2_3 INTEGER,
        P3_1 INTEGER,
        P3_2 INTEGER,
        P3_3 INTEGER,
        P4_1 INTEGER,
        P4_2 INTEGER,
        P5_1 INTEGER,
        P5_2 INTEGER,
        P6_1 INTEGER,
        P6_2 INTEGER,
        P6_3 INTEGER,
        P6_4 INTEGER,
        P7_1 INTEGER,
        P7_2 INTEGER,
        P7_3 INTEGER,
        P7_4 INTEGER,
        P8_1 INTEGER,
        P8_2 INTEGER
    );"""

    sql_create_cvidata_table = """CREATE TABLE IF NOT EXISTS
    CVIPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER,
        P1_2 INTEGER,
        P1_3 INTEGER,
        P1_4 INTEGER,
        P1_5 INTEGER,
        P1_6 INTEGER,
        P2_1 INTEGER,
        P2_2 INTEGER,
        P2_3 INTEGER,
        P2_4 INTEGER
    );"""

    sql_create_iosdata_table = """CREATE TABLE IF NOT EXISTS
    IOSPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER,
        P1_2 INTEGER,
        P1_3 INTEGER,
        P1_4 INTEGER,
        P1_5 INTEGER,
        P1_6 INTEGER,
        P1_7 INTEGER,
        P1_8 INTEGER,
        P1_9 INTEGER,
        P2_1 INTEGER,
        P2_2 INTEGER,
        P2_3 INTEGER,
        P2_4 INTEGER,
        P2_5 INTEGER,
        P2_6 INTEGER,
        P3_1 INTEGER,
        P3_2 INTEGER,
        P3_3 INTEGER,
        P3_4 INTEGER,
        P3_5 INTEGER,
        P4_1 INTEGER,
        P4_2 INTEGER,
        P4_3 INTEGER,
        P4_4 INTEGER,
        P4_5 INTEGER,
        P5_1 INTEGER,
        P5_2 INTEGER,
        P5_3 INTEGER,
        P5_4 INTEGER,
        P5_5 INTEGER,
        P5_6 INTEGER,
        P5_7 INTEGER,
        P6_1 INTEGER,
        P6_2 INTEGER,
        P6_3 INTEGER,
        P6_4 INTEGER,
        P6_5 INTEGER,
        P6_6 INTEGER,
        P6_7 INTEGER,
        P6_8 INTEGER,
        P6_9 INTEGER,
        P6_10 INTEGER,
        P6_11 INTEGER
    );"""

    sql_create_bntdata_table = """CREATE TABLE IF NOT EXISTS
    BNTPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER,
        P1_2 INTEGER,
        P1_3 INTEGER,
        P1_4 INTEGER,
        P1_5 INTEGER,
        P1_6 INTEGER,
        P1_7 INTEGER,
        P1_8 INTEGER,
        P1_9 INTEGER,
        P2_1 INTEGER,
        P2_2 INTEGER,
        P2_3 INTEGER,
        P2_4 INTEGER,
        P2_5 INTEGER,
        P2_6 INTEGER,
        P2_7 INTEGER,
        P3_1 INTEGER,
        P3_2 INTEGER,
        P3_3 INTEGER,
        P3_4 INTEGER,
        P3_5 INTEGER,
        P3_6 INTEGER,
        P3_7 INTEGER,
        P4_1 INTEGER,
        P4_2 INTEGER,
        P4_3 INTEGER,
        P5_1 INTEGER,
        P5_2 INTEGER,
        P5_3 INTEGER,
        P5_4 INTEGER,
        P5_5 INTEGER,
        P5_6 INTEGER,
        P5_7 INTEGER,
        P6_1 INTEGER,
        P6_2 INTEGER,
        P6_3 INTEGER,
        P7_1 INTEGER,
        P7_2 INTEGER,
        P7_3 INTEGER,
        P7_4 INTEGER,
        P8_1 INTEGER,
        P8_2 INTEGER,
        P8_3 INTEGER,
        P8_4 INTEGER,
        P8_5 INTEGER,
        P9_1 INTEGER,
        P9_2 INTEGER,
        P9_3 INTEGER,
        P9_4 INTEGER,
        P10_1 INTEGER,
        P10_2 INTEGER,
        P10_3 INTEGER,
        P11_1 INTEGER,
        P11_2 INTEGER,
        P11_3 INTEGER,
        P11_4 INTEGER,
        P11_5 INTEGER,
        P12_1 INTEGER,
        P12_2 INTEGER,
        P12_3 INTEGER,
        P12_4 INTEGER
    );"""

    sql_create_digitalliteracydata_table = """CREATE TABLE IF NOT
    EXISTS DIGITALLITERACYPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER,
        P1_2 INTEGER,
        P1_3 INTEGER,
        P1_4 INTEGER,
        P1_5 INTEGER,
        P1_6 INTEGER,
        P2_1 INTEGER,
        P2_2 INTEGER,
        P2_3 INTEGER,
        P2_4 INTEGER,
        P2_5 INTEGER,
        P2_6 INTEGER,
        P3_1 INTEGER,
        P3_2 INTEGER,
        P3_3 INTEGER,
        P3_4 INTEGER,
        P3_5 INTEGER,
        P4_1 INTEGER,
        P4_2 INTEGER,
        P4_3 INTEGER,
        P4_4 INTEGER,
        P4_5 INTEGER,
        P5_1 INTEGER,
        P5_2 INTEGER,
        P5_3 INTEGER,
        P5_4 INTEGER,
        P5_5 INTEGER,
        P5_6 INTEGER,
        P5_7 INTEGER,
        P6_1 INTEGER,
        P6_2 INTEGER,
        P6_3 INTEGER,
        P6_4 INTEGER,
        P6_5 INTEGER,
        P7_1 INTEGER,
        P7_2 INTEGER,
        P7_3 INTEGER,
        P7_4 INTEGER,
        P7_5 INTEGER,
        P8_1 INTEGER,
        P8_2 INTEGER,
        P8_3 INTEGER,
        P8_4 INTEGER,
        P8_5 INTEGER,
        P8_6 INTEGER,
        P9_1 INTEGER,
        P9_2 INTEGER,
        P9_3 INTEGER,
        P9_4 INTEGER,
        P9_5 INTEGER,
        P10_1 INTEGER,
        P10_2 INTEGER,
        P10_3 INTEGER,
        P10_4 INTEGER,
        P10_5 INTEGER,
        P10_6 INTEGER,
        P10_7 INTEGER,
        P11_1 INTEGER,
        P11_2 INTEGER,
        P11_3 INTEGER,
        P12_1 INTEGER,
        P12_2 INTEGER,
        P12_3 INTEGER,
        P12_4 INTEGER,
        P12_5 INTEGER,
        P13_1 INTEGER,
        P13_2 INTEGER,
        P13_3 INTEGER,
        P13_4 INTEGER,
        P13_5 INTEGER,
        P14_1 INTEGER,
        P14_2 INTEGER,
        P14_3 INTEGER,
        P14_4 INTEGER,
        P14_5 INTEGER,
        P14_6 INTEGER,
        P14_7 INTEGER, 
        P14_8 INTEGER,
        P14_9 INTEGER,
        P15_1 INTEGER,
        P15_2 INTEGER,
        P15_3 INTEGER,
        P15_4 INTEGER,
        P15_5 INTEGER
    );"""

    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_keyboarding_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_studentdata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_brailledata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_screenreaderdata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_abacusdata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_cvidata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_iosdata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_bntdata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_digitalliteracydata_table)
        except Error as e:
            ui.notify(
                e,
                position="center",
                type="negative",
                close_button="OK",
            )
