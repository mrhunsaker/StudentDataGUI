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
    ##########################################################################
    # iOS SKILLS
    ##########################################################################
    @ui.page("/iosskills")
    def iosskillsprogression() -> None:
        with theme.frame("- iOS / iPad OS SKILLS -"):
            ui.label("iOS / iPad OS  SKILLS").classes("text-h4 text-grey-8")
            # ASSIGN VARIABLES
            u_studentname = ui.select(options=students, value="DonaldChamberlain").classes("hidden")
            date = ui.date().classes("hidden")
            u_ios_trial11 = ui.number().classes("hidden")
            u_ios_trial12 = ui.number().classes("hidden")
            u_ios_trial13 = ui.number().classes("hidden")
            u_ios_trial14 = ui.number().classes("hidden")
            u_ios_trial15 = ui.number().classes("hidden")
            u_ios_trial16 = ui.number().classes("hidden")
            u_ios_trial17 = ui.number().classes("hidden")
            u_ios_trial18 = ui.number().classes("hidden")
            u_ios_trial19 = ui.number().classes("hidden")
            u_ios_trial21 = ui.number().classes("hidden")
            u_ios_trial22 = ui.number().classes("hidden")
            u_ios_trial23 = ui.number().classes("hidden")
            u_ios_trial24 = ui.number().classes("hidden")
            u_ios_trial25 = ui.number().classes("hidden")
            u_ios_trial26 = ui.number().classes("hidden")
            u_ios_trial31 = ui.number().classes("hidden")
            u_ios_trial32 = ui.number().classes("hidden")
            u_ios_trial33 = ui.number().classes("hidden")
            u_ios_trial34 = ui.number().classes("hidden")
            u_ios_trial35 = ui.number().classes("hidden")
            u_ios_trial41 = ui.number().classes("hidden")
            u_ios_trial42 = ui.number().classes("hidden")
            u_ios_trial43 = ui.number().classes("hidden")
            u_ios_trial44 = ui.number().classes("hidden")
            u_ios_trial45 = ui.number().classes("hidden")
            u_ios_trial51 = ui.number().classes("hidden")
            u_ios_trial52 = ui.number().classes("hidden")
            u_ios_trial53 = ui.number().classes("hidden")
            u_ios_trial54 = ui.number().classes("hidden")
            u_ios_trial55 = ui.number().classes("hidden")
            u_ios_trial56 = ui.number().classes("hidden")
            u_ios_trial57 = ui.number().classes("hidden")
            u_ios_trial61 = ui.number().classes("hidden")
            u_ios_trial62 = ui.number().classes("hidden")
            u_ios_trial63 = ui.number().classes("hidden")
            u_ios_trial64 = ui.number().classes("hidden")
            u_ios_trial65 = ui.number().classes("hidden")
            u_ios_trial66 = ui.number().classes("hidden")
            u_ios_trial67 = ui.number().classes("hidden")
            u_ios_trial68 = ui.number().classes("hidden")
            u_ios_trial69 = ui.number().classes("hidden")
            u_ios_trial610 = ui.number().classes("hidden")
            u_ios_trial611 = ui.number().classes("hidden")

            def save(event):
                """
                :param event
                :type event
                """
                studentname = u_studentname.value
                date = datenow
                ios_trial11 = int(u_ios_trial11.value)
                ios_trial12 = int(u_ios_trial12.value)
                ios_trial13 = int(u_ios_trial13.value)
                ios_trial14 = int(u_ios_trial14.value)
                ios_trial15 = int(u_ios_trial15.value)
                ios_trial16 = int(u_ios_trial16.value)
                ios_trial17 = int(u_ios_trial17.value)
                ios_trial18 = int(u_ios_trial18.value)
                ios_trial19 = int(u_ios_trial19.value)
                ios_trial21 = int(u_ios_trial21.value)
                ios_trial22 = int(u_ios_trial22.value)
                ios_trial23 = int(u_ios_trial23.value)
                ios_trial24 = int(u_ios_trial24.value)
                ios_trial25 = int(u_ios_trial25.value)
                ios_trial26 = int(u_ios_trial26.value)
                ios_trial31 = int(u_ios_trial31.value)
                ios_trial32 = int(u_ios_trial32.value)
                ios_trial33 = int(u_ios_trial33.value)
                ios_trial34 = int(u_ios_trial34.value)
                ios_trial35 = int(u_ios_trial35.value)
                ios_trial41 = int(u_ios_trial41.value)
                ios_trial42 = int(u_ios_trial42.value)
                ios_trial43 = int(u_ios_trial43.value)
                ios_trial44 = int(u_ios_trial44.value)
                ios_trial45 = int(u_ios_trial45.value)
                ios_trial51 = int(u_ios_trial51.value)
                ios_trial52 = int(u_ios_trial52.value)
                ios_trial53 = int(u_ios_trial53.value)
                ios_trial54 = int(u_ios_trial54.value)
                ios_trial55 = int(u_ios_trial55.value)
                ios_trial56 = int(u_ios_trial56.value)
                ios_trial57 = int(u_ios_trial57.value)
                ios_trial61 = int(u_ios_trial61.value)
                ios_trial62 = int(u_ios_trial62.value)
                ios_trial63 = int(u_ios_trial63.value)
                ios_trial64 = int(u_ios_trial64.value)
                ios_trial65 = int(u_ios_trial65.value)
                ios_trial66 = int(u_ios_trial66.value)
                ios_trial67 = int(u_ios_trial67.value)
                ios_trial68 = int(u_ios_trial68.value)
                ios_trial69 = int(u_ios_trial69.value)
                ios_trial610 = int(u_ios_trial610.value)
                ios_trial611 = int(u_ios_trial611.value)
                studentdatabasename = f"ios{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    studentdatabasename + ".json",
                )
                ios_dictionary = {
                    "studentname": studentname,
                    "date": datenow,
                    "ios_trial11": ios_trial11,
                    "ios_trial12": ios_trial12,
                    "ios_trial13": ios_trial13,
                    "ios_trial14": ios_trial14,
                    "ios_trial15": ios_trial15,
                    "ios_trial16": ios_trial16,
                    "ios_trial17": ios_trial17,
                    "ios_trial18": ios_trial18,
                    "ios_trial19": ios_trial19,
                    "ios_trial21": ios_trial21,
                    "ios_trial22": ios_trial22,
                    "ios_trial23": ios_trial23,
                    "ios_trial24": ios_trial24,
                    "ios_trial25": ios_trial25,
                    "ios_trial26": ios_trial26,
                    "ios_trial31": ios_trial31,
                    "ios_trial32": ios_trial32,
                    "ios_trial33": ios_trial33,
                    "ios_trial34": ios_trial34,
                    "ios_trial35": ios_trial35,
                    "ios_trial41": ios_trial41,
                    "ios_trial42": ios_trial42,
                    "ios_trial43": ios_trial43,
                    "ios_trial44": ios_trial44,
                    "ios_trial45": ios_trial45,
                    "ios_trial51": ios_trial51,
                    "ios_trial52": ios_trial52,
                    "ios_trial53": ios_trial53,
                    "ios_trial54": ios_trial54,
                    "ios_trial55": ios_trial55,
                    "ios_trial56": ios_trial56,
                    "ios_trial57": ios_trial57,
                    "ios_trial61": ios_trial61,
                    "ios_trial62": ios_trial62,
                    "ios_trial63": ios_trial63,
                    "ios_trial64": ios_trial64,
                    "ios_trial65": ios_trial65,
                    "ios_trial66": ios_trial66,
                    "ios_trial67": ios_trial67,
                    "ios_trial68": ios_trial68,
                    "ios_trial69": ios_trial69,
                    "ios_trial610": ios_trial610,
                    "ios_trial611": ios_trial611,
                }
                with open(tmppath, "w", encoding="utf-8") as filename:
                    json.dump(ios_dictionary, filename)
                    tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", "Filenames.txt")
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
                            """INSERT INTO IOSPROGRESS (
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
                                            P3_1,
                                            P3_2,
                                            P3_3,
                                            P3_4,
                                            P3_5,
                                            P4_1,
                                            P4_2,
                                            P4_3,
                                            P4_4,
                                            P4_5,
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
                                            P6_4,
                                            P6_5,
                                            P6_6,
                                            P6_7,
                                            P6_8,
                                            P6_9,
                                            P6_10,
                                            P6_11
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
                                                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                                                                                    )""",
                            (
                                studentname,
                                datenow,
                                ios_trial11,
                                ios_trial12,
                                ios_trial13,
                                ios_trial14,
                                ios_trial15,
                                ios_trial16,
                                ios_trial17,
                                ios_trial18,
                                ios_trial19,
                                ios_trial21,
                                ios_trial22,
                                ios_trial23,
                                ios_trial24,
                                ios_trial25,
                                ios_trial26,
                                ios_trial31,
                                ios_trial32,
                                ios_trial33,
                                ios_trial34,
                                ios_trial35,
                                ios_trial41,
                                ios_trial42,
                                ios_trial43,
                                ios_trial44,
                                ios_trial45,
                                ios_trial51,
                                ios_trial52,
                                ios_trial53,
                                ios_trial54,
                                ios_trial55,
                                ios_trial56,
                                ios_trial57,
                                ios_trial61,
                                ios_trial62,
                                ios_trial63,
                                ios_trial64,
                                ios_trial65,
                                ios_trial66,
                                ios_trial67,
                                ios_trial68,
                                ios_trial69,
                                ios_trial610,
                                ios_trial611,
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
            df_sql = pd.read_sql_query("SELECT * FROM IOSPROGRESS", conn)
            df_student = df_sql[df_sql.STUDENTNAME == studentname]
            print(df_student)
            conn.close()
            df = df_student.drop(columns=["ID", "STUDENTNAME"])
            print(df)
            df = df.rename(columns={"DATE": "date"})
            df['date'] = df['date'].astype('string')
            df['date'] = pd.to_datetime(df['date'], format=date_fmt)
            df['date'].dtypes
            df = df.set_index("date")
            print(df)
            print(df.dtypes)
            df = df.sort_values(by="date")
            mu, sigma = 0, 0.1
            noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
            df_noisy = df + noise
            fig = make_subplots(
                rows=3,
                cols=2,
                subplot_titles=(
                    "Basic Operations",
                    "Presentation Tools",
                    "Word Processing",
                    "Acceptable Use",
                    "SpreadSheets",
                    "Additional SKills",
                    "Presentation Tools",
                ),
                print_grid=True,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_1"],
                    mode="lines+markers",
                    name="Turn Device On/Off",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_2"],
                    mode="lines+markers",
                    name="Turn VoiceOver On/Off",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_3"],
                    mode="lines+markers",
                    name="Gestures to Click Icons",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_4"],
                    mode="lines+markers",
                    name="Home Screen Icons to Open Documents",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_5"],
                    mode="lines+markers",
                    name="Save Documents",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_6"],
                    mode="lines+markers",
                    name="Online Tools/Resources",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_7"],
                    mode="lines+markers",
                    name="Keyboarding",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_8"],
                    mode="lines+markers",
                    name="Use Different Elements",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_9"],
                    mode="lines+markers",
                    name="Control Center, App Switcher...",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Basic Operations",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_1"],
                    mode="lines+markers",
                    name="Write, edit save",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Word Processing",
                ),
                row=2,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_2"],
                    mode="lines+markers",
                    name="Read, Navigate Document",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Word Processing",
                ),
                row=2,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_3"],
                    mode="lines+markers",
                    name="Use Menubar",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Word Processing",
                ),
                row=2,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_4"],
                    mode="lines+markers",
                    name="Highlight text, copy and paste text",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Word Processing",
                ),
                row=2,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_5"],
                    mode="lines+markers",
                    name="Copy and paste images",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Word Processing",
                ),
                row=2,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_6"],
                    mode="lines+markers",
                    name="Proofread and edit",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Word Processing",
                ),
                row=2,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_1"],
                    mode="lines+markers",
                    name="Describe Spreadsheet",
                    legendgroup="Phase 3",
                    legendgrouptitle_text="Spreadsheet",
                ),
                row=3,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_2"],
                    mode="lines+markers",
                    name="Explain terms and concepts ",
                    legendgroup="Phase 3",
                    legendgrouptitle_text="Spreadsheet",
                ),
                row=3,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_3"],
                    mode="lines+markers",
                    name="Enter/Edit data",
                    legendgroup="Phase 3",
                    legendgrouptitle_text="Spreadsheet",
                ),
                row=3,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_4"],
                    mode="lines+markers",
                    name="Use mathematical symbols",
                    legendgroup="Phase 3",
                    legendgrouptitle_text="Spreadsheet",
                ),
                row=3,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_5"],
                    mode="lines+markers",
                    name="Use Spreadsheet to Solve Problems",
                    legendgroup="Phase 3",
                    legendgrouptitle_text="Spreadsheet",
                ),
                row=3,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_1"],
                    mode="lines+markers",
                    name="Navigate slides ",
                    legendgroup="Phase 4",
                    legendgrouptitle_text="Presentation Tools",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_2"],
                    mode="lines+markers",
                    name="Create, edit and format text",
                    legendgroup="Phase 4",
                    legendgrouptitle_text="Presentation Tools",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_3"],
                    mode="lines+markers",
                    name="Create a series of slides ",
                    legendgroup="Phase 4",
                    legendgrouptitle_text="Presentation Tools",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_4"],
                    mode="lines+markers",
                    name="Copy and paste or import graphics",
                    legendgroup="Phase 4",
                    legendgrouptitle_text="Presentation Tools",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_5"],
                    mode="lines+markers",
                    name="Use painting and drawing tools",
                    legendgroup="Phase 4",
                    legendgrouptitle_text="Presentation Tools",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_1"],
                    mode="lines+markers",
                    name="Explain Acceptable Use Policy",
                    legendgroup="Phase 5",
                    legendgrouptitle_text="Acceptable Use",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_2"],
                    mode="lines+markers",
                    name="Explain responsible uses of technology",
                    legendgroup="Phase 5",
                    legendgrouptitle_text="Acceptable Use",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_3"],
                    mode="lines+markers",
                    name="Explain Fair Use Guidelines",
                    legendgroup="Phase 5",
                    legendgrouptitle_text="Acceptable Use",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_4"],
                    mode="lines+markers",
                    name="Safe and efficient use of computers",
                    legendgroup="Phase 5",
                    legendgrouptitle_text="Acceptable Use",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_5"],
                    mode="lines+markers",
                    name="Demonstrate safe email practices",
                    legendgroup="Phase 5",
                    legendgrouptitle_text="Acceptable Use",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_6"],
                    mode="lines+markers",
                    name="Identify cyberbullying ",
                    legendgroup="Phase 5",
                    legendgrouptitle_text="Acceptable Use",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_7"],
                    mode="lines+markers",
                    name="Describe the potential risks and dangers",
                    legendgroup="Phase 5",
                    legendgrouptitle_text="Acceptable Use",
                ),
                row=2,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_1"],
                    mode="lines+markers",
                    name="Be responsible for device",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_2"],
                    mode="lines+markers",
                    name="Tactile graphics paired with digital graphics",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_3"],
                    mode="lines+markers",
                    name="Understand and use Earcons",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_4"],
                    mode="lines+markers",
                    name="Spatial relationships on the physical iPad screen ",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_5"],
                    mode="lines+markers",
                    name="Use sonification",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_6"],
                    mode="lines+markers",
                    name="Learn and use screen reader commands",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_7"],
                    mode="lines+markers",
                    name="Increase listening speed",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_8"],
                    mode="lines+markers",
                    name="Learn and use rotor commands ",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_9"],
                    mode="lines+markers",
                    name="Learn about accessibility features",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_10"],
                    mode="lines+markers",
                    name="Learn note taking skills",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_11"],
                    mode="lines+markers",
                    name="Explain what makes digital content accessible",
                    legendgroup="Phase 6",
                    legendgrouptitle_text="Additional AT Skills",
                ),
                row=3,
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

            fig.update_layout(
                template="simple_white",
                title_text=f"{studentname}: iOS SKills  Progression",
            )
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                studentname,
                "iosProgression.html",
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
            ui.label("iOS SKILLS PROGRESSION").classes("justify-center items-center")
        with ui.row().classes("w-screen no-wrap"):
            ui.select(
                options=students,
                with_input=True,
                on_change=lambda e: ui.notify(e.value),
            ).bind_value(
                u_studentname, "value"
            ).classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip("Type Student Name, it will autocomplete AS you type")
        with ui.row().classes("w-screen no-wrap"):
            with ui.input("Date").classes("w-[300px]").props('aria-label="Date. Please type in date using the YYYY-MM-DD format"') as date:
                with date.add_slot("append"):
                    ui.icon("edit_calendar").on("click", lambda: menu.open()).classes("cursor-pointer")
                with ui.menu() as menu:
                    ui.date().bind_value(date)

        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent").props('aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center')
            ui.input().props('aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 1: Navigation").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 1: Navigation"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Turn Device On/Off",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial11.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Turn Device On/Off"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.2 Turn VoiceOver On/Off",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial12.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Turn VoiceOver On/Off"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.3 Simple Gestures to click on icons",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial13.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Simple Gestures to click on icons"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.4 Use home screen icons to open applications and documents",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial14.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Use home screen icons to open applications and documents"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.5 Save Documents",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial15.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Save Documents"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.6 Explain and use age-appropriate online tools and resources",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial16.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Explain and use age-appropriate online tools and resources "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.7 Keyboarding (Bluetooth keyboard and Braille display if appropriate)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial17.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Keyboarding (Bluetooth keyboard and Braille display if appropriate)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.8 Learn about and use different types of elements (e.g. address bar, tabs, menu)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial18.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Learn about and use different types of elements (e.g. address bar, tabs, menu)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.9 Learn about and use Control Center, Notification Center, App Switcher, Status Bar, etc.",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial19.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Learn about and use Control Center, Notification Center, App Switcher, Status Bar, etc."')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 2: Word Processing").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 2: Word Processing"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.1 Use a word processing application to write, edit, print and save simple assignments",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial21.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Use a word processing application to write, edit, print and save simple assignments"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.2 Read and navigate documents",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial22.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Read and navigate documents"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.3 Use menu/tool bar functions (e.g. font/size/style, line spacing, margins to format, edit and print a document",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial23.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Use menu/tool bar functions (e.g. font/size/style, line spacing, margins) to format, edit and print a document"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.4 Highlight text, copy and paste text",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial24.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Highlight text, copy and paste text"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.5 Copy and paste images within the document and from outside sources",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial25.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Copy and paste images within the document and from outside sources"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.6 Proofread and edit writing using appropriate resources (e.g. dictionary, spell checker, grammar, and thesaurus)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial26.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Proofread and edit writing using appropriate resources (e.g. dictionary, spell checker, grammar, and thesaurus)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 3: Spreadsheets").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 3: Spreadsheets"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.1 Demonstrate an understanding of the spreadsheet as a tool to record, organize and graph information.",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial31.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Demonstrate an understanding of the spreadsheet as a tool to record, organize and graph information."')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.2 Identify and explain terms and concepts related to spreadsheets (i.e. cell, column, row, values, labels, chart graph)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial32.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Identify and explain terms and concepts related to spreadsheets (i.e. cell, column, row, values, labels, chart graph)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.3 Enter/Edit data in spreadsheets and perform calculations using formulas",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial33.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Enter/Edit data in spreadsheets and perform calculations using formulas"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.4 Use mathematical symbols e.g. add, minus, multiply, divide, exponents",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial34.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Use mathematical symbols e.g. add, minus, multiply, divide, exponents "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.5 Use spreadsheets and other applications to make predictions, solve problems and conclusions.",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial35.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Use spreadsheets and other applications to make predictions, solve problems and draw conclusions. "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 4: Presentation Tools").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 4: Presentation Tools"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.1 Navigate slides (book format)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial41.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Navigate slides (book format)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.2 Create, edit and format text on a slide",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial42.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Create, edit and format text on a slide "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.3 Create a series of slides and organize them to present research or convey an idea",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial43.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Create a series of slides and organize them to present research or convey an idea "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.4 Copy and paste or import graphics; change their size and position on a slid",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial44.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Copy and paste or import graphics; change their size and position on a slide"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.5 Use painting and drawing tools/applications to create and edit work",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial45.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Use painting and drawing tools/applications to create and edit work" ')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 5: Digital Literacy").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 5: Digital Literacy"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.1 Explain and demonstrate compliance with classroom, school rules (Acceptable Use Policy) regarding responsible use of computers and networks",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial51.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Explain and demonstrate compliance with classroom, school rules (Acceptable Use Policy) regarding responsible use of computers and networks"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.2 Explain responsible uses of technology and digital information; describe possible consequences of inappropriate use",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial52.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Explain responsible uses of technology and digital information; describe possible consequences of inappropriate use"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.3 Explain Fair Use  Guidelines for the use  of copyrighted  materials, (e.g. text, images, music, video in student projects) and giving credit to media creators",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial53.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Explain Fair Use Guidelines for the use of copyrighted materials, (e.g. text, images, music, video in student projects) and giving credit to media creators"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.4 Identify and explain the strategies for the safe and efficient use of computers (e.g. passwords, virus protection software, spam filters, popup blockers)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial54.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Identify and explain the strategies for the safe and efficient use of computers (e.g. passwords, virus protection software, spam filters, popup blockers)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.5 Demonstrate safe email practices, recognition of the potentially public exposure of email and appropriate email etiquette",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial55.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Demonstrate safe email practices, recognition of the potentially public exposure of email and appropriate email etiquette"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.6 Identify cyberbullying and describe strategies to deal with such a situation",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial56.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Identify cyberbullying and describe strategies to deal with such a situation"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.7 Recognize and describe the potential risks and dangers associated with various forms of online communications",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial57.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Recognize and describe the potential risks and dangers associated with various forms of online communications"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 6: Advanced Skills").classes("justify-center items-center")
            ui.input().props('aria-label="PHASE 6: Advanced Skills"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.1 Be responsible for device(s)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial61.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Be responsible for device(s)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.2 Tactile graphics paired with digital graphics",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial62.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Tactile graphics paired with digital graphics"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.3 Understand and use Earcons (screen reader sound hints)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial63.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Understand and use Earcons (screen reader sound hints)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.4 Understand and use spatial relationships on the physical iPad screen",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial64.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Understand and use spatial relationships on the physical iPad screen"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.5 Use sonification to explore and understand digital graphics",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial65.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Use sonification to explore and understand digital graphics"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.6 Learn and use screen reader commands (gestures/keyboard/braille display)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial66.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Learn and use screen reader commands (gestures/keyboard/braille display)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.7 Increase listening speed (100% on the iPad for pleasure reading)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial67.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Increase listening speed (100 on the iPad for pleasure reading)"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.8 Learn and use rotor commands",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial68.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Learn and use rotor commands"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.9 Learn about accessibility features",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial69.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Learn about accessibility features"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.10 Learn note taking skills",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial610.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Learn note taking skills"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.11 Learn and be able to explain what makes digital content accessible",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_ios_trial611.set_value(e.value),
            ).classes(
                "w-[600px]"
            ).props('aria-label="Learn and be able to explain what makes digital content accessible"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes("text-white")
