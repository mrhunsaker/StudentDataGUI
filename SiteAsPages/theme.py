#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for teachers
of students with Visual Impairments
"""
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                       #
#    email: hunsakerconsulting@gmail.com                                      #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");          #
#    you may not use this file except in compliance with the License.         #
#    You may obtain a copy of the License at                                  #
#                                                                             #
#    http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                             #
#    Unless Required by applicable law or agreed to in writing, software      #
#    distributed under the License is distributed on an "AS IS" BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
#    See the License for the specific language governing permissions and      #
#    limitations under the License.                                           #
###############################################################################

from contextlib import contextmanager
from menu import menu
from nicegui import ui


@contextmanager
def frame(navtitle: str):
    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header().classes('justify-between text-white'):
        with ui.row().classes("no-wrap text-l font-bold"):
            ui.label(navtitle)
        with ui.row().classes("no-wrap text-l font-bold"):
            menu()
    with ui.column().classes(''):
        yield
    ##############################################################################
    # FOOTER
    ##############################################################################
    with ui.footer(value=True) as footer:
        with ui.row().classes(
                "w-screen no-wrap justify-center items-center text-l font-bold"
                ):
            ui.label(
                    "Copyright © 2023 Michael Ryan Hunsaker, M.Ed., Ph.D."
                    ).classes(
                    "justify-center items-center"
                    )
        with ui.row().classes(
                "w-screen no-wrap justify-center items-centertext-l font-bold"
                ):
            ui.label(
                    "Report Bugs or Request Features by emailing "
                    "hunsakerconsulting@gmail.com"
                    ).classes("justify-center items-center")