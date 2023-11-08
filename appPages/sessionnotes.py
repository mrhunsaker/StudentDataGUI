#!/usr/bin/env python3

"""
 Copyright 2023  Michael Ryan Hunsaker, M.Ed., Ph.D.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """

# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers
of students with Visual Impairments
"""

import json
from pathlib import Path

from nicegui import app, ui

from appHelpers.helpers import datenow, tasks, USER_DIR
from appHelpers.roster import students
from appTheming import theme


def create() -> None:
    """Creates Session Notes Page"""

    @ui.page("/sessionnotes")
    def sessionnotes() -> None:
        with theme.frame("- DATA COLLECTION -"):
            ui.label("SESSION NOTES").classes("text-h4 text-grey-8")
            # ASSIGN VARIABLES
            u_studentname = ui.select(
                options=students, value="DonaldChamberlain"
            ).classes("hidden")
            u_today_date = ui.date().classes("hidden")
            u_tasks = ui.select(options=tasks, value="Choose a Task").classes("hidden")
            u_anecdotalnotes = ui.textarea().classes("hidden")
            u_trial01 = ui.number().classes("hidden")
            u_trial02 = ui.number().classes("hidden")
            u_trial03 = ui.number().classes("hidden")
            u_trial04 = ui.number().classes("hidden")
            u_trial05 = ui.number().classes("hidden")
            u_trial06 = ui.number().classes("hidden")
            u_trial07 = ui.number().classes("hidden")
            u_trial08 = ui.number().classes("hidden")
            u_trial09 = ui.number().classes("hidden")
            u_trial10 = ui.number().classes("hidden")
            u_trial11 = ui.number().classes("hidden")

            def save(event):
                """
                :param event
                :type event
                """
                studentname = u_studentname.value
                today_date = u_today_date.value
                anecdotalnotes = u_anecdotalnotes.value
                task = u_tasks.value
                trial01 = (str(int(u_trial01.value)),)
                trial02 = (str(int(u_trial02.value)),)
                trial03 = (str(int(u_trial03.value)),)
                trial04 = (str(int(u_trial04.value)),)
                trial05 = (str(int(u_trial05.value)),)
                trial06 = (str(int(u_trial06.value)),)
                trial07 = (str(int(u_trial07.value)),)
                trial08 = (str(int(u_trial08.value)),)
                trial09 = (str(int(u_trial09.value)),)
                trial10 = (str(int(u_trial10.value)),)
                trial11 = str(int(u_trial11.value))

                studentdatabasename = f"anecdotalnotes{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    studentdatabasename + ".json",
                )
                anecdotal_dictionary = {
                    "studentname": studentname,
                    "date": today_date,
                    "anecdotalnotes": anecdotalnotes,
                    "trial 01": trial01,
                    "trial 02": trial02,
                    "trial 03": trial03,
                    "trial 04": trial04,
                    "trial 05": trial05,
                    "trial 06": trial06,
                    "trial 07": trial07,
                    "trial 08": trial08,
                    "trial 09": trial09,
                    "trial 10": trial10,
                    "trial 11": trial11,
                }
                with open(tmppath, "w", encoding="utf-8") as filename:
                    json.dump(anecdotal_dictionary, filename)

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
                    filename.close()
                    ui.notify(
                        "Saved successfully!",
                        position="center",
                        type="positive",
                        close_button="OK",
                    )

        # GUI Input
        with ui.row().classes("w-screen no-wrap"):
            ui.select(
                options=students,
                with_input=True,
                on_change=lambda e: ui.notify(e.value),
            ).bind_value(u_studentname, "value").classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip("Type Student Name, it will autocomplete as you type")
            ui.date(
                value="f{datenow}", on_change=lambda e: u_today_date.set_value(e.value)
            ).classes("w-1/2")
        with ui.row().classes("w-screen no-wrap"):
            ui.select(
                options=tasks, with_input=True, on_change=lambda e: ui.notify(e.value)
            ).bind_value(u_tasks, "value").classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip("Type Taske, it will autocomplete as you type")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label(
                "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"
            ).props(
                'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
            )
            ui.input().props(
                'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
            ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Trial 1",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial01.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 1"')
            ui.number(
                label="Trial 2",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial02.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 2"')
            ui.number(
                label="Trial 3",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial03.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 3"')
            ui.number(
                label="Trial 4",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial04.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 4" ')
            ui.number(
                label="Trial 5",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial05.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 5" ')
            ui.number(
                label="Trial 6",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial06.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 6" ')
            ui.number(
                label="Trial 7",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial07.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 7" ')
            ui.number(
                label="Trial 8",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial08.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 8" ')
            ui.number(
                label="Trial 9",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial09.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 9" ')
            ui.number(
                label="Trial 10",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial10.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 10" ')
            ui.number(
                label="Trial 11",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_trial11.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="Trial 11" ')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.textarea(
                label="Input Anecdotal Notes In this Box and Press Save",
                on_change=lambda e: u_anecdotalnotes.set_value(e.value),
            ).classes("h-full h-min-[400px]").props(
                'cols=80 autogrow outlined aria-label="Please type anecdotal notes" square'
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                "text-white"
            )
