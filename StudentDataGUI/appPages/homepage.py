#!/usr/bin/env python3

"""
 Copyright 2025  Michael Ryan Hunsaker, M.Ed., Ph.D.

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
Homepage Module

This module defines the homepage for the StudentDataGUI application.
It serves as the entry point for users, providing navigation to various
features and functionalities.

Purpose
-------
The homepage is designed to be a data collection and instructional tool
for teachers of students with Visual Impairments.
"""

from nicegui import ui
from ..appTheming import theme

def content() -> None:
    """
    Render the homepage content.

    This function defines the layout and structure of the homepage,
    including navigation tabs and instructional labels.

    Returns
    -------
    None
        This function does not return any value. It renders the UI components
        for the homepage.
    """
    with theme.frame("- HOW TO USE THIS APP -"):
        with ui.tabs() as tabs:
            ui.tab("DATA INPUT")
            ui.tab("DATA SUMMARY")
        with ui.tab_panels(tabs, value="DATA INPUT"):
            with ui.tab_panel("DATA INPUT"):
                ui.label("SKILLS PROGRESSIONS").classes(
                    "text-3xl font-bold pl-10"
                ).style('font-family: "Atkinson Hyperlegible"')
                with ui.row().classes("w-screen no-wrap py-4").style(
                    'font-style:normal, font-family: "Atkinson Hyperlegible"'
                ):
                    ui.label("Please Select a Task from the Menu").props(
                        'aria-label="Please Select a Task from the Menu" content-center'
                    ).style(
                        'font-style:normal, font-family: "Atkinson Hyperlegible"'
                    ).classes("text-2xl font-bold pl-10")
