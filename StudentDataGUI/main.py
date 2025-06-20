#!/usr/bin/env python3

"""
Main Module for StudentDataGUI

This module serves as the entry point for the StudentDataGUI application.
It initializes the application, sets up routes, and starts the server.

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
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""


import os
import sys
import traceback
from pathlib import Path
import logging

from nicegui import ui

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from .appTheming import theme
from .appHelpers.helpers import (
    createFolderHierarchy,
    database_dir,
    set_start_dir,
    datenow,
)

from .appHelpers.sqlgenerate import initialize_database

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

from .appPages import homepage


def warningmessage(exception_type: type, exception_value: Exception, exception_traceback: traceback.TracebackType) -> None:
    """
    Log an error message and display a warning notification.

    Parameters
    ----------
    exception_type : type
        The type of the exception that was raised.
    exception_value : Exception
        The exception instance that was raised.
    exception_traceback : traceback.TracebackType
        The traceback object containing information about where the exception occurred.

    Returns
    -------
    None
        This function does not return any value.

    Notes
    -----
    The function logs the error details to a file and displays a warning notification
    to the user. It ensures that the error logs are stored in a predefined directory.

    Examples
    --------
    >>> try:
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
    ui.notify(f"{message}\n{errortype}", type="warning", close_button="OK")


@ui.page("/")
def index_page() -> None:
    """
    Display the homepage for the application.

    This function initializes and renders the homepage of the application,
    providing users with instructions and navigation options.

    Returns
    -------
    None
        This function does not return any value.

    Notes
    -----
    The homepage includes a themed frame and content defined in the `homepage` module.

    Examples
    --------
    >>> index_page()
    """
    with theme.frame("Student Skills Progressions"):
        homepage.content()


def initialize_ui() -> None:
    """
    Initialize global UI components and register application routes.

    This function sets up the global UI components, including the footer,
    and imports all page modules to register their respective routes.

    Returns
    -------
    None
        This function does not return any value.

    Notes
    -----
    The footer is a global component that appears on all pages and includes
    copyright information and a contact email for bug reports or feature requests.
    """
    # Import the page modules to register their routes

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

def main() -> None:
    """
    Main entry point for the application.

    This function initializes the UI components and starts the NiceGUI server
    with the specified configuration.

    Returns
    -------
    None
        This function does not return any value.

    Notes
    -----
    The server configuration includes options for the host, port, and UI appearance.
    """
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
