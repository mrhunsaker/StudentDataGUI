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

import datetime
import os
import shutil
from csv import writer
from pathlib import Path


date_fmt = "%Y-%m-%d %H:%M:%S"

datenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = ""
IMAGE_DIR = Path(ROOT_DIR).joinpath("images")
START_DIR = ""


def set_start_dir() -> Path:
    """
    Create or retrieve the user directory path.

    This function determines the appropriate user directory path based on the operating system
    (Windows or POSIX) and creates the directory structure if it doesn't exist. The user directory
    path is typically used for storing application-related data.

    Returns
    -------
    Path
        The path to the user directory.

    Raises
    ------
    NameError
        If the environment variable representing the user directory is not found.

    Examples
    --------
    >>> user_directory = create_user_dir()
    >>> # Use user_directory for storing application-related data
    >>> # ...

    Notes
    -----
    The user directory path may vary depending on the operating system:
    - On Windows, it is typically under "%USERPROFILE%\OneDrive - Davis School District\Documents".
    - On POSIX systems, it is typically under "$HOME/OneDrive - Davis School District/Documents".
    """
    if os.name == "nt":
        try:
            tmp_path = Path(os.environ["USERPROFILE"]).joinpath("Documents")
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            START_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find %USERPROFILE")
    elif os.name == "posix":
        try:
            tmp_path = Path(os.environ["HOME"]).joinpath("Documents")
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            START_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find $HOME")
    else:
        print("Cannot determine OS Type")
    os.chdir(START_DIR)
    return START_DIR


START_DIR = set_start_dir()


def working_dir() -> None:
    """
    Copy the working directory information to the application's root.

    This function checks if the 'workingdirectory.py' file exists in the application's
    root directory. If not, it copies the 'workingdirectory.txt' file from the
    'START_DIR' (presumably a predefined starting directory) to the application's root
    directory, naming the copy 'workingdirectory.py'.

    Returns
    -------
    None

    Examples
    --------
    >>> working_dir()
    >>> # 'workingdirectory.py' is copied to the application's root directory
    >>> # ...

    Notes
    -----
    This function assumes the existence of 'ROOT_DIR' and 'START_DIR' variables
    representing the application's root and starting directories, respectively.
    """
    if not Path(ROOT_DIR).joinpath("workingdirectory.py").exists():
        workingdirectory_path = Path(ROOT_DIR).joinpath("workingdirectory.py")
        tmp_path = Path(START_DIR).joinpath("workingdirectory.txt")
        shutil.copy2(tmp_path, workingdirectory_path)


working_dir()


def create_roster() -> None:
    """
    Create the roster file for the application.

    This function checks if the 'roster' directory exists in the 'appHelpers'
    subdirectory of the application's root directory. If not, it copies the
    'roster.txt' file from the 'START_DIR' (presumably a predefined starting
    directory) to the 'appHelpers' subdirectory, naming the copy 'roster.py'.

    Returns
    -------
    None

    Examples
    --------
    >>> create_roster()
    >>> # 'roster.py' is created in the 'appHelpers' subdirectory
    >>> # ...

    Notes
    -----
    This function assumes the existence of 'ROOT_DIR' and 'START_DIR' variables
    representing the application's root and starting directories, respectively.
    """
    if not Path(ROOT_DIR).joinpath("appHelpers", "roster").exists():
        roster_path = Path(ROOT_DIR).joinpath("roster.py")
        tmp_path = Path(START_DIR).joinpath("roster.txt")
        shutil.copy2(tmp_path, roster_path)


create_roster()

from appHelpers.roster import students
from appHelpers.workingdirectory import create_user_dir

create_user_dir()

USER_DIR = create_user_dir()

dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")


def createFolderHierarchy() -> None:
    """
    Create a folder hierarchy on the user's computer for student data.

    This function iterates over a list of student names and checks if the
    corresponding folder structure exists in the specified user directory
    (`USER_DIR`). If not, it creates the required directory structure and
    initializes necessary files.

    Returns
    -------
    None

    Examples
    --------
    >>> createFolderHierarchy()
    >>> # Folder hierarchy and files created in the specified user directory
    >>> # ...

    Notes
    -----
    This function assumes the existence of the `students`, `USER_DIR`, `ROOT_DIR`,
    `workingdirectory.py`, and other variables representing the application's
    student data and file paths.

    The function creates the following directory structure:
    - StudentDatabase
        - errorLogs
        - StudentDataFiles
            - [StudentName]
                - StudentDataSheets
                - StudentInstructionMaterials
                - StudentVisionAssessments
                - omnibusDatabase.csv
                - BrailleSkillsProgression.csv
                - UEBLiterarySkillsProgression.html
                - UEBTechnicalSkillsProgression.html
                - BasicTactileRecognition.html
                - ScreenReaderSkillsProgression.csv
                - ScreenReaderSkillsProgression.html
                - AbacusSkillsProgression.csv
                - AbacusSkillsProgression.html
                - cviProgression.csv
                - cviProgression.html
                - digitalliteracyProgression.csv
                - digitalliteracyProgression.html
                - iosProgression.csv
                - iosProgression.html
                - bntProgression.csv
                - bntProgression.html
    """
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
        if (
            not Path(USER_DIR)
            .joinpath("StudentDatabase", "StudentDataFiles", name)
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name
            )
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if (
            not Path(USER_DIR)
            .joinpath("StudentDatabase", "StudentDataFiles", name, "StudentDataSheets")
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "StudentDataSheets"
            )
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "StudentInstructionMaterials",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "StudentInstructionMaterials",
            )
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase", "StudentDataFiles", name, "StudentVisionAssessments"
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "StudentVisionAssessments"
            )
            Path.mkdir(tmppath, parents=True, exist_ok=True)
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase", "StudentDataFiles", name, "omnibusDatabase.csv"
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "omnibusDatabase.csv"
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
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "BrailleSkillsProgression.csv",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "BrailleSkillsProgression.csv",
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
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "UEBLiterarySkillsProgression.html",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "UEBLiterarySkillsProgression.html",
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "UEBTechnicalSkillsProgression.html",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "UEBTechnicalSkillsProgression.html",
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "BasicTactileRecognition.html",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "BasicTactileRecognition.html",
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "ScreenReaderSkillsProgression.csv",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "ScreenReaderSkillsProgression.csv",
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
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "ScreenReaderSkillsProgression.html",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "ScreenReaderSkillsProgression.html",
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "AbacusSkillsProgression.csv",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "AbacusSkillsProgression.csv",
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
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "AbacusSkillsProgression.html",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "AbacusSkillsProgression.html",
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath("StudentDatabase", "StudentDataFiles", name, "cviProgression.csv")
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "cviProgression.csv"
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
                "StudentDatabase", "StudentDataFiles", name, "cviProgression.html"
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "cviProgression.html"
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "digitalliteracyProgression.csv",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "digitalliteracyProgression.csv",
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
                "P2_5",
                "P2_6",
                "P3_1",
                "P3_2",
                "P3_3",
                "P3_4",
                "P3_5",
                "P4_1",
                "P4_2",
                "P4_3",
                "P4_4",
                "P4_5",
                "P5_1",
                "P5_2",
                "P5_3",
                "P5_4",
                "P5_5",
                "P5_6",
                "P5_7",
                "P6_1",
                "P6_2",
                "P6_3",
                "P6_4",
                "P6_5",
                "P7_1",
                "P7_2",
                "P7_3",
                "P7_4",
                "P7_5",
                "P8_1",
                "P8_2",
                "P8_3",
                "P8_4",
                "P8_5",
                "P8_6",
                "P9_1",
                "P9_2",
                "P9_3",
                "P9_4",
                "P9_5",
                "P10_1",
                "P10_2",
                "P10_3",
                "P10_4",
                "P10_5",
                "P10_6",
                "P10_7",
                "P11_1",
                "P11_2",
                "P11_3",
                "P12_1",
                "P12_2",
                "P12_3",
                "P12_4",
                "P12_5",
                "P13_1",
                "P13_2",
                "P13_3",
                "P13_4",
                "P13_5",
                "P14_1",
                "P14_2",
                "P14_3",
                "P14_4",
                "P14_5",
                "P14_6",
                "P14_7",
                "P14_8",
                "P14_9",
                "P15_1",
                "P15_2",
                "P15_3",
                "P15_4",
                "P15_5",
            ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "digitalliteracyProgression.html",
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                name,
                "digitalliteracyProgression.html",
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath("StudentDatabase", "StudentDataFiles", name, "iosProgression.csv")
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "iosProgression.csv"
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
                "P1_7",
                "P1_8",
                "P1_9",
                "P2_1",
                "P2_2",
                "P2_3",
                "P2_4",
                "P2_5",
                "P2_6",
                "P3_1",
                "P3_2",
                "P3_3",
                "P3_4",
                "P3_5",
                "P4_1",
                "P4_2",
                "P4_3",
                "P4_4",
                "P4_5",
                "P5_1",
                "P5_2",
                "P5_3",
                "P5_4",
                "P5_5",
                "P5_6",
                "P5_7",
                "P6_1",
                "P6_2",
                "P6_3",
                "P6_4",
                "P6_5",
                "P6_6",
                "P6_7",
                "P6_8",
                "P6_9",
                "P6_10",
                "P6_11",
            ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase", "StudentDataFiles", name, "iosProgression.html"
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "iosProgression.html"
            )
            Path.touch(tmppath)
        if (
            not Path(USER_DIR)
            .joinpath("StudentDatabase", "StudentDataFiles", name, "bntProgression.csv")
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "bntProgression.csv"
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
                "P1_7",
                "P1_8",
                "P1_9",
                "P2_1",
                "P2_2",
                "P2_3",
                "P2_4",
                "P2_5",
                "P2_6",
                "P2_7",
                "P3_1",
                "P3_2",
                "P3_3",
                "P3_4",
                "P3_5",
                "P3_6",
                "P3_7",
                "P4_1",
                "P4_2",
                "P4_3",
                "P5_1",
                "P5_2",
                "P5_3",
                "P5_4",
                "P5_5",
                "P5_6",
                "P5_7",
                "P6_1",
                "P6_2",
                "P6_3",
                "P7_1",
                "P7_2",
                "P7_3",
                "P7_4",
                "P8_1",
                "P8_2",
                "P8_3",
                "P8_4",
                "P8_5",
                "P9_1",
                "P9_2",
                "P9_3",
                "P9_4",
                "P10_1",
                "P10_2",
                "P10_3",
                "P11_1",
                "P11_2",
                "P11_3",
                "P11_4",
                "P11_5",
                "P12_1",
                "P12_2",
                "P12_3",
                "P12_4",
            ]
            with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                writer_setup = writer(f_object)
                writer_setup.writerow(list_names)
                f_object.close()
        if (
            not Path(USER_DIR)
            .joinpath(
                "StudentDatabase", "StudentDataFiles", name, "bntProgression.html"
            )
            .exists()
        ):
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase", "StudentDataFiles", name, "bntProgression.html"
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
            "StudentDatabase", "StudentDataFiles", name, "StudentInstructionMaterials"
        )
        files = os.listdir(sourceDir)
        for fileName in files:
            shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)
        sourceDir = Path(ROOT_DIR).joinpath("visionAssessments")
        destinationDir = Path(USER_DIR).joinpath(
            "StudentDatabase", "StudentDataFiles", name, "StudentVisionAssessments"
        )
        files = os.listdir(sourceDir)
        for fileName in files:
            shutil.copy2(os.path.join(sourceDir, fileName), destinationDir)


"""
Dictionary of specific Tasks organized by task Domain to be used on the Session Notes page to specifically choose the specific task by Domain
"""
task_domains = {
    "Choose a Task Domain": ["Choose a Task"],
    "abacusSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "1.1. Setting Numbers",
        "1.2. Clearing Beads",
        "1.3. Place Value",
        "1.4. Vocabulary",
        "2.1. Addition of Single Digit Numbers",
        "2.2. Addition of Multiple Digit Numbers – Direct",
        "2.3. Addition of Multiple Digit Numbers – Indirect",
        "3.1. Subtraction",
        "3.2. Subtraction of Multiple Digit Numbers – Direct",
        "3.3. Subtraction of Multiple Digit Numbers – Indirect",
        "4.1. Multiplication – 2+ Digit Multiplicand  1 Digit Multiplier",
        "4.2. Multiplication – 2+ Digit Multiplicand AND Multiplier",
        "5.1. Division – 2+ Digit Dividend  1 Digit Divisor ",
        "5.2. Division – 2+ Digit Dividend AND 1 Digit Divisor ",
        "6.1. Addition of Decimals",
        "6.2. Subtraction of Decimals",
        "6.3. Multiplication of Decimals",
        "6.4. Division of Decimals",
        "7.1. Addition of Fractions",
        "7.2. Subtraction of Fractions",
        "7.3. Multiplication of Fractions",
        "7.4. Division of Fractions",
        "8.1. Percent",
        "8.2. Square Root",
    ],
    "brailleSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "1.1. Track left to right",
        "1.2. Track top to bottom",
        "1.3. Discriminate shapes",
        "1.4. Discriminate braille characters",
        "2.1. Mangold Progression: G C L",
        "2.2. Mangold Progression: D Y",
        "2.3. Mangold Progression: A B",
        "2.4. Mangold Progression: S",
        "2.5. Mangold Progression: W",
        "2.6. Mangold Progression: P O",
        "2.7. Mangold Progression: K",
        "2.8. Mangold Progression: R",
        "2.9. Mangold Progression: M E",
        "2.10. Mangold Progression: H",
        "2.11. Mangold Progression: N X",
        "2.12. Mangold Progression: Z F",
        "2.13. Mangold Progression: U T",
        "2.14. Mangold Progression: Q I",
        "2.15. Mangold Progression: V J ",
        "3.1. Alphabetic Wordsigns",
        "3.2. Braille Numbers",
        "3.3. Punctuation",
        "3.4. Strong Contractions (AND OF FOR WITH THE)",
        "3.5. Strong Groupsigns (CH GH SH TH WH ED ER OU OW ST AR ING)",
        "3.6. Strong Wordsigns (CH SH TH WH OU ST)",
        "3.7. Lower Groupsigns (BE CON DIS)",
        "3.8. Lower Groupsigns (EA BB CC FF GG)",
        "3.9. Lower Groupsigns/Wordsigns (EN IN)",
        "3.10. Lower Wordsigns (BE HIS WAS WERE)",
        "3.11. Dot 5 Contractions",
        "3.12. Dot 45 Contractions",
        "3.13. Dot 456 Contractions",
        "3.14. Final Letter Groupsigns",
        "3.15. Shortform Words",
        "4.1. Grade 1 Indicators",
        "4.2. Capitals Indicators",
        "4.3. Numeric Mode and Spatial math",
        "4.4. Typeform Indicators (ITALIC  SCRIPT  UNDERLINE  BOLDFACE)",
        "5.1. Page Numbering",
        "5.2. Headings",
        "5.3. Lists",
        "5.4. Poety / Drama",
        "6.1.  Operation and Comparison Signs",
        "6.2. Grade 1 Mode",
        "6.3. Special Print Symbols",
        "6.4. Omission Marks",
        "6.5. Shape Indicators",
        "6.6. Roman Numerals",
        "6.7. Fractions",
        "7.1. Grade 1 Mode and Algebra",
        "7.2. Grade 1 Mode and Fractions",
        "7.3. Advanced Operation and Comparison Signs",
        "7.4. Indices",
        "7.5. Roots and Radicals",
        "7.6. Miscellaneous Shape Indicators",
        "7.7. Functions",
        "7.8. Greek letters",
        "8.1. Functions",
        "8.2. Modifiers  Bars  and Dots",
        "8.3. Modifiers  Arrows  and Limits",
        "8.4. Probability",
        "8.5. Calculus: Differentiation",
        "8.6. Calculus: Integration",
        "8.7. Vertical Bars",
    ],
    "brailleDisplaySkills": [
        "1.1 Physical Layout",
        "1.2 Setup/Universal Commands",
        "1.3 BNT+ Navigation",
        "1.4 File System navigation",
        "1.5 Main Menu Options",
        "1.6 Settings Menus",
        "1.7 Read Book with EasyReader Plus",
        "1.8 Braille Terminal",
        "1.9 System Updates",
        "2.1 Creating folders",
        "2.2 Differences among drives, folders, and files",
        "2.3 Navigating in the file browser",
        "2.4 Moving, copying and pasting file and folders",
        "2.5 Renaming a file or a folder",
        "2.6 Sharing files",
        "2.7 File and folder commands",
        "3.1 Editing Document in Keyword",
        "3.2 Create a Document in Keyword",
        "3.3 Open a Document in Keyword",
        "3.4 Save a Document in Keyword",
        "3.5 Read a Document in Keyword",
        "3.6 Visual Preview",
        "3.7 Save as Word File",
        "4.1 Create and edit math object",
        "4.2 Paste into KeyWord",
        "4.3 Generate and Read Graphics",
        "5.1 Setting up an email account",
        "5.2 Writing and sending emails",
        "5.3 Attaching a file",
        "5.4 Reading and searching for emails",
        "5.5 Viewing attached files",
        "5.6 Marking, highlighting, deleting, and other email  options",
        "5.7 Deleting an email account",
        "6.1 Launching KeySlides",
        "6.2 Opening a PowerPoint document",
        "6.3 Navigating in your presentation document",
        "7.1 Creating appointments",
        "7.2 Viewing, editing and deleting appointments",
        "7.3 Navigating the agenda",
        "7.4 Navigating Day View",
        "8.1 Internet Browsing with Chrome",
        "8.2 Internet Navigation",
        "8.3 Bookmarks",
        "8.4 History",
        "8.5 Downloading Files",
        "9.1 Inputting calculations",
        "9.2 Inserting a Math symbol in KeyCalc",
        "9.3 Show results as fractions or decimals",
        "9.4 History",
        "10.1 Opening .brf and .brl files",
        "10.2 Creating a .brf or .brl file",
        "10.3 Finding Braille Text",
        "11.1 Creating a Python File",
        "11.2 Opening, Navigating and Editing a Python File",
        "11.3 Indentations",
        "11.4 Saving a Python File",
        "11.5 Coding with KeyCode",
        "12.1 Third Party Apps",
        "12. Downloading",
        "12.3 Deleting",
        "12.4 Usage",
    ],
    "cviSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "colorPreference",
        "needForMovement",
        "visualLatency",
        "visualFieldPreference",
        "visualComplexity",
        "nonpurposefulGaze",
        "distanceViewing",
        "visualReflexes",
        "visualNovelty",
        "visuallyGuidedReach",
    ],
    "iOSSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "Select and speak an item",
        "Select the previous / next item",
        "Move into / out of a group of items",
        "Select the first / last item on the screen",
        "Speak the entire screen from the top",
        "Speak the entire screen from the selected item",
        "Pause or continue speaking",
        "Speak additional information such as the position within a list or whether text is selected",
        "Drag over the screen",
        "Scroll up /down one page",
        "Scroll left / right  one page",
        "Activate the selected item",
        "Double-tap the selected item",
        "Drag a slider",
        "Dismiss an alert or return to the previous screen",
        "Edit an item label to make it easier to find",
        "Navigate forms",
        "Help with current element",
        "Toggle screen curtain on/off",
        "Split tap quick activation",
        "Double-press button",
        "Speak words/characters typed",
        "Access control center",
        "Backspace",
        "Write letters  numbers  punctuation",
        "Change case  punctuation  numbers",
        "Insert space",
        "Choose a rotor setting",
        "Change keyboard mode",
    ],
    "keyboardingSkills": [
        "Home Row",
        "Top Row",
        "Bottom Row",
        "Numbers",
        "Modifier Keys",
        "F-Keys",
        "Shortcut Keystrokes",
        "Custom Shortcut Keystrokes",
    ],
    "screenreaderSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "1.1. Turn on and off the screen reader",
        "1.2 Utilize modifier keys ",
        "1.3. Read text ",
        "1.4. Identify the titles with headings",
        "1.5. Access documents  open programs  navigate to desktop",
        "1.6. Switch program focus",
        "2.1. Type with all keys",
        "2.2. Change screen reader settings",
        "2.3. Cursor Placement",
        "2.4. Select  copy and paste text",
        "3.1. Define common element types",
        "3.2. Identify each element by type.",
        "3.3. Navigate to the address bar",
        "3.4. Method 1 - Navigate by Clickable Object",
        "3.5. Method 2 - Quick Keys",
        "3.6. Method 3 - Elements Lists",
        "3.7. Justify Why they used a method",
        "3.8. Switch tab focus",
        "3.9. Switch between screen reader modes",
        "3.10. Navigate a table",
        "3.11. Develop a navigation sequence",
        "4.1. Save and open files",
        "4.2. Create and move folders",
        "4.3. navigate a cloud-based file management system",
        "4.4. Download material from the internet",
        "4.5. Extract zipped folders",
        "4.6. Utilize virtual cursors",
        "4.7. Use OCR",
    ],
    "ECC_CareerEducation": [
        "SELECT SKILL FROM DROPDOWN",
        "Career awareness: differentiating between work and play  understanding the value of work",
        "Career exploration: developing awareness of careers  researching careers of interest",
        "Career preparation: reading and understanding want ads  recognizing typical job adaptations make by workers with visual impairments  developing prevocationals skills (such as work habits  attitudes  and motivation)  and having vocational interests",
        "Career placement: preparing resumes  completing applications  participating in interviews  participating in work",
        "Listen and attend to others",
        "Follow directions",
        "Stay on task",
        "Complete tasks",
        "Play make believe and dress-up activities to imitate adult roles",
        "Have responsibilities at home and school",
        "Recognize different school & community workers",
        "Participate in problem solving (locating lost items independently  for example)",
        "React appropriately to unexpected changes or events",
        "Learn to work individually and in a group",
        "Learn to be responsible for actions",
        "Recognize that workers get paid",
        "Develop good communication skills",
        "Understand the rewards of work",
        "Organize resources such as time and money",
        "Meet increased responsibilities at home  school and the community",
        "Show well-developed academic  thinking and work behavior skills",
        "Participate in work activities and jobs and possibly work part time",
        "Show an understanding  of work performed by adults and what is involved in being successful in multiple areas of work",
        "Show interest in particular areas of work",
        "Plan for life beyond high school",
    ],
    "ECC_SocialInteractionSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "Appropriate body language: knowing when to lean forward to hear a secret from a friend  maintaining appropriate eye contact  facing a person who is speaking  standing up to greet a new friend keeping hands to oneself during a group conversation",
        "Social communication: engaging in appropriate verbal and nonverbal interaction with others  initiating conversations  expressing needs and wants",
        "Effective conversation patterns:  asking for help; initiating  maintaining and end ending conversations; extending invitations",
        "Cooperative skills: working  with another to accomplish a goal  volunteering to help in the classroom  helping with home chores",
        "Interactions with others:  knowing how to react to humor  identify the person in charge in a given situation and respond  to the presence of a peer; develop dating skills",
        "Social etiquette: demonstrate courteous behavior  thanking a friend for a gift  sharing a seat with another on the bus  smiling at others.",
        "Development of relationships and friendships: taking turns  seeking friendships with others  working effectively in groups",
        "Knowledge of self: knowing one’s likes and dislikes  taking responsibility for actions  understanding the concept of personal body space  showing pride in accomplished tasks  stating one’s point of view",
        "Interpretation and monitoring of social behavior: knowing when to disobey an adult understanding the appropriate time to ask questions developing problem solving skills, recognizing sarcasm in a conversation, understanding the difference between reacting to requests from strangers and familiar people.",
    ],
    "ECC_IndependentLivingSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "Organization: Maintaining school notes and materials where can be accessed easily  prioritizing daily demands of everyday life and of school and work  and keeping personal objects in a specific location",
        "Personal hygiene and grooming:bathing  maintaining feminine and masculine hygiene and understanding and ensuring privacy",
        "Dressing: participating in dressing oneself with independence  and determining appropriate clothing for the weather",
        "Clothing care: labeling  clothing  selecting appropriate clothing for events  doing laundry and performing related tasks",
        "Time management: establishing a routine of sleeping at appropriate times  recognizing how long it takes to complete a task  using watches and clocks and maintaining a calendar",
        "Eating: eating with utensils   locating food on a plate  using condiments and using tableware",
        "Cooking: preparing and cooking meals pouring liquids retrieving utensils  stirring and mixing  spreading and spooning  helping with dishes  using a stove  cleaning up  learning food-related concepts involved in gardening  visiting grocery stores  applying food nutrition  and opening and closing different kinds of packages.",
        "Cleaning and general household tasks: participating in responsibilities at home and school  retrieving and replacing toys and games  and using cleaning supplies and equipment.",
        "Telephone use: calling friends  knowing how to make emergency calls and having a system of phone number retrieval",
        "Money management: identifying coins and bills using ATMs writing checks and managing money.",
    ],
    "ECC_SelfDetermination": [
        "SELECT SKILL FROM DROPDOWN",
        "Self-knowledge: developing personal preferences  needs and desires",
        "Awareness of individual right and responsibilities: possessing knowledge of laws protecting people with disabilities",
        "Capacity to make informed choices: knowing what to do in an emergency  being able to express one’s likes and dislikes",
        "Problem-solving and goal-setting skills: making personal and educational goals and interacting with others to obtain assistance",
        "Ability to engage in self-regulated and self-directed behavior: developing negotiation skills and skills involved in interacting with others and the public at large",
        "Self-advocacy and empowerment: choosing favorite or desired activities and being able to evaluate one’s own behavior or progress",
        "Assertiveness skills: being able to advocate for one’s needs and wants.",
    ],
    "ECC_RecreationLeisure": [
        "SELECT SKILL FROM DROPDOWN",
        "Play: interacting through play with peers and siblings  entertaining oneself for various periods of time",
        "Physical activity: participating in physical education or other active play activities  taking part in recreation and leisure activities enjoyed by the family",
        "Health  fitness and individual sports: developing a regimen of physical exercise that leads to improvement or maintenance of strength  stamina and endurance; developing skills for engaging in such activities as track  wrestling and weight-lifting.",
        "Team and spectator sports: learning  to enjoy competitive and noncompetitive sports activities such as football  baseball  soccer  golf baseball or goalball  as a participant or as a spectator",
        "Leisure activities and hobbies: being exposed to opportunities for choosing a favorite game or book experiencing arts and crafts activities appreciating and enjoying fine arts in such forms as museum visits theater dance opera and music.",
    ],
    "ECC_OrientationMobility": [
        "SELECT SKILL FROM DROPDOWN",
        "Body concepts: understanding body parts and function",
        "Environmental concepts:  understanding concepts related to the home environment (such as windows and doors) and to buildings  residential and business areas  schools  and streets and intersections.",
        "Spatial concepts: understanding self-to-object relationships  spatial terminology (such as right  left and next to)  landmarks and cues and cardinal directions",
        "Perceptual/sensory skills: interpreting environmental sounds  applying meaning to tasks and determining the nature of sensory information",
        "Mobility skills: noticing and negotiating unexpected drop-offs  using systematic search techniques  and knowing built elements such as block distances  corners  intersection types streets and road structures.",
        "Orientation skills: knowing routes and understanding layouts",
        "Interpersonal skills: requesting directions  arranging for rides; soliciting information from individuals such as dispatchers  drivers  and store personnel; and using appropriate telephone manners",
        "Decision-making skills: altering travel in response to inclement weather choosing appropriate clothing and gear choosing between routes knowing the advantage and disadvantage of different modes of travel and making back up plans.",
    ],
    "ECC_AssistiveTechnology": [
        "SELECT SKILL FROM DROPDOWN",
        "Access to information: developing facility with general applications and basic technology skills such as inputting information and producing documents",
        "Communication: developing awareness of electronic communication modes and the ability to conduct research and written assignments.",
        "Personal productivity: practicing the use of basic applications in activities related to learning and daily living",
    ],
    "ECC_SensoryEfficiency": [
        "SELECT SKILL FROM DROPDOWN",
        "Visual function: fixating  orienting  tracking and recognizing objects and using optical devices",
        "Auditory function: localization  aural discrimination and presentation  and sound pattern use",
        "Tactile function: tactile discrimination  scanning  manipulation and dexterity",
        "Gustatory (taste) function: appreciation for food  discrimination of food types and recognition of various tastes",
        "Olfactory (smell) function: localization of smells discrimination of odors and recognition of pleasant and unpleasant odors.",
    ],
    "ECC_CompensatorySkills": [
        "SELECT SKILL FROM DROPDOWN",
        "Concept development: developing mental ideas about the environment and the objects  people and processes and interactions taking place in the world.",
        "Spatial understanding:  understanding the physical location of objects in relation to one’s self and to other objects",
        "Communication modes: developing facility with techniques and tools needed to access information presented in print and to write or communicate thoughts",
        "Speaking and listening skills: learning appropriate methods of addressing others in conversation and comprehending what is said.",
        "Study and organization skills: developing methods that allow a student to maintain order in the use of materials and time and to set priorities for such activities as they completion of school work.",
        "Use of adapted and specialized educational materials: independently using tools and devices that provide compensatory access.",
    ],
    "magnifierSkills": [
        "SELECT SKILL FROM DROPDOWN",
        "Concept of 'in focus' and how to bring the image into focus.",
        "Change the image size and then focus. Provide the students with materials of various print sizes and practice adjusting the image appropriately.",
        "Spot or locate an image on the page and then focus.",
        "Follow a line of text  and then track down to locate the next line of text.",
        "Use various features of the electronic magnifier and when it is adventitious to use those features.",
        "Become accustomed to writing and drawing while looking at the monitor.",
        "Care for the video magnifier and demonstrate safe use.",
    ],
    "digitalLiteracySkills": [
        "Turn computer on and off",
        "Use pointing device such as a mouse to manipulate shapes, icons; click on urls, radio buttons, check boxes; use scroll bar ",
        "Use desktop icons, windows and menus to open applications and documents ",
        "Save documents ",
        "Explain and use age-appropriate online tools and resources (e.g. tutorial, assessment, web browser) ",
        "Keyboarding (Use proper posture and ergonomics, Locate and use letter and numbers keys with left and right hand placement, Locate and use correct finger, hand for space bar,return/enter and shift key, "
        "Use a word processing application to write, edit, print and save simple assignments ",
        "Use menu/tool bar functions (e.g. font/size/style/, line spacing, margins) to format, edit and print a document ",
        "Highlight text, copy and paste text ",
        "Copy and paste images within the document and from outside sources ",
        "Insert and size a graphic in a document ",
        "Proofread and edit writing using appropriate resources (e.g. dictionary, spell checker, grammar, and thesaurus) ",
        "Demonstrate an understanding of the spreadsheet as a tool to record, organize and graph information. ",
        "Identify and explain terms and concepts related to spreadsheets (i.e. cell, column, row, values, labels, chart graph) ",
        "Enter/edit data in spreadsheets and perform calculations using formulas ",
        "Use mathematical symbols e.g. + add, - minus, *multiply, /divide, ^ exponents ",
        "Use spreadsheets and other applications to make predictions, solve problems and draw conclusions ",
        "Create, edit and format text on a slide ",
        "Create a series of slides and organize them to present research or convey an idea ",
        "Copy and paste or import graphics; change their size and position on a slide ",
        "Use painting and drawing tools/ applications to create and edit work ",
        "Watch online videos and use play, pause, rewind and forward buttons while taking notes ",
        "Explain and demonstrate compliance with classroom, school rules (Acceptable Use Policy) regarding responsible use of computers and networks ",
        "Explain responsible uses of technology and digital information; describe possible consequences of inappropriate use ",
        "Explain Fair Use Guidelines for the use of copyrighted materials,(e.g. text, images, music, video in student projects) and giving credit to media creators ",
        "Identify and explain the strategies for the safe and efficient use of computers (e.g. passwords, virus protection software, spam filters, popup blockers)",
        "Demonstrate safe email practices, recognition of the potentially public exposure of email and appropriate email etiquette ",
        "Identify cyberbullying and describe strategies to deal with such a situation  ",
        "Recognize and describe the potential risks and dangers associated with various forms of online communications ",
        "Use age appropriate technologies to locate, collect, organize content from media collection for specific purposes, citing sources ",
        "Perform basic searches on databases, (e.g. library, card catalog, encyclopedia) to locate information. Evaluate teacher-selected or self-selected Internet resources in terms of their usefulness for research ",
        "Use content specific technology tools (e.g. environmental probes, sensors, and measuring devices, simulations) to gather and analyze data. ",
        "Use Web 2.0 tools (e.g. online discussions, blogs and wikis) to gather and share information  ",
        "Identify and analyze the purpose of a media message (to inform, persuade and entertain) ",
        "Work collaboratively online with other students under teacher supervision  ",
        "Use a variety of age-appropriate technologies (e.g. drawing program, presentation software) to communicate and exchange ideas ",
        "Create projects that use text and various forms of graphics, audio, and video, (with proper citations) to communicate ideas. ",
        "Use teacher developed guidelines to evaluate multimedia presentations for organization, content, design, presentation and appropriateness of citations. ",
        "Use district approved Web 2.0 tools for communication and collaboration ",
        " Identify successful troubleshooting strategies for minor hardware and software issues/problems (e.g., “frozen screen”)",
        "Independently operate peripheral equipment (e.g., scanner, digital camera, camcorder), if available.  ",
        "Compress and expand large files  ",
        "Identify and use a variety of storage media (e.g., CDs, DVDs, flash drives, school servers, and online storage spaces), and provide a rationale for using a certain medium for a specific purpose.",
        "Demonstrate automaticity in keyboarding skills by increasing accuracy and speed (For students with disabilities, demonstrate alternate input techniques as appropriate.)",
        "Identify and assess the capabilities and limitations of emerging technologies. ",
        "Demonstrate use of intermediate features in word processing application (e.g., tabs, indents, headers and footers, end notes, bullet and numbering, tables). ",
        "Apply advanced formatting and page layout features when appropriate (e.g., columns, templates, and styles) to improve the appearance of documents and materials.",
        "Highlight text, copy and paste text ",
        "Use the Comment function in Review for peer editing of documents ",
        "Use the Track Changes feature in Review for peer editing of documents ",
        "Use spreadsheets to calculate, graph, organize, and present data in a variety of real-world settings and choose the most appropriate type to represent given data",
        "Enter formulas and functions; use the auto-fill feature in a spreadsheet application.",
        "Use functions of a spreadsheet application (e.g., sort, filter, find).",
        "Use various number formats (e.g. scientific notations, percentages, exponents) as appropriate ",
        "Use various number formats (e.g. scientific notations, percentages, exponents) as appropriate ",
        "Differentiate between formulas with absolute and relative cell references. ",
        "Use multiple sheets within a workbook, and create links among worksheets to solve problems. ",
        "Draw two and three dimensional geometric shapes using a variety of technology tools ",
        "Use and interpret scientific notations using a variety of technology applications ",
        "Explain and demonstrate how specialized technology tools can be used for problem solving, decision making, and creativity in all subject areas (e.g., simulation software, environmental probes, computer aided design, "
        "Create presentations for a variety of audiences and purposes with use of appropriate transitions and animations to add interest. ",
        " Use a variety of technology tools (e.g., dictionary, thesaurus, grammar checker, calculator/graphing calculator) to maximize the accuracy of work. Make strategic use of digital media to enhance understanding ",
        "Use painting and drawing tools/ applications to create and edit work ",
        "Use note-taking skills while viewing online videos and using the play, pause, rewind and stop buttons. ",
        "Independently use appropriate technology tools (e.g., graphic organizer, audio, visual) to define problems and propose hypotheses. ",
        "Comply with the district’s Acceptable Use Policy related to ethical use, cyberbullying, privacy, plagiarism, spam, viruses, hacking, and file sharing. ",
        "Explain Fair Use guidelines for using copyrighted materials and possible consequences (e.g., images, music, video, text) in school projects. ",
        "Analyze and explain how media and technology can be used to distort, exaggerate, and misrepresent information. ",
        "Give examples of hardware and applications that enable people with disabilities to use technology. ",
        "Explain the potential risks associated with the use of networked digital environments (e.g., internet, mobile phones, wireless, LANs) and sharing personal information. ",
        " Identify probable types and locations of Web sites by examining their domain names (e.g., edu, com, org, gov, au)",
        "Use effective search strategies for locating and retrieving electronic information (e.g., using syntax and Boolean logic operators) ",
        "Use search engines and online directories. Explain the differences among various search engines and how they rank results. ",
        "Use appropriate academic language in online learning environments (e.g., post, thread, intranet, discussion forum, drop box, account, and password). ",
        "Explain how technology can support communication and collaboration, personal and professional productivity, and lifelong learning. ",
        "Write correct in-text citations and reference lists for text and images gathered from electronic sources. ",
        "Use Web browsing to access information (e.g., enter a URL, access links, create bookmarks/favorites, print Web pages) ",
        "Use and modify databases and spreadsheets to analyze data and propose solutions. ",
        "Develop and use guidelines to evaluate the content, organization, design, use of citations, and presentation of technologically enhanced projects. ",
        "Use a variety of media to present information for specific purposes (e.g., reports, research papers, presentations, newsletters, Web sites, podcasts, blogs), citing sources. ",
        "Demonstrate how the use of various techniques and effect (e.g., editing, music, color, rhetorical devices) can be used to convey meaning in media. ",
        "Use a variety of district approved Web 2.0 tools (e.g., email discussion groups, blogs, etc.) to collaborate and communicate with peers, experts, and other audiences using appropriate academic language. ",
        "Use teacher developed guidelines to evaluate multimedia presentations for organization, content, design, presentation and appropriateness of citations ",
        " Plan and implement a collaborative project with students in other classrooms and schools using telecommunications tools (e.g., e-mail, discussion forums, groupware, interactive Web sites, videoconferencing) ",
    ],
}
