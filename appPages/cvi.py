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
    """
    CVI Progress Page Creation
    """

    @ui.page("/cviprogress")
    def cviprogress():
        with theme.frame("- CORTICAL/NEUROLOGICAL VISION IMPAIRMENT-"):
            ui.label("CVI PROGRESSION").classes("text-h4 text-grey-8")
            u_studentname = ui.select(
                options=students, value="DonaldChamberlain"
            ).classes("hidden")
            # ASSIGN VARIABLES
            date = ui.date().classes("hidden")
            u_cvi_trial11 = ui.number().classes("hidden")
            u_cvi_trial12 = ui.number().classes("hidden")
            u_cvi_trial13 = ui.number().classes("hidden")
            u_cvi_trial14 = ui.number().classes("hidden")
            u_cvi_trial21 = ui.number().classes("hidden")
            u_cvi_trial22 = ui.number().classes("hidden")
            u_cvi_trial23 = ui.number().classes("hidden")
            u_cvi_trial31 = ui.number().classes("hidden")
            u_cvi_trial32 = ui.number().classes("hidden")
            u_cvi_trial33 = ui.number().classes("hidden")

            def save(event):
                """
                :param event:
                :type event:
                """
                studentname = u_studentname.value
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
                    "date": datenow,
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
                    """ """
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
                            datenow,
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

                :param event:
                :type event:
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
                print(df)
                df = df.sort_values(by="date")
                mu, sigma = 0, 0.1
                noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
                df_noisy = df + noise
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

                # GUI Input

        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
        with ui.row().classes("w-screen no-wrap"):
            ui.select(
                options=students,
                with_input=True,
                on_change=lambda e: ui.notify(e.value),
            ).bind_value(u_studentname, "value").classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip(
                "Type Student Name, it will autocomplete as you type"
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
                "RUBRIC: 0=CVI Range 1-2 | 1=CVI Range 3-4 | 2=CVI Range 5-6 |  3=CVI Range 7-8"
            ).props(
                'aria-label="RUBRIC: 0=CVI Range 1-2 | 1=CVI Range 3-4 | 2=CVI Range 5-6 |  3=CVI Range 7-8"'
            )
            ui.input().props(
                'aria-label="RUBRIC: 0=CVI Range 1-2 | 1=CVI Range 3-4 | 2=CVI Range 5-6 |  3=CVI Range 7-8" content-center'
            ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Color Preference",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial11.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Color Preference"').tooltip(
                "Color Preference"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Need for Movement",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial12.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Need for Movement"').tooltip(
                "Need for Movement"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Latency",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial13.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Latency"').tooltip("Latency")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Field Preference",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial14.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Field Preference"').tooltip(
                "Field Preference"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Visual Complexity",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial21.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Visual Complexity"').tooltip(
                "Visual Complexity"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Nonpurposeful Gaze",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial22.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Nonpurposeful Gaze"').tooltip(
                "Nonpurposeful Gaze"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Distance Viewing",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial23.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Distance Viewing"').tooltip(
                "Distance Viewing"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Atypical Reflexes",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial31.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Atypical Reflexes"').tooltip(
                "Atypical Reflexes"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Visual Novelty",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial32.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Visual Novelty"').tooltip(
                "Visual Novelty"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Visual Reach",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_cvi_trial33.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Visual Reach"').tooltip(
                "Visual Reach"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                "text-white"
            )
