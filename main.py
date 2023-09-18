#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers
of students with Visual Impairments
"""
########################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.
#    #
#    email: hunsakerconsulting@gmail.com
#    #
#                                                                      #
#    Licensed under the Apache License, Version 2.0 (the "License");
#    #
#    you may not use this file except in compliance with the License.
#    #
#    You may obtain a copy of the License at
#    #
#                                                                      #
#    http://www.apache.org/licenses/LICENSE-2.0
#    #
#                                                                      #
#    Unless Required by applicable law or agreed to in writing,
#    software      #
#    distributed under the License is distributed on an "AS IS"
#    BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#    implied. #
#    See the License for the specific language governing permissions
#    and      #
#    limitations under the License.
#    #
########################################################################

import sys

from nicegui import ui
from screeninfo import get_monitors

import abacus
import anecdotalnotes
import braille
import braillenote
import contactlog
import cvi
import homepage
import InstructionalMaterials
import ios
import screenreader
import theme
from helpers import createFolderHierarchy, dataBasePath, warningmessage
from sqlgenerate import (create_connection, createTables)

createFolderHierarchy()
create_connection(dataBasePath)
createTables()
sys.excepthook = warningmessage


########################################################################
# Begin GUI
########################################################################
@ui.page('/')
def index_page() -> None:
    with theme.frame('Student Skills Progressions'):
        homepage.content()


########################################################################
# CONTENT PAGES
########################################################################
contactlog.create()
abacus.create()
anecdotalnotes.create()
braille.create()
braillenote.create()
cvi.create()
ios.create()
screenreader.create()
InstructionalMaterials.create()

########################################################################
# FOOTER
########################################################################
with ui.footer(value=True) as footer:
    with ui.row().classes(
            "w-screen no-wrap justify-center "
            "items-center text-l font-bold"
            ):
        ui.label(
                "Copyright © 2023 Michael Ryan Hunsaker, M.Ed., "
                "Ph.D."
                ).classes("justify-center items-center")
    with ui.row().classes(
            "w-screen no-wrap justify-center "
            "items-centertext-l font-bold"
            ):
        ui.label(
                "Report Bugs or Request Features by emailing "
                "hunsakerconsulting@gmail.com"
                ).classes("justify-center items-center")

########################################################################
# EXECUTE PROGRAM WINDOW
########################################################################
'''Get Monitor Size to allow me to create the app to fill screen without
setting fullscreen=True. 72 is subtracted from the height to
accommodate the
height of my Taskbar'''

monitor = ""
for monitor in get_monitors():
    ScreenResolution = "{str(monitor.width)}x{str(monitor.height)}"

########################################################################
# RUN CALL
########################################################################
ui.run(
        native=True, reload=False, dark=False, title="Student Skills "
                                                     "Progressions", fullscreen=False, window_size=(monitor.width, monitor.height - 72), )
