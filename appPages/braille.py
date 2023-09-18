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

import os
import sqlite3
from csv import writer
from pathlib import Path
import json
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nicegui import app, ui
from plotly.subplots import make_subplots

from appPages import theme
from appHelpers.helpers import dataBasePath, datenow, USER_DIR
from appHelpers.roster import students


def create() -> None:
    ##########################################################################
    # BRAILLE SKILLS
    ##########################################################################
    @ui.page("/brailleskills")
    def brailleskills():
        with theme.frame("- BRAILLE SKILLS -"):
            ui.label("BRAILLE SKILLS").classes("text-h4 text-grey-8")

            u_studentname = ui.select(
                options=students, value="DonaldChamberlain"
            ).classes("hidden")
            date = ui.date().classes("hidden")
            u_braille_trial11 = ui.number().classes("hidden")
            u_braille_trial12 = ui.number().classes("hidden")
            u_braille_trial13 = ui.number().classes("hidden")
            u_braille_trial14 = ui.number().classes("hidden")
            u_braille_trial21 = ui.number().classes("hidden")
            u_braille_trial22 = ui.number().classes("hidden")
            u_braille_trial23 = ui.number().classes("hidden")
            u_braille_trial24 = ui.number().classes("hidden")
            u_braille_trial25 = ui.number().classes("hidden")
            u_braille_trial26 = ui.number().classes("hidden")
            u_braille_trial27 = ui.number().classes("hidden")
            u_braille_trial28 = ui.number().classes("hidden")
            u_braille_trial29 = ui.number().classes("hidden")
            u_braille_trial210 = ui.number().classes("hidden")
            u_braille_trial211 = ui.number().classes("hidden")
            u_braille_trial212 = ui.number().classes("hidden")
            u_braille_trial213 = ui.number().classes("hidden")
            u_braille_trial214 = ui.number().classes("hidden")
            u_braille_trial215 = ui.number().classes("hidden")
            u_braille_trial31 = ui.number().classes("hidden")
            u_braille_trial32 = ui.number().classes("hidden")
            u_braille_trial33 = ui.number().classes("hidden")
            u_braille_trial34 = ui.number().classes("hidden")
            u_braille_trial35 = ui.number().classes("hidden")
            u_braille_trial36 = ui.number().classes("hidden")
            u_braille_trial37 = ui.number().classes("hidden")
            u_braille_trial38 = ui.number().classes("hidden")
            u_braille_trial39 = ui.number().classes("hidden")
            u_braille_trial310 = ui.number().classes("hidden")
            u_braille_trial311 = ui.number().classes("hidden")
            u_braille_trial312 = ui.number().classes("hidden")
            u_braille_trial313 = ui.number().classes("hidden")
            u_braille_trial314 = ui.number().classes("hidden")
            u_braille_trial315 = ui.number().classes("hidden")
            u_braille_trial41 = ui.number().classes("hidden")
            u_braille_trial42 = ui.number().classes("hidden")
            u_braille_trial43 = ui.number().classes("hidden")
            u_braille_trial44 = ui.number().classes("hidden")
            u_braille_trial51 = ui.number().classes("hidden")
            u_braille_trial52 = ui.number().classes("hidden")
            u_braille_trial53 = ui.number().classes("hidden")
            u_braille_trial54 = ui.number().classes("hidden")
            u_braille_trial61 = ui.number().classes("hidden")
            u_braille_trial62 = ui.number().classes("hidden")
            u_braille_trial63 = ui.number().classes("hidden")
            u_braille_trial64 = ui.number().classes("hidden")
            u_braille_trial65 = ui.number().classes("hidden")
            u_braille_trial66 = ui.number().classes("hidden")
            u_braille_trial67 = ui.number().classes("hidden")
            u_braille_trial71 = ui.number().classes("hidden")
            u_braille_trial72 = ui.number().classes("hidden")
            u_braille_trial73 = ui.number().classes("hidden")
            u_braille_trial74 = ui.number().classes("hidden")
            u_braille_trial75 = ui.number().classes("hidden")
            u_braille_trial76 = ui.number().classes("hidden")
            u_braille_trial77 = ui.number().classes("hidden")
            u_braille_trial78 = ui.number().classes("hidden")
            u_braille_trial81 = ui.number().classes("hidden")
            u_braille_trial82 = ui.number().classes("hidden")
            u_braille_trial83 = ui.number().classes("hidden")
            u_braille_trial84 = ui.number().classes("hidden")
            u_braille_trial85 = ui.number().classes("hidden")
            u_braille_trial86 = ui.number().classes("hidden")
            u_braille_trial87 = ui.number().classes("hidden")

            def save(event):
                """

                :param event:
                :type event:
                """
                studentname = u_studentname.value
                date = datenow
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
                braille_dictionary={
                "studentname": studentname,
                "date": datenow,
                "braille_trial11": braille_trial11,
                "braille_trial12" : braille_trial12,
                "braille_trial13" : braille_trial13,
                "braille_trial14" : braille_trial14,
                "braille_trial21" : braille_trial21,
                "braille_trial22" : braille_trial22,
                "braille_trial23" : braille_trial23,
                "braille_trial24" : braille_trial24,
                "braille_trial25" : braille_trial25,
                "braille_trial26" : braille_trial26,
                "braille_trial27" : braille_trial27,
                "braille_trial28" : braille_trial28,
                "braille_trial29" : braille_trial29,
                "braille_trial210" : braille_trial210,
                "braille_trial211" : braille_trial211,
                "braille_trial212" : braille_trial212,
                "braille_trial213" : braille_trial213,
                "braille_trial214" : braille_trial214,
                "braille_trial215" : braille_trial215,
                "braille_trial31" : braille_trial31,
                "braille_trial32" : braille_trial32,
                "braille_trial33" : braille_trial33,
                "braille_trial34" : braille_trial34,
                "braille_trial35" : braille_trial35,
                "braille_trial36" : braille_trial36,
                "braille_trial37" : braille_trial37,
                "braille_trial38" : braille_trial38,
                "braille_trial39" : braille_trial39,
                "braille_trial310" : braille_trial310,
                "braille_trial311" : braille_trial311,
                "braille_trial312" : braille_trial312,
                "braille_trial313" : braille_trial313,
                "braille_trial314" : braille_trial314,
                "braille_trial315" : braille_trial315,
                "braille_trial41" : braille_trial41,
                "braille_trial42" : braille_trial42,
                "braille_trial43" : braille_trial43,
                "braille_trial44" : braille_trial44,
                "braille_trial51" : braille_trial51,
                "braille_trial52" : braille_trial52,
                "braille_trial53" : braille_trial53,
                "braille_trial54" : braille_trial54,
                "braille_trial61" : braille_trial61,
                "braille_trial62" : braille_trial62,
                "braille_trial63" : braille_trial63,
                "braille_trial64" : braille_trial64,
                "braille_trial65" : braille_trial65,
                "braille_trial66" : braille_trial66,
                "braille_trial67" : braille_trial67,
                "braille_trial71" : braille_trial71,
                "braille_trial72" : braille_trial72,
                "braille_trial73" : braille_trial73,
                "braille_trial74" : braille_trial74,
                "braille_trial75" : braille_trial75,
                "braille_trial76" : braille_trial76,
                "braille_trial77" : braille_trial77,
                "braille_trial78" : braille_trial78,
                "braille_trial81" : braille_trial81,
                "braille_trial82" : braille_trial82,
                "braille_trial83" : braille_trial83,
                "braille_trial84" : braille_trial84,
                "braille_trial85" : braille_trial85,
                "braille_trial86" : braille_trial86,
                "braille_trial87" : braille_trial87
                }
                with open(tmppath, "w") as filename:
                    json.dump(braille_dictionary,filename)
                filename.close()
        
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase", "StudentDataFiles", "Filenames.txt"
                )
                filename = open(tmppath, "a")
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    studentdatabasename + ".txt",
                )
                filename.write(f"'{tmppath}'" + "\n")
                filename.close()
                os.chdir(USER_DIR)
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    "BrailleSkillsProgression.csv",
                )
                with open(tmppath, "a", newline="") as f_setup:
                    list_data = [
                        datenow,
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
                    ]
                writer_setup = writer(f_setup)
                writer_setup.writerow(list_data)
                f_setup.close()
                os.chdir(USER_DIR)
                tmpdir = Path(
                    USER_DIR,
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    "BrailleSkillsProgression.csv",
                )
                with open(tmpdir, "a", newline="") as f_setup:
                    writer_setup = writer(f_setup)
                writer_setup.writerow(list_data)
                f_setup.close()

                # noinspection SqlResolve

                def data_entry():
                    """ """
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
                            datenow,
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

                Graphing

                """
                dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")
                studentname = u_studentname.value
                conn = sqlite3.connect(dataBasePath)
                df_sql = pd.read_sql_query("SELECT * FROM " "BRAILLEPROGRESS", conn)
                df_student = df_sql[df_sql.STUDENTNAME == studentname]
                print(df_student)
                conn.close()
                df = df_student.drop(columns=["ID", "STUDENTNAME"])
                print(df)
                df = df.rename(columns={"DATE": "date"})
                df = df.set_index("date")
                print(df)
                df = df.sort_values(by="date")
                mu, sigma = 0, 0.1
                noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
                df_noisy = df + noise
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
                        y=df_noisy["P1_3"].iloc[[-1]],
                        mode="lines+markers",
                        name="Discriminate shapes",
                        legendgroup="Phase 1",
                        legendgrouptitle_text="Phase 1",
                    ),
                    row=2,
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
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_1"].iloc[[-1]],
                        mode="text",
                        text=[" G C L"],
                        textposition="middle " "right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_2"].iloc[[-1]],
                        mode="text",
                        text=[" D Y"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_3"].iloc[[-1]],
                        mode="text",
                        text=[" A B"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_4"].iloc[[-1]],
                        mode="text",
                        text=[" S"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_5"].iloc[[-1]],
                        mode="text",
                        text=[" W"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_6"].iloc[[-1]],
                        mode="text",
                        text=[" P O"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_7"].iloc[[-1]],
                        mode="text",
                        text=[" K"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_8"].iloc[[-1]],
                        mode="text",
                        text=[" R"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_9"].iloc[[-1]],
                        mode="text",
                        text=[" M E"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_10"].iloc[[-1]],
                        mode="text",
                        text=[" H"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_11"].iloc[[-1]],
                        mode="text",
                        text=[" N X"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_12"].iloc[[-1]],
                        mode="text",
                        text=[" Z F"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_13"].iloc[[-1]],
                        mode="text",
                        text=[" U T"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_14"].iloc[[-1]],
                        mode="text",
                        text=[" Q I"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                    ),
                    row=1,
                    col=2,
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_noisy.index[[-1]],
                        y=df_noisy["P2_15"].iloc[[-1]],
                        mode="text",
                        text=[" V J"],
                        textposition="middle right",
                        legendgroup="Phase 2",
                        legendgrouptitle_text="Phase 2",
                        showlegend=False,
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
                        legendgroup="Phase " "3a",
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
                        name="Strong Contractions <br>(AND OF FOR " "WITH " "THE)",
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
                        name="Strong Wordsigns <br>(CH SH TH WH OU " "ST)",
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
                        name="Lower Groupsigns <br>(EA BB CC FF " "GG)",
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
                        name="Lower Groupsigns/Wordsigns <br>(EN " "IN)",
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
                        name="Lower Wordsigns <br>(BE HIS WAS " "WERE)",
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
                        name="Dot " "5 " "Contractions",
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
                        name="Dot " "45 " "Contractions",
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
                        name="Dot " "456 " "Contractions",
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
                        name="Page " "Numbering",
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
                        legendgroup="Phase " "5",
                        legendgrouptitle_text="Phase 5",
                    ),
                    row=7,
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
                fig.add_hrect(
                    y0=-0.5,
                    y1=0.5,
                    line_width=0,
                    fillcolor="#b3c7f7",
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
                    fillcolor="#b3c7f7",
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
                    xaxis2_tickformat="%d " "%b",
                    xaxis3_tickformat="%d %b",
                    xaxis4_tickformat="%d %b",
                    xaxis5_tickformat="%d %b",
                    xaxis6_tickformat="%d %b",
                    xaxis7_tickformat="%d %b",
                    xaxis8_tickformat="%d %b",
                    xaxis9_tickformat="%d %b",
                    template="simple_white",
                    title_text=f"{studentname}: Literary UEB Skills " f"Progression",
                    legend=dict(font=dict(size=10)),
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
                    "Graph Successful. The Graphs will open in a " "Browser " "Window",
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
                        legendgroup="Phase " "6",
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
                        legendgroup="Phase " "6",
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
                        legendgroup="Phase " "6",
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
                        name="Advanced Operation and Comparison " "Signs",
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
                        legendgroup="Phase " "7",
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
                        legendgroup="Phase " "8",
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
                        legendgroup="Phase " "8",
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
                    xaxis2_tickformat="%d " "%b",
                    xaxis3_tickformat="%d %b",
                    template="simple_white",
                    title_text=f""
                    f"{studentname}: Technical UEB Skills "
                    f"Progression",
                    legend=dict(font=dict(size=10)),
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
                    "Graph Successful. The Graphs will open in a " "Browser " "Window",
                    position="center",
                    type="positive",
                    close_button="OK",
                )

        # BRAILLE SKILLS PROGRESSION TAB

        with ui.row().classes("w-screen no-wrap"):
            ui.label("BRAILLE SKILLS PROGRESSION").classes(
                "justify-center items-center"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.select(
                options=students,
                with_input=True,
                on_change=lambda e: ui.notify(e.value),
            ).bind_value(u_studentname, "value").classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It '
                "will "
                'autocomplete as you type"'
            ).tooltip(
                "Type Student Name, it will " "autocomplete AS you type"
            )
            with ui.input("Date").classes("w-[300px]").props(
                'aria-label="Date. Please type in date using '
                "the "
                'YYYY-MM-DD format"'
            ).tooltip(
                "Date. Please type in date using " "the YYYY-MM-DD format"
            ) as date:
                with date.add_slot("append"):
                    ui.icon("edit_calendar").on("click", lambda: menu.open()).classes(
                        "cursor-pointer"
                    )
                with ui.menu() as menu:
                    ui.date().bind_value(date)
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label(
                "RUBRIC: 0=No attempt 1=Required Assistance "
                "2=Hesitated "
                "3=Independent"
            ).props(
                'aria-label="RUBRIC: 0=No attempt 1=Required '
                "Assistance "
                '2=Hesitated 3=Independent" content-center'
            )
            ui.input().props(
                'aria-label="RUBRIC: 0=No attempt 1=Required '
                "Assistance "
                '2=Hesitated 3=Independent" content-center'
            ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 1: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 1:"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="1.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial11.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="1.1 Track Left to Right"'
            ).tooltip(
                "1.1 " "Track Left to Right"
            )
            ui.number(
                label="1.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial12.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="1.2 Track Top to Bottom"')
            ui.number(
                label="1.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial13.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="1.3 Discriminate Shapes"')
            ui.number(
                label="1.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial14.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="1.4 Discriminate Braille Characters"'
            )
            ui.label(" ").classes("w-[200px]")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 2: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 2: "').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial21.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.1 Mangold Progression: G C L"')
            ui.number(
                label="2.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial22.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.2 Mangold Progression: D Y"')
            ui.number(
                label="2.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial23.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.3 Mangold Progression: A B"')
            ui.number(
                label="2.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial24.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.4 Mangold Progression: S"')
            ui.number(
                label="2.5",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial25.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.5 Mangold Progression: W"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.6",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial26.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.6 Mangold Progression: P O"')
            ui.number(
                label="2.7",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial27.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.7 Mangold Progression: K"')
            ui.number(
                label="2.8",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial28.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.8 Mangold Progression: R"')
            ui.number(
                label="2.9",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial29.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.9 Mangold Progression: M E"')
            ui.number(
                label="2.10",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial210.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.10 Mangold Progression: H"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="2.11",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial211.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.11 Mangold Progression: N X"')
            ui.number(
                label="2.12",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial212.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.12 Mangold Progression: Z F"')
            ui.number(
                label="2.13",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial213.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.13 Mangold Progression: U T"')
            ui.number(
                label="2.14",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial214.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.14 Mangold Progression: Q I"')
            ui.number(
                label="2.15",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial215.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="2.15 Mangold Progression: V J"')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 3: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 3: "').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial31.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="3.1 Alphabetic Wordsigns"')
            ui.number(
                label="3.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial32.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="3.2 Braille Numbers"')
            ui.number(
                label="3.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial33.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="3.3 Punctuation"')
            ui.number(
                label="3.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial34.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.4 Strong Contractions - AND OF FOR ' "WITH " 'THE"'
            )
            ui.number(
                label="3.5",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial35.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.5 Strong Groupsigns - CH GH SH TH '
                "WH "
                "ED "
                'ER OU OW ST AR ING"'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.6",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial36.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.6 Strong Wordsigns - CH SH TH WH OU ST"'
            )
            ui.number(
                label="3.7",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial37.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.7 Lower Groupsigns - BE CON DIS"'
            )
            ui.number(
                label="3.8",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial38.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.8 Lower Groupsigns - EA BB CC FF GG"'
            )
            ui.number(
                label="3.9",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial39.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.9 Lower Group/Wordsigns - EN IN"'
            )
            ui.number(
                label="3.10",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial310.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.10 Lower Wordsigns - BE HIS WAS ' 'WERE"'
            ).tooltip(
                "3.10 Lower Wordsigns - BE HIS WAS " "WERE"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="3.11",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial311.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.11 Dot 5 Contractions"'
            ).tooltip(
                "3.11 " "Dot 5 Contractions"
            )
            ui.number(
                label="3.12",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial312.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.12 Dot 45 Contractions"'
            ).tooltip(
                "3.12 Dot 45 Contractions"
            )
            ui.number(
                label="3.13",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial313.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.13 Dot 456 Contractions"'
            ).tooltip(
                "3.13 Dot 456 Contractions"
            )
            ui.number(
                label="3.14",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial314.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="3.14 Final Letter Groupsigns"'
            ).tooltip(
                "3.14 Final Letter Groupsigns"
            )
            ui.number(
                label="3.15",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial315.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="3.15 Shortform Words"').tooltip(
                "3.15 " "Shortform Words"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 4: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 4: "').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="4.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial41.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="4.1 Grade 1 Indicators"').tooltip(
                "4.1 " "Grade 1 Indicators"
            )
            ui.number(
                label="4.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial42.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="4.2 Capitals Indicators"'
            ).tooltip(
                "4.2 " "Capitals Indicators"
            )
            ui.number(
                label="4.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial43.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="4.3 Numeric Mode and Spatial ' 'Math"'
            ).tooltip(
                "4.3 Numeric Mode and Spatial Math"
            )
            ui.number(
                label="4.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial44.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="4.4 Typeform Indicators - ITALIC BOLD ' 'UNDERLINE SCRIPT"'
            ).tooltip(
                "4.4 Typeform Indicators - ITALIC BOLD UNDERLINE " "SCRIPT"
            )
            ui.label(" ").classes("w-[200px]")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 5: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 5: "').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="5.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial51.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="5.1 Page Numbering"').tooltip(
                "5.1 Page " "Numbering"
            )
            ui.number(
                label="5.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial52.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="5.2 Headings"').tooltip(
                "5.2 Headings"
            )
            ui.number(
                label="5.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial53.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="5.3 Lists"').tooltip("5.3 Lists")
            ui.number(
                label="5.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial54.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="5.4 Poetry / Drama"').tooltip(
                "5.4 " "Poetry / Drama"
            )
            ui.label(" ").classes("w-[200px]")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 6: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 6: "').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial61.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="6.1 Operation and Comparison ' 'Signs"'
            ).tooltip(
                "6.1 Operation and Comparison Signs"
            )
            ui.number(
                label="6.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial62.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="6.2 Grade 1 Mode"').tooltip(
                "6.2 Grade 1 " "Mode"
            )
            ui.number(
                label="6.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial63.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="6.3 Special Print Symbols"'
            ).tooltip(
                "6.3 Special Print Symbols"
            )
            ui.number(
                label="6.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial64.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="6.4 Omission Marks"').tooltip(
                "6.4 " "Omission Marks"
            )
            ui.number(
                label="6.5",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial65.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="6.5 Shape Indicators"').tooltip(
                "6.5 " "Shape Indicators"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="6.6",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial66.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="6.6 Roman Numerals"').tooltip(
                "6.6 Roman " "Numerals"
            )
            ui.number(
                label="6.7",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial67.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="6.7 Fractions"').tooltip(
                "6.7 Fractions"
            )
            ui.label(" ").classes("w-[200px]")
            ui.label(" ").classes(" w-[200px]")
            ui.label(" ").classes("w-[200px]")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 7: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 7: "').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="7.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial71.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="7.1 Grade 1 Mode and algebra"'
            ).tooltip(
                "7.1 Grade 1 Mode and algebra"
            )
            ui.number(
                label="7.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial72.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="7.2 Grade 1 Mode and ' 'Fractions"'
            ).tooltip(
                "7.2 Grade 1 Mode and Fractions"
            )
            ui.number(
                label="7.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial73.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="7.3 Advanced Operation and Comparison ' 'Signs"'
            ).tooltip(
                "7.3 Advanced Operation and Comparison " "Signs"
            )
            ui.number(
                label="7.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial74.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="7.4 Indices"').tooltip(
                "7.4 Indices"
            )
            ui.number(
                label="7.5",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial75.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="7.5 Roots and Radicals"').tooltip(
                "7.5 " "Roots and Radicals"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="7.6",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial76.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="7.6 Miscellaneous Shape ' 'Indicators"'
            ).tooltip(
                "7.6 Miscellaneous Shape " "Indicators"
            )
            ui.number(
                label="7.7",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial77.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="7.7 Functions"').tooltip(
                "7.7 Functions"
            )
            ui.number(
                label="7.8",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial78.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="7.8 Greek Letters"').tooltip(
                "7.8 Greek " "Letters"
            )
            ui.label(" ").classes("w-[200px]")
            ui.label(" ").classes("w-[200px]")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 8: ").classes("justify-center " "items-center")
            ui.input().props('aria-label="PHASE 8:"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="8.1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial81.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="8.1 Functions"')
            ui.number(
                label="8.2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial82.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="8.2 Modifiers: Bars and Dots"'
            ).tooltip(
                "8.2 Modifiers: Bars and Dots"
            )
            ui.number(
                label="8.3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial83.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="8.3 Modifiers: Arrows and ' 'Limits"'
            ).tooltip(
                "8.3 Modifiers: Arrows and Limits"
            )
            ui.number(
                label="8.4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial84.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="8.4 Probability"').tooltip(
                "8.4 " "Probability"
            )
            ui.number(
                label="8.5",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial85.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="8.5 Calculus: ' 'Differentiation"'
            ).tooltip(
                "8.5 Calculus: " "Differentiation"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="8.6",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial86.set_value(e.value),
            ).classes("w-[200px]").props(
                'aria-label="8.6 Calculus: Integration"'
            ).tooltip(
                "8.6 Calculus: Integration"
            )
            ui.number(
                label="8.7",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_braille_trial87.set_value(e.value),
            ).classes("w-[200px]").props('aria-label="8.7 Vertical Bars"').tooltip(
                "8.7 " "Vertical Bars"
            )
            ui.label(" ").classes("w-[200px]")
            ui.label(" ").classes("w-[200px]")
            ui.label(" ").classes("w-[200px]")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                "text-white"
            )
