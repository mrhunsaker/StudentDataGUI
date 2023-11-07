#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""
#########################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                 #
#    email: hunsakerconsulting@gmail.com                                #
#                                                                       #
#                                                                       #
#    Licensed under the Apache License, Version 2.0 (the "License");    #
#    you may not use this file except in compliance with the License.   #
#    You may obtain a copy of the License at                            #
#    http://www.apache.org/licenses/LICENSE-2.0                         #
#                                                                       #
#    Unless Required by applicable law or agreed to in writing,         #
#    software distributed under the License is distributed on an        #
#    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,       #
#    either express or  implied.  See the License for the specific      #
#   language governing permissions and limitations under the License.   #
#########################################################################

from contextlib import contextmanager
from pathlib import Path 
from nicegui import ui

from appTheming.menu import menu
from appHelpers.helpers import ROOT_DIR


@contextmanager
def frame(navtitle: str):
    """Custom page frame to share the same styling and behavior
    across all pages"""
    ui.colors(
            primary="#183969", secondary="#bed2e3", positive="#ffca58", accent="#cfcac1"
            )
    '''ui.colors(
            primary="#ffc8dd", secondary="#cdb4db", accent="#bde0fe", positive="#a2d2ff"
            )'''
    with ui.header().classes("justify-between text-black"):
        dsd_icon=Path('dsd-mark-white.png')
        ui.element(dsd_icon)
        with ui.row().classes("no-wrap text-l font-bold text-black"):
            ui.label(navtitle).classes("no-wrap text-2xl text-white font-bold ")
        with ui.row().classes("no-wrap text-l font-bold text-black"):
            menu()
    with ui.column().classes(""):
        yield
    ##############################################################################
    # FOOTER
    ##############################################################################
    with ui.footer(value=True) as footer:
        with ui.row().classes(
                "w-screen no-wrap justify-center items-center text-l font-bold text-white"
                ):
            ui.label("Copyright © 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.").classes(
                    "justify-center items-center "
                    )
        with ui.row().classes(
                "w-screen no-wrap justify-center items-center text-l font-bold text-white"
                ):
            ui.label(
                    "Report Bugs or Request Features by emailing hunsakerconsulting@gmail.com"
                    ).classes("justify-center items-center")
