
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

from nicegui import ui


def menu() -> None:
        ui.link("HOME", '/').classes(replace='text-white')
        ui.link("ABACUS SKILLS", '/abacusskills').classes(replace='text-white')
        ui.link("BRAILLE SKILLS", '/brailleskills').classes(replace='text-white')
        ui.link("SCREENREADER SKILLS", '/screenreaderskills').classes(replace='text-white')
        ui.link("BRAILLENOTE TOUCH SKILLS", '/braillenotetouchskills').classes(replace='text-white')
        ui.link("iOS/iPadOS VOICEOVER SKILLS", '/iosskills').classes(replace='text-white')
        ui.link("CVI PROGRESS", '/cviprogress').classes(replace='text-white')
        ui.link("CONTACT LOG", '/contactlog').classes(replace='text-white')