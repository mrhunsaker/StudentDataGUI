#!/usr/bin/env python3
from datetime import datetime

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
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""


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
            /* Strong visible focus for all interactive elements */
            a:focus, button:focus, input:focus, select:focus, textarea:focus, [tabindex]:focus {
                outline: 3px solid #ffca58 !important; /* Gold, matches your accent */
                outline-offset: 2px;
                background: #fffbe6;
                color: #183969;
            }
            </style>
        """
    )

    ui.colors(
        primary="#183969", secondary="#bed2e3", positive="#ffca58", accent="#cfcac1"
    )

    # Add a visually hidden but focusable "Skip to main content" link for accessibility
    ui.add_body_html("""
    <a href="#main-content" id="skip-link"
       style="
         position:absolute;
         left:0;
         top:0;
         background:#ffca58;
         color:#183969;
         padding:8px 16px;
         z-index:1000;
         transform:translateY(-200%);
         transition:transform 0.2s;
         font-weight:bold;
         font-family:'Atkinson Hyperlegible', Arial, sans-serif;
         text-decoration:none;
         border-radius:0 0 8px 0;
         outline:none;
       "
       onfocus="this.style.transform='translateY(0)';"
       onblur="this.style.transform='translateY(-200%)';"
       onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();document.getElementById('main-content').focus();}"
       tabindex="0"
    >Skip to main content</a>
    """)

    with ui.header().props('role=banner').classes("justify-between text-black h-[100px]"):
        with ui.row().classes("no-wrap text-l font-bold text-black"):
            with ui.html('<nav role="navigation">'):
                with ui.link(target="https://davis.k12.ut.us").classes(
                    "max-[305px]:hidden absolute-left flex-none mt-5"
                ).tooltip("Davis School District"):
                    branding().classes("fill-white scale-150 m-1")
                menu()
            ui.label(navtitle).classes(
                "absolute-center no-wrap text-2xl text-white font-bold self-center"
            ).classes().style('font-family: "Atkinson Hyperlegible"')
    with ui.html('<main role="main" id="main-content" tabindex="-1">'):
        yield

    with ui.footer(value=True).props('role=contentinfo').classes("h-[75px]") as footer:
        with ui.row().classes(
            "w-screen no-wrap justify-between items-center text-l font-bold text-white h-full pt-2.5"
        ):
            ui.label(f"Copyright © {datetime.now().year} Michael Ryan Hunsaker, M.Ed., Ph.D.").classes(
                "absolute-center flex-1 self-bottom"
            ).style('font-family: "Atkinson Hyperlegible"')
            with ui.link(target="https://github.com/mrhunsaker/StudentDataGUI").classes(
                "max-[305px]:hidden absolute-right flex-none mt-2.5"
            ).tooltip("GitHub Repo"):
                github().classes("fill-white scale-75 m-1 mt-2.5")
