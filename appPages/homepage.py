#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""
#########################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                 #
#    email: hunsakerconsulting@gmail.com                                #
#                                                                       #
#                                                                       #
#    Licensed under the Apache License, Version 2.0 (the "License");    #
#    you may not use this file except in compliance with the License.   #
#    You may obtain a copy of the License at                            #
#    http://www.apache.org/licenses/LICENSE-2.0                         #
#                                                                       #
#    Unless Required by applicable law or agreed to in writing,         #
#    software distributed under the License is distributed on an        #
#    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,       #
#    either express or  implied.  See the License for the specific      #
#   language governing permissions and limitations under the License.   #
#########################################################################

from nicegui import ui

from appTheming import theme


def content() -> None:
    with theme.frame("- HOW TO USE THIS APP -"):
        ui.label("VISION SKILLS PROGRESSIONS").classes(
                "text-h4 font-bold text-grey-8 pl-10"
                )
        with ui.row().classes("w-screen no-wrap py-4 pl-10"):
            ui.markdown(
                    """
    ### About this app
    This app was designed to help TVIs engage in data-based decision making. The app is designed to be screenreader accessible using all known screenreaders (specifically tested with JAWS, NVDA, Dolphin ScreenReader, Narrator, and ZDSR).
                                                """
                    )
        with ui.row().classes("w-screen no-wrap py-4 pl-10"):
            ui.markdown(
                    """
        ### Use Instructions
        - Navigation
            - The site is designed to be worked with a screenreader using the **TAB** key.
            - Tab through each option and follow audio prompts (if using a screenreader) or tooltips (if not) to input data
    - Press the "Exit" button to close the app. Then close the window with the button in the upper left corner.
        - Data Input
            - Select the Student from the drop-down menu (it will autofill when you type as well)
            - Choose the Date using the date picker or else type in the date using the YYYY-MM-DD format (_i.e._, 2023-12-31)
            - For each measure, type in the 0,1, 2, or 3 Rubric value
            - Activate the "Save" button to save data to .csv format as well as to a Database
        - Data Visualization
            - Press the "Graph" button to pull saved data and open interactive plots in a new window.
            - The graph is also saved in HTML format in the Student data folder
            """
                    )
        with ui.row().classes("w-screen center  no-wrap py-4 pl-10"):
            ui.markdown(
                    """
                                        ### Scoring Rubrics
                                        All measures are evaluated using the  following rubric
                                        
                                        | RUBRIC SCORE | Narrative Meaning   | Interpretation                                                               |
                                        |:-------------|:--------------------|:-----------------------------------------------------------------------------|
                                        | 0            | No attempt          | Teach or Reteach skills  as if  previously  untaught                         |
                                        | 1            | Required Assistance | Student needs to learn to quickly recognize what skills is  needed           |
                                        | 2            | Hesitated           | Student needs  to develop confidence in using their  skills without waiting	|
                                        | 3            | Independent         | Student has  mastered the skill                                             |
                                        
                                        The motivation for this system is from  the Screen Reader Skills  Progression course available at  eyeTvision.org
                                        """,
                    extras=["tables"],
                    )

        with ui.row().classes("w-screen center  no-wrap py-4 pl-10"):
            ui.markdown(
                    """
                                        ### Folder Structure
                                        
                                        On initial setup, the program tries to
                                        set up the following
                                        folder hierarchy on your computer
                                        
                                        ```bash
                                        HOME/Documents
                                        +---StudentDatabase
                                        +-- errorLogs
                                        +-- StudentDataFiles
                                        ¦   +--Filenames.txt
                                        ¦   +--Student 1
                                        ¦   ¦   +-- AbacusSkillsProgression.csv
                                        ¦   ¦   +-- AbacusSkillsProgression.html
                                        ¦   ¦   +-- BrailleSkillsProgression.csv
                                        ¦   ¦   +-- cviProgression.csv
                                        ¦   ¦   +-- cviProgression.html
                                        ¦   ¦   +-- omnibusDatabase.csv
                                        ¦   ¦   +-- ScreenReaderSkillsProgression.csv
                                        ¦   ¦   +-- ScreenReaderSkillsProgression.html
                                        ¦   ¦   +-- StudentDataSheets
                                        ¦   ¦   +-- BlankVisionTemplate.pdf
                                        ¦   ¦   +-- GenericDataSheets.pdf
                                        ¦   ¦   +-- ProgressMonitoring.pdf
                                        ¦   ¦   +-- StudentInstructionMaterials
                                        ¦   ¦   +-- StudentVisionAssessments
                                        ¦   ¦   +-- EducationVisionAssessments.pdf
                                        ¦   ¦   +-- UEBLiterarySkillsProgression.html
                                        ¦   ¦   +-- UEBTechnicalSkillsProgression.html
                                        ...  ...
                                        ¦   +--Student n
                                        ¦   ¦   +-- AbacusSkillsProgression.csv
                                        ¦   ¦   +-- AbacusSkillsProgression.html
                                        ¦   ¦   +-- BrailleSkillsProgression.csv
                                        ¦   ¦   +-- cviProgression.csv
                                        ¦   ¦   +-- cviProgression.html
                                        ¦   ¦   +-- omnibusDatabase.csv
                                        ¦   ¦   +-- ScreenReaderSkillsProgression.csv
                                        ¦   ¦   +-- ScreenReaderSkillsProgression.html
                                        ¦   ¦   +-- StudentDataSheets
                                        ¦   ¦   +-- BlankVisionTemplate.pdf
                                        ¦   ¦   +-- GenericDataSheets.pdf
                                        ¦   ¦   +-- ProgressMonitoring.pdf
                                        ¦   ¦   +-- StudentInstructionMaterials
                                        ¦   ¦   +-- StudentVisionAssessments
                                        ¦   ¦   +-- EducationVisionAssessments.pdf
                                        ¦   ¦   +-- UEBLiterarySkillsProgression.html
                                        ¦   ¦   +-- UEBTechnicalSkillsProgression.html
                                        +-- students.db
                                        ```
                                        """,
                    extras=["fenced-code-blocks"],
                    )
