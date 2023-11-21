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

from appHelpers.helpers import datenow, USER_DIR
from appHelpers.roster import students
from appTheming import theme


def create() -> None:
    """Creates Session Notes Page"""

    @ui.page("/observations")
    def observations() -> None:
        with theme.frame("- DATA COLLECTION -"):
            ui.label("OBSERVATION NOTES").classes("text-h4 text-grey-8").style('font-family: "Atkinson Hyperlegible"')
            # ASSIGN VARIABLES
            u_studentname = ui.select(
                options=students, value="DonaldChamberlain"
            ).classes("hidden").style('font-family: "Atkinson Hyperlegible"')
            u_today_date = ui.date().classes("hidden").style('font-family: "Atkinson Hyperlegible"')
            u_observationnotes = ui.textarea().classes("hidden").style('font-family: "Atkinson Hyperlegible"')

            def save(event):
                """
                :param event
                :type event
                """
                studentname = u_studentname.value
                today_date = u_today_date.value
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
                    "date": today_date,
                    "observationnotes": observationnotes,
                }
                with open(tmppath, "w", encoding="utf-8") as filename:
                    json.dump(observation_dictionary, filename)
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

        def create_ui() -> None:
            """
            Create a GUI layout for entering student information and trial data.

            Returns
            -------
            None

            Notes
            -----
            This function assumes the existence of various UI elements (e.g., `u_studentname`,
            `u_today_date`, ...`), and other variables related to the application.

            The UI consists of several rows with different input elements for selecting a
            student, entering the date, selecting a task, providing a rubric, entering trial
            data, inputting anecdotal notes, and buttons for saving and exiting.

            Examples
            --------
            >>> create_ui()
            >>> # GUI layout created with various input elements and buttons.
            >>> # Users can interact with the UI to enter student information and trial data.

            See Also
            --------
            Some related functions or classes that might be useful.

            """
            with ui.row().classes("w-screen no-wrap py-4").style('font-family: "Atkinson Hyperlegible"'):
                ui.select(
                    options=students,
                    with_input=True,
                    on_change=lambda e: u_studentname.set_value(e.value),).classes("w-[300px]").style('font-family: "Atkinson Hyperlegible"').props(
                    'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
                ).tooltip("Type Student Name, it will autocomplete AS you type")
                ui.date(
                    value="f{datenow}",
                    on_change=lambda e: u_today_date.set_value(e.value),
                ).classes("w-1/2").style('font-family: "Atkinson Hyperlegible"')
            with ui.row().classes("w-screen no-wrap py-4").style('font-family: "Atkinson Hyperlegible"'):
                ui.textarea(
                    label="Input Observation Notes In this Box and Press Save",
                    on_change=lambda e: u_observationnotes.set_value(e.value),
                ).classes("v-min-[600px]").style('font-family: "Atkinson Hyperlegible"').props(
                    'cols=200 autogrow outlined aria-label="Please type observation notes" square'
                )
            with ui.row().classes("w-screen no-wrap py-4").style('font-family: "Atkinson Hyperlegible"'):
                ui.button("SAVE", color="#172554", on_click=save).classes("text-white").style('font-family: "Atkinson Hyperlegible"')
                ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                    "text-white"
                )

        create_ui()
