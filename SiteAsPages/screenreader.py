#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for teachers
of students with Visual Impairments
"""
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                       #
#    email: hunsakerconsulting@gmail.com                                      #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");          #
#    you may not use this file except in compliance with the License.         #
#    You may obtain a copy of the License at                                  #
#                                                                             #
#    http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                             #
#    Unless Required by applicable law or agreed to in writing, software      #
#    distributed under the License is distributed on an "AS IS" BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
#    See the License for the specific language governing permissions and      #
#    limitations under the License.                                           #
###############################################################################

import datetime
import os
import shutil
import sqlite3
import sys
import traceback
from csv import writer
from pathlib import Path
from sqlite3 import Error

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nicegui import app, ui
from plotly.subplots import make_subplots
from screeninfo import get_monitors

import homepage
import menu
import theme
from helpers import students

def create() -> None:
    ##########################################################################
    # SCREENREADER SKILLS
    ##########################################################################
    @ui.page('/screenreaderskills')
    def screenreaderskills():
        with theme.frame('- SCREENREADER SKILLS -'):
            ui.label('SCREENREADER SKILLS').classes('text-h4 text-grey-8')
            u_studentname = ui.select(
                    options=students, value="DonaldChamberlain"
                    ).classes(
                    "hidden"
                    )
            # ASSIGN VARIABLES
            date = ui.date().classes("hidden")
            u_trial11 = ui.number().classes("hidden")
            u_trial12 = ui.number().classes("hidden")
            u_trial13 = ui.number().classes("hidden")
            u_trial14 = ui.number().classes("hidden")
            u_trial15 = ui.number().classes("hidden")
            u_trial16 = ui.number().classes("hidden")
            u_trial21 = ui.number().classes("hidden")
            u_trial22 = ui.number().classes("hidden")
            u_trial23 = ui.number().classes("hidden")
            u_trial24 = ui.number().classes("hidden")
            u_trial31 = ui.number().classes("hidden")
            u_trial32 = ui.number().classes("hidden")
            u_trial33 = ui.number().classes("hidden")
            u_trial34 = ui.number().classes("hidden")
            u_trial35 = ui.number().classes("hidden")
            u_trial36 = ui.number().classes("hidden")
            u_trial37 = ui.number().classes("hidden")
            u_trial38 = ui.number().classes("hidden")
            u_trial39 = ui.number().classes("hidden")
            u_trial310 = ui.number().classes("hidden")
            u_trial311 = ui.number().classes("hidden")
            u_trial41 = ui.number().classes("hidden")
            u_trial42 = ui.number().classes("hidden")
            u_trial43 = ui.number().classes("hidden")
            u_trial44 = ui.number().classes("hidden")
            u_trial45 = ui.number().classes("hidden")
            u_trial46 = ui.number().classes("hidden")
            u_trial47 = ui.number().classes("hidden")
            
            
            # SAVE FUNCTION (USED BELOW)
            def save(event):
                """
                :param event:
                :type event:
                """
                studentname = u_studentname.value
                date = datenow
                trial11 = int(u_trial11.value)
                trial12 = int(u_trial12.value)
                trial13 = int(u_trial13.value)
                trial14 = int(u_trial14.value)
                trial15 = int(u_trial15.value)
                trial16 = int(u_trial16.value)
                trial21 = int(u_trial21.value)
                trial22 = int(u_trial22.value)
                trial23 = int(u_trial23.value)
                trial24 = int(u_trial24.value)
                trial31 = int(u_trial31.value)
                trial32 = int(u_trial32.value)
                trial33 = int(u_trial33.value)
                trial34 = int(u_trial34.value)
                trial35 = int(u_trial35.value)
                trial36 = int(u_trial36.value)
                trial37 = int(u_trial37.value)
                trial38 = int(u_trial38.value)
                trial39 = int(u_trial39.value)
                trial310 = int(u_trial310.value)
                trial311 = int(u_trial311.value)
                trial41 = int(u_trial41.value)
                trial42 = int(u_trial42.value)
                trial43 = int(u_trial43.value)
                trial44 = int(u_trial44.value)
                trial45 = int(u_trial45.value)
                trial46 = int(u_trial46.value)
                trial47 = int(u_trial47.value)
                studentdatabasename = f"screenreader{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        studentdatabasename + ".txt",
                        )
                
                with open(tmppath, "w") as filename:
                    filename.write("studentname" + ", ")
                    filename.write("date" + ", ")
                    filename.write("trial11" + ", ")
                    filename.write("trial12" + ", ")
                    filename.write("trial13" + ", ")
                    filename.write("trial14" + ", ")
                    filename.write("trial15" + ", ")
                    filename.write("trial16" + ", ")
                    filename.write("trial21" + ", ")
                    filename.write("trial22" + ", ")
                    filename.write("trial23" + ", ")
                    filename.write("trial24" + ", ")
                    filename.write("trial31" + ", ")
                    filename.write("trial32" + ", ")
                    filename.write("trial33" + ", ")
                    filename.write("trial34" + ", ")
                    filename.write("trial35" + ", ")
                    filename.write("trial36" + ", ")
                    filename.write("trial37" + ", ")
                    filename.write("trial38" + ", ")
                    filename.write("trial39" + ", ")
                    filename.write("trial310" + ", ")
                    filename.write("trial311" + ", ")
                    filename.write("trial41" + ", ")
                    filename.write("trial42" + ", ")
                    filename.write("trial43" + ", ")
                    filename.write("trial44" + ", ")
                    filename.write("trial45" + ", ")
                    filename.write("trial46" + ", ")
                    filename.write("trial47" + "\n")
                    filename.write(studentname + ", ")
                    filename.write(date + ", ")
                    filename.write(str(trial11) + ", ")
                    filename.write(str(trial12) + ", ")
                    filename.write(str(trial13) + ", ")
                    filename.write(str(trial14) + ", ")
                    filename.write(str(trial15) + ", ")
                    filename.write(str(trial16) + ", ")
                    filename.write(str(trial21) + ", ")
                    filename.write(str(trial22) + ", ")
                    filename.write(str(trial23) + ", ")
                    filename.write(str(trial24) + ", ")
                    filename.write(str(trial31) + ", ")
                    filename.write(str(trial32) + ", ")
                    filename.write(str(trial33) + ", ")
                    filename.write(str(trial34) + ", ")
                    filename.write(str(trial35) + ", ")
                    filename.write(str(trial36) + ", ")
                    filename.write(str(trial37) + ", ")
                    filename.write(str(trial38) + ", ")
                    filename.write(str(trial39) + ", ")
                    filename.write(str(trial310) + ", ")
                    filename.write(str(trial311) + ", ")
                    filename.write(str(trial41) + ", ")
                    filename.write(str(trial42) + ", ")
                    filename.write(str(trial43) + ", ")
                    filename.write(str(trial44) + ", ")
                    filename.write(str(trial45) + ", ")
                    filename.write(str(trial46) + ", ")
                    filename.write(str(trial47) + ", ")
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
                    list_data = [
                            datenow,
                            trial11,
                            trial12,
                            trial13,
                            trial14,
                            trial15,
                            trial16,
                            trial21,
                            trial22,
                            trial23,
                            trial24,
                            trial31,
                            trial32,
                            trial33,
                            trial34,
                            trial35,
                            trial36,
                            trial37,
                            trial38,
                            trial39,
                            trial310,
                            trial311,
                            trial41,
                            trial42,
                            trial43,
                            trial44,
                            trial45,
                            trial46,
                            trial47,
                            ]
                    tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase",
                            "StudentDataFiles",
                            studentname,
                            "ScreenReaderSkillsProgression.csv",
                            )
                    os.chdir(USER_DIR)
                    with open(tmppath, "a", newline="") as f_setup:
                        writer_setup = writer(f_setup)
                        writer_setup.writerow(list_data)
                        f_setup.close()
                    ui.notify("Saved successfully!", close_button="OK")
                
                # noinspection SqlResolve
                def data_entry():
                    """ """
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
                                    datenow,
                                    trial11,
                                    trial12,
                                    trial13,
                                    trial14,
                                    trial15,
                                    trial16,
                                    trial21,
                                    trial22,
                                    trial23,
                                    trial24,
                                    trial31,
                                    trial32,
                                    trial33,
                                    trial34,
                                    trial35,
                                    trial36,
                                    trial37,
                                    trial38,
                                    trial39,
                                    trial310,
                                    trial311,
                                    trial41,
                                    trial42,
                                    trial43,
                                    trial44,
                                    trial45,
                                    trial46,
                                    trial47,
                                    ),
                            )
                    conn.commit()
                
                data_entry()
            
            
            def graph(event):
                """

                :param event:
                :type event:
                """
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
                df = df.set_index("date")
                print(df)
                df = df.sort_values(by="date")
                mu, sigma = 0, 0.1
                noise = np.random.normal(
                        mu, sigma, [len(df.index), len(df.columns)]
                        )
                df_noisy = df + noise
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
                                name="Turn ON/OFF",
                                legendgroup="Phase 1a",
                                legendgrouptitle_text="Phase 1a",
                                ),
                        row=1,
                        col=1,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P1_2"],
                                mode="lines+markers",
                                name="Use Modifier Keys",
                                legendgroup="Phase 1a",
                                legendgrouptitle_text="Phase 1a",
                                ),
                        row=1,
                        col=1,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P1_3"],
                                mode="lines+markers",
                                name="Use Reading Commands",
                                legendgroup="Phase 1a",
                                legendgrouptitle_text="Phase 1a",
                                ),
                        row=1,
                        col=1,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P1_4"],
                                mode="lines+markers",
                                name="ID Titles",
                                legendgroup="Phase 1b",
                                legendgrouptitle_text=" ",
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
                                ),
                        row=2,
                        col=1,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P2_1"],
                                mode="lines+markers",
                                name="Type with all keys",
                                legendgroup="Phase 2",
                                legendgrouptitle_text="Phase 2",
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
                                ),
                        row=1,
                        col=2,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P3_4"],
                                mode="lines+markers",
                                name="TAB Navigation",
                                legendgroup="Phase 3a",
                                legendgrouptitle_text="Phase 3a",
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
                                ),
                        row=3,
                        col=2,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P3_2"],
                                mode="lines+markers",
                                name="ID HTML Elements",
                                legendgroup="Phase 3b",
                                legendgrouptitle_text="Phase 3b",
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
                                legendgroup="Phase 3b",
                                legendgrouptitle_text="Phase 3b",
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
                                ),
                        row=4,
                        col=2,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P4_1"],
                                mode="lines+markers",
                                name="Save and Open Files",
                                legendgroup="Phase 4a",
                                legendgrouptitle_text="Phase 4a",
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
                                legendgroup="Phase 4a",
                                legendgrouptitle_text="Phase 4a",
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
                                legendgroup="Phase 4b",
                                legendgrouptitle_text="Phase 4b",
                                ),
                        row=5,
                        col=2,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P4_6"],
                                mode="lines+markers",
                                name="Use Virtual Cursor",
                                legendgroup="Phase 4b",
                                legendgrouptitle_text="Phase 4b",
                                ),
                        row=5,
                        col=2,
                        )
                fig.add_trace(
                        go.Scatter(
                                x=df_noisy.index,
                                y=df_noisy["P4_7"],
                                mode="lines+markers",
                                name="Use Built-In OCR",
                                legendgroup="Phase 4b",
                                legendgrouptitle_text="Phase 4b",
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
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=1,
                        col=1,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=2,
                        col=1,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=1,
                        col=2,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=3,
                        col=1,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=3,
                        col=2,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=4,
                        col=2,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=5,
                        col=1,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=5,
                        col=2,
                        )
                fig.update_layout(
                        template="simple_white",
                        title_text=f"{studentname}: Screen Reader Skills "
                                f"Progression",
                        )
                tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "ScreenReaderSkillsProgression.html",
                        )
                fig.write_html(tmppath)
                fig.show()
                ui.notify(
                        "Graph Successful. The Graphs will open in a Browser "
                        "Window",
                        close_button="OK",
                        )
            
            
            # SCREENREADER SKILLS PROGRESSION TAB
            with ui.row().classes("w-screen no-wrap"):
                ui.label("SCREENREADER SKILLS PROGRESSION").classes(
                        "justify-center items-center"
                        )
            with ui.row().classes("w-screen no-wrap"):
                ui.select(
                        options=students,
                        with_input=True,
                        on_change=lambda e: ui.notify(e.value),
                        ).bind_value(u_studentname, "value").classes(
                        "w-[300px]"
                        ).props(
                        'aria-label="Select Student from the Dropdown. It will '
                        'autocomplete as you type"'
                        ).tooltip(
                        "Type Student Name, it will autocomplete AS you type"
                        )
                with ui.input("Date").classes("w-[300px]").props(
                        'aria-label="Date. Please type in date using the '
                        'YYYY-MM-DD format"'
                        ).tooltip(
                        "Date. Please type in date using the YYYY-MM-DD format"
                        ) as date:
                    with date.add_slot("append"):
                        ui.icon("edit_calendar").on(
                                "click", lambda: menu.open()
                                ).classes(
                                "cursor-pointer"
                                )
                    with ui.menu() as menu:
                        ui.date().bind_value(date)
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label(
                        "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated "
                        "3=Independent"
                        ).props(
                        'aria-label="RUBRIC: 0=No attempt 1=Required Assistance '
                        '2=Hesitated 3=Independent" content-center'
                        )
                ui.input().props(
                        'aria-label="RUBRIC: 0=No attempt 1=Required Assistance '
                        '2=Hesitated 3=Independent" content-center'
                        ).classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 1: READING").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 1: READING"').classes(
                        "sr-only"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="1.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial11.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.1 Turn on and off the screen reader"'
                        ).tooltip(
                        "1.1 Turn on and off the screen reader"
                        )
                ui.number(
                        label="1.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial12.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.2 Utilize modifier keys such as ctrl alt '
                        ""
                        'and shift"'
                        ).tooltip(
                        "1.2 Utilize modifier keys such as ctrl alt and shift"
                        )
                ui.number(
                        label="1.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial13.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.3 Read text using a variety of reading '
                        'commands"'
                        ).tooltip(
                        "1.3 Read text using a variety of reading commands"
                        )
                ui.number(
                        label="1.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial14.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.4 Identify the titles and section titles '
                        'of documents with Headings"'
                        ).tooltip(
                        "1.4 Identify the titles and section titles of documents "
                        "with Headings"
                        )
                ui.number(
                        label="1.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial15.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.5 Access documents open and close '
                        'programs  navigate to the  desktop"'
                        ).tooltip(
                        "1.5 Access documents open and close programs  navigate "
                        "to "
                        "the  desktop"
                        )
                ui.number(
                        label="1.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial16.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.6 Switch Program Focus"'
                        ).tooltip(
                        "1.6 Switch Program Focus"
                        )
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 2: WRITING").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 2: WRITING"').classes(
                        "sr-only"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="2.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial21.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.1 Type with all alphanumeric keys on the '
                        ""
                        'keyboard."'
                        ).tooltip(
                        "2.1 Type with all alphanumeric keys on the keyboard."
                        )
                ui.number(
                        label="2.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial22.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.2 Navigate to and change screen reader '
                        'settings"'
                        ).tooltip(
                        "2.2 Navigate to and change screen reader settings"
                        )
                ui.number(
                        label="2.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial23.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.3 Write and edit documents using a basic '
                        'understanding of cursor placement"'
                        ).tooltip(
                        "2.3 Write and edit documents using a basic "
                        "understanding of "
                        "cursor placement"
                        )
                ui.number(
                        label="2.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial24.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.4. Select copy and paste text"'
                        ).tooltip(
                        "2.4. Select copy and paste text"
                        )
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 3: USING THE INTERNET").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 3: USING THE INTERNET"'
                        ).classes(
                        "sr-only"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="3.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial31.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.1 Define common element types on the '
                        'internet such as Headings Buttons"'
                        ).tooltip(
                        "3.1 Define common element types on the internet such as "
                        "Headings Buttons"
                        )
                ui.number(
                        label="3.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial32.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.2 identify each element by type."'
                        ).tooltip(
                        "3.2 identify each element by type."
                        )
                ui.number(
                        label="3.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial33.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.3 navigate to the address bar"'
                        ).tooltip(
                        "3.3 navigate to the address bar"
                        )
                ui.number(
                        label="3.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial34.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.4 Use the “Tab” key to navigate to the '
                        'next clickable object"'
                        ).tooltip(
                        "3.4 Use the “Tab” key to navigate to the next clickable "
                        "" "" "object"
                        )
                ui.number(
                        label="3.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial35.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aira-label="3.5 Navigate by “Quick Keys” (h for heading '
                        'b for button and u for link"'
                        )
                ui.number(
                        label="3.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial36.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.6 Use Elements Lists on a website to '
                        'navigate by element type"'
                        ).tooltip(
                        "3.6 Use Elements Lists on a website to navigate by "
                        "element " "type"
                        )
                ui.number(
                        label="3.7",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial37.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.7 Justify why he/she/they selected a '
                        'particular method for the situation"'
                        ).tooltip(
                        "3.7 Justify why he/she/they selected a particular method "
                        "for the situation"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="3.8",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial38.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.8 Switch tab focus"'
                        ).tooltip(
                        "3.8 Switch tab focus"
                        )
                ui.number(
                        label="3.9",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial39.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.9 Switch between screen reader modes"'
                        ).tooltip(
                        "3.9 Switch between screen reader modes"
                        )
                ui.number(
                        label="3.10",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial310.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.10 Navigate a table"'
                        ).tooltip(
                        "3.10 Navigate a table"
                        )
                ui.number(
                        label="3.11",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial311.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.11 Develop a navigation sequence to '
                        'access an unfamiliar website"'
                        ).tooltip(
                        "3.11 Develop a navigation sequence to access an "
                        "unfamiliar "
                        "website"
                        )
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 4: NAVIGATING AND FILE MANAGEMENT").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 4: NAVIGATING AND FILE MANAGEMENT"'
                        ).classes("sr-only")
            
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="4.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial41.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.1 Be able to save and open files using '
                        'File Explorer."'
                        ).tooltip(
                        "4.1 Be able to save and open files using File Explorer."
                        )
                ui.number(
                        label="4.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial42.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.2 Create folders and move files in File '
                        'Explorer"'
                        ).tooltip(
                        "4.2 Create folders and move files in File Explorer"
                        )
                ui.number(
                        label="4.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial43.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.3 Navigate a cloud-based file management '
                        'system (eg: Google Drive)"'
                        ).tooltip(
                        "4.3 Navigate a cloud-based file management system (eg: "
                        "Google Drive)"
                        )
                ui.number(
                        label="4.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial44.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.4 Download and save material from the '
                        'internet"'
                        ).tooltip(
                        "4.4 Download and save material from the internet"
                        )
                ui.number(
                        label="4.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial45.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.5 Extract zipped folders"'
                        ).tooltip(
                        "4.5 Extract zipped folders"
                        )
                ui.number(
                        label="4.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial46.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.6 Utilize the virtual cursor and mouse '
                        'keys"'
                        ).tooltip(
                        "4.6 Utilize the virtual cursor and mouse keys"
                        )
                ui.number(
                        label="4.7",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial47.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.7 To use OCR features to read '
                        'inaccessible material"'
                        ).tooltip(
                        "4.7 To use OCR features to read inaccessible material"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.button("SAVE", color="#172554", on_click=save).classes(
                        "text-white"
                        )
                ui.button("GRAPH", color="#172554", on_click=graph).classes(
                        "text-white"
                        )
                ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                        "text-white"
                        )
                