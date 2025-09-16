#!/usr/bin/env python3

"""
 Copyright 2025  Michael Ryan Hunsaker, M.Ed., Ph.D.

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

import os
import datetime
import shutil
from csv import writer
from pathlib import Path
import json
import logging

date_fmt = "%Y-%m-%d %H:%M:%S"

datenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Set APP_HOME to /app_home at the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
APP_HOME = PROJECT_ROOT / "app_home"
APP_HOME.mkdir(exist_ok=True)
ROOT_DIR = str(PROJECT_ROOT)
USER_DIR = str(APP_HOME)
IMAGE_DIR = Path(__file__).resolve().parent / "images"
START_DIR = str(APP_HOME)
DATA_ROOT = str(APP_HOME)



def set_start_dir() -> Path:
    """
    Set the start directory to /app_home at the project root.
    """
    return APP_HOME

START_DIR = str(APP_HOME)


def working_dir() -> None:
    """
    Set working directory to /app_home at the project root.
    """
    os.chdir(APP_HOME)
    student_data_dir = APP_HOME / "StudentDataFiles"
    student_data_dir.mkdir(parents=True, exist_ok=True)
    logging.debug(f"Ensured StudentDataFiles directory exists at: {student_data_dir}")

working_dir()


def create_roster() -> None:
    """
    Create the roster file for the application in /app_home.
    """
    # Write a simple roster.py fallback in both the package appHelpers folder
    # and the current working directory's appHelpers so legacy imports and
    # tests that look for a file in CWD succeed.
    targets = [
        Path(ROOT_DIR).joinpath("appHelpers", "roster.py"),
        Path(os.getcwd()).joinpath("appHelpers", "roster.py"),
    ]
    try:
        if students:
            for roster_path in targets:
                if not roster_path.exists():
                    roster_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(roster_path, "w", encoding="utf-8") as rf:
                        rf.write("# Auto-generated roster fallback\n")
                        rf.write("students = [\n")
                        for s in students:
                            rf.write(f'    "{s}",\n')
                        rf.write("]\n")
        else:
            # If students list is empty, fallback to copying roster.txt from APP_HOME
            tmp_path = APP_HOME / "roster.txt"
            if tmp_path.exists():
                for roster_path in targets:
                    if not roster_path.exists():
                        roster_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(tmp_path, roster_path)
    except Exception:
        # Do not raise exceptions during roster creation
        logging.exception("Failed to create roster fallback")

# Load students list from json_Files/students.json (runtime-controlled)
import json
import logging
import datetime

def _load_students_from_json() -> list[str]:
    """Load student names from json_Files/students.json under the project root.
    Returns a list of cleaned "First Last" strings (may be empty)."""
    try:
        students_path = PROJECT_ROOT.joinpath("json_Files", "students.json")
        if not students_path.exists():
            logging.warning("students.json not found at %s", students_path)
            return []
        text = students_path.read_text(encoding="utf-8")
        data = json.loads(text)
        raw = data.get("students") if isinstance(data, dict) else data
        result = []
        if isinstance(raw, list):
            for item in raw:
                if not isinstance(item, str):
                    continue
                name = " ".join(item.split()).strip()
                if name:
                    result.append(name)
        seen = set()
        cleaned = []
        for n in result:
            if n not in seen:
                cleaned.append(n)
                seen.add(n)
        return cleaned
    except Exception:
        logging.exception("Failed to load students.json")
        return []

class StudentsProxy:
    """List-like proxy that reloads students.json on each access."""
    def __iter__(self):
        return iter(_load_students_from_json())
    def __len__(self):
        return len(_load_students_from_json())
    def __getitem__(self, idx):
        return _load_students_from_json()[idx]
    def __contains__(self, item):
        return item in _load_students_from_json()
    def keys(self):
        """Compatibility: return list of student names (like dict.keys())."""
        return _load_students_from_json()
    def items(self):
        """Compatibility: return list of (name, name) pairs."""
        lst = _load_students_from_json()
        return [(s, s) for s in lst]
    def values(self):
        """Compatibility: return list of student names (like dict.values())."""
        return _load_students_from_json()
    def get(self, key, default=None):
        """Compatibility: return the key if present, else default."""
        lst = _load_students_from_json()
        return key if key in lst else default
    def __repr__(self):
        return repr(_load_students_from_json())

# public API: students (dynamic) and accessor
students = StudentsProxy()

def get_students() -> list[str]:
    """Return the runtime-loaded list of students (fresh copy)."""
    return _load_students_from_json()

# All database and student data will be stored in /app_home at the project root
dataBasePath = str(APP_HOME / "students20252026.db")
database_dir = dataBasePath
logging.debug(f"Resolved dataBasePath: {dataBasePath}")

# After loading students, ensure a roster.py exists for legacy/tests
create_roster()



def createFolderHierarchy() -> None:
    """
    Create the folder hierarchy for student data, logs, and backups under DATA_ROOT.

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
    and other variables representing the applications
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
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("createFolderHierarchy")

    for name in students:
        logging.debug(f"Processing student: {name}")
        # Sanitize student name for filesystem safety and normalize whitespace/newlines
        def _sanitize_filename(s: str) -> str:
            s = str(s)
            s = " ".join(s.split())
            s = s.strip().strip('.')
            for ch in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
                s = s.replace(ch, '_')
            return s

        name_clean = _sanitize_filename(name)
        # Reassign name so the remainder of the code uses the sanitized value
        name = name_clean
        # StudentDatabase root and sub-folders
        student_database_root = Path(DATA_ROOT).joinpath("StudentDatabase")
        student_datafiles_root = student_database_root.joinpath("StudentDataFiles")
        student_errorlogs_root = student_database_root.joinpath("errorLogs")
        student_backups_root = student_database_root.joinpath("backups")
        student_folder = student_datafiles_root.joinpath(name)
        student_datasheets = student_folder.joinpath("StudentDataSheets")
        student_instruction = student_folder.joinpath("StudentInstructionMaterials")
        student_vision = student_folder.joinpath("StudentVisionAssessments")

        for folder in [
            student_datafiles_root,
            student_errorlogs_root,
            student_backups_root,
            student_folder,
            student_datasheets,
            student_instruction,
            student_vision,
        ]:
            if not folder.exists():
                try:
                    folder.mkdir(parents=True, exist_ok=True)
                    logger.info(f"Created folder: {folder}")
                except Exception as e:
                    logger.error(f"Failed to create folder {folder}: {e}")
            else:
                logger.debug(f"Folder already exists: {folder}")
        if not student_folder.joinpath("omnibusDatabase.csv").exists():
            tmppath = student_folder.joinpath("omnibusDatabase.csv")
            logging.debug(f"Resolved tmppath for omnibusDatabase.csv: {tmppath}")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("BrailleSkillsProgression.csv").exists():
            tmppath = student_folder.joinpath("BrailleSkillsProgression.csv")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("UEBLiterarySkillsProgression.html").exists():
            tmppath = student_folder.joinpath("UEBLiterarySkillsProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("UEBTechnicalSkillsProgression.html").exists():
            tmppath = student_folder.joinpath("UEBTechnicalSkillsProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("BasicTactileRecognition.html").exists():
            tmppath = student_folder.joinpath("BasicTactileRecognition.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("ScreenReaderSkillsProgression.csv").exists():
            tmppath = student_folder.joinpath("ScreenReaderSkillsProgression.csv")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("ScreenReaderSkillsProgression.html").exists():
            tmppath = student_folder.joinpath("ScreenReaderSkillsProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("AbacusSkillsProgression.csv").exists():
            tmppath = student_folder.joinpath("AbacusSkillsProgression.csv")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("AbacusSkillsProgression.html").exists():
            tmppath = student_folder.joinpath("AbacusSkillsProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("cviProgression.csv").exists():
            tmppath = student_folder.joinpath("cviProgression.csv")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("cviProgression.html").exists():
            tmppath = student_folder.joinpath("cviProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("digitalliteracyProgression.csv").exists():
            tmppath = student_folder.joinpath("digitalliteracyProgression.csv")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
                "P15_1",
                "P15_2",
                "P15_3",
                "P15_4",
                "P15_5",
            ]
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("digitalliteracyProgression.html").exists():
            tmppath = student_folder.joinpath("digitalliteracyProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("iosProgression.csv").exists():
            tmppath = student_folder.joinpath("iosProgression.csv")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("iosProgression.html").exists():
            tmppath = student_folder.joinpath("iosProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        if not student_folder.joinpath("bntProgression.csv").exists():
            tmppath = student_folder.joinpath("bntProgression.csv")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
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
            try:
                with open(tmppath, "a", newline="", encoding="UTF-8") as f_object:
                    writer_setup = writer(f_object)
                    writer_setup.writerow(list_names)
                    f_object.close()
                logger.info(f"Wrote header to file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to write header to file {tmppath}: {e}")
        if not student_folder.joinpath("bntProgression.html").exists():
            tmppath = student_folder.joinpath("bntProgression.html")
            try:
                tmppath.parent.mkdir(parents=True, exist_ok=True)
                tmppath.touch(exist_ok=True)
                logger.info(f"Created file: {tmppath}")
            except Exception as e:
                logger.error(f"Failed to create file {tmppath}: {e}")
        sourceDir = Path(ROOT_DIR).joinpath("datasheets")
        destinationDir = Path(DATA_ROOT).joinpath(
            "StudentDataFiles", name, "StudentDataSheets"
        )
        logging.debug(f"Resolved sourceDir: {sourceDir}")
        logging.debug(f"Resolved destinationDir for StudentDataSheets: {destinationDir}")
        if sourceDir.exists():
            files = os.listdir(sourceDir)
            for fileName in files:
                tmppath = os.path.join(sourceDir, fileName)
                try:
                    copy_if_not_exists(tmppath, str(destinationDir))
                    logger.info(f"Copied {tmppath} to {destinationDir}")
                except Exception as e:
                    logger.error(f"Failed to copy {tmppath} to {destinationDir}: {e}")
        else:
            logger.debug(f"Source directory for StudentDataSheets not found: {sourceDir}. Skipping copy.")
        sourceDir = Path(ROOT_DIR).joinpath("instructionMaterials")
        destinationDir = Path(DATA_ROOT).joinpath(
            "StudentDataFiles", name, "StudentInstructionMaterials"
        )
        logging.debug(f"Resolved sourceDir: {sourceDir}")
        logging.debug(f"Resolved destinationDir for StudentInstructionMaterials: {destinationDir}")
        if sourceDir.exists():
            files = os.listdir(sourceDir)
            for fileName in files:
                tmppath = os.path.join(sourceDir, fileName)
                try:
                    copy_if_not_exists(tmppath, str(destinationDir))
                    logger.info(f"Copied {tmppath} to {destinationDir}")
                except Exception as e:
                    logger.error(f"Failed to copy {tmppath} to {destinationDir}: {e}")
        else:
            logger.debug(f"Source directory for StudentInstructionMaterials not found: {sourceDir}. Skipping copy.")
        sourceDir = Path(ROOT_DIR).joinpath("visionAssessments")
        destinationDir = Path(DATA_ROOT).joinpath(
            "StudentDataFiles", name, "StudentVisionAssessments"
        )
        logging.debug(f"Resolved sourceDir: {sourceDir}")
        logging.debug(f"Resolved destinationDir for StudentVisionAssessments: {destinationDir}")
        if sourceDir.exists():
            files = os.listdir(sourceDir)
            for fileName in files:
                tmppath = os.path.join(sourceDir, fileName)
                try:
                    copy_if_not_exists(tmppath, str(destinationDir))
                    logger.info(f"Copied {tmppath} to {destinationDir}")
                except Exception as e:
                    logger.error(f"Failed to copy {tmppath} to {destinationDir}: {e}")
        else:
            logger.debug(f"Source directory for StudentVisionAssessments not found: {sourceDir}. Skipping copy.")


def copy_if_not_exists(source: str, destination: str) -> None:
    if not os.path.exists(destination):
        shutil.copy2(source, destination)


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
        "Play make believe and dress-up activities"
    ]
}