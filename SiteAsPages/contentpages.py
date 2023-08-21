
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

from helpers import students
import theme

def create() -> None:
    
    ##########################################################################
    # CONTACT LOG
    ##########################################################################
    @ui.page('/contactlog')
    def contactlog():
        with theme.frame('- CONTACT LOG -'):
            ui.label('CONTACT LOG').classes('text-h4 text-grey-8')

            u_studentname = ui.select(
                    options=students, value="DonaldChamberlain"
                    ).classes(
                    "hidden"
                    )
            date = ui.date().classes("hidden")
            u_guardianName = ui.input().classes("hidden")
            u_contactMethod = ui.radio(
                    ["Phone", "Text", "In-Person", "Email"]
                    ).classes(
                    "hidden"
                    )
            u_phoneNumber = ui.input().classes("hidden")
            u_emailAddress = ui.input().classes("hidden")
            u_contactResponse = ui.radio(
                    ["Answered", "Left Message", "Unable to Leave Message",
                    "Disconnected"]
                    ).classes("hidden")
            u_contactGeneral = ui.radio(
                    ["IEP Related", "Discipline Related", "Student Requested"]
                    ).classes("hidden")
            u_contactSpecific = ui.radio(
                    [
                            "Schedule IEP Meeting",
                            "IEP Team Follow-Up",
                            "Collaborate on Student IEP Goals",
                            "Progress Monitoring Update",
                            ]
                    ).classes("hidden")
            u_contactNotes = ui.textarea().classes("hidden")
            
            
            def save(event):
                """
                :param event:
                :type event:
                """
                studentname = u_studentname.value
                date = datenow
                guardianName = u_guardianName.value
                contactMethod = u_contactMethod.value
                phoneNumber = u_phoneNumber.value
                emailAddress = u_emailAddress.value
                contactResponse = u_contactResponse.value
                contactGeneral = u_contactGeneral.value
                contactSpecific = u_contactSpecific.value
                contactNotes = u_contactNotes.value
                
                studentdatabasename = f"contact{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        studentdatabasename + ".csv",
                        )
                with open(tmppath, "w") as filename:
                    filename.write("studentname" + ", ")
                    filename.write("date" + ", ")
                    filename.write("guardianName" + ", ")
                    filename.write("contactMethod" + ", ")
                    filename.write("phoneNumber" + ", ")
                    filename.write("emailAddress" + ", ")
                    filename.write("contactResponse" + ", ")
                    filename.write("contactGeneral" + ", ")
                    filename.write("contactSpecific" + ", ")
                    filename.write("contactNotes" + "\n")
                    filename.write(studentname + ", ")
                    filename.write(date + ", ")
                    filename.write(guardianName + ", ")
                    filename.write(contactMethod + ", ")
                    filename.write(phoneNumber + ", ")
                    filename.write(emailAddress + ", ")
                    filename.write(contactResponse + ", ")
                    filename.write(contactGeneral + ", ")
                    filename.write(contactSpecific + ", ")
                    filename.write(contactNotes + ", ")
            
            
            with ui.row().classes("w-full no-wrap py-4"):
                ui.label().classes("w-[250px]")
                ui.label("PARENT CONTACT LOG").classes(
                        "w-screen justify-center items-center text-lg font-bold"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label().classes("w-[50px]")
                ui.label("STUDENT INFORMATION").classes(
                        "w-full justify-center items-center font-bold"
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
                ui.label().classes("w-[50px]")
                ui.label("GUARDIAN INFORMATION").classes(
                        "w-screen justify-center items-center font-bold"
                        )
            with ui.row().classes("w-screen no-wrap"):
                ui.input(
                        label="Guardian Name",
                        value="",
                        on_change=lambda e: u_guardianName.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="Guardian Name"'
                        ).tooltip(
                        "Guardian Name"
                        )
                ui.input(
                        label="Phone Number",
                        value="",
                        on_change=lambda e: u_phoneNumber.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="Phone Number"'
                        ).tooltip(
                        "Phone Number"
                        )
                ui.input(
                        label="Email Address",
                        value="",
                        on_change=lambda e: u_emailAddress.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="Email Address"'
                        ).tooltip(
                        "Email Address"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label().classes("w-[50px]")
                ui.label("DETAILS OF CONTACT ATTEMPT").classes(
                        "w-screen justify-center items-center font-bold"
                        )
            with ui.row().classes("w-screen no-wrap"):
                ui.label("Contact Method").classes("w-[50px]")
                ui.select(
                        options=["Phone", "Text", "In-Person", "Email"],
                        value="",
                        on_change=lambda e: u_contactMethod.set_value(e.value),
                        ).classes("w-[240px]").props(
                        'aria-label="Contact Method"'
                        ).tooltip(
                        "Contact Method"
                        )
                ui.label("Contact Response").classes("w-[50px]")
                ui.select(
                        options=[
                                "Answered",
                                "Left Message",
                                "Unable to Leave Message",
                                "Disconnected",
                                ],
                        value="",
                        on_change=lambda e: u_contactResponse.set_value(e.value),
                        ).classes("w-[240px]").props(
                        'aria-label="Contact Response"'
                        ).tooltip(
                        "Contact Response"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label().classes("w-[50px]")
                ui.label("TOPIC OF CONTACT").classes(
                        "w-screen justify-center items-center font-bold"
                        )
            with ui.row().classes("w-screen no-wrap"):
                ui.label("General Topic").classes("w-[50px]")
                ui.select(
                        options=["IEP Related", "Discipline Related",
                                "Student Requested"],
                        value="",
                        on_change=lambda e: u_contactGeneral.set_value(e.value),
                        ).classes("w-[240px]").props(
                        'aria-label="Reason for Contact - General Category"'
                        ).tooltip(
                        "Reason for Contact - General Category"
                        )
                ui.label("Specific Topic").classes("w-[50px]")
                ui.select(
                        options=[
                                "Schedule IEP Meeting",
                                "IEP Team Follow-Up",
                                "Collaborate on Student IEP Goals",
                                "Progress Monitoring Update",
                                ],
                        value="",
                        on_change=lambda e: u_contactSpecific.set_value(e.value),
                        ).classes("w-[240px]").props(
                        'aria-label="Reason for Contact - Specific Reason"'
                        ).tooltip(
                        "Reason for Contact - Specific Reason"
                        )
            with ui.row().classes("w-screen no-wrap "):
                ui.textarea(
                        label="Contact Notes (if email please copy/paste email "
                            "into "
                            "the box)",
                        value="",
                        on_change=lambda e: u_contactNotes.set_value(e.value),
                        ).classes("w-[640px]").props(
                        'aria-label="Contact Notes (if email please copy/paste '
                        'email into the box)"'
                        ).tooltip(
                        "Contact Notes (if email please copy/paste email into "
                        "the box)"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.button("SAVE", color="#172554", on_click=save).classes(
                        "text-white"
                        )
                ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                        "text-white"
                        )
    
    ##########################################################################
    # ABACUS SKILLS
    ##########################################################################
    @ui.page('/abacusskills')
    def abacusskills():
        with theme.frame('- ABACUS SKILLS -'):
            ui.label('ABACUS SKILLS').classes('text-h4 text-grey-8')

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
                        "ScreenReaderSkillsProgression.html",
                        )
                fig.write_html(tmppath)
                fig.show()
            
            
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

    ##########################################################################
    # BRAILLE SKILLS
    ##########################################################################
    @ui.page('/brailleskills')
    def brailleskills():
        with theme.frame('- BRAILLE SKILLS -'):
            ui.label('BRAILLE SKILLS').classes('text-h4 text-grey-8')

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
            u_trial24 = ui.number().classes("hidden")
            u_trial25 = ui.number().classes("hidden")
            u_trial26 = ui.number().classes("hidden")
            u_trial27 = ui.number().classes("hidden")
            u_trial28 = ui.number().classes("hidden")
            u_trial29 = ui.number().classes("hidden")
            u_trial210 = ui.number().classes("hidden")
            u_trial211 = ui.number().classes("hidden")
            u_trial212 = ui.number().classes("hidden")
            u_trial213 = ui.number().classes("hidden")
            u_trial214 = ui.number().classes("hidden")
            u_trial215 = ui.number().classes("hidden")
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
            u_trial312 = ui.number().classes("hidden")
            u_trial313 = ui.number().classes("hidden")
            u_trial314 = ui.number().classes("hidden")
            u_trial315 = ui.number().classes("hidden")
            u_trial41 = ui.number().classes("hidden")
            u_trial42 = ui.number().classes("hidden")
            u_trial43 = ui.number().classes("hidden")
            u_trial44 = ui.number().classes("hidden")
            u_trial51 = ui.number().classes("hidden")
            u_trial52 = ui.number().classes("hidden")
            u_trial53 = ui.number().classes("hidden")
            u_trial54 = ui.number().classes("hidden")
            u_trial61 = ui.number().classes("hidden")
            u_trial62 = ui.number().classes("hidden")
            u_trial63 = ui.number().classes("hidden")
            u_trial64 = ui.number().classes("hidden")
            u_trial65 = ui.number().classes("hidden")
            u_trial66 = ui.number().classes("hidden")
            u_trial67 = ui.number().classes("hidden")
            u_trial71 = ui.number().classes("hidden")
            u_trial72 = ui.number().classes("hidden")
            u_trial73 = ui.number().classes("hidden")
            u_trial74 = ui.number().classes("hidden")
            u_trial75 = ui.number().classes("hidden")
            u_trial76 = ui.number().classes("hidden")
            u_trial77 = ui.number().classes("hidden")
            u_trial78 = ui.number().classes("hidden")
            u_trial81 = ui.number().classes("hidden")
            u_trial82 = ui.number().classes("hidden")
            u_trial83 = ui.number().classes("hidden")
            u_trial84 = ui.number().classes("hidden")
            u_trial85 = ui.number().classes("hidden")
            u_trial86 = ui.number().classes("hidden")
            u_trial87 = ui.number().classes("hidden")
            
            
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
                trial24 = int(u_trial24.value)
                trial25 = int(u_trial25.value)
                trial26 = int(u_trial26.value)
                trial27 = int(u_trial27.value)
                trial28 = int(u_trial28.value)
                trial29 = int(u_trial29.value)
                trial210 = int(u_trial210.value)
                trial211 = int(u_trial211.value)
                trial212 = int(u_trial212.value)
                trial213 = int(u_trial213.value)
                trial214 = int(u_trial214.value)
                trial215 = int(u_trial215.value)
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
                trial312 = int(u_trial312.value)
                trial313 = int(u_trial313.value)
                trial314 = int(u_trial314.value)
                trial315 = int(u_trial315.value)
                trial41 = int(u_trial41.value)
                trial42 = int(u_trial42.value)
                trial43 = int(u_trial43.value)
                trial44 = int(u_trial44.value)
                trial51 = int(u_trial51.value)
                trial52 = int(u_trial52.value)
                trial53 = int(u_trial53.value)
                trial54 = int(u_trial54.value)
                trial61 = int(u_trial61.value)
                trial62 = int(u_trial62.value)
                trial63 = int(u_trial63.value)
                trial64 = int(u_trial64.value)
                trial65 = int(u_trial65.value)
                trial66 = int(u_trial66.value)
                trial67 = int(u_trial67.value)
                trial71 = int(u_trial71.value)
                trial72 = int(u_trial72.value)
                trial73 = int(u_trial73.value)
                trial74 = int(u_trial74.value)
                trial75 = int(u_trial75.value)
                trial76 = int(u_trial76.value)
                trial77 = int(u_trial77.value)
                trial78 = int(u_trial78.value)
                trial81 = int(u_trial81.value)
                trial82 = int(u_trial82.value)
                trial83 = int(u_trial83.value)
                trial84 = int(u_trial84.value)
                trial85 = int(u_trial85.value)
                trial86 = int(u_trial86.value)
                trial87 = int(u_trial87.value)
                studentdatabasename = f"braille{studentname.title()}{datenow}"
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
                    filename.write("trial24" + ", ")
                    filename.write("trial25" + ", ")
                    filename.write("trial26" + ", ")
                    filename.write("trial27" + ", ")
                    filename.write("trial28" + ", ")
                    filename.write("trial29" + ", ")
                    filename.write("trial210" + ", ")
                    filename.write("trial211" + ", ")
                    filename.write("trial212" + ", ")
                    filename.write("trial213" + ", ")
                    filename.write("trial214" + ", ")
                    filename.write("trial215" + ", ")
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
                    filename.write("trial312" + ", ")
                    filename.write("trial313" + ", ")
                    filename.write("trial314" + ", ")
                    filename.write("trial315" + ", ")
                    filename.write("trial41" + ", ")
                    filename.write("trial42" + ", ")
                    filename.write("trial43" + ", ")
                    filename.write("trial44" + ", ")
                    filename.write("trial51" + ", ")
                    filename.write("trial52" + ", ")
                    filename.write("trial53" + ", ")
                    filename.write("trial54" + ", ")
                    filename.write("trial61" + ", ")
                    filename.write("trial62" + ", ")
                    filename.write("trial63" + ", ")
                    filename.write("trial64" + ", ")
                    filename.write("trial65" + ", ")
                    filename.write("trial66" + ", ")
                    filename.write("trial67" + ", ")
                    filename.write("trial71" + ", ")
                    filename.write("trial72" + ", ")
                    filename.write("trial73" + ", ")
                    filename.write("trial74" + ", ")
                    filename.write("trial75" + ", ")
                    filename.write("trial76" + ", ")
                    filename.write("trial77" + ", ")
                    filename.write("trial78" + ", ")
                    filename.write("trial81" + ", ")
                    filename.write("trial82" + ", ")
                    filename.write("trial83" + ", ")
                    filename.write("trial84" + ", ")
                    filename.write("trial85" + ", ")
                    filename.write("trial86" + ", ")
                    filename.write("trial87" + "\n")
                    filename.write(studentname + ", ")
                    filename.write(date + ", ")
                    filename.write(str(trial11) + ", ")
                    filename.write(str(trial12) + ", ")
                    filename.write(str(trial13) + ", ")
                    filename.write(str(trial14) + ", ")
                    filename.write(str(trial21) + ", ")
                    filename.write(str(trial22) + ", ")
                    filename.write(str(trial23) + ", ")
                    filename.write(str(trial24) + ", ")
                    filename.write(str(trial25) + ", ")
                    filename.write(str(trial26) + ", ")
                    filename.write(str(trial27) + ", ")
                    filename.write(str(trial28) + ", ")
                    filename.write(str(trial29) + ", ")
                    filename.write(str(trial210) + ", ")
                    filename.write(str(trial211) + ", ")
                    filename.write(str(trial212) + ", ")
                    filename.write(str(trial213) + ", ")
                    filename.write(str(trial214) + ", ")
                    filename.write(str(trial215) + ", ")
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
                    filename.write(str(trial312) + ", ")
                    filename.write(str(trial313) + ", ")
                    filename.write(str(trial314) + ", ")
                    filename.write(str(trial315) + ", ")
                    filename.write(str(trial41) + ", ")
                    filename.write(str(trial42) + ", ")
                    filename.write(str(trial43) + ", ")
                    filename.write(str(trial44) + ", ")
                    filename.write(str(trial51) + ", ")
                    filename.write(str(trial52) + ", ")
                    filename.write(str(trial53) + ", ")
                    filename.write(str(trial54) + ", ")
                    filename.write(str(trial61) + ", ")
                    filename.write(str(trial62) + ", ")
                    filename.write(str(trial63) + ", ")
                    filename.write(str(trial64) + ", ")
                    filename.write(str(trial65) + ", ")
                    filename.write(str(trial66) + ", ")
                    filename.write(str(trial67) + ", ")
                    filename.write(str(trial71) + ", ")
                    filename.write(str(trial72) + ", ")
                    filename.write(str(trial73) + ", ")
                    filename.write(str(trial74) + ", ")
                    filename.write(str(trial75) + ", ")
                    filename.write(str(trial76) + ", ")
                    filename.write(str(trial77) + ", ")
                    filename.write(str(trial78) + ", ")
                    filename.write(str(trial81) + ", ")
                    filename.write(str(trial82) + ", ")
                    filename.write(str(trial83) + ", ")
                    filename.write(str(trial84) + ", ")
                    filename.write(str(trial85) + ", ")
                    filename.write(str(trial86) + ", ")
                    filename.write(str(trial87) + ", ")
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
                                trial11,
                                trial12,
                                trial13,
                                trial14,
                                trial21,
                                trial22,
                                trial23,
                                trial24,
                                trial25,
                                trial26,
                                trial27,
                                trial28,
                                trial29,
                                trial210,
                                trial211,
                                trial212,
                                trial213,
                                trial214,
                                trial215,
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
                                trial312,
                                trial313,
                                trial314,
                                trial315,
                                trial41,
                                trial42,
                                trial43,
                                trial44,
                                trial51,
                                trial52,
                                trial53,
                                trial54,
                                trial61,
                                trial62,
                                trial63,
                                trial64,
                                trial65,
                                trial66,
                                trial67,
                                trial71,
                                trial72,
                                trial73,
                                trial74,
                                trial75,
                                trial76,
                                trial77,
                                trial78,
                                trial81,
                                trial82,
                                trial83,
                                trial84,
                                trial85,
                                trial86,
                                trial87,
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
                            "ScreenReaderSkillsProgression.csv",
                            )
                    with open(tmpdir, "a", newline="") as f_setup:
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
                                    trial11,
                                    trial12,
                                    trial13,
                                    trial14,
                                    trial21,
                                    trial22,
                                    trial23,
                                    trial24,
                                    trial25,
                                    trial26,
                                    trial27,
                                    trial28,
                                    trial29,
                                    trial210,
                                    trial211,
                                    trial212,
                                    trial213,
                                    trial214,
                                    trial215,
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
                                    trial312,
                                    trial313,
                                    trial314,
                                    trial315,
                                    trial41,
                                    trial42,
                                    trial43,
                                    trial44,
                                    trial51,
                                    trial52,
                                    trial53,
                                    trial54,
                                    trial61,
                                    trial62,
                                    trial63,
                                    trial64,
                                    trial65,
                                    trial66,
                                    trial67,
                                    trial71,
                                    trial72,
                                    trial73,
                                    trial74,
                                    trial75,
                                    trial76,
                                    trial77,
                                    trial78,
                                    trial81,
                                    trial82,
                                    trial83,
                                    trial84,
                                    trial85,
                                    trial86,
                                    trial87,
                                    ),
                            )
                    conn.commit()
                
                data_entry()
            
            
            def graph(event):
                """

                Graphing

                """
                studentname = u_studentname.value
                conn = sqlite3.connect(dataBasePath)
                df_sql = pd.read_sql_query("SELECT * FROM BRAILLEPROGRESS", conn)
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
                                name="Strong Contractions <br>(AND OF FOR WITH "
                                    "THE)",
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
                                name="Strong Groupsigns <br>(CH GH SH TH WH ED "
                                    "ER OU OW ST AR ING)",
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
                                name="Typeform Indicators <br>(ITALIC, SCRIPT, "
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
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=5,
                        col=2,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
                        tickvals=[0.1, 1, 2, 3],
                        row=7,
                        col=2,
                        )
                fig.update_yaxes(
                        range=[-0.5, 3.5],
                        fixedrange=True,
                        ticktext=["Unable", "Prompted", "Hesitated",
                                "Independent"],
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
                        )
                tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "UEBLiterarySkillsProgression.html",
                        )
                fig.write_html(tmppath)
                fig.show()
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
                        xaxis2_tickformat="%d %b",
                        xaxis3_tickformat="%d %b",
                        template="simple_white",
                        title_text=f"{studentname}: Technical UEB Skills "
                                f"Progression",
                        legend=dict(font=dict(size=10)),
                        )
                tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        "UEBTechnicalSkillsProgression.html",
                        )
                fig.write_html(tmppath)
                fig.show()
            
            
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
                ui.label("PHASE 1: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 1:"').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="1.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial11.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.1 Track Left to Right"'
                        ).tooltip(
                        "1.1 Track Left to Right"
                        )
                ui.number(
                        label="1.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial12.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.2 Track Top to Bottom"'
                        )
                ui.number(
                        label="1.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial13.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.3 Discriminate Shapes"'
                        )
                ui.number(
                        label="1.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial14.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="1.4 Discriminate Braille Characters"'
                        )
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 2: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 2: "').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="2.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial21.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.1 Mangold Progression: G C L"'
                        )
                ui.number(
                        label="2.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial22.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.2 Mangold Progression: D Y"'
                        )
                ui.number(
                        label="2.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial23.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.3 Mangold Progression: A B"'
                        )
                ui.number(
                        label="2.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial24.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.4 Mangold Progression: S"'
                        )
                ui.number(
                        label="2.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial25.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.5 Mangold Progression: W"'
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="2.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial26.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.6 Mangold Progression: P O"'
                        )
                ui.number(
                        label="2.7",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial27.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.7 Mangold Progression: K"'
                        )
                ui.number(
                        label="2.8",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial28.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.8 Mangold Progression: R"'
                        )
                ui.number(
                        label="2.9",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial29.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.9 Mangold Progression: M E"'
                        )
                ui.number(
                        label="2.10",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial210.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.10 Mangold Progression: H"'
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="2.11",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial211.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.11 Mangold Progression: N X"'
                        )
                ui.number(
                        label="2.12",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial212.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.12 Mangold Progression: Z F"'
                        )
                ui.number(
                        label="2.13",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial213.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.13 Mangold Progression: U T"'
                        )
                ui.number(
                        label="2.14",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial214.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.14 Mangold Progression: Q I"'
                        )
                ui.number(
                        label="2.15",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial215.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="2.15 Mangold Progression: V J"'
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 3: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 3: "').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="3.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial31.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.1 Alphabetic Wordsigns"'
                        )
                ui.number(
                        label="3.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial32.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.2 Braille Numbers"'
                        )
                ui.number(
                        label="3.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial33.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.3 Punctuation"'
                        )
                ui.number(
                        label="3.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial34.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.4 Strong Contractions - AND OF FOR WITH '
                        'THE"'
                        )
                ui.number(
                        label="3.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial35.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.5 Strong Groupsigns - CH GH SH TH WH ED '
                        'ER OU OW ST AR ING"'
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="3.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial36.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.6 Strong Wordsigns - CH SH TH WH OU ST"'
                        )
                ui.number(
                        label="3.7",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial37.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.7 Lower Groupsigns - BE CON DIS"'
                        )
                ui.number(
                        label="3.8",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial38.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.8 Lower Groupsigns - EA BB CC FF GG"'
                        )
                ui.number(
                        label="3.9",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial39.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.9 Lower Group/Wordsigns - EN IN"'
                        )
                ui.number(
                        label="3.10",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial310.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.10 Lower Wordsigns - BE HIS WAS WERE"'
                        ).tooltip(
                        "3.10 Lower Wordsigns - BE HIS WAS WERE"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="3.11",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial311.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.11 Dot 5 Contractions"'
                        ).tooltip(
                        "3.11 Dot 5 Contractions"
                        )
                ui.number(
                        label="3.12",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial312.set_value(e.value),
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
                        on_change=lambda e: u_trial313.set_value(e.value),
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
                        on_change=lambda e: u_trial314.set_value(e.value),
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
                        on_change=lambda e: u_trial315.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="3.15 Shortform Words"'
                        ).tooltip(
                        "3.15 Shortform Words"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 4: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 4: "').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="4.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial41.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.1 Grade 1 Indicators"'
                        ).tooltip(
                        "4.1 Grade 1 Indicators"
                        )
                ui.number(
                        label="4.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial42.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.2 Capitals Indicators"'
                        ).tooltip(
                        "4.2 Capitals Indicators"
                        )
                ui.number(
                        label="4.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial43.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.3 Numeric Mode and Spatial Math"'
                        ).tooltip(
                        "4.3 Numeric Mode and Spatial Math"
                        )
                ui.number(
                        label="4.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial44.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="4.4 Typeform Indicators - ITALIC BOLD '
                        'UNDERLINE SCRIPT"'
                        ).tooltip(
                        "4.4 Typeform Indicators - ITALIC BOLD UNDERLINE SCRIPT"
                        )
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 5: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 5: "').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="5.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial51.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="5.1 Page Numbering"'
                        ).tooltip(
                        "5.1 Page Numbering"
                        )
                ui.number(
                        label="5.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial52.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="5.2 Headings"'
                        ).tooltip(
                        "5.2 Headings"
                        )
                ui.number(
                        label="5.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial53.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="5.3 Lists"'
                        ).tooltip("5.3 Lists")
                ui.number(
                        label="5.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial54.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="5.4 Poetry / Drama"'
                        ).tooltip(
                        "5.4 Poetry / Drama"
                        )
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 6: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 6: "').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="6.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial61.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="6.1 Operation and Comparison Signs"'
                        ).tooltip(
                        "6.1 Operation and Comparison Signs"
                        )
                ui.number(
                        label="6.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial62.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="6.2 Grade 1 Mode"'
                        ).tooltip(
                        "6.2 Grade 1 Mode"
                        )
                ui.number(
                        label="6.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial63.set_value(e.value),
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
                        on_change=lambda e: u_trial64.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="6.4 Omission Marks"'
                        ).tooltip(
                        "6.4 Omission Marks"
                        )
                ui.number(
                        label="6.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial65.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="6.5 Shape Indicators"'
                        ).tooltip(
                        "6.5 Shape Indicators"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="6.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial66.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="6.6 Roman Numerals"'
                        ).tooltip(
                        "6.6 Roman Numerals"
                        )
                ui.number(
                        label="6.7",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial67.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="6.7 Fractions"'
                        ).tooltip(
                        "6.7 Fractions"
                        )
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes(" w-[200px]")
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 7: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 7: "').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="7.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial71.set_value(e.value),
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
                        on_change=lambda e: u_trial72.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="7.2 Grade 1 Mode and Fractions"'
                        ).tooltip(
                        "7.2 Grade 1 Mode and Fractions"
                        )
                ui.number(
                        label="7.3",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial73.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="7.3 Advanced Operation and Comparison Signs"'
                        ).tooltip(
                        "7.3 Advanced Operation and Comparison Signs"
                        )
                ui.number(
                        label="7.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial74.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="7.4 Indices"'
                        ).tooltip(
                        "7.4 Indices"
                        )
                ui.number(
                        label="7.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial75.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="7.5 Roots and Radicals"'
                        ).tooltip(
                        "7.5 Roots and Radicals"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="7.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial76.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="7.6 Miscellaneous Shape Indicators"'
                        ).tooltip(
                        "7.6 Miscellaneous Shape Indicators"
                        )
                ui.number(
                        label="7.7",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial77.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="7.7 Functions"'
                        ).tooltip(
                        "7.7 Functions"
                        )
                ui.number(
                        label="7.8",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial78.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="7.8 Greek Letters"'
                        ).tooltip(
                        "7.8 Greek Letters"
                        )
                ui.label(" ").classes("w-[200px]")
                ui.label(" ").classes("w-[200px]")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.label("PHASE 8: ").classes("justify-center items-center")
                ui.input().props('aria-label="PHASE 8:"').classes("sr-only")
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="8.1",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial81.set_value(e.value),
                        ).classes("w-[200px]").props('aria-label="8.1 Functions"')
                ui.number(
                        label="8.2",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial82.set_value(e.value),
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
                        on_change=lambda e: u_trial83.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="8.3 Modifiers: Arrows and Limits"'
                        ).tooltip(
                        "8.3 Modifiers: Arrows and Limits"
                        )
                ui.number(
                        label="8.4",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial84.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="8.4 Probability"'
                        ).tooltip(
                        "8.4 Probability"
                        )
                ui.number(
                        label="8.5",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial85.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="8.5 Calculus: Differentiation"'
                        ).tooltip(
                        "8.5 Calculus: Differentiation"
                        )
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.number(
                        label="8.6",
                        min=0,
                        max=3,
                        format="%.0f",
                        on_change=lambda e: u_trial86.set_value(e.value),
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
                        on_change=lambda e: u_trial87.set_value(e.value),
                        ).classes("w-[200px]").props(
                        'aria-label="8.7 Vertical Bars"'
                        ).tooltip(
                        "8.7 Vertical Bars"
                        )
                ui.label(" ").classes("w-[200px]")
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

    ##########################################################################
    # BRAILLENOTE TOUCH  SKILLS
    ##########################################################################
    @ui.page('/braillenotetouchskills')
    def braillenotetouchskills():
        with theme.frame('- BRAILLENOTE TOUCH PLUS SKILLS -'):
            ui.label('BRAILLENOTE TOUCH PLUS SKILLS').classes('text-h4 text-grey-8')
                        
            def save():
                a=1
            def graph():
                a=1
            def exit():
                a=1
            with ui.row().classes("w-screen no-wrap"):
                ui.label("BRAILLENOTE TOUCH PLUS SKILLS PROGRESSION").classes(
                        "justify-center items-center"
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
                        

    ##########################################################################
    # iOS/iPadOS VOICEOVER  SKILLS
    ##########################################################################
    @ui.page('/iosskills')
    def iosskills():
        with theme.frame('- iOS/iPadOS VOICEOVER SKILLS -'):
            ui.label('iOS/iPadOS VOICEOVER SKILLS').classes('text-h4 text-grey-8')
            with ui.row().classes("w-screen no-wrap"):
                ui.label("iOS/iPadOS VOICEOVER SKILLS PROGRESSION").classes(
                        "justify-center items-center"
                        )
            def save():
                a=1
            def graph():
                a=1
            def exit():
                a=1
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
            
    #########################################################################
    # CVI PROGRESSION
    ##########################################################################
    @ui.page('/cviprogress')
    def cviprogress():
        with theme.frame('- CVI PROGRESSION-'):
            ui.label('CVI PROGRESSION').classes('text-h4 text-grey-8')
            with ui.row().classes("w-screen no-wrap"):
                ui.label("CVI PROGRESSION").classes("justify-center items-center")
            
            def save():
                a=1
            def graph():
                a=1
            def exit():
                a=1
                
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
                


