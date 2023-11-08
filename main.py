#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""
########################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                #
#    email: hunsakerconsulting@gmail.com                               #
#                                                                      #
#    Licensed under the Apache License, Version 2.0 (the "License");   #
#    you may not use this file except in compliance with the License.  #
#    You may obtain a copy of the License at                           #
#    http://www.apache.org/licenses/LICENSE-2.0                        #
#                                                                      #
#    Unless Required by applicable law or agreed to in writing,        #
#    software distributed under the License is distributed on an       #
#    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,      #
#    either express or  implied.  See the License for the specific     #
#   language governing permissions and limitations under the License.  #
########################################################################

import os
import sqlite3
import sys
import traceback
from pathlib import Path

from nicegui import ui
from screeninfo import get_monitors

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from appTheming import theme
from appHelpers.helpers import (
    createFolderHierarchy,
    dataBasePath,
    set_start_dir,
    working_dir,
    create_roster,
    USER_DIR,
    datenow,
)
from appHelpers.workingdirectory import create_user_dir
from appHelpers.sqlgenerate import create_connection, createTables

set_start_dir()
working_dir()
create_user_dir()
create_roster()
createFolderHierarchy()
create_connection(dataBasePath)
createTables()

from appPages import abacus
from appPages import sessionnotes
from appPages import braille
from appPages import braillenote
from appPages import contactlog
from appPages import cvi
from appPages import homepage
from appPages import InstructionalMaterials
from appPages import ios
from appPages import observations
from appPages import screenreader
from appPages import digitalliteracy
from appPages import keyboarding


def warningmessage(exception_type, exception_value, exception_traceback) -> None:
    """
    exception_type (_type_): _description_
    exception_value (_type_): _description_
    exception_traceback (_type_): _description_
    """
    i = ""
    message = "Please make sure all fields are selected / filled out properly\n\n"
    tb = traceback.format_exception(
        exception_type, exception_value, exception_traceback
    )
    log_path = Path(USER_DIR).joinpath(
        "StudentDatabase", "errorLogs", f"logfile_{datenow}.log"
    )
    Path.touch(log_path)
    for i in tb:
        message += i
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datenow}\n{i}" + "\n")
        errortype = str(exception_type)
    ui.notify(f"{message}\n{errortype}", type="warn" "ing", close_button="OK")


@ui.page("/")
def index_page() -> None:
    """Opens Homepage for App"""
    with theme.frame("Student Skills Progressions"):
        homepage.content()


contactlog.create()
abacus.create()
sessionnotes.create()
observations.create()
braille.create()
braillenote.create()
cvi.create()
ios.create()
screenreader.create()
InstructionalMaterials.create()
digitalliteracy.create()
keyboarding.create()

with ui.footer(value=True) as footer:
    with ui.row().classes(
        "w-screen no-wrap justify-center items-center text-l font-bold"
    ):
        ui.label(
            "Copyright © 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.\nReport Bugs or Request Features by emailing hunsakerconsulting@gmail.com"
        ).classes("justify-center items-center")

MONITOR = ""


def getresolution() -> str:
    SCREEN = " "
    for SCREEN in get_monitors():
        SCREENRESOLUTION = "{str(SCREEN.width)}x{str(SCREEN.height)}"
    return SCREEN


MONITOR = getresolution()
print(f"SQLite Version is: {sqlite3.sqlite_version}")
print(f"SQLite DB-API Version is: {sqlite3.version}")
print(f"Monitor: \nwidth = {MONITOR.width} \nheight = {MONITOR.height}")
ui.run(
    native=False,
    reload=False,
    dark=False,
    title="Student Skills Progressions",
    fullscreen=False,
    window_size=(MONITOR.width, MONITOR.height - 72),
)
