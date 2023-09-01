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
import plotly.io as pio
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nicegui import app, ui
from plotly.subplots import make_subplots
from screeninfo import get_monitors

import homepage
import menu
import theme
# import contentpages
import abacus
import braille
import braillenote
import contactLog
import ios
import cvi
import screenreader
from helpers import students

##############################################################################
# Define Paths
##############################################################################
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = ""
IMAGE_DIR = Path(ROOT_DIR).joinpath("images")
##############################################################################
# Set User Directory based on OS
##############################################################################
if os.name == "nt":
    try:
        tmppath = Path(os.environ["USERPROFILE"]).joinpath("Documents")
        Path.mkdir(tmppath, parents=True, exist_ok=True)
        USER_DIR = Path(tmppath)
    except Error as e:
        print(f"{e}\n Cannot find %USERPROFILE")
elif os.name == "posix":
    try:
        tmppath = Path(os.environ["HOME"]).joinpath("Documents")
        Path.mkdir(tmppath, parents=True, exist_ok=True)
        USER_DIR = Path(tmppath)
    except Error as e:
        print(f"{e}\n Cannot find $HOME")
else:
    print("Cannot determine OS Type")
os.chdir(USER_DIR)

def create() -> None:
        ##########################################################################
    # ABACUS SKILLS
    ##########################################################################
    @ui.page('/abacusskills')
    def abacusskills():
        with theme.frame('- ABACUS SKILLS -'):
            ui.label('ABACUS SKILLS').classes('text-h4 text-grey-8')
            datenow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")
            u_studentname = ui.select(
                    options=students, value="DonaldChamberlain"
                    ).classes(
                    "hidden"
                    )
            date = ui.date().classes("hidden")
            u_trial11 = ui.number().classes("hidden")
            u_trial12 = ui.number().classes("hidden")
            u_trial13 = ui.number().classes("hidden")
            u_trial14 = ui.number().classes("hidden")
            u_trial21 = ui.number().classes("hidden")
            u_trial22 = ui.number().classes("hidden")
            u_trial23 = ui.number().classes("hidden")
            u_trial31 = ui.number().classes("hidden")
            u_trial32 = ui.number().classes("hidden")
            u_trial33 = ui.number().classes("hidden")
            u_trial41 = ui.number().classes("hidden")
            u_trial42 = ui.number().classes("hidden")
            u_trial51 = ui.number().classes("hidden")
            u_trial52 = ui.number().classes("hidden")
            u_trial61 = ui.number().classes("hidden")
            u_trial62 = ui.number().classes("hidden")
            u_trial63 = ui.number().classes("hidden")
            u_trial64 = ui.number().classes("hidden")
            u_trial71 = ui.number().classes("hidden")
            u_trial72 = ui.number().classes("hidden")
            u_trial73 = ui.number().classes("hidden")
            u_trial74 = ui.number().classes("hidden")
            u_trial81 = ui.number().classes("hidden")
            u_trial82 = ui.number().classes("hidden")
            
            
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
                trial21 = int(u_trial21.value)
                trial22 = int(u_trial22.value)
                trial23 = int(u_trial23.value)
                trial31 = int(u_trial31.value)
                trial32 = int(u_trial32.value)
                trial33 = int(u_trial33.value)
                trial41 = int(u_trial41.value)
                trial42 = int(u_trial42.value)
                trial51 = int(u_trial51.value)
                trial52 = int(u_trial52.value)
                trial61 = int(u_trial61.value)
                trial62 = int(u_trial62.value)
                trial63 = int(u_trial63.value)
                trial64 = int(u_trial64.value)
                trial71 = int(u_trial71.value)
                trial72 = int(u_trial72.value)
                trial73 = int(u_trial73.value)
                trial74 = int(u_trial74.value)
                trial81 = int(u_trial81.value)
                trial82 = int(u_trial82.value)
                studentdatabasename = f"abacus{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        studentdatabasename + ".csv",
                        )
                with open(tmppath, "w") as filename:
                    filename.write("studentname" + ", ")
                    filename.write("date" + ", ")
                    filename.write("trial11" + ", ")
                    filename.write("trial12" + ", ")
                    filename.write("trial13" + ", ")
                    filename.write("trial14" + ", ")
                    filename.write("trial21" + ", ")
                    filename.write("trial22" + ", ")
                    filename.write("trial23" + ", ")
                    filename.write("trial31" + ", ")
                    filename.write("trial32" + ", ")
                    filename.write("trial33" + ", ")
                    filename.write("trial41" + ", ")
                    filename.write("trial42" + ", ")
                    filename.write("trial51" + ", ")
                    filename.write("trial52" + ", ")
                    filename.write("trial61" + ", ")
                    filename.write("trial62" + ", ")
                    filename.write("trial63" + ", ")
                    filename.write("trial64" + ", ")
                    filename.write("trial71" + ", ")
                    filename.write("trial72" + ", ")
                    filename.write("trial73" + ", ")
                    filename.write("trial74" + ", ")
                    filename.write("trial81" + ", ")
                    filename.write("trial82" + "\n")
                    filename.write(studentname + ", ")
                    filename.write(date + ", ")
                    filename.write(str(trial11) + ", ")
                    filename.write(str(trial12) + ", ")
                    filename.write(str(trial13) + ", ")
                    filename.write(str(trial14) + ", ")
                    filename.write(str(trial21) + ", ")
                    filename.write(str(trial22) + ", ")
                    filename.write(str(trial23) + ", ")
                    filename.write(str(trial31) + ", ")
                    filename.write(str(trial32) + ", ")
                    filename.write(str(trial33) + ", ")
                    filename.write(str(trial41) + ", ")
                    filename.write(str(trial42) + ", ")
                    filename.write(str(trial51) + ", ")
                    filename.write(str(trial52) + ", ")
                    filename.write(str(trial61) + ", ")
                    filename.write(str(trial62) + ", ")
                    filename.write(str(trial63) + ", ")
                    filename.write(str(trial64) + ", ")
                    filename.write(str(trial71) + ", ")
                    filename.write(str(trial72) + ", ")
                    filename.write(str(trial73) + ", ")
                    filename.write(str(trial74) + ", ")
                    filename.write(str(trial81) + ", ")
                    filename.write(str(trial82) + ", ")
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
                    filename.write(f"{tmppath}" + "\n")
                    filename.close()
                    list_data = [
                            datenow,
                            trial11,
                            trial12,
                            trial13,
                            trial14,
                            trial21,
                            trial22,
                            trial23,
                            trial31,
                            trial32,
                            trial33,
                            trial41,
                            trial42,
                            trial51,
                            trial52,
                            trial61,
                            trial62,
                            trial63,
                            trial64,
                            trial71,
                            trial72,
                            trial73,
                            trial74,
                            trial81,
                            trial82,
                            ]
                    os.chdir(USER_DIR)
                    with open(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\"
                            f"{studentname}\\ScreenReaderSkillsProgression.csv",
                            "a",
                            newline="",
                            ) as f_setup:
                        writer_setup = writer(f_setup)
                        writer_setup.writerow(list_data)
                        f_setup.close()
                    ui.notify("Saved successfully!", close_button="OK")
                
                # noinspection SqlResolve
                def data_entry():
                    """ """
                    dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")
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
                                    trial11,
                                    trial12,
                                    trial13,
                                    trial14,
                                    trial21,
                                    trial22,
                                    trial23,
                                    trial31,
                                    trial32,
                                    trial33,
                                    trial41,
                                    trial42,
                                    trial51,
                                    trial52,
                                    trial61,
                                    trial62,
                                    trial63,
                                    trial64,
                                    trial71,
                                    trial72,
                                    trial73,
                                    trial74,
                                    trial81,
                                    trial82,
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
                dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")
                conn = sqlite3.connect(dataBasePath)
                df_sql = pd.read_sql_query("SELECT * FROM ABACUSPROGRESS", conn)
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
                                legendgroup="Phase 1",
                                legendgrouptitle_text="Phase 1",
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
                                name="Vocabulary",
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
                                mode="lines+markers",
                                name="Setting Numbers",
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
                                name="Clearing Beads",
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
                                name="Place Value",
                                legendgroup="Phase 2",
                                legendgrouptitle_text="Phase 2",
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
                                legendgroup="Phase 3",
                                legendgrouptitle_text="Phase 3",
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
                                legendgroup="Phase 3",
                                legendgrouptitle_text="Phase 3",
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
                                legendgroup="Phase 4",
                                legendgrouptitle_text="Phase 4",
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
                                legendgroup="Phase 5",
                                legendgrouptitle_text="Phase 5",
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
                                legendgroup="Phase 5",
                                legendgrouptitle_text="Phase 5",
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
                                legendgroup="Phase 6",
                                legendgrouptitle_text="Phase 6",
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
                                legendgroup="Phase 6",
                                legendgrouptitle_text="Phase 6",
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
                                legendgroup="Phase 6",
                                legendgrouptitle_text="Phase 6",
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
                                legendgroup="Phase 7",
                                legendgrouptitle_text="Phase 7",
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
                                legendgroup="Phase 7",
                                legendgrouptitle_text="Phase 7",
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
                                legendgroup="Phase 7",
                                legendgrouptitle_text="Phase 7",
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
                                legendgroup="Phase 8",
                                legendgrouptitle_text="Phase 8",
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
                        row=1,
                        col=2,
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
                        row=2,
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
                        col=1,
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
                fig.update_layout(
                        template="simple_white",
                        title_text=f"{studentname}: Abacus Skills Progression",
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
                        "Graph Successful. The Graphs will open in a Browser "
                        "Window",
                        close_button="OK",
                        )            
            
            # ABACUS SKILLS PROGRESSION TAB
            with ui.row().classes("w-screen no-wrap"):
                ui.label("ABACUS SKILLS PROGRESSION").classes(
                        "justify-center items-center"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
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
                ui.label("PHASE 1: Setting and Clearing Numbers").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 1: Setting and Clearing Numbers" '
                        "content-center"
                        ).classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="1.1", value="",
                        on_change=lambda e: u_trial11.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="1.1 Setting Numbers"'
                        ).tooltip(
                        "1.1 Setting Numbers"
                        )
                ui.number(
                        label="1.2", value="",
                        on_change=lambda e: u_trial12.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="1.2 Clearing Numbers"'
                        ).tooltip(
                        "1.2 Clearing Numbers"
                        )
                ui.number(
                        label="1.3", value="",
                        on_change=lambda e: u_trial13.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="1.3 Place Value"'
                        ).tooltip(
                        "1.3 Place Value"
                        )
                ui.number(
                        label="1.4", value="",
                        on_change=lambda e: u_trial14.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="1.4 Vocabulary"'
                        ).tooltip(
                        "1.4 Vocabulary"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 2: Addition").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 2: Addition" content-center'
                        ).classes(
                        "sr-only"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="2.1", value="",
                        on_change=lambda e: u_trial21.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="2.1 Addition of Single Digit Numbers"'
                        ).tooltip(
                        "2.1 Addition of Single Digit Numbers"
                        )
                ui.number(
                        label="2.2", value="",
                        on_change=lambda e: u_trial22.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="2.2 Addition of Multiple Digit Numbers – '
                        'Direct"'
                        ).tooltip(
                        "2.2 Addition of Multiple Digit Numbers – Direct"
                        )
                ui.number(
                        label="2.3", value="",
                        on_change=lambda e: u_trial23.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="2.3 Addition of Multiple Digit Numbers – '
                        'Indirect"'
                        ).tooltip(
                        "2.3 Addition of Multiple Digit Numbers – Indirect"
                        )
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 3: Subtraction").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 3: Subtraction" content-center'
                        ).classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="3.1", value="",
                        on_change=lambda e: u_trial31.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="3.1 Subtraction"'
                        ).tooltip(
                        "3.1 Subtraction"
                        )
                ui.number(
                        label="3.2", value="",
                        on_change=lambda e: u_trial32.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="3.2 Subtraction of Multiple Digit Numbers – '
                        '' "" 'Direct"'
                        ).tooltip(
                        "3.2 Subtraction of Multiple Digit Numbers – Direct"
                        )
                ui.number(
                        label="3.3", value="",
                        on_change=lambda e: u_trial33.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="3.3 Subtraction of Multiple Digit Numbers – '
                        ""
                        'Indirect"'
                        ).tooltip(
                        "3.3 Subtraction of Multiple Digit Numbers – Indirect"
                        )
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 4: Multiplication").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 4: Multiplication" content-center'
                        ).classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="4.1", value="",
                        on_change=lambda e: u_trial41.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="4.1 Multiplication – 2+ Digit Multiplicand '
                        '1-Digit Multiplier"'
                        ).tooltip(
                        "4.1 Multiplication – 2+ Digit Multiplicand 1-Digit "
                        "Multiplier"
                        )
                ui.number(
                        label="4.2", value="",
                        on_change=lambda e: u_trial42.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="4.2 Multiplication – 2+ Digit Multiplicand '
                        'AND Multiplier"'
                        ).tooltip(
                        "4.2 Multiplication – 2+ Digit Multiplicand AND Multiplier"
                        )
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 5: Division").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 5: Division" content-center'
                        ).classes(
                        "sr-only"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="5.1", value="",
                        on_change=lambda e: u_trial51.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="5.1 Division – 2+ Digit Dividend 1-Digit '
                        'Divisor"'
                        ).tooltip(
                        "5.1 Division – 2+ Digit Dividend 1-Digit Divisor"
                        )
                ui.number(
                        label="5.2", value="",
                        on_change=lambda e: u_trial52.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="5.2 Division – 2+ Digit Dividend AND 1 '
                        'Digit Divisor"'
                        ).tooltip(
                        "5.2 Division – 2+ Digit Dividend AND 1 Digit Divisor"
                        )
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 6: Decimals").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 6: Decimals" content-center'
                        ).classes(
                        "sr-only"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="6.1", value="",
                        on_change=lambda e: u_trial61.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="6.1 Addition of Decimals"'
                        ).tooltip(
                        "6.1 Addition of Decimals"
                        )
                ui.number(
                        label="6.2", value="",
                        on_change=lambda e: u_trial62.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="6.2 Subtraction of Decimals"'
                        ).tooltip(
                        "6.2 Subtraction of Decimals"
                        )
                ui.number(
                        label="6.3", value="",
                        on_change=lambda e: u_trial63.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="6.3 Multiplication of Decimals"'
                        ).tooltip(
                        "6.3 Multiplication of Decimals"
                        )
                ui.number(
                        label="6.4", value="",
                        on_change=lambda e: u_trial64.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="6.4 Division of Decimals"'
                        ).tooltip(
                        "6.4 Division of Decimals"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 7: Fractions").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="PHASE 7: Fractions" content-center'
                        ).classes(
                        "sr-only"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="7.1", value="",
                        on_change=lambda e: u_trial71.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="7.1 Addition of Fractions"'
                        ).tooltip(
                        "7.1 Addition of Fractions"
                        )
                ui.number(
                        label="7.2", value="",
                        on_change=lambda e: u_trial72.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="7.2 Subtraction of Fractions"'
                        ).tooltip(
                        "7.2 Subtraction of Fractions"
                        )
                ui.number(
                        label="7.3", value="",
                        on_change=lambda e: u_trial73.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="7.3 Multiplication of Fractions"'
                        ).tooltip(
                        "7.3 Multiplication of Fractions"
                        )
                ui.number(
                        label="7.4", value="",
                        on_change=lambda e: u_trial74.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="7.4 Division of Fractions"'
                        ).tooltip(
                        "7.4 Division of Fractions"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 8: Roots and Percents").classes(
                        "justify-center items-center"
                        )
                ui.input().props(
                        'aria-label="HASE 8: Roots and Percents" content-center'
                        ).classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="8.1", value="",
                        on_change=lambda e: u_trial81.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="8.1 Percent"'
                        ).tooltip(
                        "8.1 Percent"
                        )
                ui.number(
                        label="8.2", value="",
                        on_change=lambda e: u_trial82.set_value(e.value)
                        ).classes("w-[200px]").props(
                        'aria-label="8.2 Square Root"'
                        ).tooltip(
                        "8.2 Square Root"
                        )
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
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
