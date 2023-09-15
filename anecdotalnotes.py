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

import theme
from helpers import (dataBasePath, datenow, students, USER_DIR)
from roster import students


def create() -> None:
    ##########################################################################
    # ANECDOTAL NOTES
    ##########################################################################
    @ui.page('/anecdotalnotes')
    def anecdotalnotes():
        with theme.frame('- ANECDOTAL NOTES -'):
            ui.label('SESSION NOTES').classes('text-h4 text-grey-8')
            # ASSIGN VARIABLES
            u_studentname = ui.select(options=students, value='DonaldChamberlain').classes('hidden')
            date = ui.date().classes('hidden')
            u_anecdotalnotes = ui.textarea().classes('hidden')
            
            def save(event):
                '''
                :param event
                :type event
                '''
                studentname = u_studentname.value
                date = datenow
                anecdotalnotes = u_anecdotalnotes.value
                
                studentdatabasename = (f"anecdotalnotes{studentname.title()}"
                                       f"{datenow}")
                tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", studentname, studentdatabasename + ".json" )
                anecdotal_dictionary = {"studentname": studentname,
                                        "date" : datenow,
                                        "anecdotalnotes" : anecdotalnotes
                                        }
                with open(tmppath, "w") as filename:
                    json.dump(anecdotal_dictionary, filename)
                    
                    tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", "Filenames.txt")
                    filename = open(tmppath, "a")
                    tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", studentname, studentdatabasename + ".txt", )
                    filename.write(f"'{tmppath}'" + "\n")
                    filename.close()
                    tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", "Filenames.txt")
                    filename = open(tmppath, "a")
                    tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", studentname, studentdatabasename + ".txt", )
                    filename.write(f"'{tmppath}'" + "\n")
                    filename.close()
                    list_data = [datenow, anecdotalnotes]
                    tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", studentname, "anecdotalnotes.csv", )
                    os.chdir(USER_DIR)
                    with open(tmppath, "a", newline="") as f_setup:
                        writer_setup = writer(f_setup)
                        writer_setup.writerow(list_data)
                        f_setup.close()
                    ui.notify("Saved successfully!", position='center', type='positive', close_button="OK")


        with ui.row().classes("w-screen no-wrap"):
            ui.label("Anecdotal Notes").classes("justify-center items-center")
        with ui.row().classes("w-screen no-wrap"):
            ui.select(options=students, with_input=True, on_change=lambda e: ui.notify(e.value), ).bind_value(u_studentname, "value").classes("w-[300px]").props(
            'aria-label="Select Student from the Dropdown. It '
            'will '
            'autocomplete as you type"'
            ).tooltip("Type Student Name, it will autocomplete AS you type")
        with ui.input("Date").classes("w-[300px]").props(
                'aria-label="Date. Please type in date using the '
                'YYYY-MM-DD format"'
                ).tooltip("Date. Please type in date using the YYYY-MM-DD format") as date:
            with date.add_slot("append"):
                ui.icon("edit_calendar").on("click", lambda: menu.open()).classes("cursor-pointer")
            with ui.menu() as menu:
                ui.date().bind_value(date)
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.textarea(label='Input Anecdotal Notes In this Box and Press Save', on_change=lambda e: u_anecdotalnotes.set_value(e.value)).classes("h-full h-min-[400px] ").props('cols=80 autogrow outlined aria-label="Please type anecdotal notes" square' )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes("text-white")
