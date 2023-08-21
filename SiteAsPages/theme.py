from contextlib import contextmanager

from menu import menu

from nicegui import ui


@contextmanager
def frame(navtitle: str):
    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header().classes('justify-between text-white'):
        with ui.row().classes("no-wrap text-l font-bold"):
            ui.label(navtitle)
        with ui.row().classes("no-wrap text-l font-bold"):
            menu()
    with ui.column().classes(''):
        yield
    ##############################################################################
    # FOOTER
    ##############################################################################
    with ui.footer(value=True) as footer:
        with ui.row().classes(
                "w-screen no-wrap justify-center items-center text-l font-bold"
                ):
            ui.label(
                    "Copyright © 2023 Michael Ryan Hunsaker, M.Ed., Ph.D."
                    ).classes(
                    "justify-center items-center"
                    )
        with ui.row().classes(
                "w-screen no-wrap justify-center items-centertext-l font-bold"
                ):
            ui.label(
                    "Report Bugs or Request Features by emailing "
                    "hunsakerconsulting@gmail.com"
                    ).classes("justify-center items-center")

    ##############################################################################
    # SIDEBAR
    ##############################################################################
    '''
    with ui.left_drawer(value=True) as left_drawer:
        with ui.row().classes("w-full no-wrap"):
            ui.label("MATERIALS").classes(
                    "w-screen no-wrap py-4 text-white font-bold text-xl "
                    "justify-center items-center"
                    )
        with ui.row().classes("w-full no-wrap"):
            ui.label("ABACUS").classes(
                    "w-screen no-wrap font-bold text-white text-xl justify-center "
                    "items-center"
                    )
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Hadley Abacus Curriculum I",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/Abacus1.pdf",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Hadley Abacus Curriculum II",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/Abacus2.pdf",
                    new_tab=True,
                    ).classes("text-left w-full align-left text-white font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Abacus Made Easy",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/AbacusMadeEasy.pdf",
                    new_tab=True,
                    ).classes(
                    "text-left w-full text-white align-left font-bold font-bold"
                    )
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Using the Cranmer Abacus",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/UsingCranmerAbacus.pdf",
                    new_tab=True,
                    ).classes("text-left w-full align-left text-white font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Japanese Abacus Use and Theory",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/abacusUseTheory.pdf",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Advanced Japanese Abacus",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/AdvancedAbacus.pdf",
                    new_tab=True,
                    ).classes("text-left w-full align-left text-white font-bold")
        with ui.row().classes("w-full no-wrap"):
            ui.label("BRAILLE").classes(
                    "w-screen no-wrap font-bold text-white text-xl justify-center "
                    "items-center"
                    )
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "NLS-IMBT UEB Literary Braille",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/NLSLOCLessons1-11.pdf",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "UEB Australian Training Manual",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/UEBAustralianTrainingManual.pdf",
                    new_tab=True,
                    ).classes("text-left w-full align-left text-white font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "UEB Technical Course",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/UEBTechnicalCourse.pdf",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "UEB Technical Guidelines",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/UEBTechnicalGuidelines.pdf",
                    new_tab=True,
                    ).classes("text-left w-full align-left text-white font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "UEB with Nemeth",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/NemethUEBContext.pdf",
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap"):
            ui.label("SCREENREADER").classes(
                    "w-screen no-wrap font-bold text-white text-xl justify-center "
                    "items-center"
                    )
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "NVDA Trainings",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/NVDATrainings.pdf",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Windows Screen Reader Primer",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/instructionMaterials/WindowsScreenreaderPrimer.zip",
                    new_tab=True,
                    ).classes("text-left w-full align-left text-white font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Getting Started with Windows 11",
                    "https://github.com/mrhunsaker/Materials/blob/main"
                    "/instructionMaterials/GettingStartedWindows11.doc",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap"):
            ui.label("DATASHEETS").classes(
                    "w-screen no-wrap content-center font-bold text-white text-xl"
                    )
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Blank Vision Template",
                    "https://github.com/mrhunsaker/Materials/raw/main/datasheets"
                    "/BlankVisionTemplate.pdf",
                    new_tab=True,
                    ).classes("text-left w-screen text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Generic Data Sheets",
                    "https://github.com/mrhunsaker/Materials/raw/main/datasheets"
                    "/GenericDataSheets.pdf",
                    new_tab=True,
                    ).classes("text-left w-full align-left text-white font-bold")
        with ui.row().classes("w-full no-wrap py-4"):
            ui.link(
                    "Bi-Weekly Progress Monitoring",
                    "https://github.com/mrhunsaker/Materials/raw/main/datasheets"
                    "/ProgressMonitoring.pdf",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        with ui.row().classes("w-full no-wrap"):
            ui.label("ASSESSMENT FORMS").classes(
                    "w-screen no-wrap py-4 font-bold text-white text-xl "
                    "justify-center items-center"
                    )
        with ui.row().classes("w-full no-wrap"):
            ui.link(
                    "Educational Vision Evaluation Forms",
                    "https://github.com/mrhunsaker/Materials/raw/main"
                    "/visionAssessments/EducationVisionAssessments.pdf",
                    new_tab=True,
                    ).classes("text-left w-full text-white align-left font-bold")
        '''