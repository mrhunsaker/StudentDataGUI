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
import sys
import traceback
from pathlib import Path
import logging

from nicegui import ui
from screeninfo import get_monitors, ScreenInfoError

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from .appTheming import theme
from .appHelpers.helpers import (
    createFolderHierarchy,
    database_dir,
    dataBasePath,
    set_start_dir,
    working_dir,
    create_roster,
    USER_DIR,
    datenow,
)

from .appHelpers.sqlgenerate import create_connection, create_tables, initialize_database
import logging

set_start_dir()

# Configure logging
log_path = Path(database_dir).joinpath("StudentDatabase", "errorLogs", f"logfile_{datenow}.log")
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.debug(f"Resolved database_dir: {database_dir}")
createFolderHierarchy()
initialize_database()

from .appPages import abacus
from .appPages import sessionnotes
from .appPages import braille
from .appPages import braillenote
from .appPages import contactlog
from .appPages import cvi
from .appPages import homepage
from .appPages import InstructionalMaterials
from .appPages import ios
from .appPages import observations
from .appPages import screenreader
from .appPages import digitalliteracy
from .appPages import keyboarding


def warningmessage(exception_type, exception_value, exception_traceback) -> None:
    """
    Log an error message and display a warning notification.

    Parameters
    ----------
    exception_type : type
        The type of the exception.
    exception_value : Exception
        The value of the exception.
    exception_traceback : traceback.TracebackType
        The traceback object containing information about the exception.

    Returns
    -------
    None

    Examples
    --------
    >>> try:
    ...     # Code that may raise an exception
    ...     result = 1 / 0
    ... except Exception as e:
    ...     warningmessage(type(e), e, traceback.extract_tb(e.__traceback__))
    """
    i = ""
    message = "Please make sure all fields are selected / filled out properly\n\n"
    tb = traceback.format_exception(
        exception_type, exception_value, exception_traceback
    )
    log_path = Path(database_dir).joinpath(
        "StudentDatabase", "errorLogs", f"logfile_{datenow}.log"
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    for i in tb:
        message += i
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datenow}\n{i}" + "\n")
        errortype = str(exception_type)
    ui.notify(f"{message}\n{errortype}", type="warn" "ing", close_button="OK")


@ui.page("/")
def index_page() -> None:
    """
    Opens the homepage for the app.

    This function initializes the homepage of the app by displaying the main
    homepage content with instructions and navigation.

    Returns
    -------
    None

    Examples
    --------
    >>> index_page()
    """
    with theme.frame("Student Skills Progressions"):
        homepage.content()


def initialize_ui():
    """Initialize global UI components after NiceGUI is ready."""
    # Import the page modules to register their routes
    import StudentDataGUI.appPages.contactlog
    import StudentDataGUI.appPages.abacus
    import StudentDataGUI.appPages.sessionnotes
    import StudentDataGUI.appPages.observations
    import StudentDataGUI.appPages.braille
    import StudentDataGUI.appPages.braillenote
    import StudentDataGUI.appPages.cvi
    import StudentDataGUI.appPages.ios
    import StudentDataGUI.appPages.screenreader
    import StudentDataGUI.appPages.InstructionalMaterials
    import StudentDataGUI.appPages.digitalliteracy
    import StudentDataGUI.appPages.keyboarding

    # Create global footer that appears on all pages
    with ui.footer(value=True) as footer:
        with ui.row().classes(
            "w-screen no-wrap justify-center items-center text-l font-bold"
        ):
            ui.label(
                "Copyright © 2025 Michael Ryan Hunsaker, M.Ed., Ph.D.\nReport Bugs or Request Features by emailing hunsakerconsulting@gmail.com"
            ).classes("justify-center items-center text-lg").style(
                'font-family: "Atkinson Hyperlegible"'
            )

MONITOR = ""

def main():
    """Main application entry point."""
    # Initialize UI components
    initialize_ui()

    # Start the server
    ui.run(
        native=False,
        reload=False,
        dark=False,
        title="Student Skills Progressions",
        fullscreen=False,
        host=os.getenv("NICEGUI_HOST", "127.0.0.1"),
        port=int(os.getenv("NICEGUI_PORT", "8080")),
    )

if __name__ == "__main__":
    main()
