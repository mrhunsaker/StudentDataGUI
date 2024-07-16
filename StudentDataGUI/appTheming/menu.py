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

import os
from contextlib import contextmanager
from pathlib import Path
from nicegui import ui, app


def create_sidebar():
    with ui.left_drawer(value=True).style('background-color: #f0f0f0') as left_drawer:
        ui.button('CONTACT LOG', on_click=lambda: ui.open('/contactlog')).classes('w-full')
        ui.separator()
        ui.label('DATA COLLECTION').classes('font-bold text-center')
        ui.button('SESSION NOTES', on_click=lambda: ui.open('/sessionnotes')).classes('w-full')
        ui.button('OBSERVATIONS', on_click=lambda: ui.open('/observations')).classes('w-full')
        ui.separator()
        ui.label('CVI / NVI').classes('font-bold text-center')
        ui.button('CVI PROGRESS', on_click=lambda: ui.open('/cviprogress')).classes('w-full')
        ui.separator()
        ui.label('TACTILE SKILLS').classes('font-bold text-center')
        ui.button('ABACUS SKILLS', on_click=lambda: ui.open('/abacusskills')).classes('w-full')
        ui.button('BRAILLE SKILLS', on_click=lambda: ui.open('/brailleskills')).classes('w-full')
        ui.separator()
        ui.label('TECHNOLOGY SKILLS').classes('font-bold text-center')
        ui.button('KEYBOARDING SKILLS', on_click=lambda: ui.open('/keyboardingskills')).classes('w-full')
        ui.button('SCREENREADER SKILLS', on_click=lambda: ui.open('/screenreaderskills')).classes('w-full')
        ui.button('BRAILLENOTE TOUCH SKILLS', on_click=lambda: ui.open('/braillenotetouchskills')).classes('w-full')
        ui.button('iOS/iPadOS VOICEOVER SKILLS', on_click=lambda: ui.open('/iosskills')).classes('w-full')
        ui.separator()
        ui.label('DIGITAL LITERACY').classes('font-bold text-center')
        ui.button('DIGITAL LITERACY', on_click=lambda: ui.open('/digitalliteracy')).classes('w-full')
        ui.separator()
        ui.label('MATERIALS').classes('font-bold text-center')
        ui.button('INSTRUCTIONAL MATERIALS', on_click=lambda: ui.open('/instructionalmaterials')).classes('w-full')
    return left_drawer

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
    def menu():
        create_sidebar()
        ui.button('Navigation Menu', on_click=lambda: left_drawer.toggle()).classes('absolute-right self-center').style('font-family: "Atkinson Hyperlegible"')
