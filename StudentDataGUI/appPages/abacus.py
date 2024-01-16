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
    """Abacus Skills Progression"""

    @ui.page("/abacusskills")
    def abacusskills() -> None:
        with theme.frame("- TACTILE SKILLS -"):
            with ui.tabs() as tabs:
                ui.tab("DATA INPUT")
                ui.tab("DATA VISUALIZATION")
            with ui.tab_panels(tabs, value="DATA INPUT"):
                with ui.tab_panel("DATA INPUT"):
                    ui.label("ABACUS SKILLS").classes("text-h4 text-grey-8").style(
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
                    u_abacus_trial11 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial12 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial13 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial14 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial21 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial22 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial23 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial31 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial32 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial33 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial41 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial42 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial51 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial52 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial61 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial62 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial63 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial64 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial71 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial72 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial73 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial74 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial81 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_abacus_trial82 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )

                    def save(event):
                        """
                        Save abacus trial data for a student.

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
                        `u_today_date`, `u_abacus_trial11`, ..., `u_abacus_trial82`), `datenow`, `json`,
                        `Path`, and other variables related to the application.

                        The function extracts abacus trial data and student information from UI elements,
                        creates a dictionary with this data, and saves it as a JSON file in the student's
                        directory within the "StudentDataFiles" folder. The filename is constructed based
                        on the student's name and the current date.

                        The function also appends the filename to a "Filenames.txt" file for reference.

                        Examples
                        --------
                        >>> save(some_event)
                        >>> # Abacus trial data and student information saved successfully.
                        >>> # The data is stored in a JSON file named based on the student's name and date.

                        See Also
                        --------
                        Some related functions or classes that might be useful.

                        """
                        studentname = u_studentname.value
                        datestring = u_today_date.value
                        today_date = datetime.datetime.strptime(
                            datestring, "%Y-%m-%d"
                        ).strftime("%Y_%m_%d-%H%M%S_%p")
                        abacus_trial11 = int(u_abacus_trial11.value)
                        abacus_trial12 = int(u_abacus_trial12.value)
                        abacus_trial13 = int(u_abacus_trial13.value)
                        abacus_trial14 = int(u_abacus_trial14.value)
                        abacus_trial21 = int(u_abacus_trial21.value)
                        abacus_trial22 = int(u_abacus_trial22.value)
                        abacus_trial23 = int(u_abacus_trial23.value)
                        abacus_trial31 = int(u_abacus_trial31.value)
                        abacus_trial32 = int(u_abacus_trial32.value)
                        abacus_trial33 = int(u_abacus_trial33.value)
                        abacus_trial41 = int(u_abacus_trial41.value)
                        abacus_trial42 = int(u_abacus_trial42.value)
                        abacus_trial51 = int(u_abacus_trial51.value)
                        abacus_trial52 = int(u_abacus_trial52.value)
                        abacus_trial61 = int(u_abacus_trial61.value)
                        abacus_trial62 = int(u_abacus_trial62.value)
                        abacus_trial63 = int(u_abacus_trial63.value)
                        abacus_trial64 = int(u_abacus_trial64.value)
                        abacus_trial71 = int(u_abacus_trial71.value)
                        abacus_trial72 = int(u_abacus_trial72.value)
                        abacus_trial73 = int(u_abacus_trial73.value)
                        abacus_trial74 = int(u_abacus_trial74.value)
                        abacus_trial81 = int(u_abacus_trial81.value)
                        abacus_trial82 = int(u_abacus_trial82.value)
                        studentdatabasename = f"abacus{studentname.title()}{datenow}"
                        tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase",
                            "StudentDataFiles",
                            studentname,
                            studentdatabasename + ".json",
                        )
                        abacus_dictionary = {
                            "studentname": u_studentname.value,
                            "date": today_date,
                            "abacus_trial11": abacus_trial11,
                            "abacus_trial12": abacus_trial12,
                            "abacus_trial13": abacus_trial13,
                            "abacus_trial14": abacus_trial14,
                            "abacus_trial21": abacus_trial21,
                            "abacus_trial22": abacus_trial22,
                            "abacus_trial23": abacus_trial23,
                            "abacus_trial31": abacus_trial31,
                            "abacus_trial32": abacus_trial32,
                            "abacus_trial33": abacus_trial33,
                            "abacus_trial41": abacus_trial41,
                            "abacus_trial42": abacus_trial42,
                            "abacus_trial51": abacus_trial51,
                            "abacus_trial52": abacus_trial52,
                            "abacus_trial61": abacus_trial61,
                            "abacus_trial62": abacus_trial62,
                            "abacus_trial63": abacus_trial63,
                            "abacus_trial64": abacus_trial64,
                            "abacus_trial71": abacus_trial71,
                            "abacus_trial72": abacus_trial72,
                            "abacus_trial73": abacus_trial73,
                            "abacus_trial74": abacus_trial74,
                            "abacus_trial81": abacus_trial81,
                            "abacus_trial82": abacus_trial82,
                        }
                        with open(tmppath, "w", encoding="utf-8") as filename:
                            json.dump(abacus_dictionary, filename)
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
                            filename.write(f"{tmppath}" + "\n")

                        # noinspection SqlResolve
                        def data_entry():
                            """
                            Write abacus progress data to the database.

                            Connects to the SQLite database specified by `dataBasePath` and inserts a new row
                            into the 'ABACUSPROGRESS' table with the provided abacus progress data.

                            Parameters
                            ----------
                            None

                            Returns
                            -------
                            None

                            Notes
                            -----
                            This function assumes the existence of variables such as `dataBasePath`,
                            `studentname`, `today_date`, `abacus_trial11`, ..., `abacus_trial82`, `sqlite3`,
                            and `ui`.

                            The function establishes a connection to the database, creates a cursor, executes an
                            SQL INSERT command with the abacus progress data, commits the changes, and notifies
                            the user of successful data entry.

                            Examples
                            --------
                            >>> data_entry()
                            >>> # Abacus progress data successfully written to the database.
                            >>> # The user is notified of successful data entry.

                            See Also
                            --------
                            Some related functions or classes that might be useful.

                            """
                            conn = sqlite3.connect(dataBasePath)
                            c = conn.cursor()
                            c.execute(
                                """INSERT INTO ABACUSPROGRESS (
                                                                        STUDENTNAME,
                                                                        DATE,
                                                                        P1_1,
                                                                        P1_2,
                                                                        P1_3,
                                                                        P1_4,
                                                                        P2_1,
                                                                        P2_2,
                                                                        P2_3,
                                                                        P3_1,
                                                                        P3_2,
                                                                        P3_3,
                                                                        P4_1,
                                                                        P4_2,
                                                                        P5_1,
                                                                        P5_2,
                                                                        P6_1,
                                                                        P6_2,
                                                                        P6_3,
                                                                        P6_4,
                                                                        P7_1,
                                                                        P7_2,
                                                                        P7_3,
                                                                        P7_4,
                                                                        P8_1,
                                                                        P8_2
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
                                                                        ?)""",
                                (
                                    studentname,
                                    today_date,
                                    abacus_trial11,
                                    abacus_trial12,
                                    abacus_trial13,
                                    abacus_trial14,
                                    abacus_trial21,
                                    abacus_trial22,
                                    abacus_trial23,
                                    abacus_trial31,
                                    abacus_trial32,
                                    abacus_trial33,
                                    abacus_trial41,
                                    abacus_trial42,
                                    abacus_trial51,
                                    abacus_trial52,
                                    abacus_trial61,
                                    abacus_trial62,
                                    abacus_trial63,
                                    abacus_trial64,
                                    abacus_trial71,
                                    abacus_trial72,
                                    abacus_trial73,
                                    abacus_trial74,
                                    abacus_trial81,
                                    abacus_trial82,
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
                    Generate and display Abacus Skills Progression graphs for a specific student.

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
                    `dataBasePath`, `USER_DIR`, `sqlite3`, `pd`, `np`, `go`, `make_subplots`,
                    `date_fmt`, `ui`, and other global variables.

                    The function connects to the SQLite database, retrieves the abacus progress data
                    for the specified student, preprocesses the data, adds noise, performs descriptive
                    statistics, calculates growth factors, creates subplots for each abacus phase,
                    and generates an HTML file with the interactive graph. The generated HTML file is
                    opened in a browser window, and the user is notified of successful graph
                    generation.

                    Examples
                    --------
                    >>> graph(some_event)
                    >>> # Abacus Skills Progression graphs for the specified student are generated.
                    >>> # The graphs are displayed in a browser window, and the user is notified.

                    See Also
                    --------
                    Some related functions or classes that might be useful.

                    """
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
                    descriptiveStats = df.describe()
                    print("Descriptive Statistics")
                    print(descriptiveStats)
                    growthCalculation = df.diff(periods=3)
                    growth = growthCalculation[-1:]
                    print("Growth Factor (Now vs 3 Measurements ago)")
                    print(growth)
                    fig = make_subplots(
                        rows=4,
                        cols=2,
                        subplot_titles=(
                            "Phase 1: Foundation",
                            "Phase 2: Addition",
                            "Phase 3: Subtraction",
                            "Phase 4: Multiplication",
                            "Phase 5: Division",
                            "Phase 6: Decimals",
                            "Phase 7: Fractions",
                            "Phase 8: Special Functions",
                        ),
                        print_grid=True,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P1_1"],
                            mode="lines+markers",
                            name="Setting Numbers",
                            legendgroup="Phase 1",
                            legendgrouptitle_text="Phase 1",
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
                            name="Clearing Beads",
                            legendgroup="Phase " "1",
                            legendgrouptitle_text="Phase 1",
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
                            name="Place Value",
                            legendgroup="Phase " "1",
                            legendgrouptitle_text="Phase 1",
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
                            name="Vocabulary",
                            legendgroup="Phase " "1",
                            legendgrouptitle_text="Phase 1",
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
                            name="Setting Numbers",
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
                            name="Clearing Beads",
                            legendgroup="Phase " "2",
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
                            name="Place Value",
                            legendgroup="Phase " "2",
                            legendgrouptitle_text="Phase 2",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=1,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_1"],
                            mode="lines+markers",
                            name="Setting Numbers",
                            legendgroup="Phase 3",
                            legendgrouptitle_text="Phase 3",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_2"],
                            mode="lines+markers",
                            name="Clearing Beads",
                            legendgroup="Phase " "3",
                            legendgrouptitle_text="Phase 3",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P3_3"],
                            mode="lines+markers",
                            name="Place Value",
                            legendgroup="Phase " "3",
                            legendgrouptitle_text="Phase 3",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_1"],
                            mode="lines+markers",
                            name="Setting Numbers",
                            legendgroup="Phase 4",
                            legendgrouptitle_text="Phase 4",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P4_2"],
                            mode="lines+markers",
                            name="Clearing Beads",
                            legendgroup="Phase " "4",
                            legendgrouptitle_text="Phase 4",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=2,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_1"],
                            mode="lines+markers",
                            name="Place Value",
                            legendgroup="Phase " "5",
                            legendgrouptitle_text="Phase 5",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P5_2"],
                            mode="lines+markers",
                            name="Vocabulary",
                            legendgroup="Phase " "5",
                            legendgrouptitle_text="Phase 5",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_1"],
                            mode="lines+markers",
                            name="Setting Numbers",
                            legendgroup="Phase 6",
                            legendgrouptitle_text="Phase 6",
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
                            name="Clearing Beads",
                            legendgroup="Phase " "6",
                            legendgrouptitle_text="Phase 6",
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
                            name="Place Value",
                            legendgroup="Phase " "6",
                            legendgrouptitle_text="Phase 6",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=3,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P6_4"],
                            mode="lines+markers",
                            name="Vocabulary",
                            legendgroup="Phase " "6",
                            legendgrouptitle_text="Phase 6",
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
                            name="Setting Numbers",
                            legendgroup="Phase 7",
                            legendgrouptitle_text="Phase 7",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_2"],
                            mode="lines+markers",
                            name="Clearing Beads",
                            legendgroup="Phase " "7",
                            legendgrouptitle_text="Phase 7",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_3"],
                            mode="lines+markers",
                            name="Place Value",
                            legendgroup="Phase " "7",
                            legendgrouptitle_text="Phase 7",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P7_4"],
                            mode="lines+markers",
                            name="Vocabulary",
                            legendgroup="Phase " "7",
                            legendgrouptitle_text="Phase 7",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=1,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_1"],
                            mode="lines+markers",
                            name="Setting Numbers",
                            legendgroup="Phase 8",
                            legendgrouptitle_text="Phase 8",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
                        col=2,
                    )
                    fig.add_trace(
                        go.Scatter(
                            x=df_noisy.index,
                            y=df_noisy["P8_2"],
                            mode="lines+markers",
                            name="Clearing Beads",
                            legendgroup="Phase " "8",
                            legendgrouptitle_text="Phase 8",
                            hovertemplate="  %{y:.1f} ",
                        ),
                        row=4,
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
                        col=1,
                    )
                    fig.add_hrect(
                        y0=0.5,
                        y1=1.5,
                        line_width=0,
                        fillcolor="orange",
                        opacity=0.2,
                        row=4,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=1.5,
                        y1=2.5,
                        line_width=0,
                        fillcolor="yellow",
                        opacity=0.2,
                        row=4,
                        col=1,
                    )
                    fig.add_hrect(
                        y0=2.5,
                        y1=3.5,
                        line_width=0,
                        fillcolor="green",
                        opacity=0.2,
                        row=4,
                        col=1,
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
                    # Define the common properties for y-axes
                    y_axes_properties = {
                        "range": [-0.5, 3.5],
                        "fixedrange": True,
                        "ticktext": ["Unable", "Prompted", "Hesitated", "Independent"],
                        "tickvals": [0.1, 1, 2, 3],
                    }

                    # Update y-axes for each row and column
                    for row in range(1, 4):
                        for col in range(1, 3):
                            fig.update_yaxes(**y_axes_properties, row=row, col=col)

                    fig.update_layout(
                        template="simple_white",
                        title_text=f"{studentname}: Abacus Skills Progression",
                        hovermode="x unified",
                        hoverlabel=dict(namelength=-1),
                    )
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "AbacusSkillsProgression.html",
                    )
                    fig.write_html(tmppath, auto_open=True)
                    # fig.show( )
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
                            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    ui.input().props(
                        'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"'
                    ).classes("sr-only").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 1: Setting and Clearing Numbers").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    ui.input().props(
                        'aria-label="PHASE 1: Setting and Clearing Numbers"'
                    ).classes("sr-only").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.1 Setting Numbers",
                            value="",
                            on_change=lambda e: u_abacus_trial11.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="1.1 Setting Numbers"').tooltip(
                            "1.1 Setting Numbers"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.2 Clearing Numbers",
                            value="",
                            on_change=lambda e: u_abacus_trial12.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="1.2 Clearing Numbers"').tooltip(
                            "1.2 Clearing Numbers"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.3 Place Value",
                            value="",
                            on_change=lambda e: u_abacus_trial13.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="1.3 Place Value"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("1.3 Place Value")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="1.4 Vocabulary",
                            value="",
                            on_change=lambda e: u_abacus_trial14.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="1.4 Vocabulary"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("1.4 Vocabulary")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 2: Addition").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    ui.input().props('aria-label="PHASE 2: Addition"').classes(
                        "sr-only"
                    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.1 Addition of Single Digit Numbers",
                            value="",
                            on_change=lambda e: u_abacus_trial21.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="2.1 Addition of Single Digit Numbers"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.2 Addition of Multiple Digit Numbers – Direct",
                            value="",
                            on_change=lambda e: u_abacus_trial22.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="2.2 Addition of Multiple Digit Numbers – Direct"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="2.3 Addition of Multiple Digit Numbers – Indirect",
                            value="",
                            on_change=lambda e: u_abacus_trial23.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="2.3 Addition of Multiple Digit Numbers – Indirect"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 3: Subtraction").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props('aria-label="PHASE 3: Subtraction"').classes(
                            "sr-only"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.1 Subtraction",
                            value="",
                            on_change=lambda e: u_abacus_trial31.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="3.1 Subtraction"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.2 Subtraction of Multiple Digit Numbers – Direct",
                            value="",
                            on_change=lambda e: u_abacus_trial32.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="3.2 Subtraction of Multiple Digit Numbers – Direct"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="3.3 Subtraction of Multiple Digit Numbers – Indirect",
                            value="",
                            on_change=lambda e: u_abacus_trial33.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="3.3 Subtraction of Multiple Digit Numbers – Indirect"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 4: Multiplication").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 4: Multiplication"'
                        ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.1 Multiplication – 2+ Digit Multiplicand 1-Digit Multiplier",
                            value="",
                            on_change=lambda e: u_abacus_trial41.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="4.1 Multiplication – 2+ Digit Multiplicand 1-Digit Multiplier"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="4.2 Multiplication – 2+ Digit Multiplicand AND Multiplier",
                            value="",
                            on_change=lambda e: u_abacus_trial42.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="4.2 Multiplication – 2+ Digit Multiplicand AND Multiplier"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 5: Division").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props('aria-label="PHASE 5: Division"').classes(
                            "sr-only"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.1 Division – 2+ Digit Dividend 1-Digit Divisor",
                            value="",
                            on_change=lambda e: u_abacus_trial51.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="5.1 Division – 2+ Digit Dividend 1-Digit Divisor"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="5.2 Division – 2+ Digit Dividend AND 1 Digit Divisor",
                            value="",
                            on_change=lambda e: u_abacus_trial52.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="5.2 Division – 2+ Digit Dividend AND 1 Digit Divisor"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 6: Decimals").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props('aria-label="PHASE 6: Decimals"').classes(
                            "sr-only"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.1 Addition of Decimals",
                            value="",
                            on_change=lambda e: u_abacus_trial61.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="6.1 Addition of Decimals"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.2 Subtraction of Decimals",
                            value="",
                            on_change=lambda e: u_abacus_trial62.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="6.2 Subtraction of Decimals"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.3 Multiplication of Decimals",
                            value="",
                            on_change=lambda e: u_abacus_trial63.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="6.3 Multiplication of Decimals"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="6.4 Division of Decimals",
                            value="",
                            on_change=lambda e: u_abacus_trial64.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="6.4 Division of Decimals"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 7: Fractions").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props('aria-label="PHASE 7: Fractions"').classes(
                            "sr-only"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.1 Addition of Fractions",
                            value="",
                            on_change=lambda e: u_abacus_trial71.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="7.1 Addition of Fractions"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.2 Subtraction of Fractions",
                            value="",
                            on_change=lambda e: u_abacus_trial72.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="7.2 Subtraction of Fractions"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.3 Multiplication of Fractions",
                            value="",
                            on_change=lambda e: u_abacus_trial73.set_value(e.value),
                        ).classes("w-[600px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="7.3 Multiplication of Fractions"')
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="7.4 Division of Fractions",
                            value="",
                            on_change=lambda e: u_abacus_trial74.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="7.4 Division of Fractions"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("PHASE 8: Roots and Percents").classes(
                            "justify-center items-center text-lg"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.input().props(
                            'aria-label="PHASE 8: Roots and Percents"'
                        ).classes("sr-only")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.1 Percent",
                            value="",
                            on_change=lambda e: u_abacus_trial81.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="8.1 Percent"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="8.2 Square Root",
                            value="",
                            on_change=lambda e: u_abacus_trial82.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="8.2 Square Root"'
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
                    with ui.dialog() as dialog, ui.card():
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
                        abacustable = ui.table(
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
                        abacustable.add_slot('body-cell', '''
                                <q-td key="Days_Since_Last" :props="props">
                                <q-badge :color="props.value  <= 0 ? 'red' : props.value <= 1 ? 'orange' : props.value <= 2 ? 'yellow' :  'green'" text-color="black" outline>
                                    {{ props.value }}
                                </q-badge>
                                </q-td>
                                ''')
                        abacustable.visible = True
                        ui.button('Close', on_click=dialog.close)

                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.button('Show Data', on_click=dialog.open)
