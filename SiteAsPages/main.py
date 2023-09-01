#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for teachers
of students with Visual Impairments
"""
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                       #
#    email: hunsakerconsulting@gmail.com                                      #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");          #
#    you may not use this file except in compliance with the License.         #
#    You may obtain a copy of the License at                                  #
#                                                                             #
#    http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                             #
#    Unless Required by applicable law or agreed to in writing, software      #
#    distributed under the License is distributed on an "AS IS" BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
#    See the License for the specific language governing permissions and      #
#    limitations under the License.                                           #
###############################################################################

import datetime
import os
import shutil
import sqlite3
import sys
import traceback
from csv import writer
from pathlib import Path
from sqlite3 import Error

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from nicegui import app, ui
from plotly.subplots import make_subplots
from screeninfo import get_monitors

import homepage
import theme

import abacus
import braille
import braillenote
import contactLog
import ios
import cvi
import screenreader
from helpers import students

##############################################################################
# Define Paths
##############################################################################
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = ""
IMAGE_DIR = Path(ROOT_DIR).joinpath("images")
##############################################################################
# Set User Directory based on OS
##############################################################################
if os.name == "nt":
    try:
        tmppath = Path(os.environ["USERPROFILE"]).joinpath("Documents")
        Path.mkdir(tmppath, parents=True, exist_ok=True)
        USER_DIR = Path(tmppath)
    except Error as e:
        print(f"{e}\n Cannot find %USERPROFILE")
elif os.name == "posix":
    try:
        tmppath = Path(os.environ["HOME"]).joinpath("Documents")
        Path.mkdir(tmppath, parents=True, exist_ok=True)
        USER_DIR = Path(tmppath)
    except Error as e:
        print(f"{e}\n Cannot find $HOME")
else:
    print("Cannot determine OS Type")
os.chdir(USER_DIR)

##############################################################################
# Set User Folders and necessary files in ~/Documents for each Student
##############################################################################
for name in students:
    if not Path(USER_DIR).joinpath("StudentDatabase").exists():
        tmppath = Path(USER_DIR).joinpath("StudentDatabase")
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    if not Path(USER_DIR).joinpath("StudentDatabase", "errorLogs").exists():
        tmppath = Path(USER_DIR).joinpath("StudentDatabase", "errorLogs")
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    if not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles"
            ).exists():
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles"
                )
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name
                )
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name, "StudentDataSheets"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "StudentDataSheets"
                )
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "StudentInstructionMaterials"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "StudentInstructionMaterials"
                )
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "StudentVisionAssessments"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "StudentVisionAssessments"
                )
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name, "omnibusDatabase.csv"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "omnibusDatabase.csv"
                )
        Path.touch(tmppath)
        list_names = [
                "student",
                "date",
                "task",
                "lesson",
                "session",
                "trial01",
                "trial02",
                "trial03",
                "trial04",
                "trial05",
                "trial06",
                "trial07",
                "trial08",
                "trial09",
                "trial10",
                "trial11",
                "median",
                "notes",
                ]
        with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "BrailleSkillsProgression.csv"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "BrailleSkillsProgression.csv"
                )
        Path.touch(tmppath)
        list_names = [
                "date",
                "P1_1",
                "P1_2",
                "P1_3",
                "P1_4",
                "P2_1",
                "P2_2",
                "P2_3",
                "P2_4",
                "P2_5",
                "P2_6",
                "P2_7",
                "P2_8",
                "P2_9",
                "P2_10",
                "P2_11",
                "P2_12",
                "P2_13",
                "P2_14",
                "P2_15",
                "P3_1",
                "P3_2",
                "P3_3",
                "P3_4",
                "P3_5",
                "P3_6",
                "P3_7",
                "P3_8",
                "P3_9",
                "P3_10",
                "P3_11",
                "P3_12",
                "P3_13",
                "P3_14",
                "P3_15",
                "P4_1",
                "P4_2",
                "P4_3",
                "P4_4",
                "P5_1",
                "P5_2",
                "P5_3",
                "P5_4",
                "P6_1",
                "P6_2",
                "P6_3",
                "P6_4",
                "P6_5",
                "P6_6",
                "P6_7",
                "P7_1",
                "P7_2",
                "P7_3",
                "P7_4",
                "P7_5",
                "P7_6",
                "P7_7",
                "P7_8",
                "P8_1",
                "P8_2",
                "P8_3",
                "P8_4",
                "P8_5",
                "P8_6",
                "P8_7",
                ]
        with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "UEBLiterarySkillsProgression.html"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "UEBLiterarySkillsProgression.html"
                )
        Path.touch(tmppath)
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "UEBTechnicalSkillsProgression.html"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "UEBTechnicalSkillsProgression.html"
                )
        Path.touch(tmppath)
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "ScreenReaderSkillsProgression.csv"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "ScreenReaderSkillsProgression.csv"
                )
        Path.touch(tmppath)
        list_names = [
                "date",
                "P1_1",
                "P1_2",
                "P1_3",
                "P1_4",
                "P1_5",
                "P1_6",
                "P2_1",
                "P2_2",
                "P2_3",
                "P2_4",
                "P3_1",
                "P3_2",
                "P3_3",
                "P3_4",
                "P3_5",
                "P3_6",
                "P3_7",
                "P3_8",
                "P3_9",
                "P3_10",
                "P3_11",
                "P4_1",
                "P4_2",
                "P4_3",
                "P4_4",
                "P4_5",
                "P4_6",
                "P4_7",
                ]
        with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if (not Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "ScreenReaderSkillsProgression.html"
            ).exists()):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "ScreenReaderSkillsProgression.html"
                )
        Path.touch(tmppath)
    if (
            not Path(USER_DIR)
                    .joinpath(
                    "StudentDatabase", "StudentDataFiles", name,
                    "AbacusSkillsProgression.csv"
                    )
                    .exists()
    ):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "AbacusSkillsProgression.csv"
                )
        Path.touch(tmppath)
        list_names = [
                "date",
                "P1_1",
                "P1_2",
                "P1_3",
                "P1_4",
                "P2_1",
                "P2_2",
                "P2_3",
                "P3_1",
                "P3_2",
                "P3_3",
                "P4_1",
                "P4_2",
                "P5_1",
                "P5_2",
                "P6_1",
                "P6_2",
                "P6_3",
                "P6_4",
                "P7_1",
                "P7_2",
                "P7_3",
                "P7_4",
                "P8_1",
                "P8_2",
                ]
        with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if (
            not Path(USER_DIR)
                    .joinpath(
                    "StudentDatabase", "StudentDataFiles", name,
                    "AbacusSkillsProgression.html"
                    )
                    .exists()
    ):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "AbacusSkillsProgression.html"
                )
        Path.touch(tmppath)
    if (
            not Path(USER_DIR)
                    .joinpath(
                    "StudentDatabase", "StudentDataFiles", name,
                    "cviProgression.csv"
                    )
                    .exists()
    ):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "cviProgression.csv"
                )
        Path.touch(tmppath)
        list_names = [
                "date",
                "P1_1",
                "P1_2",
                "P1_3",
                "P1_4",
                "P1_5",
                "P1_6",
                "P2_1",
                "P2_2",
                "P2_3",
                "P2_4",
                ]
        with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if (
            not Path(USER_DIR)
                    .joinpath(
                    "StudentDatabase", "StudentDataFiles", name,
                    "cviProgression.html"
                    )
                    .exists()
    ):
        tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name,
                "cviProgression.html"
                )
        Path.touch(tmppath)
    
    sourceDir = Path(ROOT_DIR).joinpath("datasheets")
    destinationDir = Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name, "StudentDataSheets"
            )
    files = os.listdir(sourceDir)
    for fileName in files:
        shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)
    
    sourceDir = Path(ROOT_DIR).joinpath("instructionMaterials")
    destinationDir = Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "StudentInstructionMaterials"
            )
    files = os.listdir(sourceDir)
    for fileName in files:
        shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)
    
    sourceDir = Path(ROOT_DIR).joinpath("visionAssessments")
    destinationDir = Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name,
            "StudentVisionAssessments"
            )
    files = os.listdir(sourceDir)
    for fileName in files:
        shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)

##############################################################################
# Create SQL database with SQLite and create data tables
##############################################################################

dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")
'''print(f"SQLite version {sqlite3.sqlite_version}")
print(dataBasePath)'''
print("Program is Loading, Please be Patient")


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


create_connection(dataBasePath)

conn = sqlite3.connect(dataBasePath)


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


def createTables():
    """create tables within SQL database for all projects"""
    sql_create_studentdata_table = """CREATE TABLE IF NOT EXISTS STUDENTDATA(
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
    
    sql_create_abacusdata_table = """CREATE TABLE IF NOT EXISTS ABACUSPROGRESS(
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
    
    sql_create_cvidata_table = """CREATE TABLE IF NOT EXISTS CVIPROGRESS(
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


createTables()

datenow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")


##############################################################################
# Error Logging
##############################################################################
def warningmessage(exception_type, exception_value, exception_traceback):
    """
    exception_type (_type_): _description_
    exception_value (_type_): _description_
    exception_traceback (_type_): _description_
    """
    global i
    message = "Please make sure all fields are selected / filled out " \
              "properly\n\n"
    tb = traceback.format_exception(
            exception_type, exception_value, exception_traceback
            )
    log_path = Path(USER_DIR).joinpath(
            "StudentDatabase", "errorLogs", f"logfile_{date}.log"
            )
    Path.touch(log_path)
    for i in tb:
        message += i
    with open(log_path, "a") as log_file:
        log_file.write(f"{date}\n{i}" + "\n")
        errortype = str(exception_type)
    ui.notify(f"{message}\n{errortype}", 
              type='warning',
              close_button="OK")

sys.excepthook = warningmessage

##############################################################################
# Begin GUI
##############################################################################
@ui.page('/')
def index_page() -> None:
    with theme.frame('Student Skills Progressions'):
        homepage.content()

# contentpages.create()
abacus.create()
braille.create()
contactLog.create()
cvi.create()
ios.create()
braillenote.create()
screenreader.create()

'''
##############################################################################
# FOOTER
##############################################################################
with ui.footer(value=True) as footer:
    with ui.row().classes(
            "w-screen no-wrap justify-center items-center text-l font-bold"
            ):
        ui.label(
                "Copyright © 2023 Michael Ryan Hunsaker, M.Ed., Ph.D."
                ).classes(
                "justify-center items-center"
                )
    with ui.row().classes(
            "w-screen no-wrap justify-center items-centertext-l font-bold"
            ):
        ui.label(
                "Report Bugs or Request Features by emailing "
                "hunsakerconsulting@gmail.com"
                ).classes("justify-center items-center")
##############################################################################
# SIDEBAR
##############################################################################
with ui.left_drawer(value=True) as left_drawer:
    with ui.row().classes("w-full no-wrap"):
        ui.label("MATERIALS").classes(
       N         "w-screen no-wrap py-4 text-white font-bold text-xl "
                "justify-center items-center"
                )
    with ui.row().classes("w-full no-wrap"):
        ui.label("ABACUS").classes(
                "w-screen no-wrap font-bold text-white text-xl justify-center "
                "items-center"
                )
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Hadley Abacus Curriculum I",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/Abacus1.pdf",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Hadley Abacus Curriculum II",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/Abacus2.pdf",
                new_tab=True,
                ).classes("text-left w-full align-left text-white font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Abacus Made Easy",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/AbacusMadeEasy.pdf",
                new_tab=True,
                ).classes(
                "text-left w-full text-white align-left font-bold font-bold"
                )
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Using the Cranmer Abacus",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/UsingCranmerAbacus.pdf",
                new_tab=True,
                ).classes("text-left w-full align-left text-white font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Japanese Abacus Use and Theory",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/abacusUseTheory.pdf",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Advanced Japanese Abacus",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/AdvancedAbacus.pdf",
                new_tab=True,
                ).classes("text-left w-full align-left text-white font-bold")
    with ui.row().classes("w-full no-wrap"):
        ui.label("BRAILLE").classes(
                "w-screen no-wrap font-bold text-white text-xl justify-center "
                "items-center"
                )
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "NLS-IMBT UEB Literary Braille",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/NLSLOCLessons1-11.pdf",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "UEB Australian Training Manual",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/UEBAustralianTrainingManual.pdf",
                new_tab=True,
                ).classes("text-left w-full align-left text-white font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "UEB Technical Course",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/UEBTechnicalCourse.pdf",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "UEB Technical Guidelines",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/UEBTechnicalGuidelines.pdf",
                new_tab=True,
                ).classes("text-left w-full align-left text-white font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "UEB with Nemeth",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/NemethUEBContext.pdf",
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap"):
        ui.label("SCREENREADER").classes(
                "w-screen no-wrap font-bold text-white text-xl justify-center "
                "items-center"
                )
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "NVDA Trainings",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/NVDATrainings.pdf",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Windows Screen Reader Primer",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/instructionMaterials/WindowsScreenreaderPrimer.zip",
                new_tab=True,
                ).classes("text-left w-full align-left text-white font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Getting Started with Windows 11",
                "https://github.com/mrhunsaker/Materials/blob/main"
                "/instructionMaterials/GettingStartedWindows11.doc",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap"):
        ui.label("DATASHEETS").classes(
                "w-screen no-wrap content-center font-bold text-white text-xl"
                )
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Blank Vision Template",
                "https://github.com/mrhunsaker/Materials/raw/main/datasheets"
                "/BlankVisionTemplate.pdf",
                new_tab=True,
                ).classes("text-left w-screen text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Generic Data Sheets",
                "https://github.com/mrhunsaker/Materials/raw/main/datasheets"
                "/GenericDataSheets.pdf",
                new_tab=True,
                ).classes("text-left w-full align-left text-white font-bold")
    with ui.row().classes("w-full no-wrap py-4"):
        ui.link(
                "Bi-Weekly Progress Monitoring",
                "https://github.com/mrhunsaker/Materials/raw/main/datasheets"
                "/ProgressMonitoring.pdf",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
    with ui.row().classes("w-full no-wrap"):
        ui.label("ASSESSMENT FORMS").classes(
                "w-screen no-wrap py-4 font-bold text-white text-xl "
                "justify-center items-center"
                )
    with ui.row().classes("w-full no-wrap"):
        ui.link(
                "Educational Vision Evaluation Forms",
                "https://github.com/mrhunsaker/Materials/raw/main"
                "/visionAssessments/EducationVisionAssessments.pdf",
                new_tab=True,
                ).classes("text-left w-full text-white align-left font-bold")
'''
##############################################################################
# EXECUTE PROGRAM WINDOW
##############################################################################
'''Get Monitor Size to allow me to create the app to fill screen without
setting fullscreen=True. 72 is subtracted from the height to accommodate the
height of my Taskbar'''

for monitor in get_monitors():
    ScreenResolution = "{str(monitor.width)}x{str(monitor.height)}"

##############################################################################
# RUN CALL
##############################################################################
ui.run(
        native=True,
        reload=False,
        dark=False,
        title="Student Skills Progressions",
        fullscreen=False,
        window_size=(monitor.width, monitor.height - 72),
        )
##############################################################################
# END FILE
##############################################################################
