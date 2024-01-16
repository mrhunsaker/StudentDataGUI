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
import sqlite3
from pathlib import Path

from appHelpers.helpers import dataBasePath, datenow, USER_DIR
from appHelpers.roster import students
from appTheming import theme
from nicegui import app, ui


def create() -> None:
    ##########################################################################
    # CONTACT LOG
    ##########################################################################
    @ui.page("/keyboardingskills")
    def keyboardingskills() -> None:
        with theme.frame("- TECHNOLOGY SKILLS -"):
            with ui.tabs() as tabs:
                ui.tab("DATA INPUT")
                ui.tab("DATA VISUALIZATION")
            with ui.tab_panels(tabs, value="DATA INPUT"):
                with ui.tab_panel("DATA INPUT"):
                    ui.label("Keyboarding Skills").classes("text-h4 text-grey-8").style(
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
                    u_keyboarding_program = (
                        ui.radio([
                            "Typio",
                            "TypeAbility",
                            "APH Typer",
                            "Typing Club",
                            "MonkeyType",
                            "Custom Assignment",
                        ])
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_topic_covered = (
                        ui.radio([
                            "Home Row",
                            "Top Row",
                            "Bottom Row",
                            "Numbers",
                            "Modifier Keys",
                            "F-Keys",
                            "Shortcut Keystrokes",
                        ])
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_typing_speed = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                    )
                    u_typing_accuracy = (
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
                        keyboarding_program = u_keyboarding_program.value
                        topic_covered = u_topic_covered.value
                        typing_speed = u_typing_speed.value
                        typing_accuracy = u_typing_accuracy.value

                        studentdatabasename = f"contact{studentname.title()}{datenow}"
                        tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase",
                            "StudentDataFiles",
                            studentname,
                            studentdatabasename + ".json",
                        )
                        keyboarding_dictionary = {
                            "studentname": studentname,
                            "date": today_date,
                            "KeyboardingProgram": keyboarding_program,
                            "TopicCovered": topic_covered,
                            "TypingSpeed": typing_speed,
                            "TypingAccuracy": typing_accuracy,
                        }
                        with open(tmppath, "w", encoding="utf-8") as filename:
                            json.dump(keyboarding_dictionary, filename)
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

                        # noinspection SqlResolve
                        def data_entry():
                            """
                            Write progress data to the database.

                            Connects to the SQLite database specified by `dataBasePath` and inserts a new row
                            into the appropriate table with the provided abacus progress data.

                            Parameters
                            ----------
                            None

                            Returns
                            -------
                            None

                            Notes
                            -----
                            This function assumes the existence of variables such as `dataBasePath`,
                            `studentname`, `today_date`,  and  `sqlite3`

                            The function establishes a connection to the database, creates a cursor, executes an
                            SQL INSERT command with the abacus progress data, commits the changes, and notifies
                            the user of successful data entry.

                            Examples
                            --------
                            >>> data_entry()
                            >>> # Progress data successfully written to the database.
                            >>> # The user is notified of successful data entry.

                            See Also
                            --------
                            Some related functions or classes that might be useful.

                            """
                            conn = sqlite3.connect(dataBasePath)
                            c = conn.cursor()
                            c.execute(
                                """INSERT INTO KEYBOARDING (
                                                        STUDENTNAME,
                                                        DATE,
                                                        PROGRAM,
                                                        TOPIC,
                                                        SPEED,
                                                        ACCURACY
                                                        )
                                                        VALUES (
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?,
                                                            ?
                                                            )""",
                                (
                                    studentname,
                                    today_date,
                                    keyboarding_program,
                                    topic_covered,
                                    typing_speed,
                                    typing_accuracy,
                                ),
                            )
                            conn.commit()
                            ui.notify(
                                "Saved successfully!",
                                position="center",
                                type="positive",
                                close_button="OK",
                            )

                        data_entry()

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
                        ui.label().classes("w-[50px]").style(
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
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Keyboarding Program").classes("w-[50px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.select(
                            options=[
                                "Typio",
                                "TypeAbility",
                                "APH Typer",
                                "Typing Club",
                                "MonkeyType",
                                "Custom Assignment",
                            ],
                            value="",
                            on_change=lambda e: u_keyboarding_program.set_value(
                                e.value
                            ),
                        ).classes("w-[240px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).props('aria-label="Keyboarding Program"').tooltip(
                            "Keyboarding Program"
                        )
                    with ui.row().classes("w-screen no-wrap py-4").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Topic Covered").classes("w-[50px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.select(
                            options=[
                                "Home Row",
                                "Top Row",
                                "Bottom Row",
                                "Numbers",
                                "Modifier Keys",
                                "F-Keys",
                                "Shortcut Keystrokes",
                            ],
                            value="",
                            on_change=lambda e: u_topic_covered.set_value(e.value),
                        ).classes("w-[240px]").props(
                            'aria-label="Topic Covered"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Topic Covered")
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Typing Speed").classes("w-[50px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            min=0,
                            max=150,
                            format="%.0f",
                            label="Typing Speed",
                            value="",
                            on_change=lambda e: u_typing_speed.set_value(e.value),
                        ).classes("w-[240px]").props('aria-label="Typing Speed"').style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Typing Speed")
                    with ui.row().classes("w-screen no-wrap").style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ):
                        ui.label("Typing Speed").classes("w-[50px]").style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            min=0,
                            max=100,
                            format="%.0f",
                            label="Typing Accuracy",
                            value="",
                            on_change=lambda e: u_typing_accuracy.set_value(e.value),
                        ).classes("w-[240px]").props(
                            'aria-label="Typing Accuracy"'
                        ).style(
                            'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ).tooltip("Typing Accuracy")
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
                    with ui.dialog() as dialog, ui.card():
                        studentname = u_studentname.value
                        dataBasePath = Path(USER_DIR).joinpath(
                            "StudentDatabase", "students.db"
                        )
                        conn = sqlite3.connect(dataBasePath)
                        df_sql = pd.read_sql_query("SELECT * FROM ABACUSPROGRESS", conn)
                        df_student = df_sql[df_sql.STUDENTNAME == studentname]
                        print(df_student)
                        conn.close()
                        df = df_student.drop(columns=["ID", "STUDENTNAME"])
                        print(df)
                        df = df.rename(columns={"DATE": "date"})
                        df["date"] = df["date"].astype("string")
                        df["date"] = pd.to_datetime(df["date"], format=date_fmt)
                        df = df.set_index("date")
                        print("Abacus Skills Progression")
                        print(df)
                        df = df.sort_values(by="date")
                        mu, sigma = 0, 0.1
                        noise = np.random.normal(
                            mu, sigma, [len(df.index), len(df.columns)]
                        )
                        df_noisy = df + noise
                        abacustable = ui.table(
                            columns=[
                                {"name": col,
                                 "label": col,
                                 "field": col,
                                 "headerClasses": "border-b border-secondary",
                                 "align": 'left'}
                                for col in df.columns
                            ],
                            rows=df.to_dict("records"), pagination={'rowsPerPage': 10}
                        ).style("font-family: JetBrainsMono; background-color: #f5f5f5").classes('my-table')
                        abacustable.add_slot('body-cell', '''
                                <q-td key="Days_Since_Last" :props="props">
                                <q-badge :color="props.value  <= 0 ? 'red' : props.value <= 1 ? 'orange' : props.value <= 2 ? 'yellow' :  'green'" text-color="black" outline>
                                    {{ props.value }}
                                </q-badge>
                                </q-td>
                                ''')
                        abacustable.visible = True
                        ui.button('Close', on_click=dialog.close)

                    with ui.row().classes("w-screen no-wrap py-4").style(
                                'font-style:normal, font-family: "Atkinson Hyperlegible"'
                        ):
                        ui.button('Show Data', on_click=dialog.open)