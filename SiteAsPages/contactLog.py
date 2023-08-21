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

import theme
from helpers import students

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
    