#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers
of students with Visual Impairments
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
from pathlib import Path

from nicegui import app, ui

from appHelpers.helpers import dataBasePath, datenow, USER_DIR, date_fmt
from appHelpers.roster import students
from appTheming import theme


def create() -> None:
    """Creates Session Notes Page"""

    @ui.page("/observations")
    def observations() -> None:
        with theme.frame("- OBSERVATION NOTES -"):
            ui.label("OBSERVATION NOTES").classes("text-h4 text-grey-8")
            # ASSIGN VARIABLES
            u_studentname = ui.select(options=students, value="DonaldChamberlain").classes("hidden")
            date = ui.date().classes("hidden")
            u_observationnotes = ui.textarea().classes("hidden")

            def save(event):
                """
                :param event
                :type event
                """
                studentname = u_studentname.value
                date = datenow
                observationnotes = u_observationnotes.value

                studentdatabasename = f"observationnotes{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    studentdatabasename + ".json",
                )
                observation_dictionary = {
                    "studentname": studentname,
                    "date": datenow,
                    "observationnotes": observationnotes,
                }
                with open(tmppath, "w", encoding="utf-8") as filename:
                    json.dump(observation_dictionary, filename)

                    tmppath = Path(USER_DIR).joinpath("StudentDatabase", "StudentDataFiles", "Filenames.txt")
                with open(tmppath, "a", encoding="utf-8") as filename:
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        studentdatabasename + ".json",
                    )
                    filename.write(f"'{tmppath}'" + "\n")
                    filename.close()
                ui.notify(
                    "Saved successfully!",
                    position="center",
                    type="positive",
                    close_button="OK",
                )

        with ui.row().classes("w-screen no-wrap"):
            ui.label("Observation Notes").classes("justify-center items-center")
        with ui.row().classes("w-screen no-wrap"):
            ui.select(
                options=students,
                with_input=True,
                on_change=lambda e: ui.notify(e.value),
            ).bind_value(
                u_studentname, "value"
            ).classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip("Type Student Name, it will autocomplete as you type")
        with ui.input("Date").classes("w-[300px]").props('aria-label="Date. Please type in date using the YYYY-MM-DD format"').tooltip("Date. Please type in date using the YYYY-MM-DD format") as date:
            with date.add_slot("append"):
                ui.icon("edit_calendar").on("click", lambda: menu.open()).classes("cursor-pointer")
            with ui.menu() as menu:
                ui.date().bind_value(date)
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.textarea(
                label="Input Observation Notes In this Box and Press Save",
                on_change=lambda e: u_observationnotes.set_value(e.value),
            ).classes(
                "v-min-[600px]"
            ).props('cols=200 autogrow outlined aria-label="Please type observation notes" square')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes("text-white")
