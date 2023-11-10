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


from contextlib import contextmanager
from pathlib import Path
from nicegui import ui
import os

from appTheming.menu import menu
from appHelpers.helpers import ROOT_DIR

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def github() -> ui.html:
    """
    Retrieve and display the GitHub icon as HTML.

    This function reads the content of the 'github.svg' file located in the root directory
    and returns it as an HTML object. The SVG content is typically an icon representing the
    GitHub logo.

    Returns
    -------
    ui.html
        An HTML object containing the GitHub icon.

    Examples
    --------
    >>> github()
    <ui.html object representing the GitHub icon>
    """
    return ui.html(Path(ROOT_DIR).joinpath("github.svg").read_text())


def branding() -> ui.html:
    """
    Retrieve and display the branding icon as HTML.

    This function reads the content of the 'dsd-mark-white.svg' file located in the root directory
    and returns it as an HTML object. The SVG content is typically an icon representing the
    GitHub logo.

    Returns
    -------
    ui.html
        An HTML object containing the GitHub icon.

    Examples
    --------
    >>> branding()
    <ui.html object representing the branding icon>
    """
    return ui.html(Path(ROOT_DIR).joinpath("dsd-mark-white.svg").read_text())


@contextmanager
def frame(navtitle: str):
    """
    Custom page frame to share the same styling and behavior across all pages.

    This function sets up a custom page frame with consistent styling and behavior
    for all pages in the application. It includes a header with a navigation title,
    color configurations, and a menu.

    Parameters
    ----------
    navtitle : str
        The title to be displayed in the navigation bar.

    Yields
    ------
    None

    Examples
    --------
    >>> with frame("Home"):
    ...     # Code for the content of the page goes here
    """

    ui.colors(
        primary="#183969", secondary="#bed2e3", positive="#ffca58", accent="#cfcac1"
    )
    """ui.colors(
            primary="#ffc8dd", secondary="#cdb4db", accent="#bde0fe", positive="#a2d2ff"
            )"""

    with ui.header().classes("justify-between text-black"):
        """
        """
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
            "w-screen no-wrap justify-center items-right text-l font-bold text-white"
        ):
            with ui.link(target="https://github.com/mrhunsaker/StudentDataGUI").classes(
                "max-[305px]:hidden"
            ).tooltip("GitHub"):
                github().classes("fill-white scale-125 m-1")
