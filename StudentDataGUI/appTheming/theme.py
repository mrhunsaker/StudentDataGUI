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
import logging

from ..appHelpers.helpers import ROOT_DIR
from .menu import menu
from nicegui import ui, app


def _read_svg_with_fallback(name: str) -> str:
    """Try ROOT_DIR/<name>, then StudentDataGUI/appHelpers/<name>; return empty string if not found."""
    try:
        root = Path(ROOT_DIR)
        candidates = [
            root.joinpath(name),
            root.joinpath("StudentDataGUI", "appHelpers", name),
            root.joinpath("StudentDataGUI", "appHelpers", "images", name),
        ]
        for p in candidates:
            if p.exists():
                logging.debug(f"Loaded SVG from: {p}")
                return p.read_text()
        logging.warning(f"SVG not found (tried {', '.join(str(p) for p in candidates)}): {name}")
    except Exception:
        logging.exception("Error while reading SVG")
    return ""


def github() -> ui.html:
    """Return GitHub SVG as ui.html, with fallback locations."""
    return ui.html(_read_svg_with_fallback("github.svg"), sanitize=False)


def branding() -> ui.html:
    """Return branding SVG as ui.html, with fallback locations."""
    return ui.html(_read_svg_with_fallback("dsd-mark-white.svg"), sanitize=False)


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

    ui.add_body_html(
        """
        <div id="main-content" tabindex="-1"></div>
        """
    )

    with ui.header().props('role=banner').classes("justify-between text-black h-[100px]"):
        with ui.row().classes("no-wrap text-l font-bold text-black"):
            with ui.link(target="https://davis.k12.ut.us").classes(
                "max-[305px]:hidden absolute-left flex-none mt-5"
            ).tooltip("Davis School District"):
                branding().classes("fill-white scale-150 m-1")
            menu()
            ui.label(navtitle).classes(
                "absolute-center no-wrap text-2xl text-white font-bold self-center"
            ).style('font-family: "Atkinson Hyperlegible"')

    yield  # Yield to allow page content to be inserted here

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

def register_fonts() -> None:
    """
    Register local font files as static files on the NiceGUI `app`.

    This function intentionally does NOT run at module import so that
    NiceGUI `app`/`ui` calls aren't executed during import-time. Call this
    from startup code (for example `main.initialize_ui`) after the app
    environment is ready.
    """
    try:
        PROJECT_ROOT = Path(ROOT_DIR)
        # package-local fonts (inside the installed package) and repo-root appHelpers/fonts
        preferred_fonts_dir = PROJECT_ROOT.joinpath("appHelpers", "fonts")
        repo_root_fonts_dir = PROJECT_ROOT.parent.joinpath("appHelpers", "fonts")
        legacy_fonts_dir = PROJECT_ROOT.joinpath("fonts")
        font_files = [
            "AtkinsonHyperlegible-BoldItalic.ttf",
            "AtkinsonHyperlegible-Bold.ttf",
            "AtkinsonHyperlegible-Italic.ttf",
            "AtkinsonHyperlegible-Regular.ttf",
            "JetBrainsMono-BoldItalic.ttf",
            "JetBrainsMono-Bold.ttf",
            "JetBrainsMono-Italic.ttf",
            "JetBrainsMono-Regular.ttf",
        ]

        registered_any = False
        for fname in font_files:
            # prefer package-local appHelpers/fonts
            fpath = preferred_fonts_dir.joinpath(fname)
            # fall back to repo-root appHelpers/fonts, then ROOT_DIR/fonts
            if not fpath.exists():
                fpath = repo_root_fonts_dir.joinpath(fname)
            if not fpath.exists():
                fpath = legacy_fonts_dir.joinpath(fname)
            if fpath.exists():
                app.add_static_file(local_file=fpath, url_path=f"/fonts/{fname}")
                logging.debug(f"Registered font: {fpath}")
                registered_any = True
            else:
                logging.debug(f"Font not found, skipping: {fname}")

        if not registered_any:
            logging.warning("No font files found in appHelpers/fonts or ROOT_DIR/fonts; continuing without registering fonts.")
    except Exception:
        logging.exception("Error while registering font static files")


@contextmanager
def card(**kwargs) -> None:
    """
    Standardized card context manager for consistent page card styling.

    Usage:
        with card():
            ui.label("Content")

    Any kwargs will be forwarded to `ui.card()` as attributes (for example
    `.classes()` or `.props()` are applied inside). This helper applies a
    default set of classes to keep visual appearance consistent across pages.
    """
    # default classes provide a subtle elevation, padding, and rounded corners
    default_classes = "shadow-md rounded-lg p-4 max-w-4xl"
    custom_classes = kwargs.pop("classes", None)
    combined_classes = f"{default_classes} {custom_classes or ''}".strip()
    # Use ui.card and apply the combined classes; yield control to caller
    with ui.card().classes(combined_classes):
        yield
