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

from nicegui import ui

from appTheming import theme


def content() -> None:
    with theme.frame("- HOW TO USE THIS APP -"):
        ui.label("VISION SKILLS PROGRESSIONS").classes(
            "text-3xl font-bold pl-10"
        ).style('font-family: "Atkinson Hyperlegible"')
        # fmt: off
        with ui.row().classes("w-[800px] no-wrap py-0 pl-10"):
            ui.label("About this app").classes("text-2xl font-bold").style('font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-[800px] no-wrap py-0 pl-10"):
            ui.label("This app was designed to help TVIs engage in data-based decision making. The app is designed to be screenreader accessible using all known screenreaders (specifically tested with JAWS, NVDA, Dolphin ScreenReader, Narrator, and ZDSR).").classes("text-lg font-normal").style('font-style: normal, font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("Use Instructions").classes("text-2xl font-bold").style('font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("Navigation").classes("text-xl font-bold").style('font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("The site is designed to be worked with a screenreader using the TAB key.").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px] no-wrap py-0 pl-10"):
            ui.label("Tab through each option and follow audio prompts (if using a screenreader) or tooltips (if not) to input data").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px] no-wrap py-0 pl-10"):       
            ui.label("Press the \"Exit\" button to close the app. Then close the window with the button in the upper left corner.").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px] no-wrap py-0 pl-10"):
            ui.label("Data Input").classes("text-xl font-bold").style('font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("Select the Student from the drop-down menu (it will autofill when you type as well)").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("Choose the Date using the date picker or else type in the date using the YYYY-MM-DD format (i.e., 2023-12-31)").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("For each measure, type in the 0,1, 2, or 3 Rubric value").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("Activate the \"Save\" button to save data to .csv format as well as to a Database").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("Data Visualization").classes("text-xl font-bold").style('font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-[800px]  no-wrap pl-10"):
            ui.label("Press the \"Graph\" button to pull saved data and open interactive plots in a new window.").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):            
            ui.label("The graph is also saved in HTML format in the Student data folder").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px] center no-wrap py-0 pl-10"):
            ui.label("Scoring Rubrics").classes("text-2xl font-bold").style('font-family: "Atkinson Hyperlegible"')
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("All measures are evaluated using the following rubric").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            rows = [
                {'RUBRIC SCORE': 0, 'Narrative Meaning':"No attempt", 'Interpretation':"Teach or Reteach skills as if previously untaught"},
                {'RUBRIC SCORE': 1, 'Narrative Meaning':"Required Assistance", 'Interpretation':"Student needs to learn to quickly recognize what skills is needed"},
                {'RUBRIC SCORE': 2, 'Narrative Meaning':"Hesitated", 'Interpretation':"Student needs to develop confidence in using their skills without waiting"},
                {'RUBRIC SCORE': 3, 'Narrative Meaning':"Independent", 'Interpretation':"Student has mastered the skill"}
            ]
            columns = [
                {'name': "RUBRIC SCORE", 'label':"RUBRIC SCORE", "field":"RUBRIC SCORE", "align":"left"},
                {'name': "Narrative Meaning", 'label':"Narrative Meaning", "field":"Narrative Meaning", "align":"left"},
                {'name': "Interpretation", 'label':"Interpretation", "field":"Interpretation", "align":"left"}
                ]
            ui.table(columns=columns, rows=rows, row_key='name').props('align-left').style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  no-wrap py-0 pl-10"):
            ui.label("The motivation for this system is from the Screen Reader Skills Progression course available at eyeTvision.org").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  center  no-wrap py-0 pl-10"):
            ui.label("Folder Structure").classes("text-xl font-bold").style('font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  center  no-wrap py-0 pl-10"):
            ui.label("On initial setup, the program tries to set up the following folder hierarchy on your computer").style('font-style:normal, font-family: "Atkinson Hyperlegible"').classes("text-lg font-normal")
        with ui.row().classes("w-[800px]  center  no-wrap py-0 pl-10"):
            ui.code("""
                HOME/Documents
                +---StudentDatabase
                |   +-- errorLogs
                |   +-- StudentDataFiles
                |   |   +--Filenames.txt
                |   |   +--Student 1
                |   |   |   +-- AbacusSkillsProgression.csv
                |   |   |   +-- AbacusSkillsProgression.html
                |   |   |   +-- BrailleSkillsProgression.csv
                |   |   |   +-- cviProgression.csv
                |   |   |   +-- cviProgression.html
                |   |   |   +-- omnibusDatabase.csv
                |   |   |   +-- ScreenReaderSkillsProgression.csv
                |   |   |   +-- ScreenReaderSkillsProgression.html
                |   |   |   +-- StudentDataSheets
                |   |   |   +--  BlankVisionTemplate.pdf
                |   |   |   +-- GenericDataSheets.pdf
                |   |   |   +-- ProgressMonitoring.pdf
                |   |   |   +-- StudentInstructionMaterials
                |   |   |   +-- StudentVisionAssessments
                |   |   |   +-- EducationVisionAssessments.pdf
                |   |   |   +-- UEBLiterarySkillsProgression.html
                |   |   |   +-- UEBTechnicalSkillsProgression.html
                |   |    ...  ...
                |   |   +--Student n
                |   |   |   +-- AbacusSkillsProgression.csv
                |   |   |   +-- AbacusSkillsProgression.html
                |   |   |   +-- BrailleSkillsProgression.csv
                |   |   |   +-- cviProgression.csv
                |   |   |   +-- cviProgression.html
                |   |   |   +-- omnibusDatabase.csv
                |   |   |   +-- ScreenReaderSkillsProgression.csv
                |   |   |   +-- ScreenReaderSkillsProgression.html
                |   |   |   +-- StudentDataSheets
                |   |   |   +--  BlankVisionTemplate.pdf
                |   |   |   +-- GenericDataSheets.pdf
                |   |   |   +-- ProgressMonitoring.pdf
                |   |   |   +-- StudentInstructionMaterials
                |   |   |   +-- StudentVisionAssessments
                |   |   |   +-- EducationVisionAssessments.pdf
                |   |   |   +-- UEBLiterarySkillsProgression.html
                |   |   |   +-- UEBTechnicalSkillsProgression.html
                |   +-- Students.db
                """
            )
