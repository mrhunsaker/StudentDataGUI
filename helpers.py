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
import traceback
from csv import writer
from pathlib import Path
from sqlite3 import Error

from nicegui import ui

##############################################################################
# Set User Directory based on OS
##############################################################################

datenow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")
date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")
##############################################################################
# Set User Directory based on OS
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

dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")


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


##############################################################################
# Error Logging
##############################################################################
def warningmessage(exception_type, exception_value, exception_traceback):
    """
    exception_type (_type_): _description_
    exception_value (_type_): _description_
    exception_traceback (_type_): _description_
    """
    i = ''
    message = "Please make sure all fields are selected / filled out " \
              "properly\n\n"
    tb = traceback.format_exception(exception_type, exception_value, exception_traceback)
    log_path = Path(USER_DIR).joinpath("StudentDatabase", "errorLogs", f"logfile_{date}.log")
    Path.touch(log_path)
    for i in tb:
        message += i
    with open(log_path, "a") as log_file:
        log_file.write(f"{date}\n{i}" + "\n")
        errortype = str(exception_type)
    ui.notify(f"{message}\n{errortype}", type='warning', close_button="OK")


##############################################################################
# Current Students for Project
##############################################################################
students = ['DonaldChamberlain', 'AshlynnNelson', 'AvaWilson', 'BaraahAlArbid', 'BelleWinegar', 'CelestialNelson', 'ClairePeterson', 'ColbieBlodgett', 'ColeHalbasch', 'ElyseStephensen', 'EmmaTorres', 'GrantChristensen', 'HunterTrevino', 'JerseyLenoard', 'KahvonFord', 'LilyVanwagoner', 'MilesWebster', 'OliviaEvershed', 'PaulaSackett', 'PrimrosePeterson', 'RoninSorenson', 'TrinityKellum', 'TylerAshby']


##############################################################################
# End Variables
##############################################################################

##############################################################################
# Set User Folders and necessary files in ~/Documents for each Student
##############################################################################
def createFolderHierarchy():
    '''     creates folder hierarchy on user computer     '''
    for name in students:
        if not Path(USER_DIR).joinpath("StudentDatabase").exists():
            tmppath = Path(USER_DIR).joinpath("StudentDatabase")
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if not Path(USER_DIR).joinpath("StudentDatabase", "errorLogs").exists():
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "errorLogs")
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles").exists():
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles")
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name).exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name)
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentDataSheets").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentDataSheets")
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentInstructionMaterials").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentInstructionMaterials")
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentVisionAssessments").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentVisionAssessments")
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "omnibusDatabase.csv").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "omnibusDatabase.csv")
            Path.touch(tmppath)
            list_names = ["student", "date", "task", "lesson", "session", "trial01", "trial02", "trial03", "trial04", "trial05", "trial06", "trial07", "trial08", "trial09", "trial10", "trial11", "median", "notes", ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "BrailleSkillsProgression.csv").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "BrailleSkillsProgression.csv")
            Path.touch(tmppath)
            list_names = ["date", "P1_1", "P1_2", "P1_3", "P1_4", "P2_1", "P2_2", "P2_3", "P2_4", "P2_5", "P2_6", "P2_7", "P2_8", "P2_9", "P2_10", "P2_11", "P2_12", "P2_13", "P2_14", "P2_15", "P3_1", "P3_2", "P3_3", "P3_4", "P3_5", "P3_6", "P3_7", "P3_8", "P3_9", "P3_10", "P3_11", "P3_12", "P3_13", "P3_14", "P3_15", "P4_1", "P4_2", "P4_3", "P4_4", "P5_1", "P5_2", "P5_3", "P5_4", "P6_1", "P6_2", "P6_3", "P6_4", "P6_5", "P6_6", "P6_7", "P7_1", "P7_2", "P7_3", "P7_4", "P7_5", "P7_6", "P7_7", "P7_8", "P8_1",
                          "P8_2", "P8_3", "P8_4", "P8_5", "P8_6", "P8_7", ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "UEBLiterarySkillsProgression.html").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "UEBLiterarySkillsProgression.html")
            Path.touch(tmppath)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "UEBTechnicalSkillsProgression.html").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "UEBTechnicalSkillsProgression.html")
            Path.touch(tmppath)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "ScreenReaderSkillsProgression.csv").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "ScreenReaderSkillsProgression.csv")
            Path.touch(tmppath)
            list_names = ["date", "P1_1", "P1_2", "P1_3", "P1_4", "P1_5", "P1_6", "P2_1", "P2_2", "P2_3", "P2_4", "P3_1", "P3_2", "P3_3", "P3_4", "P3_5", "P3_6", "P3_7", "P3_8", "P3_9", "P3_10", "P3_11", "P4_1", "P4_2", "P4_3", "P4_4", "P4_5", "P4_6", "P4_7", ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "ScreenReaderSkillsProgression.html").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "ScreenReaderSkillsProgression.html")
            Path.touch(tmppath)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "AbacusSkillsProgression.csv").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "AbacusSkillsProgression.csv")
            Path.touch(tmppath)
            list_names = ["date", "P1_1", "P1_2", "P1_3", "P1_4", "P2_1", "P2_2", "P2_3", "P3_1", "P3_2", "P3_3", "P4_1", "P4_2", "P5_1", "P5_2", "P6_1", "P6_2", "P6_3", "P6_4", "P7_1", "P7_2", "P7_3", "P7_4", "P8_1", "P8_2", ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "AbacusSkillsProgression.html").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "AbacusSkillsProgression.html")
            Path.touch(tmppath)
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "cviProgression.csv").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "cviProgression.csv")
            Path.touch(tmppath)
            list_names = ["date", "P1_1", "P1_2", "P1_3", "P1_4", "P1_5", "P1_6", "P2_1", "P2_2", "P2_3", "P2_4", ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (not Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "cviProgression.html").exists()):
            tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "cviProgression.html")
            Path.touch(tmppath)
        
        sourceDir = Path(ROOT_DIR).joinpath("datasheets")
        destinationDir = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentDataSheets")
        files = os.listdir(sourceDir)
        for fileName in files:
            shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)
        
        sourceDir = Path(ROOT_DIR).joinpath("instructionMaterials")
        destinationDir = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentInstructionMaterials")
        files = os.listdir(sourceDir)
        for fileName in files:
            shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)
        
        sourceDir = Path(ROOT_DIR).joinpath("visionAssessments")
        destinationDir = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", name, "StudentVisionAssessments")
        files = os.listdir(sourceDir)
        for fileName in files:
            shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)
