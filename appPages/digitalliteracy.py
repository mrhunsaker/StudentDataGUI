#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""
########################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                #
#    email: hunsakerconsulting@gmail.com                               #
#                                                                      #
#                                                                      #
#    Licensed under the Apache License, Version 2.0 (the "License");   #
#    you may not use this file except in compliance with the License.  #
#    You may obtain a copy of the License at                           #
#    http://www.apache.org/licenses/LICENSE-2.0                        #
#                                                                      #
#    Unless Required by applicable law or agreed to in writing,        #
#    software distributed under the License is distributed on an       #
#    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,      #
#    either express or  implied.  See the License for the specific     #
#   language governing permissions and limitations under the License.  #
########################################################################

import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nicegui import app, ui
from plotly.subplots import make_subplots

from appHelpers.helpers import dataBasePath, datenow, USER_DIR, date_fmt
from appHelpers.roster import students
from appTheming import theme


def create() -> None:
    ##########################################################################
    # BRAILLE SKILLS
    ##########################################################################
    @ui.page("/digitalliteracy")
    def brailleskills() -> None:
        with theme.frame("- TECHNOLOGY SKILLS -"):
            ui.label("DIGITAL LITERACY").classes("text-h4 text-grey-8")

            u_studentname = ui.select(
                options=students, value="DonaldChamberlain"
            ).classes("hidden")
            date = ui.date().classes("hidden")
            u_digitalliteracy_trial11 = ui.number().classes("hidden")
            u_digitalliteracy_trial12 = ui.number().classes("hidden")
            u_digitalliteracy_trial13 = ui.number().classes("hidden")
            u_digitalliteracy_trial14 = ui.number().classes("hidden")
            u_digitalliteracy_trial15 = ui.number().classes("hidden")
            u_digitalliteracy_trial16 = ui.number().classes("hidden")
            u_digitalliteracy_trial21 = ui.number().classes("hidden")
            u_digitalliteracy_trial22 = ui.number().classes("hidden")
            u_digitalliteracy_trial23 = ui.number().classes("hidden")
            u_digitalliteracy_trial24 = ui.number().classes("hidden")
            u_digitalliteracy_trial25 = ui.number().classes("hidden")
            u_digitalliteracy_trial26 = ui.number().classes("hidden")
            u_digitalliteracy_trial31 = ui.number().classes("hidden")
            u_digitalliteracy_trial32 = ui.number().classes("hidden")
            u_digitalliteracy_trial33 = ui.number().classes("hidden")
            u_digitalliteracy_trial34 = ui.number().classes("hidden")
            u_digitalliteracy_trial35 = ui.number().classes("hidden")
            u_digitalliteracy_trial41 = ui.number().classes("hidden")
            u_digitalliteracy_trial42 = ui.number().classes("hidden")
            u_digitalliteracy_trial43 = ui.number().classes("hidden")
            u_digitalliteracy_trial44 = ui.number().classes("hidden")
            u_digitalliteracy_trial45 = ui.number().classes("hidden")
            u_digitalliteracy_trial51 = ui.number().classes("hidden")
            u_digitalliteracy_trial52 = ui.number().classes("hidden")
            u_digitalliteracy_trial53 = ui.number().classes("hidden")
            u_digitalliteracy_trial54 = ui.number().classes("hidden")
            u_digitalliteracy_trial55 = ui.number().classes("hidden")
            u_digitalliteracy_trial56 = ui.number().classes("hidden")
            u_digitalliteracy_trial57 = ui.number().classes("hidden")
            u_digitalliteracy_trial61 = ui.number().classes("hidden")
            u_digitalliteracy_trial62 = ui.number().classes("hidden")
            u_digitalliteracy_trial63 = ui.number().classes("hidden")
            u_digitalliteracy_trial64 = ui.number().classes("hidden")
            u_digitalliteracy_trial65 = ui.number().classes("hidden")
            u_digitalliteracy_trial71 = ui.number().classes("hidden")
            u_digitalliteracy_trial72 = ui.number().classes("hidden")
            u_digitalliteracy_trial73 = ui.number().classes("hidden")
            u_digitalliteracy_trial74 = ui.number().classes("hidden")
            u_digitalliteracy_trial75 = ui.number().classes("hidden")
            u_digitalliteracy_trial81 = ui.number().classes("hidden")
            u_digitalliteracy_trial82 = ui.number().classes("hidden")
            u_digitalliteracy_trial83 = ui.number().classes("hidden")
            u_digitalliteracy_trial84 = ui.number().classes("hidden")
            u_digitalliteracy_trial85 = ui.number().classes("hidden")
            u_digitalliteracy_trial86 = ui.number().classes("hidden")
            u_digitalliteracy_trial91 = ui.number().classes("hidden")
            u_digitalliteracy_trial92 = ui.number().classes("hidden")
            u_digitalliteracy_trial93 = ui.number().classes("hidden")
            u_digitalliteracy_trial94 = ui.number().classes("hidden")
            u_digitalliteracy_trial95 = ui.number().classes("hidden")
            u_digitalliteracy_trial101 = ui.number().classes("hidden")
            u_digitalliteracy_trial102 = ui.number().classes("hidden")
            u_digitalliteracy_trial103 = ui.number().classes("hidden")
            u_digitalliteracy_trial104 = ui.number().classes("hidden")
            u_digitalliteracy_trial105 = ui.number().classes("hidden")
            u_digitalliteracy_trial106 = ui.number().classes("hidden")
            u_digitalliteracy_trial107 = ui.number().classes("hidden")
            u_digitalliteracy_trial111 = ui.number().classes("hidden")
            u_digitalliteracy_trial112 = ui.number().classes("hidden")
            u_digitalliteracy_trial113 = ui.number().classes("hidden")
            u_digitalliteracy_trial121 = ui.number().classes("hidden")
            u_digitalliteracy_trial122 = ui.number().classes("hidden")
            u_digitalliteracy_trial123 = ui.number().classes("hidden")
            u_digitalliteracy_trial124 = ui.number().classes("hidden")
            u_digitalliteracy_trial125 = ui.number().classes("hidden")
            u_digitalliteracy_trial131 = ui.number().classes("hidden")
            u_digitalliteracy_trial132 = ui.number().classes("hidden")
            u_digitalliteracy_trial133 = ui.number().classes("hidden")
            u_digitalliteracy_trial134 = ui.number().classes("hidden")
            u_digitalliteracy_trial135 = ui.number().classes("hidden")
            u_digitalliteracy_trial141 = ui.number().classes("hidden")
            u_digitalliteracy_trial142 = ui.number().classes("hidden")
            u_digitalliteracy_trial143 = ui.number().classes("hidden")
            u_digitalliteracy_trial144 = ui.number().classes("hidden")
            u_digitalliteracy_trial145 = ui.number().classes("hidden")
            u_digitalliteracy_trial146 = ui.number().classes("hidden")
            u_digitalliteracy_trial147 = ui.number().classes("hidden")
            u_digitalliteracy_trial148 = ui.number().classes("hidden")
            u_digitalliteracy_trial149 = ui.number().classes("hidden")
            u_digitalliteracy_trial151 = ui.number().classes("hidden")
            u_digitalliteracy_trial152 = ui.number().classes("hidden")
            u_digitalliteracy_trial153 = ui.number().classes("hidden")
            u_digitalliteracy_trial154 = ui.number().classes("hidden")
            u_digitalliteracy_trial155 = ui.number().classes("hidden")

            def save(event):
                """

                :param event:
                :type event:
                """
                studentname = u_studentname.value
                digitalliteracy_trial11 = int(u_digitalliteracy_trial11.value)
                digitalliteracy_trial12 = int(u_digitalliteracy_trial12.value)
                digitalliteracy_trial13 = int(u_digitalliteracy_trial13.value)
                digitalliteracy_trial14 = int(u_digitalliteracy_trial14.value)
                digitalliteracy_trial15 = int(u_digitalliteracy_trial15.value)
                digitalliteracy_trial16 = int(u_digitalliteracy_trial16.value)
                digitalliteracy_trial21 = int(u_digitalliteracy_trial21.value)
                digitalliteracy_trial22 = int(u_digitalliteracy_trial22.value)
                digitalliteracy_trial23 = int(u_digitalliteracy_trial23.value)
                digitalliteracy_trial24 = int(u_digitalliteracy_trial24.value)
                digitalliteracy_trial25 = int(u_digitalliteracy_trial25.value)
                digitalliteracy_trial26 = int(u_digitalliteracy_trial26.value)
                digitalliteracy_trial31 = int(u_digitalliteracy_trial31.value)
                digitalliteracy_trial32 = int(u_digitalliteracy_trial32.value)
                digitalliteracy_trial33 = int(u_digitalliteracy_trial33.value)
                digitalliteracy_trial34 = int(u_digitalliteracy_trial34.value)
                digitalliteracy_trial35 = int(u_digitalliteracy_trial35.value)
                digitalliteracy_trial41 = int(u_digitalliteracy_trial41.value)
                digitalliteracy_trial42 = int(u_digitalliteracy_trial42.value)
                digitalliteracy_trial43 = int(u_digitalliteracy_trial43.value)
                digitalliteracy_trial44 = int(u_digitalliteracy_trial44.value)
                digitalliteracy_trial45 = int(u_digitalliteracy_trial45.value)
                digitalliteracy_trial51 = int(u_digitalliteracy_trial51.value)
                digitalliteracy_trial52 = int(u_digitalliteracy_trial52.value)
                digitalliteracy_trial53 = int(u_digitalliteracy_trial53.value)
                digitalliteracy_trial54 = int(u_digitalliteracy_trial54.value)
                digitalliteracy_trial55 = int(u_digitalliteracy_trial55.value)
                digitalliteracy_trial56 = int(u_digitalliteracy_trial56.value)
                digitalliteracy_trial57 = int(u_digitalliteracy_trial57.value)
                digitalliteracy_trial61 = int(u_digitalliteracy_trial61.value)
                digitalliteracy_trial62 = int(u_digitalliteracy_trial62.value)
                digitalliteracy_trial63 = int(u_digitalliteracy_trial63.value)
                digitalliteracy_trial64 = int(u_digitalliteracy_trial64.value)
                digitalliteracy_trial65 = int(u_digitalliteracy_trial65.value)
                digitalliteracy_trial71 = int(u_digitalliteracy_trial71.value)
                digitalliteracy_trial72 = int(u_digitalliteracy_trial72.value)
                digitalliteracy_trial73 = int(u_digitalliteracy_trial73.value)
                digitalliteracy_trial74 = int(u_digitalliteracy_trial74.value)
                digitalliteracy_trial75 = int(u_digitalliteracy_trial75.value)
                digitalliteracy_trial81 = int(u_digitalliteracy_trial81.value)
                digitalliteracy_trial82 = int(u_digitalliteracy_trial82.value)
                digitalliteracy_trial83 = int(u_digitalliteracy_trial83.value)
                digitalliteracy_trial84 = int(u_digitalliteracy_trial84.value)
                digitalliteracy_trial85 = int(u_digitalliteracy_trial85.value)
                digitalliteracy_trial86 = int(u_digitalliteracy_trial86.value)
                digitalliteracy_trial91 = int(u_digitalliteracy_trial91.value)
                digitalliteracy_trial92 = int(u_digitalliteracy_trial92.value)
                digitalliteracy_trial93 = int(u_digitalliteracy_trial93.value)
                digitalliteracy_trial94 = int(u_digitalliteracy_trial94.value)
                digitalliteracy_trial95 = int(u_digitalliteracy_trial95.value)
                digitalliteracy_trial101 = int(u_digitalliteracy_trial101.value)
                digitalliteracy_trial102 = int(u_digitalliteracy_trial102.value)
                digitalliteracy_trial103 = int(u_digitalliteracy_trial103.value)
                digitalliteracy_trial104 = int(u_digitalliteracy_trial104.value)
                digitalliteracy_trial105 = int(u_digitalliteracy_trial105.value)
                digitalliteracy_trial106 = int(u_digitalliteracy_trial106.value)
                digitalliteracy_trial107 = int(u_digitalliteracy_trial107.value)
                digitalliteracy_trial111 = int(u_digitalliteracy_trial111.value)
                digitalliteracy_trial112 = int(u_digitalliteracy_trial112.value)
                digitalliteracy_trial113 = int(u_digitalliteracy_trial113.value)
                digitalliteracy_trial121 = int(u_digitalliteracy_trial121.value)
                digitalliteracy_trial122 = int(u_digitalliteracy_trial122.value)
                digitalliteracy_trial123 = int(u_digitalliteracy_trial123.value)
                digitalliteracy_trial124 = int(u_digitalliteracy_trial124.value)
                digitalliteracy_trial125 = int(u_digitalliteracy_trial125.value)
                digitalliteracy_trial131 = int(u_digitalliteracy_trial131.value)
                digitalliteracy_trial132 = int(u_digitalliteracy_trial132.value)
                digitalliteracy_trial133 = int(u_digitalliteracy_trial133.value)
                digitalliteracy_trial134 = int(u_digitalliteracy_trial134.value)
                digitalliteracy_trial135 = int(u_digitalliteracy_trial135.value)
                digitalliteracy_trial141 = int(u_digitalliteracy_trial141.value)
                digitalliteracy_trial142 = int(u_digitalliteracy_trial142.value)
                digitalliteracy_trial143 = int(u_digitalliteracy_trial143.value)
                digitalliteracy_trial144 = int(u_digitalliteracy_trial144.value)
                digitalliteracy_trial145 = int(u_digitalliteracy_trial145.value)
                digitalliteracy_trial146 = int(u_digitalliteracy_trial146.value)
                digitalliteracy_trial147 = int(u_digitalliteracy_trial147.value)
                digitalliteracy_trial148 = int(u_digitalliteracy_trial148.value)
                digitalliteracy_trial149 = int(u_digitalliteracy_trial149.value)
                digitalliteracy_trial151 = int(u_digitalliteracy_trial151.value)
                digitalliteracy_trial152 = int(u_digitalliteracy_trial152.value)
                digitalliteracy_trial153 = int(u_digitalliteracy_trial153.value)
                digitalliteracy_trial154 = int(u_digitalliteracy_trial154.value)
                digitalliteracy_trial155 = int(u_digitalliteracy_trial155.value)
                studentdatabasename = f"digitalliteracy{studentname.title()}{datenow}"
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase",
                    "StudentDataFiles",
                    studentname,
                    studentdatabasename + ".json",
                )
                digitalliteracy_dictionary = {
                    "studentname": studentname,
                    "date": datenow,
                    "digitalliteracy_trial11": digitalliteracy_trial11,
                    "digitalliteracy_trial12": digitalliteracy_trial12,
                    "digitalliteracy_trial13": digitalliteracy_trial13,
                    "digitalliteracy_trial14": digitalliteracy_trial14,
                    "digitalliteracy_trial15": digitalliteracy_trial15,
                    "digitalliteracy_trial16": digitalliteracy_trial16,
                    "digitalliteracy_trial21": digitalliteracy_trial21,
                    "digitalliteracy_trial22": digitalliteracy_trial22,
                    "digitalliteracy_trial23": digitalliteracy_trial23,
                    "digitalliteracy_trial24": digitalliteracy_trial24,
                    "digitalliteracy_trial25": digitalliteracy_trial25,
                    "digitalliteracy_trial26": digitalliteracy_trial26,
                    "digitalliteracy_trial31": digitalliteracy_trial31,
                    "digitalliteracy_trial32": digitalliteracy_trial32,
                    "digitalliteracy_trial33": digitalliteracy_trial33,
                    "digitalliteracy_trial34": digitalliteracy_trial34,
                    "digitalliteracy_trial35": digitalliteracy_trial35,
                    "digitalliteracy_trial41": digitalliteracy_trial41,
                    "digitalliteracy_trial42": digitalliteracy_trial42,
                    "digitalliteracy_trial43": digitalliteracy_trial43,
                    "digitalliteracy_trial44": digitalliteracy_trial44,
                    "digitalliteracy_trial45": digitalliteracy_trial45,
                    "digitalliteracy_trial51": digitalliteracy_trial51,
                    "digitalliteracy_trial52": digitalliteracy_trial52,
                    "digitalliteracy_trial53": digitalliteracy_trial53,
                    "digitalliteracy_trial54": digitalliteracy_trial54,
                    "digitalliteracy_trial55": digitalliteracy_trial55,
                    "digitalliteracy_trial56": digitalliteracy_trial56,
                    "digitalliteracy_trial57": digitalliteracy_trial57,
                    "digitalliteracy_trial61": digitalliteracy_trial61,
                    "digitalliteracy_trial62": digitalliteracy_trial62,
                    "digitalliteracy_trial63": digitalliteracy_trial63,
                    "digitalliteracy_trial64": digitalliteracy_trial64,
                    "digitalliteracy_trial65": digitalliteracy_trial65,
                    "digitalliteracy_trial71": digitalliteracy_trial71,
                    "digitalliteracy_trial72": digitalliteracy_trial72,
                    "digitalliteracy_trial73": digitalliteracy_trial73,
                    "digitalliteracy_trial74": digitalliteracy_trial74,
                    "digitalliteracy_trial75": digitalliteracy_trial75,
                    "digitalliteracy_trial81": digitalliteracy_trial81,
                    "digitalliteracy_trial82": digitalliteracy_trial82,
                    "digitalliteracy_trial83": digitalliteracy_trial83,
                    "digitalliteracy_trial84": digitalliteracy_trial84,
                    "digitalliteracy_trial85": digitalliteracy_trial85,
                    "digitalliteracy_trial86": digitalliteracy_trial86,
                    "digitalliteracy_trial91": digitalliteracy_trial91,
                    "digitalliteracy_trial92": digitalliteracy_trial92,
                    "digitalliteracy_trial93": digitalliteracy_trial93,
                    "digitalliteracy_trial94": digitalliteracy_trial94,
                    "digitalliteracy_trial95": digitalliteracy_trial95,
                    "digitalliteracy_trial101": digitalliteracy_trial101,
                    "digitalliteracy_trial102": digitalliteracy_trial102,
                    "digitalliteracy_trial103": digitalliteracy_trial103,
                    "digitalliteracy_trial104": digitalliteracy_trial104,
                    "digitalliteracy_trial105": digitalliteracy_trial105,
                    "digitalliteracy_trial106": digitalliteracy_trial106,
                    "digitalliteracy_trial107": digitalliteracy_trial107,
                    "digitalliteracy_trial111": digitalliteracy_trial111,
                    "digitalliteracy_trial112": digitalliteracy_trial112,
                    "digitalliteracy_trial113": digitalliteracy_trial113,
                    "digitalliteracy_trial121": digitalliteracy_trial121,
                    "digitalliteracy_trial122": digitalliteracy_trial122,
                    "digitalliteracy_trial123": digitalliteracy_trial123,
                    "digitalliteracy_trial124": digitalliteracy_trial124,
                    "digitalliteracy_trial125": digitalliteracy_trial125,
                    "digitalliteracy_trial131": digitalliteracy_trial131,
                    "digitalliteracy_trial132": digitalliteracy_trial132,
                    "digitalliteracy_trial133": digitalliteracy_trial133,
                    "digitalliteracy_trial134": digitalliteracy_trial134,
                    "digitalliteracy_trial135": digitalliteracy_trial135,
                    "digitalliteracy_trial141": digitalliteracy_trial141,
                    "digitalliteracy_trial142": digitalliteracy_trial142,
                    "digitalliteracy_trial143": digitalliteracy_trial143,
                    "digitalliteracy_trial144": digitalliteracy_trial144,
                    "digitalliteracy_trial145": digitalliteracy_trial145,
                    "digitalliteracy_trial146": digitalliteracy_trial146,
                    "digitalliteracy_trial147": digitalliteracy_trial147,
                    "digitalliteracy_trial148": digitalliteracy_trial148,
                    "digitalliteracy_trial149": digitalliteracy_trial149,
                    "digitalliteracy_trial151": digitalliteracy_trial151,
                    "digitalliteracy_trial152": digitalliteracy_trial152,
                    "digitalliteracy_trial153": digitalliteracy_trial153,
                    "digitalliteracy_trial154": digitalliteracy_trial154,
                    "digitalliteracy_trial155": digitalliteracy_trial155,
                }
                with open(tmppath, "w", encoding="utf-8") as filename:
                    json.dump(digitalliteracy_dictionary, filename)
                tmppath = Path(USER_DIR).joinpath(
                    "StudentDatabase", "StudentDataFiles", "Filenames.txt"
                )
                with open(tmppath, "a", encoding="utf-8") as filename:
                    tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase",
                        "StudentDataFiles",
                        studentname,
                        studentdatabasename + ".json",
                    )
                    filename.write(f"'{tmppath}'" + "\n")

                # noinspection SqlResolve
                def data_entry():
                    """ """
                    conn = sqlite3.connect(dataBasePath)
                    c = conn.cursor()
                    c.execute(
                        """INSERT INTO DIGITALLITERACYPROGRESS (
                                                STUDENTNAME,
                                                DATE,
                                                P1_1,
                                                P1_2,
                                                P1_3,
                                                P1_4,
                                                P1_5,
                                                P1_6,
                                                P2_1,
                                                P2_2,
                                                P2_3,
                                                P2_4,
                                                P2_5,
                                                P2_6,
                                                P3_1,
                                                P3_2,
                                                P3_3,
                                                P3_4,
                                                P3_5,
                                                P4_1,
                                                P4_2,
                                                P4_3,
                                                P4_4,
                                                P4_5,
                                                P5_1,
                                                P5_2,
                                                P5_3,
                                                P5_4,
                                                P5_5,
                                                P5_6,
                                                P5_7,
                                                P6_1,
                                                P6_2,
                                                P6_3,
                                                P6_4,
                                                P6_5,
                                                P7_1,
                                                P7_2,
                                                P7_3,
                                                P7_4,
                                                P7_5,
                                                P8_1,
                                                P8_2,
                                                P8_3,
                                                P8_4,
                                                P8_5,
                                                P8_6,
                                                P9_1,
                                                P9_2,
                                                P9_3,
                                                P9_4,
                                                P9_5,
                                                P10_1,
                                                P10_2,
                                                P10_3,
                                                P10_4,
                                                P10_5,
                                                P10_6,
                                                P10_7,
                                                P11_1,
                                                P11_2,
                                                P11_3,
                                                P12_1,
                                                P12_2,
                                                P12_3,
                                                P12_4,
                                                P12_5,
                                                P13_1,
                                                P13_2,
                                                P13_3,
                                                P13_4,
                                                P13_5,
                                                P14_1,
                                                P14_2,
                                                P14_3,
                                                P14_4,
                                                P14_5,
                                                P14_6,
                                                P14_7,
                                                P14_8,
                                                P14_9,
                                                P15_1,
                                                P15_2,
                                                P15_3,
                                                P15_4,
                                                P15_5
                                                )
                                                VALUES (?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?,
                                                ?
                                                )""",
                        (
                            studentname,
                            datenow,
                            digitalliteracy_trial11,
                            digitalliteracy_trial12,
                            digitalliteracy_trial13,
                            digitalliteracy_trial14,
                            digitalliteracy_trial15,
                            digitalliteracy_trial16,
                            digitalliteracy_trial21,
                            digitalliteracy_trial22,
                            digitalliteracy_trial23,
                            digitalliteracy_trial24,
                            digitalliteracy_trial25,
                            digitalliteracy_trial26,
                            digitalliteracy_trial31,
                            digitalliteracy_trial32,
                            digitalliteracy_trial33,
                            digitalliteracy_trial34,
                            digitalliteracy_trial35,
                            digitalliteracy_trial41,
                            digitalliteracy_trial42,
                            digitalliteracy_trial43,
                            digitalliteracy_trial44,
                            digitalliteracy_trial45,
                            digitalliteracy_trial51,
                            digitalliteracy_trial52,
                            digitalliteracy_trial53,
                            digitalliteracy_trial54,
                            digitalliteracy_trial55,
                            digitalliteracy_trial56,
                            digitalliteracy_trial57,
                            digitalliteracy_trial61,
                            digitalliteracy_trial62,
                            digitalliteracy_trial63,
                            digitalliteracy_trial64,
                            digitalliteracy_trial65,
                            digitalliteracy_trial71,
                            digitalliteracy_trial72,
                            digitalliteracy_trial73,
                            digitalliteracy_trial74,
                            digitalliteracy_trial75,
                            digitalliteracy_trial81,
                            digitalliteracy_trial82,
                            digitalliteracy_trial83,
                            digitalliteracy_trial84,
                            digitalliteracy_trial85,
                            digitalliteracy_trial86,
                            digitalliteracy_trial91,
                            digitalliteracy_trial92,
                            digitalliteracy_trial93,
                            digitalliteracy_trial94,
                            digitalliteracy_trial95,
                            digitalliteracy_trial101,
                            digitalliteracy_trial102,
                            digitalliteracy_trial103,
                            digitalliteracy_trial104,
                            digitalliteracy_trial105,
                            digitalliteracy_trial106,
                            digitalliteracy_trial107,
                            digitalliteracy_trial111,
                            digitalliteracy_trial112,
                            digitalliteracy_trial113,
                            digitalliteracy_trial121,
                            digitalliteracy_trial122,
                            digitalliteracy_trial123,
                            digitalliteracy_trial124,
                            digitalliteracy_trial125,
                            digitalliteracy_trial131,
                            digitalliteracy_trial132,
                            digitalliteracy_trial133,
                            digitalliteracy_trial134,
                            digitalliteracy_trial135,
                            digitalliteracy_trial141,
                            digitalliteracy_trial142,
                            digitalliteracy_trial143,
                            digitalliteracy_trial144,
                            digitalliteracy_trial145,
                            digitalliteracy_trial146,
                            digitalliteracy_trial147,
                            digitalliteracy_trial148,
                            digitalliteracy_trial149,
                            digitalliteracy_trial151,
                            digitalliteracy_trial152,
                            digitalliteracy_trial153,
                            digitalliteracy_trial154,
                            digitalliteracy_trial155,
                        ),
                    )
                    conn.commit()
                    ui.notify(
                        "Saved successfully!",
                        position="center",
                        type="positive",
                        close_button="OK",
                    )

                data_entry()

        def graph(event):
            """ """
            dataBasePath = Path(USER_DIR).joinpath("StudentDatabase", "students.db")
            studentname = u_studentname.value
            conn = sqlite3.connect(dataBasePath)
            df_sql = pd.read_sql_query("SELECT * FROM DIGITALLITERACYPROGRESS", conn)
            df_student = df_sql[df_sql.STUDENTNAME == studentname]
            print(df_student)
            conn.close()
            df = df_student.drop(columns=["ID", "STUDENTNAME"])
            print(df)
            df = df.rename(columns={"DATE": "date"})
            df["date"] = df["date"].astype("string")
            df["date"] = pd.to_datetime(df["date"], format=date_fmt)
            df = df.set_index("date")
            for column in df.columns:
                if df[column].dtype == "object":
                    df[column] = df[column].astype("int64")
            print("Digital Literacy Skills Progression")
            print(df)
            df = df.sort_values(by="date")
            mu, sigma = 0, 0.1
            noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
            df_noisy = df + noise
            descriptiveStats = df.describe()
            print("Descriptive Statistics")
            print(descriptiveStats)
            growthCalculation = df.diff(periods=3)
            growth = growthCalculation[-1:]
            print("Growth Factor (Now vs 3 Measurements ago)")
            print(growth)

            fig = make_subplots(
                rows=4,
                cols=2,
                specs=[[{"colspan": 2}, None], [{}, {}], [{}, {}], [{}, {}]],
                subplot_titles=(
                    "Basic Operations",
                    "Word Processing",
                    "Spreadsheets",
                    "Presentation Tools",
                    "Copyright and Plagiarism",
                    "Research and Gathering Information",
                    "Communication and Collaboration",
                ),
                print_grid=True,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_1"],
                    mode="lines+markers",
                    name="Turn computer on and off",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_2"],
                    mode="lines+markers",
                    name="Use pointing device such as a mouse",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_3"],
                    mode="lines+markers",
                    name="Use icons, windows and menus to open documents ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_4"],
                    mode="lines+markers",
                    name=" File management-saving documents",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_5"],
                    mode="lines+markers",
                    name="Explain and use age-appropriate online tools and resources",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P1_6"],
                    mode="lines+markers",
                    name="Keyboarding<br> (Use proper posture and ergonomics,<br> Locate and use letter and numbers keys with left and right hand placement,<br> Locate and use correct finger, hand for space bar,return/enter and shift key,<br> Gain proficiency and speed in touch typing)",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_1"],
                    mode="lines+markers",
                    name=" write, edit, print and save",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_2"],
                    mode="lines+markers",
                    name="Use menu/tool bar to format, edit and print a document ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_3"],
                    mode="lines+markers",
                    name="Highlight text, copy and paste text ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_4"],
                    mode="lines+markers",
                    name="Copy and paste images within the document and from outside sources ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_5"],
                    mode="lines+markers",
                    name="Insert and size a graphic in a document ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P2_6"],
                    mode="lines+markers",
                    name="Proofread and edit writing using appropriate resources",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_1"],
                    mode="lines+markers",
                    name="Use spreadsheet to record, organize and graph information ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_2"],
                    mode="lines+markers",
                    name="Identify/explain spreadsheet terms and concepts ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_3"],
                    mode="lines+markers",
                    name="Perform calculations using formulas ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_4"],
                    mode="lines+markers",
                    name="Use mathematical symbols e.g. + add, - minus, *multiply, /divide, ^ exponents ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P3_5"],
                    mode="lines+markers",
                    name="Use spreadsheets to solve problems and draw conclusions ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_1"],
                    mode="lines+markers",
                    name="Create, edit and format text on a slide ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_2"],
                    mode="lines+markers",
                    name="Create a  slides and organize them to present",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_3"],
                    mode="lines+markers",
                    name="Copy and paste or import graphics;<br> change their size and position on a slide ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_4"],
                    mode="lines+markers",
                    name="Use painting and drawing tools to create and edit work ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P4_5"],
                    mode="lines+markers",
                    name="Watch online videos and use play, pause, rewind and forward buttons",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_1"],
                    mode="lines+markers",
                    name="Explain and demonstrate compliance with classroom rules regarding use of computers and networks ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_2"],
                    mode="lines+markers",
                    name="Explain responsible uses of technology and digital information;<br> describe possible consequences of inappropriate use ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_3"],
                    mode="lines+markers",
                    name="Explain Fair Use Guidelines for the use of copyrighted materials and giving credit to media creators ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_4"],
                    mode="lines+markers",
                    name="Explain the strategies for the safe and efficient use of computers",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_5"],
                    mode="lines+markers",
                    name="Demonstrate safe email practices",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_6"],
                    mode="lines+markers",
                    name="Identify cyberbullying",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P5_7"],
                    mode="lines+markers",
                    name="Describe potential risks associated with online communications ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_1"],
                    mode="lines+markers",
                    name="Use age appropriate technologies to locate, collect,<br> organize content from media collection for specific purposes, citing sources ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_2"],
                    mode="lines+markers",
                    name="Perform basic searches on databases to locate information.<br> Evaluate internet resources",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_3"],
                    mode="lines+markers",
                    name="Use content specific technology to gather and analyze data. ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_4"],
                    mode="lines+markers",
                    name="Use Web 2.0 tools to gather and share information  ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P6_5"],
                    mode="lines+markers",
                    name="Identify and analyze the purpose of a media message",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P7_1"],
                    mode="lines+markers",
                    name="Work collaboratively online with other students",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P7_2"],
                    mode="lines+markers",
                    name="Use a variety of age-appropriate technologies to communicate and exchange ideas ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P7_3"],
                    mode="lines+markers",
                    name="Create projects that use text and various forms of graphics, audio, and video to communicate ideas. ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P7_4"],
                    mode="lines+markers",
                    name="Evaluate multimedia presentations for organization, content, design, presentation and appropriateness of citations ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P7_5"],
                    mode="lines+markers",
                    name="Use district approved Web 2.0 tools for communication and collaboration ",
                    legendgroup="Phase 1",
                    legendgrouptitle_text="Phase 1",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=2,
                col=2,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=2,
                col=2,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=2,
                col=2,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=2,
                col=2,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=3,
                col=2,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=3,
                col=2,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=3,
                col=2,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=3,
                col=2,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=4,
                col=2,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=4,
                col=2,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=4,
                col=2,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=4,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=1,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=2,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=2,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=3,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=3,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=4,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=4,
                col=2,
            )
            fig.update_layout(
                xaxis_tickformat="%d %b",
                xaxis2_tickformat="%d %b",
                xaxis3_tickformat="%d %b",
                xaxis4_tickformat="%d %b",
                xaxis5_tickformat="%d %b",
                xaxis6_tickformat="%d %b",
                xaxis7_tickformat="%d %b",
                template="simple_white",
                title_text=f"{studentname}: Elementary Digital Literacy Skills Progression",
                legend=dict(font=dict(size=10)),
                hovermode="x unified",
                hoverlabel=dict(namelength=-1),
            )
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                studentname,
                "ElementaryDigitalLiteracyProgression.html",
            )
            fig.write_html(tmppath, auto_open=True)
            # fig.show()
            ui.notify(
                "Graph Successful. The Graphs will open in a Browser Window!",
                position="center",
                type="positive",
                close_button="OK",
            )
            fig = make_subplots(
                rows=4,
                cols=2,
                specs=[
                    [{}, {}],
                    [{}, {}],
                    [{}, {}],
                    [{}, {}],
                ],
                subplot_titles=(
                    "Basic Operations",
                    "Word Processing",
                    "Spreadsheets",
                    "Mathematical Operations",
                    "Presentation Tools",
                    "Copyright and Plagiarism",
                    "Research and Gathering Information",
                    "Communication and Collaboration",
                ),
                print_grid=True,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P8_1"],
                    mode="lines+markers",
                    name="Identify successful troubleshooting strategies for minor hardware and software issues/problems (e.g., “frozen screen”) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P8_2"],
                    mode="lines+markers",
                    name="Independently operate peripheral equipment (e.g., scanner, digital camera, camcorder), if available ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P8_3"],
                    mode="lines+markers",
                    name="Compress and expand large files  ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P8_4"],
                    mode="lines+markers",
                    name="Identify and use a variety of storage media (e.g., CDs, DVDs, flash drives, school servers, and online storage spaces), and provide a rationale for using a certain medium for a specific purpose ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P8_5"],
                    mode="lines+markers",
                    name="Demonstrate automaticity in keyboarding skills by increasing accuracy and speed (For students with disabilities, demonstrate alternate input techniques as appropriate.) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P8_6"],
                    mode="lines+markers",
                    name="Identify and assess the capabilities and limitations of emerging technologies ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P9_1"],
                    mode="lines+markers",
                    name="Demonstrate use of intermediate features in word processing application (e.g., tabs, indents, headers and footers, end notes, bullet and numbering, tables) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P9_2"],
                    mode="lines+markers",
                    name="Apply advanced formatting and page layout features when appropriate (e.g., columns, templates, and styles) to improve the appearance of documents and materials ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P9_3"],
                    mode="lines+markers",
                    name="Highlight text, copy and paste text ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P9_4"],
                    mode="lines+markers",
                    name="Use the Comment function in Review for peer editing of documents ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P9_5"],
                    mode="lines+markers",
                    name="Use the Track Changes feature in Review for peer editing of documents ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=1,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P10_1"],
                    mode="lines+markers",
                    name="Use spreadsheets to calculate, graph, organize, and present data in a variety of real-world settings and choose the most appropriate type to represent given data ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P10_2"],
                    mode="lines+markers",
                    name="Enter formulas and functions; use the auto-fill feature in a spreadsheet application ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P10_3"],
                    mode="lines+markers",
                    name="Use functions of a spreadsheet application (e.g., sort, filter, find) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P10_4"],
                    mode="lines+markers",
                    name="Use various number formats (e.g. scientific notations, percentages, exponents) as appropriate ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P10_5"],
                    mode="lines+markers",
                    name="Use various number formats (e.g. scientific notations, percentages, exponents) as appropriate ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P10_6"],
                    mode="lines+markers",
                    name="Differentiate between formulas with absolute and relative cell references ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P10_7"],
                    mode="lines+markers",
                    name="Use multiple sheets within a workbook, and create links among worksheets to solve problems ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P11_1"],
                    mode="lines+markers",
                    name="Draw two and three dimensional geometric shapes using a variety of technology tools ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P11_2"],
                    mode="lines+markers",
                    name="Use and interpret scientific notations using a variety of technology applications ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P11_3"],
                    mode="lines+markers",
                    name="Explain and demonstrate how specialized technology tools can be used for problem solving, decision making, and creativity in all subject areas (e.g., simulation software, environmental probes, computer aided design, geographic information systems, dynamic geometric software, graphing calculators) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=2,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P12_1"],
                    mode="lines+markers",
                    name="Create presentations for a variety of audiences and purposes with use of appropriate transitions and animations to add interest ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P12_2"],
                    mode="lines+markers",
                    name="Use a variety of technology tools (e.g., dictionary, thesaurus, grammar checker, calculator/graphing calculator) to maximize the accuracy of work. Make strategic use of digital media to enhance understanding ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P12_3"],
                    mode="lines+markers",
                    name="Use painting and drawing tools/ applications to create and edit work ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P12_4"],
                    mode="lines+markers",
                    name="Use note-taking skills while viewing online videos and using the play, pause, rewind and stop buttons ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P12_5"],
                    mode="lines+markers",
                    name="Independently use appropriate technology tools (e.g., graphic organizer, audio, visual) to define problems and propose hypotheses ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P13_1"],
                    mode="lines+markers",
                    name="Comply with the district’s Acceptable Use Policy related to ethical use, cyberbullying, privacy, plagiarism, spam, viruses, hacking, and file sharing ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P13_2"],
                    mode="lines+markers",
                    name="Explain Fair Use guidelines for using copyrighted materials and possible consequences (e.g., images, music, video, text) in school projects ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P13_3"],
                    mode="lines+markers",
                    name="Analyze and explain how media and technology can be used to distort, exaggerate, and misrepresent information ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P13_4"],
                    mode="lines+markers",
                    name="Give examples of hardware and applications that enable people with disabilities to use technology ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P13_5"],
                    mode="lines+markers",
                    name="Explain the potential risks associated with the use of networked digital environments (e.g., internet, mobile phones, wireless, LANs) and sharing personal information ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=3,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_1"],
                    mode="lines+markers",
                    name="Identify probable types and locations of Web sites by examining their domain names (e.g., edu, com, org, gov, au) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_2"],
                    mode="lines+markers",
                    name="Use effective search strategies for locating and retrieving electronic information (e.g., using syntax and Boolean logic operators) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_3"],
                    mode="lines+markers",
                    name="Use search engines and online directories. Explain the differences among various search engines and how they rank results ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_4"],
                    mode="lines+markers",
                    name="Use appropriate academic language in online learning environments (e.g., post, thread, intranet, discussion forum, drop box, account, and password) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_5"],
                    mode="lines+markers",
                    name="Explain how technology can support communication and collaboration, personal and professional productivity, and lifelong learning ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_6"],
                    mode="lines+markers",
                    name="Write correct in-text citations and reference lists for text and images gathered from electronic sources ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_7"],
                    mode="lines+markers",
                    name="Use Web browsing to access information (e.g., enter a URL, access links, create bookmarks/favorites, print Web pages) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_8"],
                    mode="lines+markers",
                    name="Use and modify databases and spreadsheets to analyze data and propose solutions ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P14_9"],
                    mode="lines+markers",
                    name="Develop and use guidelines to evaluate the content, organization, design, use of citations, and presentation of technologically enhanced projects ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P15_1"],
                    mode="lines+markers",
                    name="Use a variety of media to present information for specific purposes (e.g., reports, research papers, presentations, newsletters, Web sites, podcasts, blogs), citing sources ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P15_2"],
                    mode="lines+markers",
                    name="Demonstrate how the use of various techniques and effect (e.g., editing, music, color, rhetorical devices) can be used to convey meaning in media ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P15_3"],
                    mode="lines+markers",
                    name="Use a variety of district approved Web 2.0 tools (e.g., email discussion groups, blogs, etc.) to collaborate and communicate with peers, experts, and other audiences using appropriate academic language ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P15_4"],
                    mode="lines+markers",
                    name="Use teacher developed guidelines to evaluate multimedia presentations for organization, content, design, presentation and appropriateness of citations ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="  %{y:.1f} ",
                ),
                row=4,
                col=2,
            )

            fig.add_trace(
                go.Scatter(
                    x=df_noisy.index,
                    y=df_noisy["P15_5"],
                    mode="lines+markers",
                    name="Plan and implement a collaborative project with students in other classrooms and schools using telecommunications tools (e.g., e-mail, discussion forums, groupware, interactive Web sites, videoconferencing) ",
                    legendgroup="Phase 2",
                    legendgrouptitle_text="Phase 2",
                    showlegend=False,
                    hovertemplate="%{text}   %{y:.0f} ",
                ),
                row=4,
                col=2,
            )

            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=1,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=1,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=2,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=2,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=3,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=3,
                col=2,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=4,
                col=1,
            )
            fig.update_yaxes(
                range=[-0.5, 3.5],
                fixedrange=True,
                ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                tickvals=[0.1, 1, 2, 3],
                row=4,
                col=2,
            )

            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=1,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=1,
                col=2,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=1,
                col=2,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=1,
                col=2,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=1,
                col=2,
            )

            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=2,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=2,
                col=2,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=2,
                col=2,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=2,
                col=2,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=2,
                col=2,
            )

            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=3,
                col=2,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=3,
                col=2,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=3,
                col=2,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=3,
                col=2,
            )

            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=4,
                col=1,
            )
            fig.add_hrect(
                y0=-0.5,
                y1=0.5,
                line_width=0,
                fillcolor="red",
                opacity=0.2,
                row=4,
                col=2,
            )
            fig.add_hrect(
                y0=0.5,
                y1=1.5,
                line_width=0,
                fillcolor="orange",
                opacity=0.2,
                row=4,
                col=2,
            )
            fig.add_hrect(
                y0=1.5,
                y1=2.5,
                line_width=0,
                fillcolor="yellow",
                opacity=0.2,
                row=4,
                col=2,
            )
            fig.add_hrect(
                y0=2.5,
                y1=3.5,
                line_width=0,
                fillcolor="green",
                opacity=0.2,
                row=4,
                col=2,
            )

            fig.update_layout(
                xaxis_tickformat="%d %b",
                xaxis2_tickformat="%d %b",
                xaxis3_tickformat="%d %b",
                xaxis4_tickformat="%d %b",
                xaxis5_tickformat="%d %b",
                xaxis6_tickformat="%d %b",
                xaxis7_tickformat="%d %b",
                xaxis8_tickformat="%d %b",
                # xaxis9_tickformat="%d %b",
                template="simple_white",
                title_text=f"{studentname}:Secondary Digital Literacy Skills Progression",
                legend=dict(font=dict(size=10)),
                hovermode="x unified",
                hoverlabel=dict(namelength=-1),
            )
            tmppath = Path(USER_DIR).joinpath(
                "StudentDatabase",
                "StudentDataFiles",
                studentname,
                "Secondary DigitalLiteracyProgression.html",
            )
            fig.write_html(tmppath, auto_open=True)
            # fig.show()
            ui.notify(
                "Graph Successful. The Graphs will open in a Browser Window!",
                position="center",
                type="positive",
                close_button="OK",
            )

        # GUI Input
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.select(
                options=students,
                with_input=True,
                on_change=lambda e: ui.notify(e.value),
            ).bind_value(u_studentname, "value").classes("w-[300px]").props(
                'aria-label="Select Student from the Dropdown. It will autocomplete as you type"'
            ).tooltip(
                "Type Student Name, it will autocomplete AS you type"
            )
            with ui.input("Date").classes("w-[300px]").props(
                'aria-label="Date. Please type in date using the YYYY-MM-DD format"'
            ).tooltip("Date. Please type in date using the YYYY-MM-DD format") as date:
                with date.add_slot("append"):
                    ui.icon("edit_calendar").on("click", lambda: menu.open()).classes(
                        "cursor-pointer"
                    )
                with ui.menu() as menu:
                    ui.date().bind_value(date)
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label(
                "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent"
            ).props(
                'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
            )
            ui.input().props(
                'aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center'
            ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 1: Elementary Digital Literacy Skills").classes(
                "justify-center items-center"
            )
            ui.input().props(
                'aria-label="PHASE 1: Elementary Digital Literacy Skills"'
            ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Basic Operations").classes("justify-center items-center")
            ui.input().props('aria-label=Basic Operations"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Turn computer on and off",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial11.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use pointing device such as a mouse to manipulate shapes, icons; click on urls, radio buttons, check boxes; use scroll bar ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial12.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use desktop icons, windows and menus to open applications and documents ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial13.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Save documents ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial14.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain and use age-appropriate online tools and resources (e.g. tutorial, assessment, web browser) ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial15.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Keyboarding (Use proper posture and ergonomics, Locate and use letter and numbers keys with left and right hand placement, Locate and use correct finger, hand for space bar,return/enter and shift key, Gain proficiency and speed in touch typing)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial16.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Word Processing").classes("justify-center items-center")
            ui.input().props('aria-label="Word Processing"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use a word processing application to write, edit, print and save simple assignments ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial21.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use menu/tool bar functions (e.g. font/size/style/, line spacing, margins) to format, edit and print a document ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial22.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Highlight text, copy and paste text ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial23.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Copy and paste images within the document and from outside sources ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial24.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Insert and size a graphic in a document ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial25.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Proofread and edit writing using appropriate resources (e.g. dictionary, spell checker, grammar, and thesaurus) ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial26.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Spreadsheets").classes("justify-center items-center")
            ui.input().props('aria-label="Spreadsheets"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Demonstrate an understanding of the spreadsheet as a tool to record, organize and graph information. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial31.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Identify and explain terms and concepts related to spreadsheets (i.e. cell, column, row, values, labels, chart graph) ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial32.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Enter/edit data in spreadsheets and perform calculations using formulas ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial33.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use mathematical symbols e.g. + add, - minus, *multiply, /divide, ^ exponents ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial34.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use spreadsheets and other applications to make predictions, solve problems and draw conclusions ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial35.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Presentation Tools").classes("justify-center items-center")
            ui.input().props('aria-label="Presentation Tools"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Create, edit and format text on a slide ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial41.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Create a series of slides and organize them to present research or convey an idea ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial42.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Copy and paste or import graphics; change their size and position on a slide ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial43.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use painting and drawing tools/ applications to create and edit work ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial44.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Watch online videos and use play, pause, rewind and forward buttons while taking notes ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial45.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Copyright and Plagiarism").classes("justify-center items-center")
            ui.input().props('aria-label="Copyright and Plagiarism"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain and demonstrate compliance with classroom, school rules (Acceptable Use Policy) regarding responsible use of computers and networks ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial51.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain responsible uses of technology and digital information; describe possible consequences of inappropriate use ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial52.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain Fair Use Guidelines for the use of copyrighted materials,(e.g. text, images, music, video in student projects) and giving credit to media creators ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial53.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Identify and explain the strategies for the safe and efficient use of computers (e.g. passwords, virus protection software, spam filters, popup blockers)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial54.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Demonstrate safe email practices, recognition of the potentially public exposure of email and appropriate email etiquette ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial55.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Identify cyberbullying and describe strategies to deal with such a situation  ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial56.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Recognize and describe the potential risks and dangers associated with various forms of online communications ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial57.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Research and Gathering Information").classes(
                "justify-center items-center"
            )
            ui.input().props('aria-label="Research and Gathering Information"').classes(
                "sr-only"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use age appropriate technologies to locate, collect, organize content from media collection for specific purposes, citing sources ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial61.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Perform basic searches on databases, (e.g. library, card catalog, encyclopedia) to locate information. Evaluate teacher-selected or self-selected Internet resources in terms of their usefulness for research ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial62.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use content specific technology tools (e.g. environmental probes, sensors, and measuring devices, simulations) to gather and analyze data. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial63.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use Web 2.0 tools (e.g. online discussions, blogs and wikis) to gather and share information  ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial64.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Identify and analyze the purpose of a media message (to inform, persuade and entertain) ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial65.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Communication and Collaboration").classes(
                "justify-center items-center"
            )
            ui.input().props('aria-label="Communication and Collaboration"').classes(
                "sr-only"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Work collaboratively online with other students under teacher supervision  ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial71.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use a variety of age-appropriate technologies (e.g. drawing program, presentation software) to communicate and exchange ideas ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial72.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Create projects that use text and various forms of graphics, audio, and video, (with proper citations) to communicate ideas. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial73.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use teacher developed guidelines to evaluate multimedia presentations for organization, content, design, presentation and appropriateness of citations. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial74.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use district approved Web 2.0 tools for communication and collaboration ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial75.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("PHASE 2: Secondary Digital Literacy").classes(
                "justify-center items-center"
            )
            ui.input().props(
                'aria-label="PHASE 2: Secondary Digital Literacy"'
            ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Basic Operations").classes("justify-center items-center")
            ui.input().props('aria-label="Basic Operations"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label=" Identify successful troubleshooting strategies for minor hardware and software issues/problems (e.g., “frozen screen”)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial81.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Independently operate peripheral equipment (e.g., scanner, digital camera, camcorder), if available.  ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial82.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Compress and expand large files  ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial83.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Identify and use a variety of storage media (e.g., CDs, DVDs, flash drives, school servers, and online storage spaces), and provide a rationale for using a certain medium for a specific purpose.",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial84.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Demonstrate automaticity in keyboarding skills by increasing accuracy and speed (For students with disabilities, demonstrate alternate input techniques as appropriate.)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial85.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Identify and assess the capabilities and limitations of emerging technologies. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial86.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Word Processing").classes("justify-center items-center")
            ui.input().props('aria-label="Word Processing"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Demonstrate use of intermediate features in word processing application (e.g., tabs, indents, headers and footers, end notes, bullet and numbering, tables). ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial91.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Apply advanced formatting and page layout features when appropriate (e.g., columns, templates, and styles) to improve the appearance of documents and materials.",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial92.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Highlight text, copy and paste text ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial93.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use the Comment function in Review for peer editing of documents ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial94.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use the Track Changes feature in Review for peer editing of documents ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial95.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Spreadsheets").classes("justify-center items-center")
            ui.input().props('aria-label="Spreadsheets"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use spreadsheets to calculate, graph, organize, and present data in a variety of real-world settings and choose the most appropriate type to represent given data",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial101.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Enter formulas and functions; use the auto-fill feature in a spreadsheet application.",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial102.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use functions of a spreadsheet application (e.g., sort, filter, find).",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial103.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use various number formats (e.g. scientific notations, percentages, exponents) as appropriate ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial104.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use various number formats (e.g. scientific notations, percentages, exponents) as appropriate ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial105.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Differentiate between formulas with absolute and relative cell references. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial106.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use multiple sheets within a workbook, and create links among worksheets to solve problems. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial107.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Mathematical Applications").classes("justify-center items-center")
            ui.input().props('aria-label="Mathematical Applications"').classes(
                "sr-only"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Draw two and three dimensional geometric shapes using a variety of technology tools ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial111.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use and interpret scientific notations using a variety of technology applications ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial112.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain and demonstrate how specialized technology tools can be used for problem solving, decision making, and creativity in all subject areas (e.g., simulation software, environmental probes, computer aided design, geographic information systems, dynamic geometric software, graphing calculators).",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial113.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Presentation Tools").classes("justify-center items-center")
            ui.input().props('aria-label="Presentation Tools"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Create presentations for a variety of audiences and purposes with use of appropriate transitions and animations to add interest. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial121.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label=" Use a variety of technology tools (e.g., dictionary, thesaurus, grammar checker, calculator/graphing calculator) to maximize the accuracy of work. Make strategic use of digital media to enhance understanding ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial122.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use painting and drawing tools/ applications to create and edit work ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial123.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use note-taking skills while viewing online videos and using the play, pause, rewind and stop buttons. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial124.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Independently use appropriate technology tools (e.g., graphic organizer, audio, visual) to define problems and propose hypotheses. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial125.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Copyright and Plagiarism").classes("justify-center items-center")
            ui.input().props('aria-label="Copyright and Plagiarism"').classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Comply with the district’s Acceptable Use Policy related to ethical use, cyberbullying, privacy, plagiarism, spam, viruses, hacking, and file sharing. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial131.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain Fair Use guidelines for using copyrighted materials and possible consequences (e.g., images, music, video, text) in school projects. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial132.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Analyze and explain how media and technology can be used to distort, exaggerate, and misrepresent information. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial133.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Give examples of hardware and applications that enable people with disabilities to use technology. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial134.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain the potential risks associated with the use of networked digital environments (e.g., internet, mobile phones, wireless, LANs) and sharing personal information. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial135.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Research and Gathering Information").classes(
                "justify-center items-center"
            )
            ui.input().props('aria-label="Research and Gathering Information"').classes(
                "sr-only"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label=" Identify probable types and locations of Web sites by examining their domain names (e.g., edu, com, org, gov, au)",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial141.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use effective search strategies for locating and retrieving electronic information (e.g., using syntax and Boolean logic operators) ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial142.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use search engines and online directories. Explain the differences among various search engines and how they rank results. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial143.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use appropriate academic language in online learning environments (e.g., post, thread, intranet, discussion forum, drop box, account, and password). ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial144.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Explain how technology can support communication and collaboration, personal and professional productivity, and lifelong learning. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial145.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Write correct in-text citations and reference lists for text and images gathered from electronic sources. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial146.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use Web browsing to access information (e.g., enter a URL, access links, create bookmarks/favorites, print Web pages) ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial147.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use and modify databases and spreadsheets to analyze data and propose solutions. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial148.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Develop and use guidelines to evaluate the content, organization, design, use of citations, and presentation of technologically enhanced projects. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial149.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label("Communication and Collaboration").classes(
                "justify-center items-center"
            )
            ui.input().props('aria-label="Communication and Collaboration"').classes(
                "sr-only"
            )
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use a variety of media to present information for specific purposes (e.g., reports, research papers, presentations, newsletters, Web sites, podcasts, blogs), citing sources. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial151.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Demonstrate how the use of various techniques and effect (e.g., editing, music, color, rhetorical devices) can be used to convey meaning in media. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial152.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use a variety of district approved Web 2.0 tools (e.g., email discussion groups, blogs, etc.) to collaborate and communicate with peers, experts, and other audiences using appropriate academic language. ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial153.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label="Use teacher developed guidelines to evaluate multimedia presentations for organization, content, design, presentation and appropriateness of citations ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial154.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                label=" Plan and implement a collaborative project with students in other classrooms and schools using telecommunications tools (e.g., e-mail, discussion forums, groupware, interactive Web sites, videoconferencing) ",
                min=0,
                max=3,
                format="%.0f",
                on_change=lambda e: u_digitalliteracy_trial155.set_value(e.value),
            ).classes("w-[600px]").props('aria-label="  "')

        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes("text-white")
            ui.button("GRAPH", color="#172554", on_click=graph).classes("text-white")
            ui.button("EXIT", color="#172554", on_click=app.shutdown).classes(
                "text-white"
            )
