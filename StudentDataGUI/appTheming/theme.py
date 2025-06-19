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

from ..appHelpers.helpers import ROOT_DIR
from .menu import menu
from nicegui import ui, app


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
def frame(navtitle: str) -> None:
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

    style = """
        <style>
        @font-face {
        font-family: 'Atkinson Hyperlegible';
        src: url('/fonts/AtkinsonHyperlegible-Regular.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
        }

        @font-face {
        font-family: 'Atkinson Hyperlegible';
        src: url('/fonts/AtkinsonHyperlegible-Bold.ttf') format('truetype');
        font-weight: bold;
        font-style: normal;
        }

        @font-face {
        font-family: 'Atkinson Hyperlegible';
        src: url('/fonts/AtkinsonHyperlegible-Italic.ttf') format('truetype');
        font-weight: normal;
        font-style: italic;
        }

        @font-face {
        font-family: 'Atkinson Hyperlegible';
        src: url('/fonts/AtkinsonHyperlegible-BoldItalic.ttf') format('truetype');
        font-weight: bold;
        font-style: italic;
        }

        @font-face {
        font-family: 'JetBrainsMono';
        src: url('/fonts/JetBrainsMono-Regular.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
        }

        @font-face {
        font-family: 'JetBrainsMono';
        src: url('/fonts/JetBrainsMono-Bold.ttf') format('truetype');
        font-weight: bold;
        font-style: normal;
        }

        @font-face {
        font-family: 'JetBrainsMono';
        src: url('/fonts/JetBrainsMono-Italic.ttf') format('truetype');
        font-weight: normal;
        font-style: italic;
        }

        @font-face {
        font-family: 'JetBrainsMono';
        src: url('/fonts/JetBrainsMono-BoldItalic.ttf') format('truetype');
        font-weight: bold;
        font-style: italic;
        }

        </style>
        """
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath(
            "fonts", "AtkinsonHyperlegible-BoldItalic.ttf"
        ),
        url_path="/fonts/AtkinsonHyperlegible-BoldItalic.ttf",
    )
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath("fonts", "AtkinsonHyperlegible-Bold.ttf"),
        url_path="/fonts/AtkinsonHyperlegible-Bold.ttf",
    )
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath("fonts", "AtkinsonHyperlegible-Italic.ttf"),
        url_path="/fonts/AtkinsonHyperlegible-Italic.ttf",
    )
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath("fonts", "AtkinsonHyperlegible-Regular.ttf"),
        url_path="/fonts/AtkinsonHyperlegible-Regular.ttf",
    )
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath("fonts", "JetBrainsMono-BoldItalic.ttf"),
        url_path="/fonts/JetBrainsMono-BoldItalic.ttf",
    )
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath("fonts", "JetBrainsMono-Bold.ttf"),
        url_path="/fonts/JetBrainsMono-Bold.ttf",
    )
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath("fonts", "JetBrainsMono-Italic.ttf"),
        url_path="/fonts/JetBrainsMono-Italic.ttf",
    )
    app.add_static_file(
        local_file=Path(ROOT_DIR).joinpath("fonts", "JetBrainsMono-Regular.ttf"),
        url_path="/fonts/JetBrainsMono-Regular.ttf",
    )

    ui.add_head_html(style)
    ui.add_head_html(
        """
            <style>
            .q-table__bottom {
                justify-content: flex-start !important;
            }
            .q-table__bottom .q-table__separator {
                display: none;
            }
            .q-badge--outline {
                border-width: 4px;
                font-weight: bold;
                font-size: 1.25rem;
            }
            .my-table tbody td {
                font-size: 1.25em;
                align: left;
            }
            .my-table thead th {
                font-size: 1.25em;
                font-weight: bold;
                align: left;
            }
            </style>
        """
    )

    ui.colors(
        primary="#183969", secondary="#bed2e3", positive="#ffca58", accent="#cfcac1"
    )

    with ui.header().classes("justify-between text-black h-[100px]"):
        """
        Create a custom layout using the NiceGUI UI framework.

        Parameters:
        - navtitle (str): The title to be displayed in the navigation bar.

        Usage:
        ```python
        with nicegui_custom_layout("Page Title"):
            # Content to be displayed in the custom layout
            # ...
        ```

        This function defines a layout structure using the NiceGUI UI framework, consisting of a header with a navigation title,
        a menu section, and a main content column. The `navtitle` parameter specifies the title to be displayed in the navigation bar.

        Example:
        ```python
        with nicegui_custom_layout("Home"):
            # Main content goes here
            # ...
        ```

        Note:
        - This function is designed to be used within a context manager (i.e., with statement).
        - The layout structure is implemented using NiceGUI UI components and styling classes.
        - The `yield` statement is used to allow the caller to insert their custom content within the main content column.

        See Also:
        - NiceGUI UI framework documentation for more details on the UI components and styling classes.
        """
        with ui.row().classes("no-wrap text-l font-bold text-black"):
            with ui.link(target="https://davis.k12.ut.us").classes(
                "max-[305px]:hidden absolute-left flex-none mt-5"
            ).tooltip("Davis School District"):
                branding().classes("fill-white scale-150 m-1")
            ui.label(navtitle).classes(
                "absolute-center no-wrap text-2xl text-white font-bold self-center"
            ).classes().style('font-family: "Atkinson Hyperlegible"')
            menu()
    yield

    with ui.footer(value=True).classes("h-[75px]") as footer:
        with ui.row().classes(
            "w-screen no-wrap justify-between items-center text-l font-bold text-white h-full pt-2.5"
        ):
            ui.label("Copyright © 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.").classes(
                "absolute-center flex-1 self-bottom"
            ).style('font-family: "Atkinson Hyperlegible"')
            with ui.link(target="https://github.com/mrhunsaker/StudentDataGUI").classes(
                "max-[305px]:hidden absolute-right flex-none mt-2.5"
            ).tooltip("GitHub Repo"):
                github().classes("fill-white scale-75 m-1 mt-2.5")
