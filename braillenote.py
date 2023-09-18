#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers
of students with Visual Impairments
"""
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.
#    #
#    email: hunsakerconsulting@gmail.com
#    #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");
#    #
#    you may not use this file except in compliance with the License.
#    #
#    You may obtain a copy of the License at
#    #
#                                                                             #
#    http://www.apache.org/licenses/LICENSE-2.0
#    #
#                                                                             #
#    Unless Required by applicable law or agreed to in writing,
#    software      #
#    distributed under the License is distributed on an "AS IS"
#    BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#    implied. #
#    See the License for the specific language governing permissions
#    and      #
#    limitations under the License.
#    #
###############################################################################

# !/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers
of students with Visual Impairments
"""
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.
#    #
#    email: hunsakerconsulting@gmail.com
#    #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");
#    #
#    you may not use this file except in compliance with the License.
#    #
#    You may obtain a copy of the License at
#    #
#                                                                             #
#    http://www.apache.org/licenses/LICENSE-2.0
#    #
#                                                                             #
#    Unless Required by applicable law or agreed to in writing,
#    software      #
#    distributed under the License is distributed on an "AS IS"
#    BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#    implied. #
#    See the License for the specific language governing permissions
#    and      #
#    limitations under the License.
#    #
###############################################################################

import os
import sqlite3
from csv import writer
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nicegui import app, ui
from plotly.subplots import make_subplots

import theme
from helpers import (dataBasePath, datenow, USER_DIR, )
from roster import students


def create() -> None:
    ##########################################################################
    # BRAILLENOTE TOUCH  SKILLS
    ##########################################################################
    @ui.page('/braillenotetouchskills')
    def braillenotetouchskills():
        with theme.frame('- BRAILLENOTE TOUCH PLUS SKILLS -'):
            ui.label('BRAILLENOTE TOUCH PLUS SKILLS').classes(
                    'text-h4 '
                    'text-grey-8'
                    )
            
            # ASSIGN VARIABLES
            u_studentname = ui.select(
                    options=students, value='DonaldChamberlain'
                    ).classes(
                    'hidden'
                    )
            date = ui.date().classes('hidden')
            u_bnt_trial11 = ui.number().classes('hidden')
            u_bnt_trial12 = ui.number().classes('hidden')
            u_bnt_trial13 = ui.number().classes('hidden')
            u_bnt_trial14 = ui.number().classes('hidden')
            u_bnt_trial15 = ui.number().classes('hidden')
            u_bnt_trial16 = ui.number().classes('hidden')
            u_bnt_trial17 = ui.number().classes('hidden')
            u_bnt_trial18 = ui.number().classes('hidden')
            u_bnt_trial19 = ui.number().classes('hidden')
            u_bnt_trial21 = ui.number().classes('hidden')
            u_bnt_trial22 = ui.number().classes('hidden')
            u_bnt_trial23 = ui.number().classes('hidden')
            u_bnt_trial24 = ui.number().classes('hidden')
            u_bnt_trial25 = ui.number().classes('hidden')
            u_bnt_trial26 = ui.number().classes('hidden')
            u_bnt_trial27 = ui.number().classes('hidden')
            u_bnt_trial31 = ui.number().classes('hidden')
            u_bnt_trial32 = ui.number().classes('hidden')
            u_bnt_trial33 = ui.number().classes('hidden')
            u_bnt_trial34 = ui.number().classes('hidden')
            u_bnt_trial35 = ui.number().classes('hidden')
            u_bnt_trial36 = ui.number().classes('hidden')
            u_bnt_trial37 = ui.number().classes('hidden')
            u_bnt_trial41 = ui.number().classes('hidden')
            u_bnt_trial42 = ui.number().classes('hidden')
            u_bnt_trial43 = ui.number().classes('hidden')
            u_bnt_trial51 = ui.number().classes('hidden')
            u_bnt_trial52 = ui.number().classes('hidden')
            u_bnt_trial53 = ui.number().classes('hidden')
            u_bnt_trial54 = ui.number().classes('hidden')
            u_bnt_trial55 = ui.number().classes('hidden')
            u_bnt_trial56 = ui.number().classes('hidden')
            u_bnt_trial57 = ui.number().classes('hidden')
            u_bnt_trial61 = ui.number().classes('hidden')
            u_bnt_trial62 = ui.number().classes('hidden')
            u_bnt_trial63 = ui.number().classes('hidden')
            u_bnt_trial71 = ui.number().classes('hidden')
            u_bnt_trial72 = ui.number().classes('hidden')
            u_bnt_trial73 = ui.number().classes('hidden')
            u_bnt_trial74 = ui.number().classes('hidden')
            u_bnt_trial81 = ui.number().classes('hidden')
            u_bnt_trial82 = ui.number().classes('hidden')
            u_bnt_trial83 = ui.number().classes('hidden')
            u_bnt_trial84 = ui.number().classes('hidden')
            u_bnt_trial85 = ui.number().classes('hidden')
            u_bnt_trial91 = ui.number().classes('hidden')
            u_bnt_trial92 = ui.number().classes('hidden')
            u_bnt_trial93 = ui.number().classes('hidden')
            u_bnt_trial94 = ui.number().classes('hidden')
            u_bnt_trial101 = ui.number().classes('hidden')
            u_bnt_trial102 = ui.number().classes('hidden')
            u_bnt_trial103 = ui.number().classes('hidden')
            u_bnt_trial111 = ui.number().classes('hidden')
            u_bnt_trial112 = ui.number().classes('hidden')
            u_bnt_trial113 = ui.number().classes('hidden')
            u_bnt_trial114 = ui.number().classes('hidden')
            u_bnt_trial115 = ui.number().classes('hidden')
            u_bnt_trial121 = ui.number().classes('hidden')
            u_bnt_trial122 = ui.number().classes('hidden')
            u_bnt_trial123 = ui.number().classes('hidden')
            u_bnt_trial124 = ui.number().classes('hidden')
            
            def save(event):
                '''
                :param event
                :type event
                '''
                studentname = u_studentname.value
                date = datenow
                bnt_trial11 = int(u_bnt_trial11.value)
                bnt_trial12 = int(u_bnt_trial12.value)
                bnt_trial13 = int(u_bnt_trial13.value)
                bnt_trial14 = int(u_bnt_trial14.value)
                bnt_trial15 = int(u_bnt_trial15.value)
                bnt_trial16 = int(u_bnt_trial16.value)
                bnt_trial17 = int(u_bnt_trial17.value)
                bnt_trial18 = int(u_bnt_trial18.value)
                bnt_trial19 = int(u_bnt_trial19.value)
                bnt_trial21 = int(u_bnt_trial21.value)
                bnt_trial22 = int(u_bnt_trial22.value)
                bnt_trial23 = int(u_bnt_trial23.value)
                bnt_trial24 = int(u_bnt_trial24.value)
                bnt_trial25 = int(u_bnt_trial25.value)
                bnt_trial26 = int(u_bnt_trial26.value)
                bnt_trial27 = int(u_bnt_trial27.value)
                bnt_trial31 = int(u_bnt_trial31.value)
                bnt_trial32 = int(u_bnt_trial32.value)
                bnt_trial33 = int(u_bnt_trial33.value)
                bnt_trial34 = int(u_bnt_trial34.value)
                bnt_trial35 = int(u_bnt_trial35.value)
                bnt_trial36 = int(u_bnt_trial36.value)
                bnt_trial37 = int(u_bnt_trial37.value)
                bnt_trial41 = int(u_bnt_trial41.value)
                bnt_trial42 = int(u_bnt_trial42.value)
                bnt_trial43 = int(u_bnt_trial43.value)
                bnt_trial51 = int(u_bnt_trial51.value)
                bnt_trial52 = int(u_bnt_trial52.value)
                bnt_trial53 = int(u_bnt_trial53.value)
                bnt_trial54 = int(u_bnt_trial54.value)
                bnt_trial55 = int(u_bnt_trial55.value)
                bnt_trial56 = int(u_bnt_trial56.value)
                bnt_trial57 = int(u_bnt_trial57.value)
                bnt_trial61 = int(u_bnt_trial61.value)
                bnt_trial62 = int(u_bnt_trial62.value)
                bnt_trial63 = int(u_bnt_trial63.value)
                bnt_trial71 = int(u_bnt_trial71.value)
                bnt_trial72 = int(u_bnt_trial72.value)
                bnt_trial73 = int(u_bnt_trial73.value)
                bnt_trial74 = int(u_bnt_trial74.value)
                bnt_trial81 = int(u_bnt_trial81.value)
                bnt_trial82 = int(u_bnt_trial82.value)
                bnt_trial83 = int(u_bnt_trial83.value)
                bnt_trial84 = int(u_bnt_trial84.value)
                bnt_trial85 = int(u_bnt_trial85.value)
                bnt_trial91 = int(u_bnt_trial91.value)
                bnt_trial92 = int(u_bnt_trial92.value)
                bnt_trial93 = int(u_bnt_trial93.value)
                bnt_trial94 = int(u_bnt_trial94.value)
                bnt_trial101 = int(u_bnt_trial101.value)
                bnt_trial102 = int(u_bnt_trial102.value)
                bnt_trial103 = int(u_bnt_trial103.value)
                bnt_trial111 = int(u_bnt_trial111.value)
                bnt_trial112 = int(u_bnt_trial112.value)
                bnt_trial113 = int(u_bnt_trial113.value)
                bnt_trial114 = int(u_bnt_trial114.value)
                bnt_trial115 = int(u_bnt_trial115.value)
                bnt_trial121 = int(u_bnt_trial121.value)
                bnt_trial122 = int(u_bnt_trial122.value)
                bnt_trial123 = int(u_bnt_trial123.value)
                bnt_trial124 = int(u_bnt_trial124.value)
                studentdatabasename = (f"bnt{studentname.title()}"
                                       f"{datenow}")
                tmppath = Path(USER_DIR).joinpath(
                        "StudentDatabase", "StudentDataFiles", studentname, studentdatabasename + ".txt", )
                with open(tmppath, "w") as filename:
                    filename.write("studentname" + ", ")
                    filename.write("date" + ", ")
                    filename.write("bnt_trial11" + ", ")
                    filename.write("bnt_trial12" + ", ")
                    filename.write("bnt_trial13" + ", ")
                    filename.write("bnt_trial14" + ", ")
                    filename.write("bnt_trial15" + ", ")
                    filename.write("bnt_trial16" + ", ")
                    filename.write("bnt_trial17" + ", ")
                    filename.write("bnt_trial18" + ", ")
                    filename.write("bnt_trial19" + ", ")
                    filename.write("bnt_trial21" + ", ")
                    filename.write("bnt_trial22" + ", ")
                    filename.write("bnt_trial23" + ", ")
                    filename.write("bnt_trial24" + ", ")
                    filename.write("bnt_trial25" + ", ")
                    filename.write("bnt_trial26" + ", ")
                    filename.write("bnt_trial27" + ", ")
                    filename.write("bnt_trial31" + ", ")
                    filename.write("bnt_trial32" + ", ")
                    filename.write("bnt_trial33" + ", ")
                    filename.write("bnt_trial34" + ", ")
                    filename.write("bnt_trial35" + ", ")
                    filename.write("bnt_trial36" + ", ")
                    filename.write("bnt_trial37" + ", ")
                    filename.write("bnt_trial41" + ", ")
                    filename.write("bnt_trial42" + ", ")
                    filename.write("bnt_trial43" + ", ")
                    filename.write("bnt_trial51" + ", ")
                    filename.write("bnt_trial52" + ", ")
                    filename.write("bnt_trial53" + ", ")
                    filename.write("bnt_trial54" + ", ")
                    filename.write("bnt_trial55" + ", ")
                    filename.write("bnt_trial56" + ", ")
                    filename.write("bnt_trial57" + ", ")
                    filename.write("bnt_trial61" + ", ")
                    filename.write("bnt_trial62" + ", ")
                    filename.write("bnt_trial63" + ", ")
                    filename.write("bnt_trial71" + ", ")
                    filename.write("bnt_trial72" + ", ")
                    filename.write("bnt_trial73" + ", ")
                    filename.write("bnt_trial74" + ", ")
                    filename.write("bnt_trial81" + ", ")
                    filename.write("bnt_trial82" + ", ")
                    filename.write("bnt_trial83" + ", ")
                    filename.write("bnt_trial84" + ", ")
                    filename.write("bnt_trial85" + ", ")
                    filename.write("bnt_trial91" + ", ")
                    filename.write("bnt_trial92" + ", ")
                    filename.write("bnt_trial93" + ", ")
                    filename.write("bnt_trial94" + ", ")
                    filename.write("bnt_trial101" + ", ")
                    filename.write("bnt_trial102" + ", ")
                    filename.write("bnt_trial103" + ", ")
                    filename.write("bnt_trial111" + ", ")
                    filename.write("bnt_trial112" + ", ")
                    filename.write("bnt_trial113" + ", ")
                    filename.write("bnt_trial114" + ", ")
                    filename.write("bnt_trial115" + ", ")
                    filename.write("bnt_trial121" + ", ")
                    filename.write("bnt_trial122" + ", ")
                    filename.write("bnt_trial123" + ", ")
                    filename.write("bnt_trial124" + ", ")
                    filename.write(studentname + ", ")
                    filename.write(date + ", ")
                    filename.write(str(bnt_trial11) + ", ")
                    filename.write(str(bnt_trial12) + ", ")
                    filename.write(str(bnt_trial13) + ", ")
                    filename.write(str(bnt_trial14) + ", ")
                    filename.write(str(bnt_trial15) + ", ")
                    filename.write(str(bnt_trial16) + ", ")
                    filename.write(str(bnt_trial17) + ", ")
                    filename.write(str(bnt_trial18) + ", ")
                    filename.write(str(bnt_trial19) + ", ")
                    filename.write(str(bnt_trial21) + ", ")
                    filename.write(str(bnt_trial22) + ", ")
                    filename.write(str(bnt_trial23) + ", ")
                    filename.write(str(bnt_trial24) + ", ")
                    filename.write(str(bnt_trial25) + ", ")
                    filename.write(str(bnt_trial26) + ", ")
                    filename.write(str(bnt_trial27) + ", ")
                    filename.write(str(bnt_trial31) + ", ")
                    filename.write(str(bnt_trial32) + ", ")
                    filename.write(str(bnt_trial33) + ", ")
                    filename.write(str(bnt_trial34) + ", ")
                    filename.write(str(bnt_trial35) + ", ")
                    filename.write(str(bnt_trial36) + ", ")
                    filename.write(str(bnt_trial37) + ", ")
                    filename.write(str(bnt_trial41) + ", ")
                    filename.write(str(bnt_trial42) + ", ")
                    filename.write(str(bnt_trial43) + ", ")
                    filename.write(str(bnt_trial51) + ", ")
                    filename.write(str(bnt_trial52) + ", ")
                    filename.write(str(bnt_trial53) + ", ")
                    filename.write(str(bnt_trial54) + ", ")
                    filename.write(str(bnt_trial55) + ", ")
                    filename.write(str(bnt_trial56) + ", ")
                    filename.write(str(bnt_trial57) + ", ")
                    filename.write(str(bnt_trial61) + ", ")
                    filename.write(str(bnt_trial62) + ", ")
                    filename.write(str(bnt_trial63) + ", ")
                    filename.write(str(bnt_trial71) + ", ")
                    filename.write(str(bnt_trial72) + ", ")
                    filename.write(str(bnt_trial73) + ", ")
                    filename.write(str(bnt_trial74) + ", ")
                    filename.write(str(bnt_trial81) + ", ")
                    filename.write(str(bnt_trial82) + ", ")
                    filename.write(str(bnt_trial83) + ", ")
                    filename.write(str(bnt_trial84) + ", ")
                    filename.write(str(bnt_trial85) + ", ")
                    filename.write(str(bnt_trial91) + ", ")
                    filename.write(str(bnt_trial92) + ", ")
                    filename.write(str(bnt_trial93) + ", ")
                    filename.write(str(bnt_trial94) + ", ")
                    filename.write(str(bnt_trial101) + ", ")
                    filename.write(str(bnt_trial102) + ", ")
                    filename.write(str(bnt_trial103) + ", ")
                    filename.write(str(bnt_trial111) + ", ")
                    filename.write(str(bnt_trial112) + ", ")
                    filename.write(str(bnt_trial113) + ", ")
                    filename.write(str(bnt_trial114) + ", ")
                    filename.write(str(bnt_trial115) + ", ")
                    filename.write(str(bnt_trial121) + ", ")
                    filename.write(str(bnt_trial122) + ", ")
                    filename.write(str(bnt_trial123) + ", ")
                    filename.write(str(bnt_trial124) + ", ")
                    filename.close()
                    
                    tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase", "StudentDataFiles", "Filenames.txt"
                            )
                    filename = open(tmppath, "a")
                    tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase", "StudentDataFiles", studentname, studentdatabasename + ".txt", )
                    filename.write(f"'{tmppath}'" + "\n")
                    filename.close()
                    tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase", "StudentDataFiles", "Filenames.txt"
                            )
                    filename = open(tmppath, "a")
                    tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase", "StudentDataFiles", studentname, studentdatabasename + ".txt", )
                    filename.write(f"'{tmppath}'" + "\n")
                    filename.close()
                    list_data = [datenow, bnt_trial11, bnt_trial12, bnt_trial13, bnt_trial14, bnt_trial15, bnt_trial16, bnt_trial17, bnt_trial18, bnt_trial19, bnt_trial21, bnt_trial22, bnt_trial23, bnt_trial24, bnt_trial25, bnt_trial26, bnt_trial27,
                                 bnt_trial31, bnt_trial32, bnt_trial33, bnt_trial34, bnt_trial35, bnt_trial36, bnt_trial37, bnt_trial41, bnt_trial42, bnt_trial43, bnt_trial51, bnt_trial52, bnt_trial53, bnt_trial54, bnt_trial55, bnt_trial56, bnt_trial57,
                                 bnt_trial61, bnt_trial62, bnt_trial63, bnt_trial71, bnt_trial72, bnt_trial73, bnt_trial74, bnt_trial81, bnt_trial82, bnt_trial83, bnt_trial84, bnt_trial85, bnt_trial91, bnt_trial92, bnt_trial93, bnt_trial94, bnt_trial101,
                                 bnt_trial102, bnt_trial103, bnt_trial111, bnt_trial112, bnt_trial113, bnt_trial114, bnt_trial115, bnt_trial121, bnt_trial122, bnt_trial123, bnt_trial124]
                    tmppath = Path(USER_DIR).joinpath(
                            "StudentDatabase", "StudentDataFiles", studentname, "bntProgression.csv", )
                    os.chdir(USER_DIR)
                    with open(tmppath, "a", newline="") as f_setup:
                        writer_setup = writer(f_setup)
                        writer_setup.writerow(list_data)
                        f_setup.close()
                    
                    # noinspection SqlResolve
                    def data_entry():
                        """ """
                        conn = sqlite3.connect(dataBasePath)
                        c = conn.cursor()
                        c.execute(
                                """INSERT INTO BNTPROGRESS (
                                        STUDENTNAME,
                                        DATE,
                                        P1_1,
                                        P1_2,
                                        P1_3,
                                        P1_4,
                                        P1_5,
                                        P1_6,
                                        P1_7,
                                        P1_8,
                                        P1_9,
                                        P2_1,
                                        P2_2,
                                        P2_3,
                                        P2_4,
                                        P2_5,
                                        P2_6,
                                        P2_7,
                                        P3_1,
                                        P3_2,
                                        P3_3,
                                        P3_4,
                                        P3_5,
                                        P3_6,
                                        P3_7,
                                        P4_1,
                                        P4_2,
                                        P4_3,
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
                                        P7_1,
                                        P7_2,
                                        P7_3,
                                        P7_4,
                                        P8_1,
                                        P8_2,
                                        P8_3,
                                        P8_4,
                                        P8_5,
                                        P9_1,
                                        P9_2,
                                        P9_3,
                                        P9_4,
                                        P10_1,
                                        P10_2,
                                        P10_3,
                                        P11_1,
                                        P11_2,
                                        P11_3,
                                        P11_4,
                                        P11_5,
                                        P12_1,
                                        P12_2,
                                        P12_3,
                                        P12_4
                                                                            )
                                                                            VALUES (
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
                                                                                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                                                                                )""", (
                                        studentname, datenow, bnt_trial11, bnt_trial12, bnt_trial13, bnt_trial14, bnt_trial15, bnt_trial16, bnt_trial17, bnt_trial18, bnt_trial19, bnt_trial21, bnt_trial22, bnt_trial23, bnt_trial24, bnt_trial25, bnt_trial26,
                                        bnt_trial27, bnt_trial31, bnt_trial32, bnt_trial33, bnt_trial34, bnt_trial35, bnt_trial36, bnt_trial37, bnt_trial41, bnt_trial42, bnt_trial43, bnt_trial51, bnt_trial52, bnt_trial53, bnt_trial54, bnt_trial55,
                                        bnt_trial56, bnt_trial57, bnt_trial61, bnt_trial62, bnt_trial63, bnt_trial71, bnt_trial72, bnt_trial73, bnt_trial74, bnt_trial81, bnt_trial82, bnt_trial83, bnt_trial84, bnt_trial85, bnt_trial91, bnt_trial92,
                                        bnt_trial93, bnt_trial94, bnt_trial101, bnt_trial102, bnt_trial103, bnt_trial111, bnt_trial112, bnt_trial113, bnt_trial114, bnt_trial115, bnt_trial121, bnt_trial122, bnt_trial123, bnt_trial124,), )
                        conn.commit()
                        ui.notify(
                                "Saved successfully!", position='center', type='positive', close_button="OK"
                                )
                    
                    data_entry()
        
        def graph(event):
            """

            :param event:
            :type event:
            """
            dataBasePath = Path(USER_DIR).joinpath(
                    "StudentDatabase", "students.db"
                    )
            studentname = u_studentname.value
            conn = sqlite3.connect(dataBasePath)
            df_sql = pd.read_sql_query(
                    "SELECT * FROM BNTPROGRESS", conn
                    )
            df_student = df_sql[df_sql.STUDENTNAME == studentname]
            print(df_student)
            conn.close()
            df = df_student.drop(columns=["ID", "STUDENTNAME"])
            print(df)
            df = df.rename(columns={"DATE": "date"})
            df = df.set_index("date")
            for column in df.columns:
                if df[column].dtype == 'object':
                    df[column] = df[column].astype('int64')
            print(df)
            print(df.dtypes)
            df = df.sort_values(by="date")
            mu, sigma = 0, 0.1
            noise = np.random.normal(
                    mu, sigma, [len(df.index), len(df.columns)]
                    )
            # df_noisy = df
            df_noisy = df + noise
            fig = make_subplots(
                    rows=3, cols=4, subplot_titles=("Basic Skills", "KeyMath", "Calendar", "KeyBRF", "KeyFiles", "Keymail", "KeyWeb", "KeyCalc", "KeyWord", "KeySlides", "KeyCode", "Third Party Apps"), print_grid=True
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_1"], mode="lines+markers", name=" 1.1PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_5"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_6"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_7"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_8"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P1_9"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P2_1"], mode="lines+markers", name=" 2.1 PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P2_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P2_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P2_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P2_5"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P2_6"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P2_7"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P3_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P3_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P3_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P3_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P3_5"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P3_6"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P3_7"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=1
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P4_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P4_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P4_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P5_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P5_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P5_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P5_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P5_5"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P5_6"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P5_7"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P6_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P6_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P6_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=2
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P7_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P7_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P7_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P7_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P8_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P8_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P8_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P8_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P8_5"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P9_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P9_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P9_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P9_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=3
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P10_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P10_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P10_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=1, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P11_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P11_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P11_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P11_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P11_5"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=2, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P12_1"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P12_2"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P12_3"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=4
                    )
            fig.add_trace(
                    go.Scatter(
                            x=df_noisy.index, y=df_noisy["P12_4"], mode="lines+markers", name=" PLACEHOLDER", legendgroup="PLACEHOLDER", legendgrouptitle_text="PLACEHOLDER"
                            ), row=3, col=4
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=1
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=1
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=1
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=1
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=2
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=2
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=2
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=2
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=3
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=3
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=3
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=3
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=4
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=4
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=4
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=4
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=1
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=1
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=1
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=1
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=2
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=2
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=2
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=2
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=3
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=3
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=3
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=3
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=4
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=4
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=4
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=4
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=1
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=1
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=1
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=1
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=2
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=2
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=2
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=2
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=3
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=3
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=3
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=3
                    )
            fig.add_hrect(
                    y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=4
                    )
            fig.add_hrect(
                    y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=4
                    )
            fig.add_hrect(
                    y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=4
                    )
            fig.add_hrect(
                    y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=4
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[" "])], row=1, col=1
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=1, col=2
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=1, col=3
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=1, col=4
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[" "])], row=2, col=1
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=2, col=2
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=2, col=3
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=2, col=4
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[" "])], row=3, col=1
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=3, col=2
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=3, col=3
                    )
            fig.update_xaxes(
                    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=[])], row=3, col=4
                    )
            fig.update_yaxes(
                    range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"], tickvals=[0.1, 1, 2, 3], row=1, col=1
                    )
            fig.update_yaxes(
                    range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"], tickvals=[0.1, 1, 2, 3], row=2, col=1
                    )
            fig.update_yaxes(
                    range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"], tickvals=[0.1, 1, 2, 3], row=3, col=1
                    )
            
            fig.update_layout(template="simple_white", title_text=f"{studentname}: iOS Skills Progression")
            tmppath = Path(USER_DIR).joinpath(
                    'StudentDatabase', 'StudentDataFiles', studentname, 'iosProgression.html'
                    )
            fig.write_html(tmppath, auto_open=True)
            # fig.show()
            ui.notify(
                    "Graph Successful. The Graphs will open in a "
                    "Browser "
                    "Window", position='center', type='positive', close_button="OK", )
        
        with ui.row().classes("w-screen no-wrap"):
            ui.label(
                    "BRAILLENOTE TOUCH PLUS SKILLS "
                    "PROGRESSION"
                    ).classes(
                    "justify-center "
                    "items-center"
                    )
        with ui.row().classes("w-screen no-wrap"):
            ui.select(
                    options=students, with_input=True, on_change=lambda e: ui.notify(e.value), ).bind_value(
                    u_studentname, "value"
                    ).classes(
                    "w-["
                    "300px]"
                    ).props(
                    'aria-label="Select Student from the Dropdown. It '
                    'will '
                    'autocomplete as you type"'
                    ).tooltip(
                    "Type Student Name, it will autocomplete AS you "
                    "type"
                    )
            with ui.input("Date").classes("w-[300px]").props(
                    'aria-label="Date. Please type in date using the '
                    'YYYY-MM-DD format"'
                    ).tooltip(
                    "Date. Please type in date using the "
                    "YYYY-MM-DD format"
                    ) as date:
                with date.add_slot("append"):
                    ui.icon("edit_calendar").on(
                            "click", lambda: menu.open(
                                    
                                    )
                            ).classes("cursor-pointer")
                with ui.menu() as menu:
                    ui.date().bind_value(date)
        
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.label(
                    "RUBRIC: 0=No attempt 1=Required Assistance "
                    "2=Hesitated "
                    "3=Independent"
                    ).props(
                    'aria-label="RUBRIC: 0=No attempt 1=Required '
                    'Assistance '
                    '2=Hesitated 3=Independent" content-center'
                    )
            ui.input().props(
                    'aria-label="RUBRIC: 0=No attempt 1=Required '
                    'Assistance '
                    '2=Hesitated 3=Independent" content-center'
                    ).classes("sr-only")
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="1.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial11.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial12.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial13.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial14.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.5", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial15.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.6", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial16.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.7", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial17.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.8", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial18.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="1.9", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial19.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="2.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial21.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="2.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial22.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="2.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial23.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="2.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial24.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="2.5", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial25.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="2.6", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial26.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="2.7", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial27.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="3.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial31.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="3.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial32.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="3.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial33.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="3.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial34.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="3.5", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial35.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="3.6", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial36.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="3.7", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial37.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="4.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial41.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="4.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial42.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="4.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial43.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="5.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial51.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="5.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial52.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="5.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial53.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="5.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial54.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="5.5", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial55.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="5.6", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial56.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="5.7", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial57.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="6.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial61.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="6.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial62.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="6.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial63.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="7.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial71.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="7.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial72.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="7.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial73.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="7.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial74.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="8.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial81.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="8.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial82.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="8.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial83.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="8.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial84.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="8.5", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial85.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="9.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial91.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="9.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial92.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="9.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial93.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="9.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial94.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="10.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial101.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="10.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial102.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="10.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial103.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="11.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial111.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="11.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial112.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="11.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial113.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="11.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial114.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="11.5", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial115.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.number(
                    label="12.1", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial121.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="12.2", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial122.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="12.3", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial123.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
            ui.number(
                    label="12.4", min=0, max=3, format="%.0f", on_change=lambda e: u_bnt_trial124.set_value(
                            e.value
                            ), ).classes("w-[200px]").props(
                    'aria-label="LABELX"'
                    ).tooltip("LABELX"),
        with ui.row().classes("w-screen no-wrap py-4"):
            ui.button("SAVE", color="#172554", on_click=save).classes(
                    "text-white"
                    )
            ui.button("GRAPH", color="#172554", on_click=graph).classes(
                    "text-white"
                    )
            ui.button(
                    "EXIT", color="#172554", on_click=app.shutdown
                    ).classes("text-white")
