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


def menu() -> None:
    with ui.button(icon="menu").classes():
        with ui.menu().classes("w-[250px]") as menu:
            ui.menu_item("HOME", lambda: ui.open("/")).classes(replace="text-black")
            ui.separator()
            ui.menu_item("CONTACT LOG", lambda: ui.open("/contactlog")).classes(
                replace="text-black"
            )
            ui.menu_item("ANECDOTAL NOTES", lambda: ui.open("/anecdotalnotes")).classes(
                replace="text-black"
            )

            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("TACTILE SKILLS").classes("font-bold")
            ui.menu_item("ABACUS SKILLS", lambda: ui.open("/abacusskills")).classes(
                replace="text-black"
            )
            ui.menu_item("BRAILLE SKILLS", lambda: ui.open("/brailleskills")).classes(
                replace="text-black"
            )
            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("TECHNOLOGY SKILLS").classes("font-bold")
            ui.menu_item(
                "SCREENREADER SKILLS", lambda: ui.open("/screenreaderskills")
            ).classes(replace="text-black")
            ui.menu_item(
                "BRAILLENOTE TOUCH SKILLS", lambda: ui.open("/braillenotetouchskills")
            ).classes(replace="text-black")
            ui.menu_item(
                "iOS/iPadOS VOICEOVER SKILLS", lambda: ui.open("/iosskills")
            ).classes(replace="text-black")
            ui.separator()
            with ui.row().classes("justify-center items-center"):
                ui.label("CVI / NVI").classes("font-bold")
            ui.menu_item("CVI PROGRESS", lambda: ui.open("/cviprogress")).classes(
                replace="text-black"
            )
            ui.separator()
            with ui.row().classes("justify-center items-center py-2"):
                ui.label("MATERIALS").classes("font-bold")
            ui.menu_item(
                "INSTRUCTIONAL MATERIALS", lambda: ui.open("/instructionalmaterials")
            ).classes(replace="text-black")