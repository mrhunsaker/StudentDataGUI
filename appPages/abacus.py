#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""
########################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                #
#    email: hunsakerconsulting@gmail.com                               #
#                                                                      #
#                                                                      #
#    Licensed under the Apache License, Version 2.0 (the "License");   #
#    you may not use this file except in compliance with the License.  #
#    You may obtain a copy of the License at                           #
#    http://www.apache.org/licenses/LICENSE-2.0                        #
#                                                                      #
#    Unless Required by applicable law or agreed to in writing,        #
#    software distributed under the License is distributed on an       #
#    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,      #
#    either express or  implied.  See the License for the specific     #
#   language governing permissions and limitations under the License.  #
########################################################################

import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nicegui import app, ui
from plotly.subplots import make_subplots

from appHelpers.helpers import dataBasePath, datenow, USER_DIR, date_fmt
from appHelpers.roster import students
from appTheming import theme


def create() -> None:
    """Abacus Skills Progression"""

    @ui.page("/abacusskills")
    def abacusskills() -> None:
        with theme.frame("- TACTILE SKILLS -"):
            ui.label("ABACUS SKILLS").classes("text-h4 text-grey-8")
            u_studentname = ui.select(
                options=students, value="DonaldChamberlain"
            ).classes("hidden")
            date = ui.date().classes("hidden")
            u_abacus_trial11 = ui.number().classes("hidden")
            u_abacus_trial12 = ui.number().classes("hidden")
            u_abacus_trial13 = ui.number().classes("hidden")
            u_abacus_trial14 = ui.number().classes("hidden")
            u_abacus_trial21 = ui.number().classes("hidden")
            u_abacus_trial22 = ui.number().classes("hidden")
            u_abacus_trial23 = ui.number().classes("hidden")
            u_abacus_trial31 = ui.number().classes("hidden")
            u_abacus_trial32 = ui.number().classes("hidden")
            u_abacus_trial33 = ui.number().classes("hidden")
            u_abacus_trial41 = ui.number().classes("hidden")
            u_abacus_trial42 = ui.number().classes("hidden")
            u_abacus_trial51 = ui.number().classes("hidden")
            u_abacus_trial52 = ui.number().classes("hidden")
            u_abacus_trial61 = ui.number().classes("hidden")
            u_abacus_trial62 = ui.number().classes("hidden")
            u_abacus_trial63 = ui.number().classes("hidden")
            u_abacus_trial64 = ui.number().classes("hidden")
            u_abacus_trial71 = ui.number().classes("hidden")
            u_abacus_trial72 = ui.number().classes("hidden")
            u_abacus_trial73 = ui.number().classes("hidden")
            u_abacus_trial74 = ui.number().classes("hidden")
            u_abacus_trial81 = ui.number().classes("hidden")
            u_abacus_trial82 = ui.number().classes("hidden")

            def save(event):
                """
                :param event:
                :type event:
                """
                studentname = u_studentname.value
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
                    "date": datenow,
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
                    """write data to database"""
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
                            datenow,
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
            :param event:
            :type event:
            """
            studentname = u_studentname.value
            dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")
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
                    legendgrouptitle_text="Phase 1",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 1",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 1",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 1",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 2",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 2",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 2",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 3",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 3",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 3",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 4",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 4",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 5",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 5",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 6",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 6",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 6",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 6",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 7",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 7",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 7",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 7",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 8",   hovertemplate = '  %{y:.1f} '
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
                    legendgrouptitle_text="Phase 8",   hovertemplate = '  %{y:.1f} '
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
                row=1,
                col=2,
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
                row=2,
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
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=4,
                col=2,
            )
            fig.update_layout(
                template="simple_white",
                title_text=f"{studentname}: Abacus Skills Progression",
                hovermode="x unified",
                hoverlabel = dict(namelength = -1),
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

        # GUI Input
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.select(
                options=students,
                with_input=True,
                on_change=lambda e: ui.notify(e.value),
            ).bind_value(u_studentname, "value").classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip(
                "Type Student Name, it will autocomplete AS you type"
            )
        with ui.input("Date").classes("w-[300px]").props(
            'aria-label="Date. Please type in date using the YYYY-MM-DD format"'
        ).tooltip("Date. Please type in date using the YYYY-MM-DD format") as date:
            with date.add_slot("append"):
                ui.icon("edit_calendar").on("click", lambda: menu.open()).classes(
                    "cursor-pointer"
                )
        with ui.menu() as menu:
            ui.date().bind_value(date)
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label(
                "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"
            ).props(
                'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"'
            )
        ui.input().props(
            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"'
        ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 1: Setting and Clearing Numbers").classes(
                "justify-center items-center"
            )
        ui.input().props('aria-label="PHASE 1: Setting and Clearing Numbers"').classes(
            "sr-only"
        )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.1 Setting Numbers",
                value="",
                on_change=lambda e: u_abacus_trial11.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="1.1 Setting Numbers"').tooltip(
                "1.1 Setting Numbers"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.2 Clearing Numbers",
                value="",
                on_change=lambda e: u_abacus_trial12.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="1.2 Clearing Numbers"').tooltip(
                "1.2 Clearing Numbers"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.3 Place Value",
                value="",
                on_change=lambda e: u_abacus_trial13.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="1.3 Place Value"').tooltip(
                "1.3 Place Value"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.4 Vocabulary",
                value="",
                on_change=lambda e: u_abacus_trial14.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="1.4 Vocabulary"').tooltip(
                "1.4 Vocabulary"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 2: Addition").classes("justify-center items-center")
        ui.input().props('aria-label="PHASE 2: Addition"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.1 Addition of Single Digit Numbers",
                value="",
                on_change=lambda e: u_abacus_trial21.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="2.1 Addition of Single Digit Numbers"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.2 Addition of Multiple Digit Numbers – Direct",
                value="",
                on_change=lambda e: u_abacus_trial22.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="2.2 Addition of Multiple Digit Numbers – Direct"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.3 Addition of Multiple Digit Numbers – Indirect",
                value="",
                on_change=lambda e: u_abacus_trial23.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="2.3 Addition of Multiple Digit Numbers – Indirect"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 3: Subtraction").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 3: Subtraction"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.1 Subtraction",
                value="",
                on_change=lambda e: u_abacus_trial31.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="3.1 Subtraction"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.2 Subtraction of Multiple Digit Numbers – Direct",
                value="",
                on_change=lambda e: u_abacus_trial32.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="3.2 Subtraction of Multiple Digit Numbers – Direct"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.3 Subtraction of Multiple Digit Numbers – Indirect",
                value="",
                on_change=lambda e: u_abacus_trial33.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="3.3 Subtraction of Multiple Digit Numbers – Indirect"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 4: Multiplication").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 4: Multiplication"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.1 Multiplication – 2+ Digit Multiplicand 1-Digit Multiplier",
                value="",
                on_change=lambda e: u_abacus_trial41.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="4.1 Multiplication – 2+ Digit Multiplicand 1-Digit Multiplier"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.2 Multiplication – 2+ Digit Multiplicand AND Multiplier",
                value="",
                on_change=lambda e: u_abacus_trial42.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="4.2 Multiplication – 2+ Digit Multiplicand AND Multiplier"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 5: Division").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 5: Division"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.1 Division – 2+ Digit Dividend 1-Digit Divisor",
                value="",
                on_change=lambda e: u_abacus_trial51.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="5.1 Division – 2+ Digit Dividend 1-Digit Divisor"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.2 Division – 2+ Digit Dividend AND 1 Digit Divisor",
                value="",
                on_change=lambda e: u_abacus_trial52.set_value(e.value),
            ).classes("w-[600px]").props(
                'aria-label="5.2 Division – 2+ Digit Dividend AND 1 Digit Divisor"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 6: Decimals").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 6: Decimals"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.1 Addition of Decimals",
                value="",
                on_change=lambda e: u_abacus_trial61.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="6.1 Addition of Decimals"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.2 Subtraction of Decimals",
                value="",
                on_change=lambda e: u_abacus_trial62.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="6.2 Subtraction of Decimals"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.3 Multiplication of Decimals",
                value="",
                on_change=lambda e: u_abacus_trial63.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="6.3 Multiplication of Decimals"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.4 Division of Decimals",
                value="",
                on_change=lambda e: u_abacus_trial64.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="6.4 Division of Decimals"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 7: Fractions").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 7: Fractions"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="7.1 Addition of Fractions",
                value="",
                on_change=lambda e: u_abacus_trial71.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="7.1 Addition of Fractions"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="7.2 Subtraction of Fractions",
                value="",
                on_change=lambda e: u_abacus_trial72.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="7.2 Subtraction of Fractions"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="7.3 Multiplication of Fractions",
                value="",
                on_change=lambda e: u_abacus_trial73.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="7.3 Multiplication of Fractions"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="7.4 Division of Fractions",
                value="",
                on_change=lambda e: u_abacus_trial74.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="7.4 Division of Fractions"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 8: Roots and Percents").classes(
                "justify-center items-center"
            )
            ui.input().props('aria-label="PHASE 8: Roots and Percents"').classes(
                "sr-only"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="8.1 Percent",
                value="",
                on_change=lambda e: u_abacus_trial81.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="8.1 Percent"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="8.2 Square Root",
                value="",
                on_change=lambda e: u_abacus_trial82.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="8.2 Square Root"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                "text-white"
            )
