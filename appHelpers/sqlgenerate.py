#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""
#########################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                 #
#    email: hunsakerconsulting@gmail.com                                #
#                                                                       #
#                                                                       #
#    Licensed under the Apache License, Version 2.0 (the "License");    #
#    you may not use this file except in compliance with the License.   #
#    You may obtain a copy of the License at                            #
#    http://www.apache.org/licenses/LICENSE-2.0                         #
#                                                                       #
#    Unless Required by applicable law or agreed to in writing,         #
#    software distributed under the License is distributed on an        #
#    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,       #
#    either express or  implied.  See the License for the specific      #
#   language governing permissions and limitations under the License.   #
#########################################################################

import sqlite3
from sqlite3 import Error

from appHelpers.helpers import dataBasePath


##############################################################################
# Create SQL database with SQLite and create data tables
##############################################################################
def create_connection(db_file):
    """
    :param db_file:
    :type db_file:
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table(conn, sql_create_sql_table):
    """
    :param conn:
    :type conn:
    :param sql_create_sql_table:
    :type sql_create_sql_table:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_sql_table)
    except Error as e:
        print(e)
    conn.close()


conn = sqlite3.connect(dataBasePath)


def createTables():
    """create tables within SQL database for all projects"""
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
        P1_1 INTEGER NOT NULL,
        P1_2 INTEGER NOT NULL,
        P1_3 INTEGER NOT NULL,
        P1_4 INTEGER NOT NULL,
        P1_5 INTEGER NOT NULL,
        P1_6 INTEGER NOT NULL,
        P2_1 INTEGER NOT NULL,
        P2_2 INTEGER NOT NULL,
        P2_3 INTEGER NOT NULL,
        P2_4 INTEGER NOT NULL
    );"""

    sql_create_iosdata_table = """CREATE TABLE IF NOT EXISTS
    IOSPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER NOT NULL,
        P1_2 INTEGER NOT NULL,
        P1_3 INTEGER NOT NULL,
        P1_4 INTEGER NOT NULL,
        P1_5 INTEGER NOT NULL,
        P1_6 INTEGER NOT NULL,
        P1_7 INTEGER NOT NULL,
        P1_8 INTEGER NOT NULL,
        P1_9 INTEGER NOT NULL,
        P2_1 INTEGER NOT NULL,
        P2_2 INTEGER NOT NULL,
        P2_3 INTEGER NOT NULL,
        P2_4 INTEGER NOT NULL,
        P2_5 INTEGER NOT NULL,
        P2_6 INTEGER NOT NULL,
        P3_1 INTEGER NOT NULL,
        P3_2 INTEGER NOT NULL,
        P3_3 INTEGER NOT NULL,
        P3_4 INTEGER NOT NULL,
        P3_5 INTEGER NOT NULL,
        P4_1 INTEGER NOT NULL,
        P4_2 INTEGER NOT NULL,
        P4_3 INTEGER NOT NULL,
        P4_4 INTEGER NOT NULL,
        P4_5 INTEGER NOT NULL,
        P5_1 INTEGER NOT NULL,
        P5_2 INTEGER NOT NULL,
        P5_3 INTEGER NOT NULL,
        P5_4 INTEGER NOT NULL,
        P5_5 INTEGER NOT NULL,
        P5_6 INTEGER NOT NULL,
        P5_7 INTEGER NOT NULL,
        P6_1 INTEGER NOT NULL,
        P6_2 INTEGER NOT NULL,
        P6_3 INTEGER NOT NULL,
        P6_4 INTEGER NOT NULL,
        P6_5 INTEGER NOT NULL,
        P6_6 INTEGER NOT NULL,
        P6_7 INTEGER NOT NULL,
        P6_8 INTEGER NOT NULL,
        P6_9 INTEGER NOT NULL,
        P6_10 INTEGER NOT NULL,
        P6_11 INTEGER NOT NULL
    );"""

    sql_create_bntdata_table = """CREATE TABLE IF NOT EXISTS
    BNTPROGRESS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER NOT NULL,
        P1_2 INTEGER NOT NULL,
        P1_3 INTEGER NOT NULL,
        P1_4 INTEGER NOT NULL,
        P1_5 INTEGER NOT NULL,
        P1_6 INTEGER NOT NULL,
        P1_7 INTEGER NOT NULL,
        P1_8 INTEGER NOT NULL,
        P1_9 INTEGER NOT NULL,
        P2_1 INTEGER NOT NULL,
        P2_2 INTEGER NOT NULL,
        P2_3 INTEGER NOT NULL,
        P2_4 INTEGER NOT NULL,
        P2_5 INTEGER NOT NULL,
        P2_6 INTEGER NOT NULL,
        P2_7 INTEGER NOT NULL,
        P3_1 INTEGER NOT NULL,
        P3_2 INTEGER NOT NULL,
        P3_3 INTEGER NOT NULL,
        P3_4 INTEGER NOT NULL,
        P3_5 INTEGER NOT NULL,
        P3_6 INTEGER NOT NULL,
        P3_7 INTEGER NOT NULL,
        P4_1 INTEGER NOT NULL,
        P4_2 INTEGER NOT NULL,
        P4_3 INTEGER NOT NULL,
        P5_1 INTEGER NOT NULL,
        P5_2 INTEGER NOT NULL,
        P5_3 INTEGER NOT NULL,
        P5_4 INTEGER NOT NULL,
        P5_5 INTEGER NOT NULL,
        P5_6 INTEGER NOT NULL,
        P5_7 INTEGER NOT NULL,
        P6_1 INTEGER NOT NULL,
        P6_2 INTEGER NOT NULL,
        P6_3 INTEGER NOT NULL,
        P7_1 INTEGER NOT NULL,
        P7_2 INTEGER NOT NULL,
        P7_3 INTEGER NOT NULL,
        P7_4 INTEGER NOT NULL,
        P8_1 INTEGER NOT NULL,
        P8_2 INTEGER NOT NULL,
        P8_3 INTEGER NOT NULL,
        P8_4 INTEGER NOT NULL,
        P8_5 INTEGER NOT NULL,
        P9_1 INTEGER NOT NULL,
        P9_2 INTEGER NOT NULL,
        P9_3 INTEGER NOT NULL,
        P9_4 INTEGER NOT NULL,
        P10_1 INTEGER NOT NULL,
        P10_2 INTEGER NOT NULL,
        P10_3 INTEGER NOT NULL,
        P11_1 INTEGER NOT NULL,
        P11_2 INTEGER NOT NULL,
        P11_3 INTEGER NOT NULL,
        P11_4 INTEGER NOT NULL,
        P11_5 INTEGER NOT NULL,
        P12_1 INTEGER NOT NULL,
        P12_2 INTEGER NOT NULL,
        P12_3 INTEGER NOT NULL,
        P12_4 INTEGER NOT NULL
    );"""

    sql_create_elemdigitalliteracydata_table = """CREATE TABLE IF NOT
    EXISTS ELEMDIGITALLITERACY(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER NOT NULL,
        P1_2 INTEGER NOT NULL,
        P1_3 INTEGER NOT NULL,
        P1_4 INTEGER NOT NULL,
        P1_5 INTEGER NOT NULL,
        P1_6 INTEGER NOT NULL,
        P2_1 INTEGER NOT NULL,
        P2_2 INTEGER NOT NULL,
        P2_3 INTEGER NOT NULL,
        P2_4 INTEGER NOT NULL,
        P2_5 INTEGER NOT NULL,
        P2_6 INTEGER NOT NULL,
        P3_1 INTEGER NOT NULL,
        P3_2 INTEGER NOT NULL,
        P3_3 INTEGER NOT NULL,
        P3_4 INTEGER NOT NULL,
        P3_5 INTEGER NOT NULL,
        P4_1 INTEGER NOT NULL,
        P4_2 INTEGER NOT NULL,
        P4_3 INTEGER NOT NULL,
        P4_4 INTEGER NOT NULL,
        P4_5 INTEGER NOT NULL,
        P5_1 INTEGER NOT NULL,
        P5_2 INTEGER NOT NULL,
        P5_3 INTEGER NOT NULL,
        P5_4 INTEGER NOT NULL,
        P5_5 INTEGER NOT NULL,
        P5_6 INTEGER NOT NULL,
        P5_7 INTEGER NOT NULL,
        P6_1 INTEGER NOT NULL,
        P6_2 INTEGER NOT NULL,
        P6_3 INTEGER NOT NULL,
        P6_4 INTEGER NOT NULL,
        P7_1 INTEGER NOT NULL,
        P7_2 INTEGER NOT NULL,
        P7_3 INTEGER NOT NULL,
        P7_4 INTEGER NOT NULL,
        P7_5 INTEGER NOT NULL
    );"""

    sql_create_hsdigitalliteracydata_table = """CREATE TABLE IF NOT
    EXISTS HSDIGITALLITERACY(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENTNAME TEXT NOT NULL,
        DATE TEXT NOT NULL,
        P1_1 INTEGER NOT NULL,
        P1_2 INTEGER NOT NULL,
        P1_3 INTEGER NOT NULL,
        P1_4 INTEGER NOT NULL,
        P1_5 INTEGER NOT NULL,
        P2_1 INTEGER NOT NULL,
        P2_2 INTEGER NOT NULL,
        P2_3 INTEGER NOT NULL,
        P2_4 INTEGER NOT NULL,
        P2_5 INTEGER NOT NULL,
        P2_6 INTEGER NOT NULL,
        P2_7 INTEGER NOT NULL,
        P3_1 INTEGER NOT NULL,
        P3_2 INTEGER NOT NULL,
        P3_3 INTEGER NOT NULL,
        P3_4 INTEGER NOT NULL,
        P3_5 INTEGER NOT NULL,
        P3_6 INTEGER NOT NULL,
        P3_7 INTEGER NOT NULL,
        P4_1 INTEGER NOT NULL,
        P4_2 INTEGER NOT NULL,
        P4_3 INTEGER NOT NULL,
        P5_1 INTEGER NOT NULL,
        P5_2 INTEGER NOT NULL,
        P5_3 INTEGER NOT NULL,
        P5_4 INTEGER NOT NULL,
        P5_5 INTEGER NOT NULL,
        P6_1 INTEGER NOT NULL,
        P6_2 INTEGER NOT NULL,
        P6_3 INTEGER NOT NULL,
        P6_4 INTEGER NOT NULL,
        P6_5 INTEGER NOT NULL,
        P7_1 INTEGER NOT NULL,
        P7_2 INTEGER NOT NULL,
        P7_3 INTEGER NOT NULL,
        P7_4 INTEGER NOT NULL,
        P7_5 INTEGER NOT NULL,
        P7_6 INTEGER NOT NULL,
        P7_7 INTEGER NOT NULL,
        P7_8 INTEGER NOT NULL,
        P7_9 INTEGER NOT NULL,
        P8_1 INTEGER NOT NULL,
        P8_2 INTEGER NOT NULL,
        P8_3 INTEGER NOT NULL,
        P8_4 INTEGER NOT NULL,
        P8_5 INTEGER NOT NULL
    );"""
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_studentdata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_brailledata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_screenreaderdata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_abacusdata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_cvidata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_iosdata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_bntdata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_elemdigitalliteracydata_table)
        except Error as e:
            print(e)
    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        try:
            create_table(conn, sql_create_hsdigitalliteracydata_table)
        except Error as e:
            print(e)