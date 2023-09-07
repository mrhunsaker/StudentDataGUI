#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for teachers
of students with Visual Impairments
"""
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                       #
#    email: hunsakerconsulting@gmail.com                                      #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");          #
#    you may not use this file except in compliance with the License.         #
#    You may obtain a copy of the License at                                  #
#                                                                             #
#    http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                             #
#    Unless Required by applicable law or agreed to in writing, software      #
#    distributed under the License is distributed on an "AS IS" BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
#    See the License for the specific language governing permissions and      #
#    limitations under the License.                                           #
###############################################################################

from nicegui import app, ui

import theme


def create() -> None:
    ##########################################################################
    # iOS/iPadOS VOICEOVER  SKILLS
    ##########################################################################
    @ui.page('/iosskills')
    def iosskills():
        with theme.frame('- iOS/iPadOS VOICEOVER SKILLS -'):
            ui.label('iOS/iPadOS VOICEOVER SKILLS').classes('text-h4 text-grey-8')
            with ui.row().classes("w-screen no-wrap"):
                ui.label("iOS/iPadOS VOICEOVER SKILLS PROGRESSION").classes("justify-center items-center")
            
            def save():
                a = 1
            
            def graph():
                ui.notify("This Function is Not Yet Configured", position='center', type='warning', close_button="OK", )
                '''ui.notify(
                        "Graph Successful. The Graphs will open in a Browser "
                        "Window",
                        color='pink',
                        position='center',
                        type='positive',
                        close_button="OK",
                        )
                '''
            
            with ui.row().classes("w-screen no-wrap py-4"):
                ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
                ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
                ui.button("EXIT", color="#172554", on_click=app.shutdown).classes("text-white")
