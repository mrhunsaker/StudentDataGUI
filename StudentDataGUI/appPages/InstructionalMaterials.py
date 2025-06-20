#!/usr/bin/env python3

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

from ..appTheming import theme
from nicegui import ui



@ui.page("/instructionalmaterials")
def create() -> None:
    """
    Render the Instructional Materials Page.

    This function defines a NiceGUI UI route for the "/instructionalmaterials" endpoint.
    It displays a page containing categorized links to various instructional materials.

    Categories:
        - Abacus: Links to resources like Hadley Abacus Curriculum and Japanese Abacus Use.
        - Braille: Links to UEB Literary Braille and Technical Guidelines.
        - Screen Reader: Links to NVDA Trainings and Windows Screen Reader Primer.
        - Datasheets: Links to templates and progress monitoring sheets.
        - Assessment Forms: Links to educational vision evaluation forms.

    Returns
    -------
    None
        This function does not return any value. It renders the UI components for the page.
    """
    with theme.frame("- INSTRUCTIONAL MATERIALS -", menu_position="left"):
        ui.label("Instructional Materials").classes(
            "text-h4 font-bold text-grey-8"
        ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-full no-wrap").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.label("MATERIALS").classes(
                "text-h4 w-screen no-wrap py-4 text-black font-bold text-xl justify-center items-center"
            )
        with ui.row().classes("w-full no-wrap").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.label("ABACUS").classes(
                "text-h4 w-screen no-wrap font-bold text-black text-xl justify-center items-center"
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Hadley Abacus Curriculum I",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/Abacus1.pdf",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Hadley Abacus Curriculum II",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/Abacus2.pdf",
                new_tab=True,
            ).classes("text-left w-full align-left text-black font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Abacus Made Easy",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/AbacusMadeEasy.pdf",
                new_tab=True,
            ).classes(
                "text-left w-full text-black align-left font-bold font-bold"
            ).style('font-style:normal, font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Using the Cranmer Abacus",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UsingCranmerAbacus.pdf",
                new_tab=True,
            ).classes("text-left w-full align-left text-black font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Japanese Abacus Use and Theory",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/abacusUseTheory.pdf",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Advanced Japanese Abacus",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/AdvancedAbacus.pdf",
                new_tab=True,
            ).classes("text-left w-full align-left text-black font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.label("BRAILLE").classes(
                "text-h4 w-screen no-wrap font-bold text-black text-xl justify-center items-center"
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "NLS-IMBT UEB Literary Braille",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/NLSLOCLessons1-11.pdf",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "UEB Australian Training Manual",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UEBAustralianTrainingManual.pdf",
                new_tab=True,
            ).classes("text-left w-full align-left text-black font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "UEB Technical Course",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UEBTechnicalCourse.pdf",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "UEB Technical Guidelines",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/UEBTechnicalGuidelines.pdf",
                new_tab=True,
            ).classes("text-left w-full align-left text-black font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "UEB with Nemeth",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/NemethUEBContext.pdf",
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.label("SCREENREADER").classes(
                "w-screen no-wrap font-bold text-black text-xl justify-center items-center"
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "NVDA Trainings",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/NVDATrainings.pdf",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Windows Screen Reader Primer",
                "https://github.com/mrhunsaker/Materials/raw/main/instructionMaterials/WindowsScreenreaderPrimer.zip",
                new_tab=True,
            ).classes("text-left w-full align-left text-black font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Getting Started with Windows 11",
                "https://github.com/mrhunsaker/Materials/blob/main/instructionMaterials/GettingStartedWindows11.doc",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.label("DATASHEETS").classes(
                "text-h4 w-screen no-wrap content-center font-bold text-black text-xl"
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Blank Vision Template",
                "https://github.com/mrhunsaker/Materials/raw/main/datasheets/BlankVisionTemplate.pdf",
                new_tab=True,
            ).classes("text-left w-screen text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Generic Data Sheets",
                "https://github.com/mrhunsaker/Materials/raw/main/datasheets/GenericDataSheets.pdf",
                new_tab=True,
            ).classes("text-left w-full align-left text-black font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap py-4").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Bi-Weekly Progress Monitoring",
                "https://github.com/mrhunsaker/Materials/raw/main/datasheets/ProgressMonitoring.pdf",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
        with ui.row().classes("w-full no-wrap").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.label("ASSESSMENT FORMS").classes(
                "text-h4 w-screen no-wrap py-4 font-bold text-black text-xl justify-center items-center"
            )
        with ui.row().classes("w-full no-wrap").style(
            'font-style:normal, font-family: "Atkinson Hyperlegible"'
        ):
            ui.link(
                "Educational Vision Evaluation Forms",
                "https://github.com/mrhunsaker/Materials/raw/main/visionAssessments/EducationVisionAssessments.pdf",
                new_tab=True,
            ).classes("text-left w-full text-black align-left font-bold").style(
                'font-style:normal, font-family: "Atkinson Hyperlegible"'
            )
