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

import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from appHelpers.helpers import dataBasePath, date_fmt, datenow, USER_DIR
from appHelpers.roster import students
from appTheming import theme
from nicegui import app, ui
from plotly.subplots import make_subplots


def create() -> None:
    ##########################################################################
    # BRAILLENOTE TOUCH  SKILLS
    ##########################################################################
    @ui.page("/braillenotetouchskills")
    def braillenotetouchskills() -> None:
        with theme.frame("- TECHNOLOGY SKILLS -"):
            with ui.tabs() as tabs:
                ui.tab("DATA INPUT")
                ui.tab("DATA VISUALIZATION")
            with ui.tab_panels(tabs, value="DATA INPUT"):
                with ui.tab_panel("DATA INPUT"):
                    ui.label("BRAILLENOTE TOUCH PLUS SKILLS").classes(
                        "text-h4 text-grey-8"
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')

                    # ASSIGN VARIABLES
                    u_studentname = (
                        ui.select(options=students, value="DonaldChamberlain")
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_today_date = (
                        ui.date()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial11 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial12 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial13 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial14 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial15 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial16 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial17 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial18 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial19 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial21 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial22 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial23 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial24 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial25 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial26 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial27 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial31 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial32 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial33 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial34 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial35 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial36 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial37 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial41 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial42 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial43 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial51 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial52 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial53 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial54 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial55 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial56 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial57 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial61 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial62 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial63 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial71 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial72 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial73 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial74 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial81 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial82 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial83 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial84 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial85 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial91 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial92 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial93 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial94 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial101 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial102 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial103 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial111 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial112 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial113 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial114 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial115 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial121 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial122 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial123 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_bnt_trial124 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )

                    def save(event):
                        """
                        Save data for a student.

                        Parameters
                        ----------
                        event : SomeEventType
                            The event triggering the save function.

                        Returns
                        -------
                        None

                        Notes
                        -----
                        This function assumes the existence of various UI elements (e.g., `u_studentname`,
                        `u_today_date`, ...), `datenow`, `json`,
                        `Path`, and other variables related to the application.

                        The function extracts abacus trial data and student information from UI elements,
                        creates a dictionary with this data, and saves it as a JSON file in the student's
                        directory within the "StudentDataFiles" folder. The filename is constructed based
                        on the student's name and the current date.

                        The function also appends the filename to a "Filenames.txt" file for reference.

                        Examples
                        --------
                        >>> save(some_event)
                        >>> # Trial data and student information saved successfully.
                        >>> # The data is stored in a JSON file named based on the student's name and date.

                        See Also
                        --------
                        Some related functions or classes that might be useful.

                        """

                        studentname = u_studentname.value
                        today_date = u_today_date.value
                        bnt_trial11 = int(u_bnt_trial11.value)
                        bnt_trial12 = int(u_bnt_trial12.value)
                        bnt_trial13 = int(u_bnt_trial13.value)
                        bnt_trial14 = int(u_bnt_trial14.value)
                        bnt_trial15 = int(u_bnt_trial15.value)
                        bnt_trial16 = int(u_bnt_trial16.value)
                        bnt_trial17 = int(u_bnt_trial17.value)
                        bnt_trial18 = int(u_bnt_trial18.value)
                        bnt_trial19 = int(u_bnt_trial19.value)
                        bnt_trial21 = int(u_bnt_trial21.value)
                        bnt_trial22 = int(u_bnt_trial22.value)
                        bnt_trial23 = int(u_bnt_trial23.value)
                        bnt_trial24 = int(u_bnt_trial24.value)
                        bnt_trial25 = int(u_bnt_trial25.value)
                        bnt_trial26 = int(u_bnt_trial26.value)
                        bnt_trial27 = int(u_bnt_trial27.value)
                        bnt_trial31 = int(u_bnt_trial31.value)
                        bnt_trial32 = int(u_bnt_trial32.value)
                        bnt_trial33 = int(u_bnt_trial33.value)
                        bnt_trial34 = int(u_bnt_trial34.value)
                        bnt_trial35 = int(u_bnt_trial35.value)
                        bnt_trial36 = int(u_bnt_trial36.value)
                        bnt_trial37 = int(u_bnt_trial37.value)
                        bnt_trial41 = int(u_bnt_trial41.value)
                        bnt_trial42 = int(u_bnt_trial42.value)
                        bnt_trial43 = int(u_bnt_trial43.value)
                        bnt_trial51 = int(u_bnt_trial51.value)
                        bnt_trial52 = int(u_bnt_trial52.value)
                        bnt_trial53 = int(u_bnt_trial53.value)
                        bnt_trial54 = int(u_bnt_trial54.value)
                        bnt_trial55 = int(u_bnt_trial55.value)
                        bnt_trial56 = int(u_bnt_trial56.value)
                        bnt_trial57 = int(u_bnt_trial57.value)
                        bnt_trial61 = int(u_bnt_trial61.value)
                        bnt_trial62 = int(u_bnt_trial62.value)
                        bnt_trial63 = int(u_bnt_trial63.value)
                        bnt_trial71 = int(u_bnt_trial71.value)
                        bnt_trial72 = int(u_bnt_trial72.value)
                        bnt_trial73 = int(u_bnt_trial73.value)
                        bnt_trial74 = int(u_bnt_trial74.value)
                        bnt_trial81 = int(u_bnt_trial81.value)
                        bnt_trial82 = int(u_bnt_trial82.value)
                        bnt_trial83 = int(u_bnt_trial83.value)
                        bnt_trial84 = int(u_bnt_trial84.value)
                        bnt_trial85 = int(u_bnt_trial85.value)
                        bnt_trial91 = int(u_bnt_trial91.value)
                        bnt_trial92 = int(u_bnt_trial92.value)
                        bnt_trial93 = int(u_bnt_trial93.value)
                        bnt_trial94 = int(u_bnt_trial94.value)
                        bnt_trial101 = int(u_bnt_trial101.value)
                        bnt_trial102 = int(u_bnt_trial102.value)
                        bnt_trial103 = int(u_bnt_trial103.value)
                        bnt_trial111 = int(u_bnt_trial111.value)
                        bnt_trial112 = int(u_bnt_trial112.value)
                        bnt_trial113 = int(u_bnt_trial113.value)
                        bnt_trial114 = int(u_bnt_trial114.value)
                        bnt_trial115 = int(u_bnt_trial115.value)
                        bnt_trial121 = int(u_bnt_trial121.value)
                        bnt_trial122 = int(u_bnt_trial122.value)
                        bnt_trial123 = int(u_bnt_trial123.value)
                        bnt_trial124 = int(u_bnt_trial124.value)
                        studentdatabasename = f"bnt{studentname.title()}" f"{datenow}"
                        tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase",
                            "StudentDataFiles",
                            studentname,
                            studentdatabasename + ".json",
                        )
                        bnt_dictionary = {
                            "studentname": studentname,
                            "date": today_date,
                            "bnt_trial11": bnt_trial11,
                            "bnt_trial12": bnt_trial12,
                            "bnt_trial13": bnt_trial13,
                            "bnt_trial14": bnt_trial14,
                            "bnt_trial15": bnt_trial15,
                            "bnt_trial16": bnt_trial16,
                            "bnt_trial17": bnt_trial17,
                            "bnt_trial18": bnt_trial18,
                            "bnt_trial19": bnt_trial19,
                            "bnt_trial21": bnt_trial21,
                            "bnt_trial22": bnt_trial22,
                            "bnt_trial23": bnt_trial23,
                            "bnt_trial24": bnt_trial24,
                            "bnt_trial25": bnt_trial25,
                            "bnt_trial26": bnt_trial26,
                            "bnt_trial27": bnt_trial27,
                            "bnt_trial31": bnt_trial31,
                            "bnt_trial32": bnt_trial32,
                            "bnt_trial33": bnt_trial33,
                            "bnt_trial34": bnt_trial34,
                            "bnt_trial35": bnt_trial35,
                            "bnt_trial36": bnt_trial36,
                            "bnt_trial37": bnt_trial37,
                            "bnt_trial41": bnt_trial41,
                            "bnt_trial42": bnt_trial42,
                            "bnt_trial43": bnt_trial43,
                            "bnt_trial51": bnt_trial51,
                            "bnt_trial52": bnt_trial52,
                            "bnt_trial53": bnt_trial53,
                            "bnt_trial54": bnt_trial54,
                            "bnt_trial55": bnt_trial55,
                            "bnt_trial56": bnt_trial56,
                            "bnt_trial57": bnt_trial57,
                            "bnt_trial61": bnt_trial61,
                            "bnt_trial62": bnt_trial62,
                            "bnt_trial63": bnt_trial63,
                            "bnt_trial71": bnt_trial71,
                            "bnt_trial72": bnt_trial72,
                            "bnt_trial73": bnt_trial73,
                            "bnt_trial74": bnt_trial74,
                            "bnt_trial81": bnt_trial81,
                            "bnt_trial82": bnt_trial82,
                            "bnt_trial83": bnt_trial83,
                            "bnt_trial84": bnt_trial84,
                            "bnt_trial85": bnt_trial85,
                            "bnt_trial91": bnt_trial91,
                            "bnt_trial92": bnt_trial92,
                            "bnt_trial93": bnt_trial93,
                            "bnt_trial94": bnt_trial94,
                            "bnt_trial101": bnt_trial101,
                            "bnt_trial102": bnt_trial102,
                            "bnt_trial103": bnt_trial103,
                            "bnt_trial111": bnt_trial111,
                            "bnt_trial112": bnt_trial112,
                            "bnt_trial113": bnt_trial113,
                            "bnt_trial114": bnt_trial114,
                            "bnt_trial115": bnt_trial115,
                            "bnt_trial121": bnt_trial121,
                            "bnt_trial122": bnt_trial122,
                            "bnt_trial123": bnt_trial123,
                            "bnt_trial124": bnt_trial124,
                        }
                        with open(tmppath, "w", encoding="utf-8") as filename:
                            json.dump(bnt_dictionary, filename)
                        tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase", "StudentDataFiles", "Filenames.txt"
                        )
                        with open(tmppath, "a", encoding="utf-8") as filename:
                            tmppath = Path(USER_DIR).joinpath(
                                "StudentDatabase",
                                "StudentDataFiles",
                                studentname,
                                studentdatabasename + ".json",
                            )
                            filename.write(f"'{tmppath}'" + "\n")
                            # noinspection SqlResolve

                        def data_entry():
                            """
                            Write progress data to the database.

                            Connects to the SQLite database specified by `dataBasePath` and inserts a new row
                            into the appropriate table with the provided abacus progress data.

                            Parameters
                            ----------
                            None

                            Returns
                            -------
                            None

                            Notes
                            -----
                            This function assumes the existence of variables such as `dataBasePath`,
                            `studentname`, `today_date`,  and  `sqlite3`

                            The function establishes a connection to the database, creates a cursor, executes an
                            SQL INSERT command with the abacus progress data, commits the changes, and notifies
                            the user of successful data entry.

                            Examples
                            --------
                            >>> data_entry()
                            >>> # Progress data successfully written to the database.
                            >>> # The user is notified of successful data entry.

                            See Also
                            --------
                            Some related functions or classes that might be useful.

                            """
                            conn = sqlite3.connect(dataBasePath)
                            c = conn.cursor()
                            c.execute(
                                """INSERT INTO BNTPROGRESS (
                                                    STUDENTNAME,
                                                    DATE,
                                                    P1_1,
                                                    P1_2,
                                                    P1_3,
                                                    P1_4,
                                                    P1_5,
                                                    P1_6,
                                                    P1_7,
                                                    P1_8,
                                                    P1_9,
                                                    P2_1,
                                                    P2_2,
                                                    P2_3,
                                                    P2_4,
                                                    P2_5,
                                                    P2_6,
                                                    P2_7,
                                                    P3_1,
                                                    P3_2,
                                                    P3_3,
                                                    P3_4,
                                                    P3_5,
                                                    P3_6,
                                                    P3_7,
                                                    P4_1,
                                                    P4_2,
                                                    P4_3,
                                                    P5_1,
                                                    P5_2,
                                                    P5_3,
                                                    P5_4,
                                                    P5_5,
                                                    P5_6,
                                                    P5_7,
                                                    P6_1,
                                                    P6_2,
                                                    P6_3,
                                                    P7_1,
                                                    P7_2,
                                                    P7_3,
                                                    P7_4,
                                                    P8_1,
                                                    P8_2,
                                                    P8_3,
                                                    P8_4,
                                                    P8_5,
                                                    P9_1,
                                                    P9_2,
                                                    P9_3,
                                                    P9_4,
                                                    P10_1,
                                                    P10_2,
                                                    P10_3,
                                                    P11_1,
                                                    P11_2,
                                                    P11_3,
                                                    P11_4,
                                                    P11_5,
                                                    P12_1,
                                                    P12_2,
                                                    P12_3,
                                                    P12_4
                                                                                        )
                                                                                        VALUES (
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,
                                                                                            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                                                                                            )""",
                                (
                                    studentname,
                                    today_date,
                                    bnt_trial11,
                                    bnt_trial12,
                                    bnt_trial13,
                                    bnt_trial14,
                                    bnt_trial15,
                                    bnt_trial16,
                                    bnt_trial17,
                                    bnt_trial18,
                                    bnt_trial19,
                                    bnt_trial21,
                                    bnt_trial22,
                                    bnt_trial23,
                                    bnt_trial24,
                                    bnt_trial25,
                                    bnt_trial26,
                                    bnt_trial27,
                                    bnt_trial31,
                                    bnt_trial32,
                                    bnt_trial33,
                                    bnt_trial34,
                                    bnt_trial35,
                                    bnt_trial36,
                                    bnt_trial37,
                                    bnt_trial41,
                                    bnt_trial42,
                                    bnt_trial43,
                                    bnt_trial51,
                                    bnt_trial52,
                                    bnt_trial53,
                                    bnt_trial54,
                                    bnt_trial55,
                                    bnt_trial56,
                                    bnt_trial57,
                                    bnt_trial61,
                                    bnt_trial62,
                                    bnt_trial63,
                                    bnt_trial71,
                                    bnt_trial72,
                                    bnt_trial73,
                                    bnt_trial74,
                                    bnt_trial81,
                                    bnt_trial82,
                                    bnt_trial83,
                                    bnt_trial84,
                                    bnt_trial85,
                                    bnt_trial91,
                                    bnt_trial92,
                                    bnt_trial93,
                                    bnt_trial94,
                                    bnt_trial101,
                                    bnt_trial102,
                                    bnt_trial103,
                                    bnt_trial111,
                                    bnt_trial112,
                                    bnt_trial113,
                                    bnt_trial114,
                                    bnt_trial115,
                                    bnt_trial121,
                                    bnt_trial122,
                                    bnt_trial123,
                                    bnt_trial124,
                                ),
                            )
                            conn.commit()
                            ui.notify(
                                "Saved successfully!",
                                position="center",
                                type="positive",
                                close_button="OK",
                            )

                        data_entry()

                def graph(event):
                    """
                    Generate and display graphs for a specific student.

                    Parameters
                    ----------
                    event : SomeEventType
                        The event triggering the graph generation (not used in the function).

                    Returns
                    -------
                    None

                    Notes
                    -----
                    This function assumes the existence of variables such as `u_studentname.value`,
                    `dataBasePath`, `USER_DIR`, `sqlite3`, pandas = `pd`, numpy = `np`, plotly graph-objects = `go`, and other global variables.

                    The function connects to the SQLite database, retrieves the abacus progress data
                    for the specified student, preprocesses the data, adds noise, performs descriptive
                    statistics, calculates growth factors, creates subplots for each abacus phase,
                    and generates an HTML file with the interactive graph. The generated HTML file is
                    opened in a browser window, and the user is notified of successful graph
                    generation.

                    Examples
                    --------
                    >>> graph(some_event)
                    >>> # BrailleNote Touch Plus Skills Progression graphs for the specified student are generated.
                    >>> # The graphs are displayed in a browser window, and the user is notified.

                    See Also
                    --------
                    Some related functions or classes that might be useful.

                    """
                    dataBasePath = Path(USER_DIR).joinpath(
                        "StudentDatabase", "students.db"
                    )
                    studentname = u_studentname.value
                    conn = sqlite3.connect(dataBasePath)
                    df_sql = pd.read_sql_query("SELECT * FROM BNTPROGRESS", conn)
                    df_student = df_sql[df_sql.STUDENTNAME == studentname]
                    print(df_student)
                    conn.close()
                    df = df_student.drop(columns=["ID", "STUDENTNAME"])
                    print(df)
                    df = df.rename(columns={"DATE": "date"})
                    df["date"] = df["date"].astype("string")
                    df["date"] = pd.to_datetime(df["date"], format=date_fmt)
                    df = df.set_index("date")
                    for column in df.columns:
                        if df[column].dtype == "object":
                            df[column] = df[column].astype("int64")
                    print("Braillenote Touch Plus Skills Progression")
                    print(df)
                    df = df.sort_values(by="date")
                    mu, sigma = 0, 0.1
                    noise = np.random.normal(
                        mu, sigma, [len(df.index), len(df.columns)]
                    )
                    df_noisy = df + noise
                    descriptiveStats = df.describe()
                    print("Descriptive Statistics")
                    print(descriptiveStats)
                    growthCalculation = df.diff(periods=3)
                    growth = growthCalculation[-1:]
                    print("Growth Factor (Now vs 3 Measurements ago)")
                    print(growth)
                    fig = make_subplots(
                        rows=3,
                        cols=4,
                        subplot_titles=(
                            "Basic Skills",
                            "KeyMath",
                            "Calendar",
                            "KeyBRF",
                            "KeyFiles",
                            "Keymail",
                            "KeyWeb",
                            "KeyCalc",
                            "KeyWord",
                            "KeySlides",
                            "KeyCode",
                            "Third Party Apps",
                        ),
                        print_grid=True,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_1"],
                            mode="lines+markers",
                            name="Physical Layout",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_2"],
                            mode="lines+markers",
                            name="Setup/Universal Commands",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_3"],
                            mode="lines+markers",
                            name="BNT+ Navigation",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_4"],
                            mode="lines+markers",
                            name="File System navigation",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_5"],
                            mode="lines+markers",
                            name="Main Menu Options",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_6"],
                            mode="lines+markers",
                            name="Settings Menus",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_7"],
                            mode="lines+markers",
                            name="Read Book with EasyReader Plus",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_8"],
                            mode="lines+markers",
                            name="Braille Terminal",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_9"],
                            mode="lines+markers",
                            name="System Updates",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_1"],
                            mode="lines+markers",
                            name="Creating folders",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_2"],
                            mode="lines+markers",
                            name="Differences among drives, folders, and files",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_3"],
                            mode="lines+markers",
                            name="Navigating in the file browser",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_4"],
                            mode="lines+markers",
                            name="Moving, copying and pasting file and folders",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_5"],
                            mode="lines+markers",
                            name="Renaming a file or a folder",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_6"],
                            mode="lines+markers",
                            name="Sharing files",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_7"],
                            mode="lines+markers",
                            name="File and folder commands",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_1"],
                            mode="lines+markers",
                            name="Editing Document in Keyword",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_2"],
                            mode="lines+markers",
                            name="Create a Document",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_3"],
                            mode="lines+markers",
                            name="Open a Document",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_4"],
                            mode="lines+markers",
                            name="Save a Document",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_5"],
                            mode="lines+markers",
                            name="Read a Document",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_6"],
                            mode="lines+markers",
                            name="Visual Preview",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_7"],
                            mode="lines+markers",
                            name="Save as .docx Word File",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_1"],
                            mode="lines+markers",
                            name="Create and edit math object",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_2"],
                            mode="lines+markers",
                            name="Paste into KeyWord",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_3"],
                            mode="lines+markers",
                            name="Generate and Read Graphics",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_1"],
                            mode="lines+markers",
                            name="Setting up an email account",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_2"],
                            mode="lines+markers",
                            name="Writing and sending emails",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_3"],
                            mode="lines+markers",
                            name="Attaching a file",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_4"],
                            mode="lines+markers",
                            name="Reading and searching for emails",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_5"],
                            mode="lines+markers",
                            name="Viewing attached files",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_6"],
                            mode="lines+markers",
                            name="Marking, highlighting, deleting, and other email  options",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_7"],
                            mode="lines+markers",
                            name="Deleting an email account",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_1"],
                            mode="lines+markers",
                            name="Launching KeySlides",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_2"],
                            mode="lines+markers",
                            name="Opening a PowerPoint document",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_3"],
                            mode="lines+markers",
                            name="Navigating in your presentation document",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_1"],
                            mode="lines+markers",
                            name="Creating appointments",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_2"],
                            mode="lines+markers",
                            name="Viewing, editing and deleting appointments",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_3"],
                            mode="lines+markers",
                            name="Navigating the agenda",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_4"],
                            mode="lines+markers",
                            name="Navigating Day View",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_1"],
                            mode="lines+markers",
                            name="Internet Browsing with Chrome",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_2"],
                            mode="lines+markers",
                            name="Internet Navigation",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_3"],
                            mode="lines+markers",
                            name="Bookmarks",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_4"],
                            mode="lines+markers",
                            name="History",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_5"],
                            mode="lines+markers",
                            name="Downloading Files",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P9_1"],
                            mode="lines+markers",
                            name="Inputting calculations",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P9_2"],
                            mode="lines+markers",
                            name="Inserting a Math symbol in KeyCalc",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P9_3"],
                            mode="lines+markers",
                            name="Show results as fractions or decimals",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P9_4"],
                            mode="lines+markers",
                            name="History",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=3,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P10_1"],
                            mode="lines+markers",
                            name="Opening .brf and .brl files",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P10_2"],
                            mode="lines+markers",
                            name="Creating a .brf or .brl file",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P10_3"],
                            mode="lines+markers",
                            name="Finding Braille Text",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P11_1"],
                            mode="lines+markers",
                            name="Creating a Python File",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P11_2"],
                            mode="lines+markers",
                            name="Opening, Navigating and Editing a Python File",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P11_3"],
                            mode="lines+markers",
                            name="Indentations",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P11_4"],
                            mode="lines+markers",
                            name="Saving a Python File",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P11_5"],
                            mode="lines+markers",
                            name="Coding with KeyCode",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P12_1"],
                            mode="lines+markers",
                            name="Third Party Apps",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P12_2"],
                            mode="lines+markers",
                            name="Downloading Third-Party Apps",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P12_3"],
                            mode="lines+markers",
                            name="Deleting Third-Party Apps",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=4,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P12_4"],
                            mode="lines+markers",
                            name="Third-Part App Usage",
                            legendgroup=" ",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=1,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=1,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=1,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=1,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=1,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=1,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=1,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=1,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=1,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=1,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=1,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=1,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=1,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=1,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=1,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=1,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=2,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=2,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=2,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=2,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=2,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=2,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=2,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=2,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=2,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=2,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=2,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=2,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=2,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=2,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=2,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=2,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=3,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=3,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=3,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=3,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=3,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=3,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=3,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=3,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=3,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=3,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=3,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=3,
                        col=3,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=3,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=3,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=3,
                        col=4,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=3,
                        col=4,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=1,
                        col=1,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=2,
                        col=1,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=3,
                        col=1,
                    )

                    fig.update_layout(
                        template="simple_white",
                        title_text=f"{studentname}: iOS Skills Progression",
                        hovermode="x unified",
                        hoverlabel=dict(namelength=-1),
                    )
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "bntProgression.html",
                    )
                    fig.write_html(tmppath, auto_open=True)
                    # fig.show()
                    ui.notify(
                        "Graph Successful. The Graphs will open in a Browser Window",
                        position="center",
                        type="positive",
                        close_button="OK",
                    )

                def create_ui() -> None:
                    """
                    Create a GUI layout for entering student information and trial data.

                    Returns
                    -------
                    None

                    Notes
                    -----
                    This function assumes the existence of various UI elements (e.g., `u_studentname`,
                    `u_today_date`, ...`), and other variables related to the application.

                    The UI consists of several rows with different input elements for selecting a
                    student, entering the date, selecting a task, providing a rubric, entering trial
                    data, inputting anecdotal notes, and buttons for saving and exiting.

                    Examples
                    --------
                    >>> create_ui()
                    >>> # GUI layout created with various input elements and buttons.
                    >>> # Users can interact with the UI to enter student information and trial data.

                    See Also
                    --------
                    Some related functions or classes that might be useful.

                    """
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.button("GRAPH", color="#172554", on_click=graph).classes(
                            "text-white"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.select(
                            options=students,
                            with_input=True,
                            on_change=lambda e: u_studentname.set_value(e.value),
                        ).classes("w-[300px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
                        ).tooltip("Type Student Name, it will autocomplete AS you type")
                        ui.date(
                            value="f{datenow}",
                            on_change=lambda e: u_today_date.set_value(e.value),
                        ).classes("w-1/2").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label(
                            "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated  3=Independent"
                        ).props(
                            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
                        )
                        ui.input().props(
                            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 1: Basic SKills").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props('aria-label="Phase 1: Basic Skills"').classes(
                            "sr-only"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.1 Physical Layout",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial11.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Physical Layout"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Physical Layout")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.2 Setup/Universal Commands",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial12.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Setup/Universal Commands"').tooltip(
                            "Setup/Universal Commands"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.3 BNT+ Navigation",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial13.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="BNT+ Navigation"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("BNT+ Navigation")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.4 File System navigation",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial14.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="File System navigation"').tooltip(
                            "File System navigation"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.5 Main Menu Options",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial15.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Main Menu Options"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Main Menu Options")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.6 Settings Menus",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial16.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Settings Menus"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Settings Menus")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.7 Read Book with EasyReader Plus",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial17.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Read Book with EasyReader Plus"').tooltip(
                            "Read Book with EasyReader Plus"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.8 Braille Terminal",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial18.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Braille Terminal"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Braille Terminal")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.9 System Updates",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial19.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="System Updates"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("System Updates")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 2: KeySoft Programs - KeyFiles").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 2: KeySoft Programs - KeyFiles"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.1 Creating folders",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial21.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Creating folders"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Creating folders")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.2 Differences among drives, folders, and files",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial22.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Differences among drives, folders, and files"'
                        ).tooltip("Differences among drives, folders, and files")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.3 Navigating in the file browser",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial23.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Navigating in the file browser"').tooltip(
                            "Navigating in the file browser"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.4 Moving, copying and pasting file and folders",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial24.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Moving, copying and pasting file and folders"'
                        ).tooltip("Moving, copying and pasting file and folders")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.5 Renaming a file or a folder",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial25.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Renaming a file or a folder"').tooltip(
                            "Renaming a file or a folder"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.6 Sharing files",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial26.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Sharing files"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Sharing files")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.7 File and folder commands",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial27.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="File and folder commands"').tooltip(
                            "File and folder commands"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 3: KeySoft Programs - KeyWord").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 3: KeySoft Programs - KeyWord"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.1 Editing Document in Keyword",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial31.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Editing Document in Keyword"').tooltip(
                            "Editing Document in Keyword"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.2 Create a Document in Keyword",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial32.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Create a Document in Keyword"').tooltip(
                            "Create a Document in Keyword"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.3 Open a Document in Keyword",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial33.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Open a Document in Keyword"').tooltip(
                            "Open a Document in Keyword"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.4 Save a Document in Keyword",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial34.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Save a Document in Keyword"').tooltip(
                            "Save a Document in Keyword"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.5 Read a Document in Keyword",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial35.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Read a Document in Keyword"').tooltip(
                            "Read a Document in Keyword"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.6 Visual Preview",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial36.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Visual Preview"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Visual Preview")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.7 Save as Word File",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial37.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Save as Word File"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Save as Word File")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 4: KeySoft Programs - Keymath").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 4: KeySoft Programs - Keymath"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.1 Create and edit math object",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial41.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Create and edit math object"').tooltip(
                            "Create and edit math object"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.2 Paste into KeyWord",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial42.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Insert into KeyWord"').tooltip(
                            "Paste into KeyWord"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.3 Generate and Read Graphics",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial43.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Generate and Read Graphics"').tooltip(
                            "Generate and Read Graphics"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 5: KeySoft Programs - KeyMail").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 5: KeySoft Programs - KeyMail"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.1 Setting up an email account",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial51.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Setting up an email account"').tooltip(
                            "Setting up an email account"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.2 Writing and sending emails",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial52.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Writing and sending emails"').tooltip(
                            "Writing and sending emails"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.3 Attaching a file",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial53.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Attaching a file"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Attaching a file")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.4 Reading and searching for emails",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial54.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Reading and searching for emails"'
                        ).tooltip("Reading and searching for emails")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.5 Viewing attached files",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial55.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Viewing attached files"').tooltip(
                            "Viewing attached files"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.6 Marking, highlighting, deleting, and other email  options",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial56.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Marking, highlighting, deleting, and other email  options"'
                        ).tooltip(
                            "Marking, highlighting, deleting, and other email  options"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.7 Deleting an email account",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial57.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Deleting an email account"').tooltip(
                            "Deleting an email account"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 6: KeySoft Programs - KeySlides").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 6: KeySoft Programs - KeySlides"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.1 Launching KeySlides",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial61.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Launching KeySlides"').tooltip(
                            "Launching KeySlides"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.2 Opening a PowerPoint document",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial62.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Opening a PowerPoint document"').tooltip(
                            "Opening a PowerPoint document"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.3 Navigating in your presentation document",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial63.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Navigating in your presentation document"'
                        ).tooltip("Navigating in your presentation document")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 7: KeySoft Programs - Calendar").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 7: KeySoft Programs - Calendar"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.1 Creating appointments",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial71.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Creating appointments"').tooltip(
                            "Creating appointments"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.2 Viewing, editing and deleting appointments",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial72.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Viewing, editing and deleting appointments"'
                        ).tooltip("Viewing, editing and deleting appointments")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.3 Navigating the agenda",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial73.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Navigating the agenda"').tooltip(
                            "Navigating the agenda"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.4 Navigating Day View",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial74.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Navigating Day View"').tooltip(
                            "Navigating Day View"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 8: KeySoft Programs - KeyMail").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 8: KeySoft Programs - KeyMail"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.1 Internet Browsing with Chrome",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial81.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Internet Browsing with Chrome"').tooltip(
                            "Internet Browsing with Chrome"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.2 Internet Navigation",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial82.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Internet Navigation"').tooltip(
                            "Internet Navigation"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.3 Bookmarks",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial83.set_value(e.value),
                        ).classes("w-[400px]").props('aria-label="Bookmarks"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Bookmarks")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.4 History",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial84.set_value(e.value),
                        ).classes("w-[400px]").props('aria-label="History"').tooltip(
                            "History"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.5 Downloading Files",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial85.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Downloading Files"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Downloading Files")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 9: KeySoft Programs - KeyCalc").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 9: KeySoft Programs - KeyCalc"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="9.1 Inputting calculations",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial91.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Inputting calculations"').tooltip(
                            "Inputting calculations"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="9.2 Inserting a Math symbol in KeyCalc",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial92.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Inserting a Math symbol in KeyCalc"'
                        ).tooltip("Inserting a Math symbol in KeyCalc")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="9.3 Show results as fractions or decimals",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial93.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Show results as fractions or decimals"'
                        ).tooltip("Show results as fractions or decimals")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="9.4 History",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial94.set_value(e.value),
                        ).classes("w-[400px]").props('aria-label="History"').tooltip(
                            "History"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 10: KeySoft Programs - KeyBRF").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 10: KeySoft Programs - KeyBRF"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="10.1 Opening .brf and .brl files",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial101.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Opening .brf and .brl files"').tooltip(
                            "Opening .brf and .brl files"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="10.2 Creating a .brf or .brl file",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial102.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Creating a .brf or .brl file"').tooltip(
                            "Creating a .brf or .brl file"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="10.3 Finding Braille Text",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial103.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Finding Braille Text"').tooltip(
                            "Finding Braille Text"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 11: KeySoft Programs - KeyCode").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 11: KeySoft Programs - KeyCode"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="11.1 Creating a Python File",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial111.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Creating a Python File"').tooltip(
                            "Creating a Python File"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="11.2 Opening, Navigating and Editing a Python File",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial112.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Opening, Navigating and Editing a Python File"'
                        ).tooltip("Opening, Navigating and Editing a Python File")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="11.3 Indentations",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial113.set_value(e.value),
                        ).classes("w-[400px]").props('aria-label="Indentations"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Indentations")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="11.4 Saving a Python File",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial114.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Saving a Python File"').tooltip(
                            "Saving a Python File"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="11.5 Coding with KeyCode",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial115.set_value(e.value),
                        ).classes("w-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Coding with KeyCode"').tooltip(
                            "Coding with KeyCode"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Phase 12: Third Party Apps").classes(
                            "justify-center items-center text-lg"
                        )
                        ui.input().props(
                            'aria-label="Phase 12: Third Party Apps"'
                        ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="12.1 Third Party Apps",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial121.set_value(e.value),
                        ).classes("w-[400px]").props(
                            'aria-label="Third Party Apps"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Third Party Apps")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="12. Downloading",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial122.set_value(e.value),
                        ).classes("w-[400px]").props('aria-label="Downloading"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Downloading")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="12.3 Deleting",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial123.set_value(e.value),
                        ).classes("w-[400px]").props('aria-label="Deleting"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Deleting")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="12.4 Usage",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_bnt_trial124.set_value(e.value),
                        ).classes("w-[400px]").props('aria-label="Usage"').tooltip(
                            "Usage"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.button("SAVE", color="#172554", on_click=save).classes(
                            "text-white"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.button("GRAPH", color="#172554", on_click=graph).classes(
                            "text-white"
                        )
                        ui.button(
                            "EXIT", color="#172554", on_click=app.shutdown
                        ).classes("text-white")
        create_ui()