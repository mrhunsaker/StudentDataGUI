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

from nicegui import app, ui

from appHelpers.helpers import datenow, USER_DIR
from appHelpers.roster import students
from appTheming import theme


def create() -> None:
    ##########################################################################
    # CONTACT LOG
    ##########################################################################
    @ui.page("/keyboardingskills")
    def keyboardingskills() -> None:
        with theme.frame("- TECHNOLOGY SKILLS -"):
            ui.label("Keyboarding Skills").classes("text-h4 text-grey-8")
            u_studentname = ui.select(
                options=students, value="DonaldChamberlain"
            ).classes("hidden")

            u_today_date = ui.date().classes("hidden")
            u_keyboarding_program = ui.radio(["Typio", "TypeAbility", "APH Typer", "Typing Club", "MonkeyType", "Custom Assignment"]).classes(
                "hidden"
            )
            u_topic_covered = ui.radio(["Home Row", "Top Row", "Bottom Row", "Numbers", "Modifier Keys","F-Keys", "Shortcut Keystrokes"]).classes(
                "hidden"
            )
            u_typing_speed = ui.number().classes("hidden")
            u_typing_accuracy = ui.number().classes("hidden")

            def save(event):
                """
                :param event:
                :type event:
                """
                studentname = u_studentname.value
                today_date = u_today_date
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
                    """ """
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
                        typing_accuracy
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

        # GUI Input
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
            ).bind_value(u_studentname, "value").classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip("Type Student Name, it will autocomplete AS you type")
            ui.date(
                value="f{datenow}", on_change=lambda e: u_today_date.set_value(e.value)
            ).classes("w-1/2")
        with ui.row().classes("w-screen no-wrap"):
            ui.label("Keyboarding Program").classes("w-[50px]")
            ui.select(
                options=["Typio", "TypeAbility", "APH Typer", "Typing Club", "MonkeyType", "Custom Assignment"],
                value="",
                on_change=lambda e: u_keyboarding_program.set_value(e.value),
            ).classes("w-[240px]").props('aria-label="Keyboarding Program"').tooltip(
                "Keyboarding Program"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Topic Covered").classes("w-[50px]")
            ui.select(
                options=[
                    "Home Row", "Top Row", "Bottom Row", "Numbers", "Modifier Keys","F-Keys", "Shortcut Keystrokes"
                ],
                value="",
                on_change=lambda e: u_topic_covered.set_value(e.value),
            ).classes("w-[240px]").props('aria-label="Topic Covered"').tooltip(
                "Topic Covered"
            )
        with ui.row().classes("w-screen no-wrap"):
            ui.label("Typing Speed").classes("w-[50px]")
            ui.number(
                min=0,
                max=150,
                format="%.0f",
                label="Typing Speed",
                value="",
                on_change=lambda e: u_typing_speed.set_value(e.value),
            ).classes("w-[240px]").props(
                'aria-label="Typing Speed"'
            ).tooltip("Typing Speed")
        with ui.row().classes("w-screen no-wrap"):
            ui.label("Typing Speed").classes("w-[50px]")
            ui.number(
                min=0,
                max=100,
                format="%.0f",
                label = "Typing Accuracy",
                value="",
                on_change=lambda e: u_typing_accuracy.set_value(e.value),
            ).classes("w-[240px]").props(
                'aria-label="Typing Accuracy"'
            ).tooltip("Typing Accuracy")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                "text-white"
            )
