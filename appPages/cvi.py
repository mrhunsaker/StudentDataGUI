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
from nicegui import app, ui
from plotly.subplots import make_subplots

from appHelpers.helpers import dataBasePath, date_fmt, datenow, USER_DIR
from appHelpers.roster import students
from appTheming import theme


def create() -> None:
    """
    CVI Progress Page Creation
    """

    @ui.page("/cviprogress")
    def cviprogress():
        with theme.frame("- CORTICAL/NEUROLOGICAL VISION IMPAIRMENT-"):
            ui.label("CVI PROGRESSION").classes("text-h4 text-grey-8").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
            u_studentname = (
                ui.select(options=students, value="DonaldChamberlain")
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            # ASSIGN VARIABLES
            u_today_date = (
                ui.date()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial11 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial12 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial13 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial14 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial21 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial22 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial23 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial31 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial32 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            )
            u_cvi_trial33 = (
                ui.number()
                .classes("hidden")
                .style('font-style:normal, font-family: "Atkinson Hyperlegible"')
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
                cvi_trial11 = int(u_cvi_trial11.value)
                cvi_trial12 = int(u_cvi_trial12.value)
                cvi_trial13 = int(u_cvi_trial13.value)
                cvi_trial14 = int(u_cvi_trial14.value)
                cvi_trial21 = int(u_cvi_trial21.value)
                cvi_trial22 = int(u_cvi_trial22.value)
                cvi_trial23 = int(u_cvi_trial23.value)
                cvi_trial31 = int(u_cvi_trial31.value)
                cvi_trial32 = int(u_cvi_trial32.value)
                cvi_trial33 = int(u_cvi_trial33.value)

                studentdatabasename = f"cvi{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    studentdatabasename + ".json",
                )
                cvi_dictionary = {
                    "studentname": studentname,
                    "date": today_date,
                    "cvi_trial11": cvi_trial11,
                    "cvi_trial12": cvi_trial12,
                    "cvi_trial13": cvi_trial13,
                    "cvi_trial14": cvi_trial14,
                    "cvi_trial21": cvi_trial21,
                    "cvi_trial22": cvi_trial22,
                    "cvi_trial23": cvi_trial23,
                    "cvi_trial31": cvi_trial31,
                    "cvi_trial32": cvi_trial32,
                    "cvi_trial33": cvi_trial33,
                }
                with open(tmppath, "w", encoding="utf-8") as filename:
                    json.dump(cvi_dictionary, filename)
                filename.close()

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
                        """INSERT INTO CVIPROGRESS (
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
                                                                            P2_4
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
                                                                                ?
                                                                                )""",
                        (
                            studentname,
                            today_date,
                            cvi_trial11,
                            cvi_trial12,
                            cvi_trial13,
                            cvi_trial14,
                            cvi_trial21,
                            cvi_trial22,
                            cvi_trial23,
                            cvi_trial31,
                            cvi_trial32,
                            cvi_trial33,
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
            >>> # CVI Progression graphs for the specified student are generated.
            >>> # The graphs are displayed in a browser window, and the user is notified.

            See Also
            --------
            Some related functions or classes that might be useful.

            """
            dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")
            studentname = u_studentname.value
            conn = sqlite3.connect(dataBasePath)
            df_sql = pd.read_sql_query("SELECT * FROM CVIPROGRESS", conn)
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
            print("CVI Progression")
            print(df)
            df = df.sort_values(by="date")
            mu, sigma = 0, 0.1
            noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
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
                subplot_titles=(
                    "Color Preference",
                    "Need for Movement",
                    "Latency",
                    "Field Preference",
                    "Visual Complexity",
                    "Nonpurposeful Gaze",
                    "Distance Viewing",
                    "Atypical Reflexes",
                    "Visual Novelty",
                    "Visual Reach",
                ),
                print_grid=True,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_1"],
                    mode="lines+markers",
                    name="Color Preference",
                    legendgroup="",
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
                    name="Need " "for " "Movement",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_3"],
                    mode="lines+markers",
                    name="Latency",
                    legendgroup="",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_4"],
                    mode="lines+markers",
                    name="Field Prefence",
                    legendgroup="",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_5"],
                    mode="lines+markers",
                    name="Visual Complexity",
                    legendgroup="",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_6"],
                    mode="lines+markers",
                    name="Nonpurposeful Gaze",
                    legendgroup="",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_1"],
                    mode="lines+markers",
                    name="Distance Viewing",
                    legendgroup="",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_2"],
                    mode="lines+markers",
                    name="Atypical Reflexes",
                    legendgroup="",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_3"],
                    mode="lines+markers",
                    name="Visual Novelty",
                    legendgroup="",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=5,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_4"],
                    mode="lines+markers",
                    name="Visual Reach",
                    legendgroup="Phase " "3",
                    legendgrouptitle_text=" ",
                    hovertemplate="  %{y:.1f} ",
                ),
                row=5,
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
                fillcolor="red",
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
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=1,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=1,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=2,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=2,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=3,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=3,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=4,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=4,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=5,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Phase 1", "Phase 2", "Phase 3", "Resolving"],
                tickvals=[0.1, 1, 2, 3],
                row=5,
                col=2,
            )
            fig.update_layout(
                template="simple_white",
                title_text=f"{studentname}: CVI " f"Progression",
                hovermode="x unified",
                hoverlabel=dict(namelength=-1),
            )
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                studentname,
                "cviProgression.html",
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
                    "RUBRIC: 0=CVI Range 1-2 | 1=CVI Range 3-4 | 2=CVI Range 5-6 |  3=CVI Range 7-8"
                ).props(
                    'aria-label="RUBRIC: 0=CVI Range 1-2 | 1=CVI Range 3-4 | 2=CVI Range 5-6 |  3=CVI Range 7-8"'
                )
                ui.input().props(
                    'aria-label="RUBRIC: 0=CVI Range 1-2 | 1=CVI Range 3-4 | 2=CVI Range 5-6 |  3=CVI Range 7-8" content-center'
                ).classes("sr-only").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                )
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Color Preference",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial11.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Color Preference"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Color Preference")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Need for Movement",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial12.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Need for Movement"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Need for Movement")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Latency",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial13.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Latency"').tooltip(
                    "Latency"
                ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Field Preference",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial14.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Field Preference"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Field Preference")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Visual Complexity",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial21.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Visual Complexity"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Visual Complexity")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Nonpurposeful Gaze",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial22.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Nonpurposeful Gaze"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Nonpurposeful Gaze")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Distance Viewing",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial23.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Distance Viewing"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Distance Viewing")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Atypical Reflexes",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial31.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Atypical Reflexes"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Atypical Reflexes")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Visual Novelty",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial32.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Visual Novelty"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Visual Novelty")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.number(
                    label="Visual Reach",
                    min=0,
                    max=3,
                    format="%.0f",
                    on_change=lambda e: u_cvi_trial33.set_value(e.value),
                ).classes("w-[600px]").props('aria-label="Visual Reach"').style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ).tooltip("Visual Reach")
            with ui.row().classes("w-screen no-wrap py-4").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            ):
                ui.button("SAVE", color="#172554", on_click=save).classes(
                    "text-white"
                ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
                ui.button("GRAPH", color="#172554", on_click=graph).classes(
                    "text-white"
                )
                ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                    "text-white"
                )

        create_ui()
