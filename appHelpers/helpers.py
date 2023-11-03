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

import datetime
import os
import shutil
from csv import writer
from pathlib import Path

##############################################################################
# Set User Directory based on OS
##############################################################################
date_fmt = "%Y_%m_%d-%H%M%S_%p"

datenow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")
##############################################################################
# Set User Directory based on OS
##############################################################################
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = ""
IMAGE_DIR = Path(ROOT_DIR).joinpath("images")
START_DIR = ""


##############################################################################
# Set User Directory based on OS
##############################################################################
def set_start_dir() -> Path:
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
    if not Path(ROOT_DIR).joinpath("workingdirectory.py").exists():
        workingdirectory_path = Path(ROOT_DIR).joinpath("workingdirectory.py")
        tmp_path = Path(START_DIR).joinpath("workingdirectory.txt")
        shutil.copy2(tmp_path, workingdirectory_path)


working_dir()


def create_roster() -> None:
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


##############################################################################
# Error Logging
##############################################################################


##############################################################################
# Set User Folders and necessary files in ~/Documents for each Student
##############################################################################
def createFolderHierarchy() -> None:
    """creates folder hierarchy on user computer"""
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


tasks = [
        "Choose a Task",
        "braille tracking",
        "literary braille alphabet reading",
        "literary braille contractions reading",
        "UEB math reading",
        "literary braille alphabet writing",
        "literary braille contractions writing",
        "UEB math writing",
        "abacus addition",
        "abacus subtraction",
        "abacus multiplication",
        "abacus division",
        "screenreader usage",
        "ios usage",
        "digital literacy",
        "visual reach",
        "visual scan"
        ]
