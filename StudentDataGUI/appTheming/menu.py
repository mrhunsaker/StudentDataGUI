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
from nicegui import ui


def menu() -> None:
    """
    Create and display the application menu.

    This function generates and displays a user interface menu using the `ui` module. The menu
    includes various options for navigation within the application, such as accessing the home
    page, contact log, data collection sections (session notes and observations), CVI/NVI
    progress, tactile skills (abacus and braille), technology skills (keyboarding, screen reader,
    braille note touch, iOS VoiceOver), digital literacy, and instructional materials.

    Returns
    -------
    None

    Examples
    --------
    >>> menu()
    """
    with ui.button("Navigation Menu", icon="apps").classes(
        "absolute-right self-center scale=150"
    ).style('font-style:normal, font-family: "Atkinson Hyperlegible"'):
        with ui.menu().classes("w-[250px]") as menu:
            ui.menu_item("HOME", lambda: ui.open("/")).classes(
                replace="text-black"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            ui.separator()
            ui.menu_item("CONTACT LOG", lambda: ui.open("/contactlog")).classes(
                replace="text-black"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("DATA COLLECTION").classes("font-bold").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                )
            ui.menu_item("SESSION NOTES", lambda: ui.open("/sessionnotes")).classes(
                replace="text-black"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            ui.menu_item("OBSERVATIONS", lambda: ui.open("/observations")).classes(
                replace="text-black"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("CVI / NVI").classes("font-bold").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                )
            ui.menu_item("CVI PROGRESS", lambda: ui.open("/cviprogress")).classes(
                replace="text-black"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("TACTILE SKILLS").classes("font-bold").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                )
            ui.menu_item("ABACUS SKILLS", lambda: ui.open("/abacusskills")).classes(
                replace="text-black"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            ui.menu_item("BRAILLE SKILLS", lambda: ui.open("/brailleskills")).classes(
                replace="text-black"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("TECHNOLOGY SKILLS").classes("font-bold").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                )
            ui.menu_item(
                "KEYBOARDING SKILLS", lambda: ui.open("/keyboardingskills")
            ).classes(replace="text-black").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
            ui.menu_item(
                "SCREENREADER SKILLS", lambda: ui.open("/screenreaderskills")
            ).classes(replace="text-black").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
            ui.menu_item(
                "BRAILLENOTE TOUCH SKILLS", lambda: ui.open("/braillenotetouchskills")
            ).classes(replace="text-black").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
            ui.menu_item(
                "iOS/iPadOS VOICEOVER SKILLS", lambda: ui.open("/iosskills")
            ).classes(replace="text-black").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("DIGITAL LITERACY").classes("font-bold").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                )
            ui.menu_item(
                "DIGITAL LITERACY", lambda: ui.open("/digitalliteracy")
            ).classes(replace="text-black").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
            ui.separator()
            with ui.row().classes("justify-center items-center py-2"):
                ui.label("MATERIALS").classes("font-bold").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                )
            ui.menu_item(
                "INSTRUCTIONAL MATERIALS", lambda: ui.open("/instructionalmaterials")
            ).classes(replace="text-black").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
