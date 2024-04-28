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
    """Braille Skills Progression"""

    @ui.page("/brailleskills")
    def brailleskills() -> None:
        with theme.frame("- TACTILE SKILLS -"):
            with ui.tabs() as tabs:
                ui.tab("DATA INPUT")
                ui.tab("DATA VISUALIZATION")
            with ui.tab_panels(tabs, value="DATA INPUT"):
                with ui.tab_panel("DATA INPUT"):
                    ui.label("BRAILLE SKILLS").classes("text-h4 text-grey-8").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    )

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
                    u_braille_trial11 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial12 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial13 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial14 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial21 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial22 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial23 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial24 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial25 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial26 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial27 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial28 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial29 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial210 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial211 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial212 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial213 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial214 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial215 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial31 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial32 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial33 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial34 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial35 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial36 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial37 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial38 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial39 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial310 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial311 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial312 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial313 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial314 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial315 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial41 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial42 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial43 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial44 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial51 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial52 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial53 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial54 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial61 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial62 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial63 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial64 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial65 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial66 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial67 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial71 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial72 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial73 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial74 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial75 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial76 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial77 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial78 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial81 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial82 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial83 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial84 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial85 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial86 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_braille_trial87 = (
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
                        braille_trial11 = int(u_braille_trial11.value)
                        braille_trial12 = int(u_braille_trial12.value)
                        braille_trial13 = int(u_braille_trial13.value)
                        braille_trial14 = int(u_braille_trial14.value)
                        braille_trial21 = int(u_braille_trial21.value)
                        braille_trial22 = int(u_braille_trial22.value)
                        braille_trial23 = int(u_braille_trial23.value)
                        braille_trial24 = int(u_braille_trial24.value)
                        braille_trial25 = int(u_braille_trial25.value)
                        braille_trial26 = int(u_braille_trial26.value)
                        braille_trial27 = int(u_braille_trial27.value)
                        braille_trial28 = int(u_braille_trial28.value)
                        braille_trial29 = int(u_braille_trial29.value)
                        braille_trial210 = int(u_braille_trial210.value)
                        braille_trial211 = int(u_braille_trial211.value)
                        braille_trial212 = int(u_braille_trial212.value)
                        braille_trial213 = int(u_braille_trial213.value)
                        braille_trial214 = int(u_braille_trial214.value)
                        braille_trial215 = int(u_braille_trial215.value)
                        braille_trial31 = int(u_braille_trial31.value)
                        braille_trial32 = int(u_braille_trial32.value)
                        braille_trial33 = int(u_braille_trial33.value)
                        braille_trial34 = int(u_braille_trial34.value)
                        braille_trial35 = int(u_braille_trial35.value)
                        braille_trial36 = int(u_braille_trial36.value)
                        braille_trial37 = int(u_braille_trial37.value)
                        braille_trial38 = int(u_braille_trial38.value)
                        braille_trial39 = int(u_braille_trial39.value)
                        braille_trial310 = int(u_braille_trial310.value)
                        braille_trial311 = int(u_braille_trial311.value)
                        braille_trial312 = int(u_braille_trial312.value)
                        braille_trial313 = int(u_braille_trial313.value)
                        braille_trial314 = int(u_braille_trial314.value)
                        braille_trial315 = int(u_braille_trial315.value)
                        braille_trial41 = int(u_braille_trial41.value)
                        braille_trial42 = int(u_braille_trial42.value)
                        braille_trial43 = int(u_braille_trial43.value)
                        braille_trial44 = int(u_braille_trial44.value)
                        braille_trial51 = int(u_braille_trial51.value)
                        braille_trial52 = int(u_braille_trial52.value)
                        braille_trial53 = int(u_braille_trial53.value)
                        braille_trial54 = int(u_braille_trial54.value)
                        braille_trial61 = int(u_braille_trial61.value)
                        braille_trial62 = int(u_braille_trial62.value)
                        braille_trial63 = int(u_braille_trial63.value)
                        braille_trial64 = int(u_braille_trial64.value)
                        braille_trial65 = int(u_braille_trial65.value)
                        braille_trial66 = int(u_braille_trial66.value)
                        braille_trial67 = int(u_braille_trial67.value)
                        braille_trial71 = int(u_braille_trial71.value)
                        braille_trial72 = int(u_braille_trial72.value)
                        braille_trial73 = int(u_braille_trial73.value)
                        braille_trial74 = int(u_braille_trial74.value)
                        braille_trial75 = int(u_braille_trial75.value)
                        braille_trial76 = int(u_braille_trial76.value)
                        braille_trial77 = int(u_braille_trial77.value)
                        braille_trial78 = int(u_braille_trial78.value)
                        braille_trial81 = int(u_braille_trial81.value)
                        braille_trial82 = int(u_braille_trial82.value)
                        braille_trial83 = int(u_braille_trial83.value)
                        braille_trial84 = int(u_braille_trial84.value)
                        braille_trial85 = int(u_braille_trial85.value)
                        braille_trial86 = int(u_braille_trial86.value)
                        braille_trial87 = int(u_braille_trial87.value)
                        studentdatabasename = f"braille{studentname.title()}{datenow}"
                        tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase",
                            "StudentDataFiles",
                            studentname,
                            studentdatabasename + ".json",
                        )
                        braille_dictionary = {
                            "studentname": studentname,
                            "date": today_date,
                            "braille_trial11": braille_trial11,
                            "braille_trial12": braille_trial12,
                            "braille_trial13": braille_trial13,
                            "braille_trial14": braille_trial14,
                            "braille_trial21": braille_trial21,
                            "braille_trial22": braille_trial22,
                            "braille_trial23": braille_trial23,
                            "braille_trial24": braille_trial24,
                            "braille_trial25": braille_trial25,
                            "braille_trial26": braille_trial26,
                            "braille_trial27": braille_trial27,
                            "braille_trial28": braille_trial28,
                            "braille_trial29": braille_trial29,
                            "braille_trial210": braille_trial210,
                            "braille_trial211": braille_trial211,
                            "braille_trial212": braille_trial212,
                            "braille_trial213": braille_trial213,
                            "braille_trial214": braille_trial214,
                            "braille_trial215": braille_trial215,
                            "braille_trial31": braille_trial31,
                            "braille_trial32": braille_trial32,
                            "braille_trial33": braille_trial33,
                            "braille_trial34": braille_trial34,
                            "braille_trial35": braille_trial35,
                            "braille_trial36": braille_trial36,
                            "braille_trial37": braille_trial37,
                            "braille_trial38": braille_trial38,
                            "braille_trial39": braille_trial39,
                            "braille_trial310": braille_trial310,
                            "braille_trial311": braille_trial311,
                            "braille_trial312": braille_trial312,
                            "braille_trial313": braille_trial313,
                            "braille_trial314": braille_trial314,
                            "braille_trial315": braille_trial315,
                            "braille_trial41": braille_trial41,
                            "braille_trial42": braille_trial42,
                            "braille_trial43": braille_trial43,
                            "braille_trial44": braille_trial44,
                            "braille_trial51": braille_trial51,
                            "braille_trial52": braille_trial52,
                            "braille_trial53": braille_trial53,
                            "braille_trial54": braille_trial54,
                            "braille_trial61": braille_trial61,
                            "braille_trial62": braille_trial62,
                            "braille_trial63": braille_trial63,
                            "braille_trial64": braille_trial64,
                            "braille_trial65": braille_trial65,
                            "braille_trial66": braille_trial66,
                            "braille_trial67": braille_trial67,
                            "braille_trial71": braille_trial71,
                            "braille_trial72": braille_trial72,
                            "braille_trial73": braille_trial73,
                            "braille_trial74": braille_trial74,
                            "braille_trial75": braille_trial75,
                            "braille_trial76": braille_trial76,
                            "braille_trial77": braille_trial77,
                            "braille_trial78": braille_trial78,
                            "braille_trial81": braille_trial81,
                            "braille_trial82": braille_trial82,
                            "braille_trial83": braille_trial83,
                            "braille_trial84": braille_trial84,
                            "braille_trial85": braille_trial85,
                            "braille_trial86": braille_trial86,
                            "braille_trial87": braille_trial87,
                        }
                        with open(tmppath, "w", encoding="utf-8") as filename:
                            json.dump(braille_dictionary, filename)
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
                                """INSERT INTO BRAILLEPROGRESS (
                                                            STUDENTNAME,
                                                            DATE,
                                                            P1_1,
                                                            P1_2,
                                                            P1_3,
                                                            P1_4,
                                                            P2_1,
                                                            P2_2,
                                                            P2_3,
                                                            P2_4,
                                                            P2_5,
                                                            P2_6,
                                                            P2_7,
                                                            P2_8,
                                                            P2_9,
                                                            P2_10,
                                                            P2_11,
                                                            P2_12,
                                                            P2_13,
                                                            P2_14,
                                                            P2_15,
                                                            P3_1,
                                                            P3_2,
                                                            P3_3,
                                                            P3_4,
                                                            P3_5,
                                                            P3_6,
                                                            P3_7,
                                                            P3_8,
                                                            P3_9,
                                                            P3_10,
                                                            P3_11,
                                                            P3_12,
                                                            P3_13,
                                                            P3_14,
                                                            P3_15,
                                                            P4_1,
                                                            P4_2,
                                                            P4_3,
                                                            P4_4,
                                                            P5_1,
                                                            P5_2,
                                                            P5_3,
                                                            P5_4,
                                                            P6_1,
                                                            P6_2,
                                                            P6_3,
                                                            P6_4,
                                                            P6_5,
                                                            P6_6,
                                                            P6_7,
                                                            P7_1,
                                                            P7_2,
                                                            P7_3,
                                                            P7_4,
                                                            P7_5,
                                                            P7_6,
                                                            P7_7,
                                                            P7_8,
                                                            P8_1,
                                                            P8_2,
                                                            P8_3,
                                                            P8_4,
                                                            P8_5,
                                                            P8_6,
                                                            P8_7
                                                            )
                                                            VALUES (?,
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
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?)""",
                                (
                                    studentname,
                                    today_date,
                                    braille_trial11,
                                    braille_trial12,
                                    braille_trial13,
                                    braille_trial14,
                                    braille_trial21,
                                    braille_trial22,
                                    braille_trial23,
                                    braille_trial24,
                                    braille_trial25,
                                    braille_trial26,
                                    braille_trial27,
                                    braille_trial28,
                                    braille_trial29,
                                    braille_trial210,
                                    braille_trial211,
                                    braille_trial212,
                                    braille_trial213,
                                    braille_trial214,
                                    braille_trial215,
                                    braille_trial31,
                                    braille_trial32,
                                    braille_trial33,
                                    braille_trial34,
                                    braille_trial35,
                                    braille_trial36,
                                    braille_trial37,
                                    braille_trial38,
                                    braille_trial39,
                                    braille_trial310,
                                    braille_trial311,
                                    braille_trial312,
                                    braille_trial313,
                                    braille_trial314,
                                    braille_trial315,
                                    braille_trial41,
                                    braille_trial42,
                                    braille_trial43,
                                    braille_trial44,
                                    braille_trial51,
                                    braille_trial52,
                                    braille_trial53,
                                    braille_trial54,
                                    braille_trial61,
                                    braille_trial62,
                                    braille_trial63,
                                    braille_trial64,
                                    braille_trial65,
                                    braille_trial66,
                                    braille_trial67,
                                    braille_trial71,
                                    braille_trial72,
                                    braille_trial73,
                                    braille_trial74,
                                    braille_trial75,
                                    braille_trial76,
                                    braille_trial77,
                                    braille_trial78,
                                    braille_trial81,
                                    braille_trial82,
                                    braille_trial83,
                                    braille_trial84,
                                    braille_trial85,
                                    braille_trial86,
                                    braille_trial87,
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
                    >>> # Braille Skills Progression graphs for the specified student are generated.
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
                    df_sql = pd.read_sql_query("SELECT * FROM BRAILLEPROGRESS", conn)
                    df_student = df_sql[df_sql.STUDENTNAME == studentname]
                    # print(df_student)
                    conn.close()
                    df = df_student.drop(columns=["ID", "STUDENTNAME"])
                    # print(df)
                    df = df.rename(columns={"DATE": "date"})
                    df["date"] = df["date"].astype("string")
                    df["date"] = pd.to_datetime(df["date"], format=date_fmt)
                    df = df.set_index("date")
                    print("Braille SKills Progression")
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
                        rows=7,
                        cols=2,
                        specs=[
                            [{}, {"rowspan": 2}],
                            [{}, None],
                            [{"rowspan": 2}, {"rowspan": 2}],
                            [None, None],
                            [{"rowspan": 2}, {"rowspan": 2}],
                            [None, None],
                            [{}, {}],
                        ],
                        subplot_titles=(
                            "Phase 1: Tracking Skills",
                            "Phase 2: Braille Alphabet",
                            "Phase 1: Tracking Skills",
                            "Phase 3a: Wordsigns, Numbers, Punctuation",
                            "Phase 3b: Strong Contractions",
                            "Phase 3c: Lower Cell Contractions",
                            "Phase 3d: Multiple Cell Contractions",
                            "Phase 4a: Braille Mode Indicators",
                            "Phase 5: Document Formatting",
                        ),
                        print_grid=True,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_1"],
                            mode="lines+markers",
                            name="Track left to right",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_2"],
                            mode="lines+markers",
                            name="Track top to bottom",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_4"],
                            mode="lines+markers",
                            name="Discriminate braille characters",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_1"],
                            mode="lines+markers+text",
                            name="Alphabet",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_2"],
                            mode="lines+markers+text",
                            name="D Y",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_3"],
                            mode="lines+markers+text",
                            name="A B",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_4"],
                            mode="lines+markers+text",
                            name="S",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )

                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_5"],
                            mode="lines+markers+text",
                            name="W",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_6"],
                            mode="lines+markers+text",
                            name="P O",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_7"],
                            mode="lines+markers+text",
                            name="K",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_8"],
                            mode="lines+markers+text",
                            name="R",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_9"],
                            mode="lines+markers+text",
                            name="M E",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_10"],
                            mode="lines+markers+text",
                            name="H",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_11"],
                            mode="lines+markers+text",
                            name="N X",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_12"],
                            mode="lines+markers+text",
                            name="Z F",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_13"],
                            mode="lines+markers+text",
                            name="U T",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_14"],
                            mode="lines+markers+text",
                            name="Q I",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_15"],
                            mode="lines+markers+text",
                            name="V J ",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=False,
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.update_layout(showlegend=True)
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_1"],
                            mode="lines+markers",
                            name="Alphabetic Wordsigns",
                            legendgroup="Phase 3a",
                            legendgrouptitle_text="Phase 3a",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_2"],
                            mode="lines+markers",
                            name="Braille Numbers",
                            legendgroup="Phase 3a",
                            legendgrouptitle_text="Phase 3a",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_3"],
                            mode="lines+markers",
                            name="Punctuation",
                            legendgroup="Phase 3a",
                            legendgrouptitle_text="Phase 3a",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_4"],
                            mode="lines+markers",
                            name="Strong Contractions <br>(AND OF FOR WITH THE)",
                            legendgroup="Phase 3b",
                            legendgrouptitle_text="Phase 3b",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_5"],
                            mode="lines+markers",
                            name="Strong Groupsigns <br>(CH GH SH TH "
                            "WH "
                            "ED "
                            "ER "
                            "OU OW ST AR ING)",
                            legendgroup="Phase 3b",
                            legendgrouptitle_text="Phase 3b",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_6"],
                            mode="lines+markers",
                            name="Strong Wordsigns <br>(CH SH TH WH OU ST)",
                            legendgroup="Phase 3b",
                            legendgrouptitle_text="Phase 3b",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_7"],
                            mode="lines+markers",
                            name="Lower Groupsigns <br>(BE CON DIS)",
                            legendgroup="Phase 3c",
                            legendgrouptitle_text="Phase 3c",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_8"],
                            mode="lines+markers",
                            name="Lower Groupsigns <br>(EA BB CC FF GG)",
                            legendgroup="Phase 3c",
                            legendgrouptitle_text="Phase 3c",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_9"],
                            mode="lines+markers",
                            name="Lower Groupsigns/Wordsigns <br>(EN IN)",
                            legendgroup="Phase 3c",
                            legendgrouptitle_text="Phase 3c",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_10"],
                            mode="lines+markers",
                            name="Lower Wordsigns <br>(BE HIS WAS WERE)",
                            legendgroup="Phase 3c",
                            legendgrouptitle_text="Phase 3c",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_11"],
                            mode="lines+markers",
                            name="Dot 5 Contractions",
                            legendgroup="Phase 3d",
                            legendgrouptitle_text="Phase 3d",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_12"],
                            mode="lines+markers",
                            name="Dot 45 Contractions",
                            legendgroup="Phase 3d",
                            legendgrouptitle_text="Phase 3d",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_13"],
                            mode="lines+markers",
                            name="Dot 456 Contractions",
                            legendgroup="Phase 3d",
                            legendgrouptitle_text="Phase 3d",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_14"],
                            mode="lines+markers",
                            name="Final Letter Groupsigns",
                            legendgroup="Phase 3d",
                            legendgrouptitle_text="Phase 3d",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_15"],
                            mode="lines+markers",
                            name="Shortform Words",
                            legendgroup="Phase 3d",
                            legendgrouptitle_text="Phase 3d",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_1"],
                            mode="lines+markers",
                            name="Grade 1 Indicators",
                            legendgroup="Phase 4",
                            legendgrouptitle_text="Phase 4",
                        ),
                        row=7,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_2"],
                            mode="lines+markers",
                            name="Capitals Indicators",
                            legendgroup="Phase 4",
                            legendgrouptitle_text="Phase 4",
                        ),
                        row=7,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_3"],
                            mode="lines+markers",
                            name="Numeric Mode and Spatial math",
                            legendgroup="Phase 4",
                            legendgrouptitle_text="Phase 4",
                        ),
                        row=7,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_4"],
                            mode="lines+markers",
                            name="Typeform Indicators <br>(ITALIC, "
                            "SCRIPT, "
                            "UNDERLINE, BOLDFACE)",
                            legendgroup="Phase 4",
                            legendgrouptitle_text="Phase 4",
                        ),
                        row=7,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_1"],
                            mode="lines+markers",
                            name="Page Numbering",
                            legendgroup="Phase 5",
                            legendgrouptitle_text="Phase 5",
                        ),
                        row=7,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_2"],
                            mode="lines+markers",
                            name="Headings",
                            legendgroup="Phase 5",
                            legendgrouptitle_text="Phase 5",
                        ),
                        row=7,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_3"],
                            mode="lines+markers",
                            name="Lists",
                            legendgroup="Phase 5",
                            legendgrouptitle_text="Phase 5",
                        ),
                        row=7,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_4"],
                            mode="lines+markers",
                            name="Poety / Drama",
                            legendgroup="Phase 5",
                            legendgrouptitle_text="Phase 5",
                        ),
                        row=7,
                        col=2,
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
                        row=5,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=5,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=5,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=5,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=5,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=5,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=5,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=5,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=7,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=7,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=7,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=7,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="red",
                        opacity=0.2,
                        row=7,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=7,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=7,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=7,
                        col=2,
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
                        row=1,
                        col=2,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=3,
                        col=1,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=3,
                        col=2,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=5,
                        col=1,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=5,
                        col=2,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=5,
                        col=2,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=7,
                        col=2,
                    )
                    fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=7,
                        col=2,
                    )
                    fig.update_layout(
                        xaxis_tickformat="%d %b",
                        xaxis2_tickformat="%d %b",
                        xaxis3_tickformat="%d %b",
                        xaxis4_tickformat="%d %b",
                        xaxis5_tickformat="%d %b",
                        xaxis6_tickformat="%d %b",
                        xaxis7_tickformat="%d %b",
                        xaxis8_tickformat="%d %b",
                        xaxis9_tickformat="%d %b",
                        template="simple_white",
                        title_text=f"{studentname}: Literary UEB Skills "
                        f"Progression",
                        legend=dict(font=dict(size=10)),
                        hovermode="x unified",
                        hoverlabel=dict(namelength=-1),
                    )
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "UEBLiterarySkillsProgression.html",
                    )
                    fig.write_html(tmppath, auto_open=True)
                    # fig.show()
                    ui.notify(
                        "Graph Successful. The Graphs will open in a Browser Window",
                        close_button="OK",
                    )

                    fig = make_subplots(
                        rows=3,
                        cols=1,
                        subplot_titles=(
                            "Phase 6: UEB Technical Basics",
                            "Phase 7: Advanced UEB Technical",
                            "Phase 8: Accelerated UEB Technical",
                        ),
                        print_grid=True,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_1"],
                            mode="lines+markers",
                            name=" Operation and Comparison Signs",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_2"],
                            mode="lines+markers",
                            name="Grade 1 Mode",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_3"],
                            mode="lines+markers",
                            name="Special Print Symbols",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_4"],
                            mode="lines+markers",
                            name="Omission Marks",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_5"],
                            mode="lines+markers",
                            name="Shape Indicators",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_6"],
                            mode="lines+markers",
                            name="Roman Numerals",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_7"],
                            mode="lines+markers",
                            name="Fractions",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_1"],
                            mode="lines+markers",
                            name="Grade 1 Mode and Algebra",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_2"],
                            mode="lines+markers",
                            name="Grade 1 Mode and Fractions",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_3"],
                            mode="lines+markers",
                            name="Advanced Operation and Comparison Signs",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_4"],
                            mode="lines+markers",
                            name="Indices",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_5"],
                            mode="lines+markers",
                            name="Roots and Radicals",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_6"],
                            mode="lines+markers",
                            name="Miscellaneous Shape Indicators",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_7"],
                            mode="lines+markers",
                            name="Functions",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_8"],
                            mode="lines+markers",
                            name="Greek letters",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_1"],
                            mode="lines+markers",
                            name="Functions",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_2"],
                            mode="lines+markers",
                            name="Modifiers, Bars, and Dots",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_3"],
                            mode="lines+markers",
                            name="Modifiers, Arrows, and Limits",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_4"],
                            mode="lines+markers",
                            name="Probability",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_5"],
                            mode="lines+markers",
                            name="Calculus: Differentiation",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_6"],
                            mode="lines+markers",
                            name="Calculus: Integration",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_7"],
                            mode="lines+markers",
                            name="Vertical Bars",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                        ),
                        row=3,
                        col=1,
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
                    fig.update_layout(
                        xaxis_tickformat="%d %b",
                        xaxis2_tickformat="%d %b",
                        xaxis3_tickformat="%d %b",
                        template="simple_white",
                        title_text=f""
                        f"{studentname}: Technical UEB Skills "
                        f"Progression",
                        legend=dict(font=dict(size=10)),
                        hovermode="x unified",
                        hoverlabel=dict(namelength=-1),
                    )
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "UEBTechnicalSkillsProgression.html",
                    )
                    fig.write_html(tmppath, auto_open=True)
                    # fig.show()
                    ui.notify(
                        "Graph Successful. The Graphs will open in a Browser Window",
                        position="center",
                        type="positive",
                        close_button="OK",
                    )

                    fig = make_subplots(
                        rows=1,
                        cols=2,
                        column_widths=[0.2, 0.8],
                        subplot_titles=(
                            "Phase 1: Tracking Skills Development",
                            "Phase 2: Tactile Recognition Skills",
                        ),
                        print_grid=True,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_1"],
                            mode="lines+markers",
                            name="Track left to right",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_2"],
                            mode="lines+markers",
                            name="Track top to bottom",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_3"].iloc[[-1]],
                            mode="lines+markers",
                            name="Discriminate shapes",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_4"],
                            mode="lines+markers",
                            name="Discriminate braille characters",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
                        ),
                        row=1,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_1"],
                            mode="lines+markers+text",
                            name="G C L",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_2"],
                            mode="lines+markers+text",
                            name="D Y",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_3"],
                            mode="lines+markers+text",
                            name="A B",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_4"],
                            mode="lines+markers+text",
                            name="S",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_5"],
                            mode="lines+markers+text",
                            name="W",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_6"],
                            mode="lines+markers+text",
                            name="P O",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_7"],
                            mode="lines+markers+text",
                            name="K",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_8"],
                            mode="lines+markers+text",
                            name="R",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_9"],
                            mode="lines+markers+text",
                            name="M E",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_10"],
                            mode="lines+markers+text",
                            name="H",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )

                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_11"],
                            mode="lines+markers+text",
                            name="N X",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_12"],
                            mode="lines+markers+text",
                            name="Z F",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_13"],
                            mode="lines+markers+text",
                            name="U T",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_14"],
                            mode="lines+markers+text",
                            name="Q I",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_15"],
                            mode="lines+markers+text",
                            name="V J ",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            showlegend=True,
                        ),
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
                    fig.update_layout(
                        xaxis_tickformat="%d %b",
                        xaxis2_tickformat="%d %b",
                        template="simple_white",
                        title_text=f"{studentname}: Basic Tactile Recognition "
                        f"Progression",
                        legend=dict(font=dict(size=10)),
                        hovermode="x unified",
                        hoverlabel=dict(namelength=-1),
                    )
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "BasicTactileRecognition.html",
                    )
                    fig.write_html(tmppath, auto_open=True)
                    # fig.show()
                    ui.notify(
                        "Graph Successful. The Graphs will open in a Browser Window",
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
                            "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"
                        ).props(
                            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 1: Braille Tracking Skills").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 1: Braille Tracking Skills"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.1 Track Left to Right",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial11.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="1.1 Track Left to Right"').tooltip(
                            "1.1 Track Left to Right"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.2 Track Top to Bottom",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial12.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="1.2 Track Top to Bottom"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.3 Discriminate Shapes",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial13.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="1.3 Discriminate Shapes"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.4 Discriminate Braille Characters",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial14.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="1.4 Discriminate Braille Characters"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label(
                            "PHASE 2: Tactile Letter Recognition (after Mangold)"
                        ).classes("justify-center items-center text-lg").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 2: Tactile Letter Recognition (after Mangold)"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.1 Mangold Progression: G C L",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial21.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.1 Mangold Progression: G C L"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.2 Mangold Progression: D Y",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial22.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.2 Mangold Progression: D Y"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.3 Mangold Progression: A B",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial23.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.3 Mangold Progression: A B"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.4 Mangold Progression: S",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial24.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="2.4 Mangold Progression: S"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.5 Mangold Progression: W",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial25.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="2.5 Mangold Progression: W"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.6 Mangold Progression: P O",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial26.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.6 Mangold Progression: P O"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.7 Mangold Progression: K",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial27.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="2.7 Mangold Progression: K"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.8 Mangold Progression: R",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial28.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="2.8 Mangold Progression: R"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.9 Mangold Progression: M E",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial29.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.9 Mangold Progression: M E"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.10 Mangold Progression: H",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial210.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="2.10 Mangold Progression: H"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.11 Mangold Progression: N X",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial211.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.11 Mangold Progression: N X"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.12 Mangold Progression: Z F",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial212.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.12 Mangold Progression: Z F"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.13 Mangold Progression: U T",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial213.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.13 Mangold Progression: U T"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.14 Mangold Progression: Q I",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial214.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.14 Mangold Progression: Q I"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.15 Mangold Progression: V J",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial215.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.15 Mangold Progression: V J"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label(
                            "PHASE 3: Contractions, Groupsigns, Wordsigns, and Shortform Words"
                        ).classes("justify-center items-center text-lg").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 3: Contractions, Groupsigns, Wordsigns, and Shortform Words"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.1 Alphabetic Wordsigns",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial31.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="3.1 Alphabetic Wordsigns"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.2 Braille Numbers",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial32.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="3.2 Braille Numbers"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.3 Punctuation",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial33.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="3.3 Punctuation"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.4 Strong Contractions - AND OF FOR WITH THE",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial34.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="3.4 Strong Contractions - AND OF FOR WITH THE"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.5 Strong Groupsigns - CH GH SH TH WH ED  ER OU OW ST AR ING",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial35.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="3.5 Strong Groupsigns - CH GH SH TH WH ED  ER OU OW ST AR ING"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.6 Strong Wordsigns - CH SH TH WH OU ST",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial36.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.6 Strong Wordsigns - CH SH TH WH OU ST"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.7 Lower Groupsigns - BE CON DIS",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial37.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.7 Lower Groupsigns - BE CON DIS"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.8 Lower Groupsigns - EA BB CC FF GG",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial38.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.8 Lower Groupsigns - EA BB CC FF GG"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.9 Lower Group/Wordsigns - EN IN",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial39.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.9 Lower Group/Wordsigns - EN IN"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.10 Lower Wordsigns - BE HIS WAS WERE",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial310.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="3.10 Lower Wordsigns - BE HIS WAS WERE"'
                        ).tooltip("3.10 Lower Wordsigns - BE HIS WAS WERE")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.11 Dot 5 Contractions",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial311.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.11 Dot 5 Contractions"').tooltip(
                            "3.11 Dot 5 Contractions"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.12 Dot 45 Contractions",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial312.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.12 Dot 45 Contractions"').tooltip(
                            "3.12 Dot 45 Contractions"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.13 Dot 456 Contractions",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial313.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.13 Dot 456 Contractions"').tooltip(
                            "3.13 Dot 456 Contractions"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.14 Final Letter Groupsigns",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial314.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.14 Final Letter Groupsigns"').tooltip(
                            "3.14 Final Letter Groupsigns"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.15 Shortform Words",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial315.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="3.15 Shortform Words"').tooltip(
                            "3.15 Shortform Words"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 4: Indicator Usage").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 4: Indicator Usage"'
                        ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.1 Grade 1 Indicators",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial41.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="4.1 Grade 1 Indicators"').tooltip(
                            "4.1 Grade 1 Indicators"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.2 Capitals Indicators",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial42.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="4.2 Capitals Indicators"').tooltip(
                            "4.2 Capitals Indicators"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.3 Numeric Mode and Spatial Math",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial43.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="4.3 Numeric Mode and Spatial Math"'
                        ).tooltip("4.3 Numeric Mode and Spatial Math")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.4 Typeform Indicators - ITALIC BOLD UNDERLINE SCRIPT",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial44.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="4.4 Typeform Indicators - ITALIC BOLD UNDERLINE SCRIPT"'
                        ).tooltip(
                            "4.4 Typeform Indicators - ITALIC BOLD UNDERLINE SCRIPT"
                        )
                        ui.label().classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 5: Advanced Document Formatting").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 5: Advanced Document Formatting"'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.1 Page Numbering",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial51.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="5.1 Page Numbering"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("5.1 Page Numbering")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.2 Headings",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial52.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="5.2 Headings"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("5.2 Headings")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.3 Lists",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial53.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="5.3 Lists"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.4 Poetry / Drama",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial54.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="5.4 Poetry / Drama"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("5.4 Poetry / Drama")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 6: Elementary Math").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 6: Elementary Math "'
                        ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.1 Operation and Comparison Signs",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial61.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="6.1 Operation and Comparison Signs"'
                        ).tooltip("6.1 Operation and Comparison Signs")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.2 Grade 1 Mode",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial62.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="6.2 Grade 1 Mode"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("6.2 Grade 1 Mode")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.3 Special Print Symbols",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial63.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="6.3 Special Print Symbols"').tooltip(
                            "6.3 Special Print Symbols"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.4 Omission Marks",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial64.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="6.4 Omission Marks"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("6.4 Omission Marks")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.5 Shape Indicators",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial65.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="6.5 Shape Indicators"').tooltip(
                            "6.5 Shape Indicators"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.6 Roman Numerals",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial66.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="6.6 Roman Numerals"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("6.6 Roman Numerals")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.7 Fractions",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial67.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="6.7 Fractions"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("6.7 Fractions")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 7: Advanced Mathematics").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 7: Advanced Mathematics"'
                        ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.1 Grade 1 Mode and algebra",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial71.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="7.1 Grade 1 Mode and algebra"').tooltip(
                            "7.1 Grade 1 Mode and algebra"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.2 Grade 1 Mode and Fractions",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial72.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="7.2 Grade 1 Mode and Fractions"').tooltip(
                            "7.2 Grade 1 Mode and Fractions"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.3 Advanced Operation and Comparison Signs",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial73.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="7.3 Advanced Operation and Comparison Signs"'
                        ).tooltip("7.3 Advanced Operation and Comparison Signs")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.4 Indices",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial74.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="7.4 Indices"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("7.4 Indices")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.5 Roots and Radicals",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial75.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="7.5 Roots and Radicals"').tooltip(
                            "7.5 Roots and Radicals"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.6 Miscellaneous Shape Indicators",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial76.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="7.6 Miscellaneous Shape Indicators"'
                        ).tooltip("7.6 Miscellaneous Shape Indicators")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.7 Functions",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial77.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="7.7 Functions"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("7.7 Functions")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.8 Greek Letters",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial78.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="7.8 Greek Letters"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("7.8 Greek Letters")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 8: College Mathematics").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 8: College Mathematics"'
                        ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.1 Functions",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial81.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="8.1 Functions"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.2 Modifiers: Bars and Dots",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial82.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="8.2 Modifiers: Bars and Dots"').tooltip(
                            "8.2 Modifiers: Bars and Dots"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.3 Modifiers: Arrows and Limits",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial83.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="8.3 Modifiers: Arrows and Limits"'
                        ).tooltip("8.3 Modifiers: Arrows and Limits")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.4 Probability",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial84.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="8.4 Probability"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("8.4 Probability")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.5 Calculus: Differentiation",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial85.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="8.5 Calculus: Differentiation"').tooltip(
                            "8.5 Calculus: Differentiation"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.6 Calculus: Integration",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial86.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="8.6 Calculus: Integration"').tooltip(
                            "8.6 Calculus: Integration"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.7 Vertical Bars",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_braille_trial87.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="8.7 Vertical Bars"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("8.7 Vertical Bars")
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