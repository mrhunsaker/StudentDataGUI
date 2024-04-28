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

from appHelpers.helpers import datenow, USER_DIR, task_domains
from appHelpers.roster import students
from appTheming import theme
from nicegui import app, ui


def create() -> None:
    """Creates Session Notes Page"""

    @ui.page("/sessionnotes")
    def sessionnotes() -> None:
        with theme.frame("- DATA COLLECTION -"):
            with ui.tabs() as tabs:
                ui.tab("DATA INPUT")
                ui.tab("DATA VISUALIZATION")
            with ui.tab_panels(tabs, value="DATA INPUT"):
                with ui.tab_panel("DATA INPUT"):
                    ui.label("SESSION NOTES").classes("text-h4 text-grey-8").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    )
                    # ASSIGN VARIABLES
                    u_studentname = (
                        ui.select(options=students, value="DonaldChamberlain")
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_today_date = (
                        ui.date()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_tasks = (
                        ui.select(options=[""], value="Choose a Task")
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_anecdotalnotes = (
                        ui.textarea()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial01 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial02 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial03 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial04 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial05 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial06 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial07 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial08 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial09 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial10 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_trial11 = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )

                    def save(event):
                        """
                        Save data for a student.

                        Parameters
                        ----------
                        event : SomeEventType
                            The event triggering the save function.

                        Returns
                        -------
                        None

                        Notes
                        -----
                        This function assumes the existence of various UI elements (e.g., `u_studentname`,
                        `u_today_date`, ...), `datenow`, `json`,
                        `Path`, and other variables related to the application.

                        The function extracts abacus trial data and student information from UI elements,
                        creates a dictionary with this data, and saves it as a JSON file in the student's
                        directory within the "StudentDataFiles" folder. The filename is constructed based
                        on the student's name and the current date.

                        The function also appends the filename to a "Filenames.txt" file for reference.

                        Examples
                        --------
                        >>> save(some_event)
                        >>> # Trial data and student information saved successfully.
                        >>> # The data is stored in a JSON file named based on the student's name and date.

                        See Also
                        --------
                        Some related functions or classes that might be useful.

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
                        trial11 = (str(int(u_trial11.value)),)

                        studentdatabasename = (
                            f"anecdotalnotes{studentname.title()}{datenow}"
                        )
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
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Student")
                        ui.select(
                            options=students,
                            with_input=True,
                            on_change=lambda e: u_studentname.set_value(e.value),
                        ).classes("w-[300px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
                        ).tooltip("Type Student Name, it will autocomplete AS you type")
                        ui.date(
                            value="f{datenow}",
                            on_change=lambda e: u_today_date.set_value(e.value),
                        ).classes("w-1/2").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Task Domain")
                        task_domain = (
                            ui.select(
                                options=list(task_domains.keys()),
                                with_input=True,
                                on_change=lambda e: specific_task.set_options(
                                    task_domains.get(e.value, [""])
                                ),
                            )
                            .classes("w-[300px]")
                            .style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                            )
                            .props(
                                'aria-label="Select Task Domain from the Dropdown. It will autocomplete as you type"'
                            )
                            .tooltip(
                                "Type Task Domain, it will autocomplete as you type"
                            )
                        )
                        ui.label("Specific Task")
                        specific_task = (
                            ui.select(
                                options=[""],
                                with_input=True,
                                on_change=lambda e: u_tasks.set_value(e.value),
                            )
                            .classes("w-[300px]")
                            .style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                            )
                            .props(
                                'aria-label="Select Task from the Dropdown. It will autocomplete as you type"'
                            )
                            .tooltip("Type Task, it will autocomplete as you type")
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label(
                            "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"
                        ).props(
                            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
                        )
                        ui.input().props(
                            'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
                        ).classes("sr-only").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="Trial 1",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial01.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 1"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                            ui.number(
                            label="Trial 2",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial02.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 2"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                            ui.number(
                            label="Trial 3",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial03.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 3"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="Trial 4",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial04.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 4" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.number(
                            label="Trial 5",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial05.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 5" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.number(
                            label="Trial 6",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial06.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 6" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.number(
                            label="Trial 7",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial07.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 7" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.number(
                            label="Trial 8",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial08.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 8" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.number(
                            label="Trial 9",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial09.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 9" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.number(
                            label="Trial 10",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial10.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 10" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.number(
                            label="Trial 11",
                            min=0,
                            max=3,
                            format="%.0f",
                            on_change=lambda e: u_trial11.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Trial 11" ').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.textarea(
                            label="Input Anecdotal Notes In this Box and Press Save",
                            on_change=lambda e: u_anecdotalnotes.set_value(e.value),
                        ).classes("h-full h-min-[400px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'cols=80 autogrow outlined aria-label="Please type anecdotal notes" square'
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.button("SAVE", color="#172554", on_click=save).classes(
                            "text-white"
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.button(
                            "EXIT", color="#172554", on_click=app.shutdown
                        ).classes("text-white")

        create_ui()
