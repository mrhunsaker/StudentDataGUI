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
    # SCREENREADER SKILLS
    ##########################################################################
    @ui.page("/screenreaderskills")
    def screenreaderskills() -> None:
        with theme.frame("- TECHNOLOGY SKILLS -"):
            with ui.tabs() as tabs:
                ui.tab("DATA INPUT")
                ui.tab("DATA VISUALIZATION")
            with ui.tab_panels(tabs, value="DATA INPUT"):
                with ui.tab_panel("DATA INPUT"):
                    ui.label("SCREENREADER SKILLS").classes(
                        "text-h4 text-grey-8"
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    u_studentname = (
                        ui.select(options=students, value="DonaldChamberlain")
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    # ASSIGN VARIABLES
                    u_today_date = (
                        ui.date()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial11 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial12 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial13 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial14 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial15 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial16 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial21 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial22 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial23 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial24 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial31 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial32 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial33 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial34 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial35 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial36 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial37 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial38 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial39 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial310 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial311 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial41 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial42 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial43 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial44 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial45 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial46 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_screenreader_trial47 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )

                    # SAVE FUNCTION (USED BELOW)
                    def save(event):
                        """
                        :param event:
                        :type event:
                        """
                        studentname = u_studentname.value
                        today_date = u_today_date.value
                        screenreader_trial11 = int(u_screenreader_trial11.value)
                        screenreader_trial12 = int(u_screenreader_trial12.value)
                        screenreader_trial13 = int(u_screenreader_trial13.value)
                        screenreader_trial14 = int(u_screenreader_trial14.value)
                        screenreader_trial15 = int(u_screenreader_trial15.value)
                        screenreader_trial16 = int(u_screenreader_trial16.value)
                        screenreader_trial21 = int(u_screenreader_trial21.value)
                        screenreader_trial22 = int(u_screenreader_trial22.value)
                        screenreader_trial23 = int(u_screenreader_trial23.value)
                        screenreader_trial24 = int(u_screenreader_trial24.value)
                        screenreader_trial31 = int(u_screenreader_trial31.value)
                        screenreader_trial32 = int(u_screenreader_trial32.value)
                        screenreader_trial33 = int(u_screenreader_trial33.value)
                        screenreader_trial34 = int(u_screenreader_trial34.value)
                        screenreader_trial35 = int(u_screenreader_trial35.value)
                        screenreader_trial36 = int(u_screenreader_trial36.value)
                        screenreader_trial37 = int(u_screenreader_trial37.value)
                        screenreader_trial38 = int(u_screenreader_trial38.value)
                        screenreader_trial39 = int(u_screenreader_trial39.value)
                        screenreader_trial310 = int(u_screenreader_trial310.value)
                        screenreader_trial311 = int(u_screenreader_trial311.value)
                        screenreader_trial41 = int(u_screenreader_trial41.value)
                        screenreader_trial42 = int(u_screenreader_trial42.value)
                        screenreader_trial43 = int(u_screenreader_trial43.value)
                        screenreader_trial44 = int(u_screenreader_trial44.value)
                        screenreader_trial45 = int(u_screenreader_trial45.value)
                        screenreader_trial46 = int(u_screenreader_trial46.value)
                        screenreader_trial47 = int(u_screenreader_trial47.value)
                        studentdatabasename = (
                            f"screenreader{studentname.title()}{datenow}"
                        )
                        tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase",
                            "StudentDataFiles",
                            studentname,
                            studentdatabasename + ".json",
                        )
                        screenreader_dictionary = {
                            "studentname": studentname,
                            "date": today_date,
                            "screenreader_trial11": screenreader_trial11,
                            "screenreader_trial12": screenreader_trial12,
                            "screenreader_trial13": screenreader_trial13,
                            "screenreader_trial14": screenreader_trial14,
                            "screenreader_trial15": screenreader_trial15,
                            "screenreader_trial16": screenreader_trial16,
                            "screenreader_trial21": screenreader_trial21,
                            "screenreader_trial22": screenreader_trial22,
                            "screenreader_trial23": screenreader_trial23,
                            "screenreader_trial24": screenreader_trial24,
                            "screenreader_trial31": screenreader_trial31,
                            "screenreader_trial32": screenreader_trial32,
                            "screenreader_trial33": screenreader_trial33,
                            "screenreader_trial34": screenreader_trial34,
                            "screenreader_trial35": screenreader_trial35,
                            "screenreader_trial36": screenreader_trial36,
                            "screenreader_trial37": screenreader_trial37,
                            "screenreader_trial38": screenreader_trial38,
                            "screenreader_trial39": screenreader_trial39,
                            "screenreader_trial310": screenreader_trial310,
                            "screenreader_trial311": screenreader_trial311,
                            "screenreader_trial41": screenreader_trial41,
                            "screenreader_trial42": screenreader_trial42,
                            "screenreader_trial43": screenreader_trial43,
                            "screenreader_trial44": screenreader_trial44,
                            "screenreader_trial45": screenreader_trial45,
                            "screenreader_trial46": screenreader_trial46,
                            "screenreader_trial47": screenreader_trial47,
                        }
                        with open(tmppath, "w", encoding="utf8") as filename:
                            json.dump(screenreader_dictionary, filename)

                            tmppath = Path(USER_DIR).joinpath(
                                "StudentDatabase", "StudentDataFiles", "Filenames.txt"
                            )
                        with open(tmppath, "a", encoding="utf8") as filename:
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
                                """INSERT INTO SCREENREADERPROGRESS (
                                                                                STUDENTNAME,
                                                                                DATE,
                                                                                P1_1,
                                                                                P1_2,
                                                                                P1_3,
                                                                                P1_4,
                                                                                P1_5,
                                                                                P1_6,
                                                                                P2_1,
                                                                                P2_2,
                                                                                P2_3,
                                                                                P2_4,
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
                                                                                P4_1,
                                                                                P4_2,
                                                                                P4_3,
                                                                                P4_4,
                                                                                P4_5,
                                                                                P4_6,
                                                                                P4_7
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
                                                                                    ?
                                                                                    )""",
                                (
                                    studentname,
                                    today_date,
                                    screenreader_trial11,
                                    screenreader_trial12,
                                    screenreader_trial13,
                                    screenreader_trial14,
                                    screenreader_trial15,
                                    screenreader_trial16,
                                    screenreader_trial21,
                                    screenreader_trial22,
                                    screenreader_trial23,
                                    screenreader_trial24,
                                    screenreader_trial31,
                                    screenreader_trial32,
                                    screenreader_trial33,
                                    screenreader_trial34,
                                    screenreader_trial35,
                                    screenreader_trial36,
                                    screenreader_trial37,
                                    screenreader_trial38,
                                    screenreader_trial39,
                                    screenreader_trial310,
                                    screenreader_trial311,
                                    screenreader_trial41,
                                    screenreader_trial42,
                                    screenreader_trial43,
                                    screenreader_trial44,
                                    screenreader_trial45,
                                    screenreader_trial46,
                                    screenreader_trial47,
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
                    >>> # Screenreader Skills Progression graphs for the specified student are generated.
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
                    df_sql = pd.read_sql_query(
                        "SELECT * FROM SCREENREADERPROGRESS", conn
                    )
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
                    print("ScreenReader Skills Progression")
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
                        rows=5,
                        cols=2,
                        specs=[
                            [{}, {"rowspan": 2}],
                            [{}, None],
                            [{"rowspan": 2}, {}],
                            [None, {}],
                            [{}, {}],
                        ],
                        subplot_titles=(
                            "Phase 1a: Reading",
                            "Phase 2: Writing",
                            "Phase 1b: Reading",
                            "Phase 3a: Internet",
                            "Phase 3b: Internet",
                            "Phase 3c: Internet",
                            "Phase 4a: File Management",
                            "Phase 4b: File Management",
                        ),
                        print_grid=True,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_1"],
                            mode="lines+markers",
                            name="Turn " "ON/OFF",
                            legendgroup="Phase 1a",
                            legendgrouptitle_text="Phase 1a",
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
                            name="Use " "Modifier Keys",
                            legendgroup="Phase 1a",
                            legendgrouptitle_text="Phase 1a",
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
                            name="Use " "Reading Commands",
                            legendgroup="Phase 1a",
                            legendgrouptitle_text="Phase 1a",
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
                            name="ID " "Titles",
                            legendgroup="Phase 1b",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_5"],
                            mode="lines+markers",
                            name="Access Documents",
                            legendgroup="Phase 1b",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_6"],
                            mode="lines+markers",
                            name="Switch Program Focus",
                            legendgroup="Phase 1b",
                            legendgrouptitle_text=" ",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_1"],
                            mode="lines+markers",
                            name="Type " "with" " all " "keys",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_2"],
                            mode="lines+markers",
                            name="Change Screen Reader Settings",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_3"],
                            mode="lines+markers",
                            name="Write documents",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P2_4"],
                            mode="lines+markers",
                            name="Copy/Paste Text",
                            legendgroup="Phase 2",
                            legendgrouptitle_text="Phase 2",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_4"],
                            mode="lines+markers",
                            name="TAB " "Navigation",
                            legendgroup="Phase 3a",
                            legendgrouptitle_text="Phase 3a",
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
                            name="Quick Key Navigation",
                            legendgroup="Phase 3a",
                            legendgrouptitle_text="Phase 3a",
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
                            name="Elements List Navigation",
                            legendgroup="Phase 3a",
                            legendgrouptitle_text="Phase 3a",
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
                            name="Justify Navigation Method",
                            legendgroup="Phase 3a",
                            legendgrouptitle_text="Phase 3a",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_1"],
                            mode="lines+markers",
                            name="Define HTML Elements",
                            legendgroup="Phase 3b",
                            legendgrouptitle_text="Phase 3b",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_2"],
                            mode="lines+markers",
                            name="ID " "HTML" " Elements",
                            legendgroup="Phase 3b",
                            legendgrouptitle_text="Phase 3b",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_3"],
                            mode="lines+markers",
                            name="Navigate to Address Bar",
                            legendgroup="Phase 3b",
                            legendgrouptitle_text="Phase 3b",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_8"],
                            mode="lines+markers",
                            name="ALT-TAB Focus",
                            legendgroup="Phase " "3b",
                            legendgrouptitle_text="Phase 3b",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_9"],
                            mode="lines+markers",
                            name="Toggle Screen Reader Mode",
                            legendgroup="Phase 3c",
                            legendgrouptitle_text="Phase 3c",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_10"],
                            mode="lines+markers",
                            name="Navigate a Table",
                            legendgroup="Phase 3c",
                            legendgrouptitle_text="Phase 3c",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_11"],
                            mode="lines+markers",
                            name="Navigation Sequence",
                            legendgroup="Phase 3c",
                            legendgrouptitle_text="Phase 3c",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_1"],
                            mode="lines+markers",
                            name="Save " "and " "Open " "Files",
                            legendgroup="Phase 4a",
                            legendgrouptitle_text="Phase 4a",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_2"],
                            mode="lines+markers",
                            name="Create Folders",
                            legendgroup="Phase " "4a",
                            legendgrouptitle_text="Phase 4a",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_3"],
                            mode="lines+markers",
                            name="Navigate Cloud Storage",
                            legendgroup="Phase 4a",
                            legendgrouptitle_text="Phase 4a",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_4"],
                            mode="lines+markers",
                            name="Download from Internet",
                            legendgroup="Phase 4a",
                            legendgrouptitle_text="Phase 4a",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=5,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_5"],
                            mode="lines+markers",
                            name="UNZIP Folders",
                            legendgroup="Phase " "4b",
                            legendgrouptitle_text="Phase 4b",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_6"],
                            mode="lines+markers",
                            name="Use " "Virtual Cursor",
                            legendgroup="Phase 4b",
                            legendgrouptitle_text="Phase 4b",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_7"],
                            mode="lines+markers",
                            name="Use " "Built-In OCR",
                            legendgroup="Phase 4b",
                            legendgrouptitle_text="Phase 4b",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=5,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="#b3c7f7",
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
                        fillcolor="#b3c7f7",
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
                        fillcolor="#b3c7f7",
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
                        fillcolor="#b3c7f7",
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
                        fillcolor="#b3c7f7",
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
                        fillcolor="#b3c7f7",
                        opacity=0.2,
                        row=4,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=4,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=4,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=4,
                        col=2,
                    )
                    fig.add_hrect(
                        y0=-0.5,
                        y1=0.5,
                        line_width=0,
                        fillcolor="#b3c7f7",
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
                        fillcolor="#b3c7f7",
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
                        row=4,
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
                    fig.update_layout(
                        template="simple_white",
                        title_text=f"{studentname}: Screen Reader Skills Progression",
                        hovermode="x unified",
                        hoverlabel=dict(namelength=-1),
                    )
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "ScreenReaderSkillsProgression.html",
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
                            "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"
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
                        ui.label("PHASE 1: READING").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props('aria-label="PHASE 1: READING"').classes(
                            "sr-only"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.1 Turn on and off the screen reader",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_screenreader_trial11.set_value(
                                e.value
                            ),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="1.1 Turn on and off the screen reader"')
                    ui.number(
                        label="1.2 Utilize modifier keys such as ctrl alt and shift",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial12.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="1.2 Utilize modifier keys such as ctrl alt and shift"'
                    )
                    ui.number(
                        label="1.3 Read text using a variety of reading commands",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial13.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="1.3 Read text using a variety of reading commands"'
                    )
                    ui.number(
                        label="1.4 Identify the titles and section titles of documents with Headings",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial14.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="1.4 Identify the titles and section titles of documents with Headings"'
                    )
                    ui.number(
                        label="1.5 Access documents open and close programs navigate to the  desktop",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial15.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="1.5 Access documents open and close programs  navigate to the  desktop"'
                    )
                    ui.number(
                        label="1.6 Switch Program Focus",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial16.set_value(e.value),
                    ).classes("w-[600px]").props(
                        'aria-label="1.6 Switch Program Focus"'
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 2: WRITING").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props('aria-label="PHASE 2: WRITING"').classes(
                            "sr-only"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.1 Type with all alphanumeric keys on the keyboard",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_screenreader_trial21.set_value(
                                e.value
                            ),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="2.1 Type with all alphanumeric keys on the keyboard."'
                        )
                    ui.number(
                        label="2.2 Navigate to and change screen reader settings",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial22.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="2.2 Navigate to and change screen reader settings"'
                    )
                    ui.number(
                        label="2.3 Write and edit documents using a basic understanding of cursor placement",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial23.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="2.3 Write and edit documents using a basic understanding of cursor placement"'
                    )
                    ui.number(
                        label="2.4. Select copy and paste text",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial24.set_value(e.value),
                    ).classes("w-[600px]").props(
                        'aria-label="2.4. Select copy and paste text"'
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 3: USING THE INTERNET").classes(
                            "justify-center items-center text-lg"
                        )
                    ui.input().props(
                        'aria-label="PHASE 3: USING THE INTERNET"'
                    ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.1 Define common element types on the internet such as Headings or Buttons",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_screenreader_trial31.set_value(
                                e.value
                            ),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="3.1 Define common element types on the internet such as Headings or Buttons"'
                        )
                    ui.number(
                        label="3.2 identify each element by type",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial32.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props('aria-label="3.2 identify each element by type."')
                    ui.number(
                        label="3.3 navigate to the address bar",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial33.set_value(e.value),
                    ).classes("w-[600px]").props(
                        'aria-label="3.3 navigate to the address bar"'
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    ui.number(
                        label="3.4 Use the “Tab” key to navigate to the next clickable object",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial34.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="3.4 Use the “Tab” key to navigate to the next clickable object"'
                    )
                    ui.number(
                        label="3.5 Navigate by “Quick Keys” (h for heading b for button and u for link)",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial35.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aira-label="3.5 Navigate by “Quick Keys” (h for heading b for button and u for link)"'
                    )
                    ui.number(
                        label="3.6 Use Elements Lists on a website to navigate by element type",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial36.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="3.6 Use Elements Lists on a website to navigate by element type"'
                    )
                    ui.number(
                        label="3.7 Justify why he/she/they selected a particular method xfor the situation",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial37.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="3.7 Justify why he/she/they selected a particular method for the situation"'
                    )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.8 Switch tab focus",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_screenreader_trial38.set_value(
                                e.value
                            ),
                        ).classes("w-[600px]").props(
                            'aria-label="3.8 Switch tab focus"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    ui.number(
                        label="3.9 Switch between screen reader modes",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial39.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props('aria-label="3.9 Switch between screen reader modes"')
                    ui.number(
                        label="3.10 Navigate a table",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial310.set_value(e.value),
                    ).classes("w-[600px]").props(
                        'aria-label="3.10 Navigate a table"'
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    ui.number(
                        label="3.11 Develop a navigation sequence to access an unfamiliar website",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial311.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="3.11 Develop a navigation sequence to access an unfamiliar website"'
                    )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 4: NAVIGATING AND FILE MANAGEMENT").classes(
                            "justify-center items-center text-lg"
                        )
                    ui.input().props(
                        'aria-label="PHASE 4: NAVIGATING AND FILE MANAGEMENT"'
                    ).classes("sr-only").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.1 Be able to save and open files using File Explorer",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_screenreader_trial41.set_value(
                                e.value
                            ),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="4.1 Be able to save and open files using File Explorer."'
                        )
                    ui.number(
                        label="4.2 Create folders and move files in File Explorer",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial42.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="4.2 Create folders and move files in File Explorer"'
                    )
                    ui.number(
                        label="4.3 Navigate a cloud-based file management system (eg: Google Drive)",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial43.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="4.3 Navigate a cloud-based file management system (eg: Google Drive)"'
                    )
                    ui.number(
                        label="4.4 Download and save material from the internet",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial44.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="4.4 Download and save material from the internet"'
                    )
                    ui.number(
                        label="4.5 Extract zipped folders",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial45.set_value(e.value),
                    ).classes("w-[600px]").props(
                        'aria-label="4.5 Extract zipped folders"'
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    ui.number(
                        label="4.6 Utilize the virtual cursor and mouse keys",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial46.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="4.6 Utilize the virtual cursor and mouse keys"'
                    )
                    ui.number(
                        label="4.7 To use OCR features to read inaccessible material",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_screenreader_trial47.set_value(e.value),
                    ).classes("w-[600px]").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).props(
                        'aria-label="4.7 To use OCR features to read inaccessible material"'
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
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                        "text-white"
                    )
            with ui.tab_panels(tabs, value="DATA VISUALIZATION"):
                with ui.tab_panel("DATA VISUALIZATION"):
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

                    with ui.row().classes("w-screen no-wrap py-4").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        def show_table():
                            studentname = u_studentname.value
                            dataBasePath = Path(USER_DIR).joinpath(
                                "StudentDatabase", "students.db"
                            )
                            conn = sqlite3.connect(dataBasePath)
                            df_sql = pd.read_sql_query("SELECT * FROM ABACUSPROGRESS", conn)
                            df_student = df_sql[df_sql.STUDENTNAME == studentname]
                            print(df_student)
                            conn.close()
                            df = df_student.drop(columns=["ID", "STUDENTNAME"])
                            print(df)
                            df = df.rename(columns={"DATE": "date"})
                            df["date"] = df["date"].astype("string")
                            df["date"] = pd.to_datetime(df["date"], format=date_fmt)
                            df = df.set_index("date")
                            print("Abacus Skills Progression")
                            print(df)
                            df = df.sort_values(by="date")
                            mu, sigma = 0, 0.1
                            noise = np.random.normal(
                                mu, sigma, [len(df.index), len(df.columns)]
                            )
                            df_noisy = df + noise
                            screenreadertable = ui.table(
                                columns=[
                                    {"name": col,
                                     "label": col,
                                     "field": col,
                                     "headerClasses": "border-b border-secondary",
                                     "align": 'left'}
                                    for col in df.columns
                                ],
                                rows=df.to_dict("records"), pagination={'rowsPerPage': 10}
                            ).style("font-family: JetBrainsMono; background-color: #f5f5f5").classes('my-table')
                            screenreadertable.add_slot('body-cell', '''
                                    <q-td key="Days_Since_Last" :props="props">
                                    <q-badge :color="props.value  <= 0 ? 'red' : props.value <= 1 ? 'orange' : props.value <= 2 ? 'yellow' :  'green'" text-color="black" outline>
                                        {{ props.value }}
                                    </q-badge>
                                    </q-td>
                                    ''')
                            screenreadertable.visible = True
                        ui.button('Show Data', on_click=show_table)
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        screenreadertable = ui.table(columns=[], rows=[])
                        screenreadertable.visible = False


        create_ui()
