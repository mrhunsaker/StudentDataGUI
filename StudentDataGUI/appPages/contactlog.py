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
teachers of students with Visual Impairments
"""

import json
from pathlib import Path

from appHelpers.helpers import datenow, USER_DIR
from appHelpers.roster import students
from appTheming import theme
from nicegui import app, ui


def create() -> None:
    ##########################################################################
    # CONTACT LOG
    ##########################################################################
    @ui.page("/contactlog")
    def contactlog() -> None:
        with theme.frame("- COMMUNICATION LOG -"):
            with ui.tabs() as tabs:
                ui.tab("DATA INPUT")
                ui.tab("DATA VISUALIZATION")
            with ui.tab_panels(tabs, value="DATA INPUT"):
                with ui.tab_panel("DATA INPUT"):
                    ui.label("CONTACT LOG").classes("text-h4 text-grey-8").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    )
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
                    u_guardianName = (
                        ui.input()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_contactMethod = ui.radio([
                        "Phone",
                        "Text",
                        "In-Person",
                        "Email",
                    ]).classes("hidden")
                    u_phoneNumber = (
                        ui.input()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_emailAddress = (
                        ui.input()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_contactResponse = (
                        ui.radio([
                            "Answered",
                            "Left Message",
                            "Unable to Leave Message",
                            "Disconnected",
                        ])
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_contactGeneral = (
                        ui.radio([
                            "IEP Related",
                            "Discipline Related",
                            "Student Requested",
                        ])
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_contactSpecific = (
                        ui.radio([
                            "Schedule IEP Meeting",
                            "IEP Team Follow-Up",
                            "Collaborate on Student IEP Goals",
                            "Progress Monitoring Update",
                        ])
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_contactNotes = (
                        ui.textarea()
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
                        today_date = u_today_date
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
                            studentdatabasename + ".json",
                        )
                        contactlog_dictionary = {
                            "studentname": studentname,
                            "date": today_date,
                            "guardianName": guardianName,
                            "contactMethod": contactMethod,
                            "phoneNumber": phoneNumber,
                            "emailAddress": emailAddress,
                            "contactResponse": contactResponse,
                            "contactGeneral": contactGeneral,
                            "contactSpecific": contactSpecific,
                            "contactNotes": contactNotes,
                        }
                        with open(tmppath, "w", encoding="utf-8") as filename:
                            json.dump(contactlog_dictionary, filename)
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
                            filename.write(f"{tmppath}" + "\n")

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
                        ui.label().classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.label("STUDENT INFORMATION").classes(
                            "w-full justify-center items-center font-bold"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
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
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label().classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.label("GUARDIAN INFORMATION").classes(
                            "w-screen justify-center items-center font-bold"
                        )
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.input(
                            label="Guardian Name",
                            value="",
                            on_change=lambda e: u_guardianName.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="Guardian Name"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Guardian Name")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.input(
                            label="Phone Number",
                            value="",
                            on_change=lambda e: u_phoneNumber.set_value(e.value),
                        ).classes("w-[600px]").props('aria-label="Phone Number"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Phone Number")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.input(
                            label="Email Address",
                            value="",
                            on_change=lambda e: u_emailAddress.set_value(e.value),
                        ).classes("w-[600px]").props(
                            'aria-label="Email Address"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Email Address")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label().classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.label("DETAILS OF CONTACT ATTEMPT").classes(
                            "w-screen justify-center items-center font-bold"
                        )
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Contact Method").classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.select(
                            options=["Phone", "Text", "In-Person", "Email"],
                            value="",
                            on_change=lambda e: u_contactMethod.set_value(e.value),
                        ).classes("w-[240px]").props(
                            'aria-label="Contact Method"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Contact Method")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Contact Response").classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
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
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Contact Response")
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label().classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.label("TOPIC OF CONTACT").classes(
                            "w-screen justify-center items-center font-bold"
                        )
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("General Topic").classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.select(
                            options=[
                                "IEP Related",
                                "Discipline Related",
                                "Student Requested",
                            ],
                            value="",
                            on_change=lambda e: u_contactGeneral.set_value(e.value),
                        ).classes("w-[240px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Reason for Contact - General Category"'
                        ).tooltip("Reason for Contact - General Category")
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Specific Topic").classes("w-[150px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.select(
                            options=[
                                "Schedule IEP Meeting",
                                "IEP Team Follow-Up",
                                "Collaborate on Student IEP Goals",
                                "Progress Monitoring Update",
                            ],
                            value="",
                            on_change=lambda e: u_contactSpecific.set_value(e.value),
                        ).classes("w-[240px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Reason for Contact - Specific Reason"'
                        ).tooltip("Reason for Contact - Specific Reason")
                    with ui.row().classes("w-screen no-wrap ").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.textarea(
                            label="Contact Notes (if email please copy/paste email into the box)",
                            value="",
                            on_change=lambda e: u_contactNotes.set_value(e.value),
                        ).classes("w-[640px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Contact Notes (if email please copy/paste email into the box)"'
                        ).tooltip(
                            "Contact Notes (if email please copy/paste email into the box)"
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
            with ui.tab_panels(tabs, value="DATA VISUALIZATION"):
                with ui.tab_panel("DATA VISUALIZATION"):
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.select(
                            options=students,
                            with_input=True,
                            on_change=lambda e: u_studentname.set_value(e.value),
                        ).classes("w-[300px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props(
                            'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
                        ).tooltip("Type Student Name, it will autocomplete AS you type")
        create_ui()