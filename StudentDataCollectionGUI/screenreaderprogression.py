import wx
import os
import datetime
import sqlite3
from sqlite3 import Error
import pandas as pd
import wx.html2
import statistics
import plotly.graph_objects as go
from csv import writer
import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import wx.lib.scrolledpanel as scrolled
import numpy as np
import pdfkit
import argparse
from helpers import *
from brailleprogression import *
from abacusprogression import *
from screenreaderprogression import *
from datapanel import *

class screenreaderPanel(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(wx.StaticLine(self, -1, size=(1500, -1)), 0, wx.ALL, 5)
        vbox.Add(wx.StaticLine(self, -1, size=(-1, 2100)), 0, wx.ALL, 5)
        vbox.Add((20, 20))
        self.SetSizer(vbox)
        self.SetupScrolling()
        self.SetBackgroundColour(wx.Colour(241, 205, 234))
        # super(braillePanel, self).__init__(parent)
        wx.StaticText(self, -1, "Student Name", pos=(30, 50))
        self.studentname1 = wx.Choice(self, -1, choices=students_all, pos=(400, 50), size=(300, 20))
        wx.StaticText(self, -1, date, pos=(200, 50))
        wx.StaticText(self, -1, "1.1 Track Left to Right", pos=(30, 80))
        self.trial11 = wx.TextCtrl(self, -1, "0", pos=(400, 80), size=(300, 20))
        wx.StaticText(self, -1, "1.2 Track Top to Bottom", pos=(30, 110))
        self.trial12 = wx.TextCtrl(self, -1, "0", pos=(400, 110), size=(300, 20))
        wx.StaticText(self, -1, "1.3 Discriminate Shapes", pos=(30, 140))
        self.trial13 = wx.TextCtrl(self, -1, "0", pos=(400, 140), size=(300, 20))
        wx.StaticText(self, -1, "1.4 Discriminate Braille Characters", pos=(30, 170))
        self.trial14 = wx.TextCtrl(self, -1, "0", pos=(400, 170), size=(300, 20))
        wx.StaticText(self, -1, "2.1 G C L", pos=(30, 200))
        self.trial21 = wx.TextCtrl(self, -1, "0", pos=(400, 200), size=(300, 20))
        wx.StaticText(self, -1, "2.2 D Y", pos=(30, 230))
        self.trial22 = wx.TextCtrl(self, -1, "0", pos=(400, 230), size=(300, 20))
        wx.StaticText(self, -1, "2.3 A B", pos=(30, 260))
        self.trial23 = wx.TextCtrl(self, -1, "0", pos=(400, 260), size=(300, 20))
        wx.StaticText(self, -1, "2.4 S", pos=(30, 290))
        self.trial24 = wx.TextCtrl(self, -1, "0", pos=(400, 290), size=(300, 20))
        wx.StaticText(self, -1, "2.5 W", pos=(30, 320))
        self.trial25 = wx.TextCtrl(self, -1, "0", pos=(400, 320), size=(300, 20))
        wx.StaticText(self, -1, "2.6 P O", pos=(30, 350))
        self.trial26 = wx.TextCtrl(self, -1, "0", pos=(400, 350), size=(300, 20))
        wx.StaticText(self, -1, "2.7 K", pos=(30, 380))
        self.trial27 = wx.TextCtrl(self, -1, "0", pos=(400, 380), size=(300, 20))
        wx.StaticText(self, -1, "2.8 R", pos=(30, 410))
        self.trial28 = wx.TextCtrl(self, -1, "0", pos=(400, 410), size=(300, 20))
        wx.StaticText(self, -1, "2.9 M E", pos=(30, 440))
        self.trial29 = wx.TextCtrl(self, -1, "0", pos=(400, 440), size=(300, 20))
        wx.StaticText(self, -1, "2.10 H", pos=(30, 470))
        self.trial210 = wx.TextCtrl(self, -1, "0", pos=(400, 470), size=(300, 20))
        wx.StaticText(self, -1, "2.11 N X", pos=(30, 500))
        self.trial211 = wx.TextCtrl(self, -1, "0", pos=(400, 500), size=(300, 20))
        wx.StaticText(self, -1, "2.12 Z F", pos=(30, 530))
        self.trial212 = wx.TextCtrl(self, -1, "0", pos=(400, 530), size=(300, 20))
        wx.StaticText(self, -1, "2.13 U T", pos=(30, 560))
        self.trial213 = wx.TextCtrl(self, -1, "0", pos=(400, 560), size=(300, 20))
        wx.StaticText(self, -1, "2.14 Q I", pos=(30, 590))
        self.trial214 = wx.TextCtrl(self, -1, "0", pos=(400, 590), size=(300, 20))
        wx.StaticText(self, -1, "2.15 V J", pos=(30, 620))
        self.trial215 = wx.TextCtrl(self, -1, "0", pos=(400, 620), size=(300, 20))
        wx.StaticText(self, -1, "3.1 Alphabetic Wordsigns", pos=(30, 650))
        self.trial31 = wx.TextCtrl(self, -1, "0", pos=(400, 650), size=(300, 20))
        wx.StaticText(self, -1, "3.2 Braille Numbers", pos=(30, 680))
        self.trial32 = wx.TextCtrl(self, -1, "0", pos=(400, 680), size=(300, 20))
        wx.StaticText(self, -1, "3.3 Punctuation", pos=(30, 710))
        self.trial33 = wx.TextCtrl(self, -1, "0", pos=(400, 710), size=(300, 20))
        wx.StaticText(self, -1, "3.4 Strong Contractions - AND OF FOR WITH THE", pos=(30, 740))
        self.trial34 = wx.TextCtrl(self, -1, "0", pos=(400, 740), size=(300, 20))
        wx.StaticText(self, -1, "3.5 Strong Groupsigns - CH GH SH TH WH ED ER OU OW ST AR ING", pos=(30, 770))
        self.trial35 = wx.TextCtrl(self, -1, "0", pos=(400, 770), size=(300, 20))
        wx.StaticText(self, -1, "3.6 Strong Wordsigns - CH SH TH WH OU ST", pos=(30, 800))
        self.trial36 = wx.TextCtrl(self, -1, "0", pos=(400, 800), size=(300, 20))
        wx.StaticText(self, -1, "3.7 Lower Groupsigns - BE CON DIS", pos=(30, 830))
        self.trial37 = wx.TextCtrl(self, -1, "0", pos=(400, 830), size=(300, 20))
        wx.StaticText(self, -1, "3.8 Lower Groupsigns - EA BB CC FF GG", pos=(30, 860))
        self.trial38 = wx.TextCtrl(self, -1, "0", pos=(400, 860), size=(300, 20))
        wx.StaticText(self, -1, "3.9 Lower Group/Wordsigns - EN IN", pos=(30, 890))
        self.trial39 = wx.TextCtrl(self, -1, "0", pos=(400, 890), size=(300, 20))
        wx.StaticText(self, -1, "3.10 Lower Wordsigns - BE HIS WAS WERE", pos=(30, 920))
        self.trial310 = wx.TextCtrl(self, -1, "0", pos=(400, 920), size=(300, 20))
        wx.StaticText(self, -1, "3.11 Dot 5 Contractions", pos=(30, 950))
        self.trial311 = wx.TextCtrl(self, -1, "0", pos=(400, 950), size=(300, 20))
        wx.StaticText(self, -1, "3.12 Dot 45 Contractions", pos=(30, 980))
        self.trial312 = wx.TextCtrl(self, -1, "0", pos=(400, 980), size=(300, 20))
        wx.StaticText(self, -1, "3.13 Dot 456 Contractions", pos=(30, 1010))
        self.trial313 = wx.TextCtrl(self, -1, "0", pos=(400, 1010), size=(300, 20))
        wx.StaticText(self, -1, "3.14 Final Letter Groupsigns", pos=(30, 1040))
        self.trial314 = wx.TextCtrl(self, -1, "0", pos=(400, 1040), size=(300, 20))
        wx.StaticText(self, -1, "3.15 Shortform Words", pos=(30, 1070))
        self.trial315 = wx.TextCtrl(self, -1, "0", pos=(400, 1070), size=(300, 20))
        wx.StaticText(self, -1, "4.1 Grade 1 Indicators", pos=(30, 1100))
        self.trial41 = wx.TextCtrl(self, -1, "0", pos=(400, 1100), size=(300, 20))
        wx.StaticText(self, -1, "4.2 Capitals Indicators", pos=(30, 1130))
        self.trial42 = wx.TextCtrl(self, -1, "0", pos=(400, 1130), size=(300, 20))
        wx.StaticText(self, -1, "4.3 Numeric Mode and Spatial Math", pos=(30, 1160))
        self.trial43 = wx.TextCtrl(self, -1, "0", pos=(400, 1160), size=(300, 20))
        wx.StaticText(self, -1, "4.4 Typeform Indicators - ITALIC, SCRIPT, UNDERLINE, SCRIPT", pos=(30, 1190))
        self.trial44 = wx.TextCtrl(self, -1, "0", pos=(400, 1190), size=(300, 20))
        wx.StaticText(self, -1, "5.1 Page Numbering", pos=(30, 1220))
        self.trial51 = wx.TextCtrl(self, -1, "0", pos=(400, 1220), size=(300, 20))
        wx.StaticText(self, -1, "5.2 Headings", pos=(30, 1250))
        self.trial52 = wx.TextCtrl(self, -1, "0", pos=(400, 1250), size=(300, 20))
        wx.StaticText(self, -1, "5.3 Lists", pos=(30, 1280))
        self.trial53 = wx.TextCtrl(self, -1, "0", pos=(400, 1280), size=(300, 20))
        wx.StaticText(self, -1, "5.4 Poetry / Drama", pos=(30, 1310))
        self.trial54 = wx.TextCtrl(self, -1, "0", pos=(400, 1310), size=(300, 20))
        wx.StaticText(self, -1, "6.1 Operation and Comparison Signs", pos=(30, 1340))
        self.trial61 = wx.TextCtrl(self, -1, "0", pos=(400, 1340), size=(300, 20))
        wx.StaticText(self, -1, "6.2 Grade 1 Mode", pos=(30, 1370))
        self.trial62 = wx.TextCtrl(self, -1, "0", pos=(400, 1370), size=(300, 20))
        wx.StaticText(self, -1, "6.3 Special Print Symbols", pos=(30, 1400))
        self.trial63 = wx.TextCtrl(self, -1, "0", pos=(400, 1400), size=(300, 20))
        wx.StaticText(self, -1, "6.4 Omission Marks", pos=(30, 1430))
        self.trial64 = wx.TextCtrl(self, -1, "0", pos=(400, 1430), size=(300, 20))
        wx.StaticText(self, -1, "6.5 Shape Indicators", pos=(30, 1460))
        self.trial65 = wx.TextCtrl(self, -1, "0", pos=(400, 1460), size=(300, 20))
        wx.StaticText(self, -1, "6.6 Roman Numerals", pos=(30, 1490))
        self.trial66 = wx.TextCtrl(self, -1, "0", pos=(400, 1490), size=(300, 20))
        wx.StaticText(self, -1, "6.7 Fractions", pos=(30, 1520))
        self.trial67 = wx.TextCtrl(self, -1, "0", pos=(400, 1520), size=(300, 20))
        wx.StaticText(self, -1, "7.1 Grade 1 Mode and algebra", pos=(30, 1550))
        self.trial71 = wx.TextCtrl(self, -1, "0", pos=(400, 1550), size=(300, 20))
        wx.StaticText(self, -1, "7.2 Grade 1 Mode and Fractions", pos=(30, 1580))
        self.trial72 = wx.TextCtrl(self, -1, "0", pos=(400, 1580), size=(300, 20))
        wx.StaticText(self, -1, "7.3 Advanced Operation and Comparison Signs", pos=(30, 1610))
        self.trial73 = wx.TextCtrl(self, -1, "0", pos=(400, 1610), size=(300, 20))
        wx.StaticText(self, -1, "7.4 Indices", pos=(30, 1640))
        self.trial74 = wx.TextCtrl(self, -1, "0", pos=(400, 1640), size=(300, 20))
        wx.StaticText(self, -1, "7.5 Roots and Radicals", pos=(30, 1670))
        self.trial75 = wx.TextCtrl(self, -1, "0", pos=(400, 1670), size=(300, 20))
        wx.StaticText(self, -1, "7.6 Miscellaneous Shape Indicators", pos=(30, 1700))
        self.trial76 = wx.TextCtrl(self, -1, "0", pos=(400, 1700), size=(300, 20))
        wx.StaticText(self, -1, "7.7 Functions", pos=(30, 1730))
        self.trial77 = wx.TextCtrl(self, -1, "0", pos=(400, 1730), size=(300, 20))
        wx.StaticText(self, -1, "7.8 Greek Letters", pos=(30, 1760))
        self.trial78 = wx.TextCtrl(self, -1, "0", pos=(400, 1760), size=(300, 20))
        wx.StaticText(self, -1, "8.1 Functions", pos=(30, 1790))
        self.trial81 = wx.TextCtrl(self, -1, "0", pos=(400, 1790), size=(300, 20))
        wx.StaticText(self, -1, "8.2 Modifiers, Bars, and Dots", pos=(30, 1820))
        self.trial82 = wx.TextCtrl(self, -1, "0", pos=(400, 1820), size=(300, 20))
        wx.StaticText(self, -1, "8.3 Modifiers, Arrows, and Limits", pos=(30, 1850))
        self.trial83 = wx.TextCtrl(self, -1, "0", pos=(400, 1850), size=(300, 20))
        wx.StaticText(self, -1, "8.4 Probability", pos=(30, 1880))
        self.trial84 = wx.TextCtrl(self, -1, "0", pos=(400, 1880), size=(300, 20))
        wx.StaticText(self, -1, "8.5 Calculus: Differentiation", pos=(30, 1910))
        self.trial85 = wx.TextCtrl(self, -1, "0", pos=(400, 1910), size=(300, 20))
        wx.StaticText(self, -1, "8.6 Calculus: Integration", pos=(30, 1940))
        self.trial86 = wx.TextCtrl(self, -1, "0", pos=(400, 1940), size=(300, 20))
        wx.StaticText(self, -1, "8.7 Vertical Bars", pos=(30, 1970))
        self.trial87 = wx.TextCtrl(self, -1, "0", pos=(400, 1970), size=(300, 20))

        self.btn = wx.Button(self, 201, "SAVE", pos=(450, 2000), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(650, 2000), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.exit, id=202)
        self.btn = wx.Button(self, 203, "PRINT GRAPHS", pos=(450, 2040), size=(170, 30))
        self.Bind(wx.EVT_BUTTON, self.graph, id=203)

    def exit(self, event):
        wx.Exit()

    def save(self, event):
        studentname = self.studentname1.GetString(self.studentname1.GetSelection())
        dateNow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S")
        simpleDate = datetime.datetime.now().strftime("%Y_%m_%d-%H%M")
        trial11 = self.trial11.GetValue()
        trial12 = self.trial12.GetValue()
        trial13 = self.trial13.GetValue()
        trial14 = self.trial14.GetValue()
        trial21 = self.trial21.GetValue()
        trial22 = self.trial22.GetValue()
        trial23 = self.trial23.GetValue()
        trial24 = self.trial24.GetValue()
        trial25 = self.trial25.GetValue()
        trial26 = self.trial26.GetValue()
        trial27 = self.trial27.GetValue()
        trial28 = self.trial28.GetValue()
        trial29 = self.trial29.GetValue()
        trial210 = self.trial210.GetValue()
        trial211 = self.trial211.GetValue()
        trial212 = self.trial212.GetValue()
        trial213 = self.trial213.GetValue()
        trial214 = self.trial214.GetValue()
        trial215 = self.trial215.GetValue()
        trial31 = self.trial31.GetValue()
        trial32 = self.trial32.GetValue()
        trial33 = self.trial33.GetValue()
        trial34 = self.trial34.GetValue()
        trial35 = self.trial35.GetValue()
        trial36 = self.trial36.GetValue()
        trial37 = self.trial37.GetValue()
        trial38 = self.trial38.GetValue()
        trial39 = self.trial39.GetValue()
        trial310 = self.trial310.GetValue()
        trial311 = self.trial311.GetValue()
        trial312 = self.trial312.GetValue()
        trial313 = self.trial313.GetValue()
        trial314 = self.trial314.GetValue()
        trial315 = self.trial315.GetValue()
        trial41 = self.trial41.GetValue()
        trial42 = self.trial42.GetValue()
        trial43 = self.trial43.GetValue()
        trial44 = self.trial44.GetValue()
        trial51 = self.trial51.GetValue()
        trial52 = self.trial52.GetValue()
        trial53 = self.trial53.GetValue()
        trial54 = self.trial54.GetValue()
        trial61 = self.trial61.GetValue()
        trial62 = self.trial62.GetValue()
        trial63 = self.trial63.GetValue()
        trial64 = self.trial64.GetValue()
        trial65 = self.trial65.GetValue()
        trial66 = self.trial66.GetValue()
        trial67 = self.trial67.GetValue()
        trial71 = self.trial71.GetValue()
        trial72 = self.trial72.GetValue()
        trial73 = self.trial73.GetValue()
        trial74 = self.trial74.GetValue()
        trial75 = self.trial75.GetValue()
        trial76 = self.trial76.GetValue()
        trial77 = self.trial77.GetValue()
        trial78 = self.trial78.GetValue()
        trial81 = self.trial81.GetValue()
        trial82 = self.trial82.GetValue()
        trial83 = self.trial83.GetValue()
        trial84 = self.trial84.GetValue()
        trial85 = self.trial85.GetValue()
        trial86 = self.trial86.GetValue()
        trial87 = self.trial87.GetValue()

        box = wx.TextEntryDialog(None, "Enter Address-Book name to save!", "Title",
                                 f"braille{studentname.title()}{dateNow}")
        if box.ShowModal() == wx.ID_OK:
            self.studentdatabasename = box.GetValue()
            if not os.path.exists(
                    f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\{self.studentdatabasename}.txt"):
                conn = sqlite3.connect(f"{USER_DIR}\\StudentDatabase\\students.db")
                c = conn.cursor()

        def data_entry():
            c.execute(
                "INSERT INTO brailleProgress (studentname, date, P1_1 , P1_2 , P1_3 , P1_4 , P2_1 , P2_2 , P2_3 , P2_4 , P2_5 , P2_6 , P2_7 , P2_8 , P2_9 , P2_10 , P2_11 , P2_12 , P2_13 , P2_14 , P2_15 , P3_1 , P3_2 , P3_3 , P3_4 , P3_5 , P3_6 , P3_7 , P3_8 , P3_9 , P3_10 , P3_11 , P3_12 , P3_13 , P3_14 , P3_15 , P4_1 , P4_2 , P4_3 , P4_4 , P5_1 , P5_2 , P5_3 , P5_4 , P6_1 , P6_2 , P6_3 , P6_4 , P6_5 , P6_6 , P6_7 , P7_1 , P7_2 , P7_3 , P7_4 , P7_5 , P7_6 , P7_7 , P7_8 , P8_1 , P8_2 , P8_3 , P8_4 , P8_5 , P8_6 , P8_7 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (studentname, dateNow, trial11, trial12, trial13, trial14, trial21, trial22, trial23, trial24, trial25,
                 trial26, trial27, trial28, trial29, trial210, trial211, trial212, trial213, trial214, trial215,
                 trial31, trial32, trial33, trial34, trial35, trial36, trial37, trial38, trial39, trial310, trial311,
                 trial312, trial313, trial314, trial315, trial41, trial42, trial43, trial44, trial51, trial52, trial53,
                 trial54, trial61, trial62, trial63, trial64, trial65, trial66, trial67, trial71, trial72, trial73,
                 trial74, trial75, trial76, trial77, trial78, trial81, trial82, trial83, trial84, trial85, trial86,
                 trial87))
            conn.commit()

        data_entry()

        list_names = ['date', 'P1_1', 'P1_2', 'P1_3', 'P1_4', 'P2_1', 'P2_2', 'P2_3', 'P2_4', 'P2_5', 'P2_6', 'P2_7',
                      'P2_8', 'P2_9', 'P2_10', 'P2_11', 'P2_12', 'P2_13', 'P2_14', 'P2_15', 'P3_1', 'P3_2', 'P3_3',
                      'P3_4', 'P3_5', 'P3_6', 'P3_7', 'P3_8', 'P3_9', 'P3_10', 'P3_11', 'P3_12', 'P3_13', 'P3_14',
                      'P3_15', 'P4_1', 'P4_2', 'P4_3', 'P4_4', 'P5_1', 'P5_2', 'P5_3', 'P5_4', 'P6_1', 'P6_2', 'P6_3',
                      'P6_4', 'P6_5', 'P6_6', 'P6_7', 'P7_1', 'P7_2', 'P7_3', 'P7_4', 'P7_5', 'P7_6', 'P7_7', 'P7_8',
                      'P8_1', 'P8_2', 'P8_3', 'P8_4', 'P8_5', 'P8_6', 'P8_7']
        list_data = [dateNow, trial11, trial12, trial13, trial14, trial21, trial22, trial23, trial24, trial25, trial26,
                     trial27, trial28, trial29, trial210, trial211, trial212, trial213, trial214, trial215, trial31,
                     trial32, trial33, trial34, trial35, trial36, trial37, trial38, trial39, trial310, trial311,
                     trial312, trial313, trial314, trial315, trial41, trial42, trial43, trial44, trial51, trial52,
                     trial53, trial54, trial61, trial62, trial63, trial64, trial65, trial66, trial67, trial71, trial72,
                     trial73, trial74, trial75, trial76, trial77, trial78, trial81, trial82, trial83, trial84, trial85,
                     trial86, trial87]

        os.chdir(USER_DIR)
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\BrailleSkillsProgression.csv", 'a',
                  newline='') as f_setup:
            writer_setup = writer(f_setup)
            writer_setup.writerow(list_data)
            f_setup.close()

    def graph(self, event):
        studentname = self.studentname1.GetString(self.studentname1.GetSelection())
        df = pd.read_csv(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\BrailleSkillsProgression.csv",
                         sep=',', index_col=[0], parse_dates=[0])
        df = df.sort_values(by="date")

        # Generate Jitter in Dataframe columns since all data are 0,1,2, or 3
        mu, sigma = 0, 0.1
        noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
        # print(noise)
        df_noisy = df + noise
        print(df_noisy)
#print(df_noisy) #df_noisy is used for all plotting. Replace df_noisy with df in all fig.add_trace below for unadjusted raw data

###################
# Line Plots
###################

fig = make_subplots(
    rows=5, cols=2,
    specs=[[{}, {"rowspan": 2}],
           [{}, None],
           [{"rowspan": 2},{}],
           [None,{}],
           [{}, {}]],
    subplot_titles=("Phase 1a: Reading", "Phase 2: Writing", "Phase 1b: Reading", "Phase 3a: Internet", "Phase 3b: Internet", "Phase 3c: Internet", "Phase 4a: File Management", "Phase 4b: File Management"),
    #print_grid=True
    )

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.1"], mode="lines+markers", name="Turn ON/OFF",legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.2"], mode="lines+markers", name="Use Modifier Keys",legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.3"], mode="lines+markers", name="Use Reading Commands",legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.4"], mode="lines+markers", name="ID Titles",legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.5"], mode="lines+markers", name="Access Documents",legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.6"], mode="lines+markers", name="Switch Program Focus",legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.1"], mode="lines+markers", name="Type with all keys",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.2"], mode="lines+markers", name="Change Screen Reader Settings",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.3"], mode="lines+markers", name="Write documents",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.4"], mode="lines+markers", name="Copy/Paste Text",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.4"], mode="lines+markers", name="TAB Navigation",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.5"], mode="lines+markers", name="Quick Key Navigation",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.6"], mode="lines+markers", name="Elements List Navigation",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.7"], mode="lines+markers", name="Justify Navigation Method",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.1"], mode="lines+markers", name="Define HTML Elements",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.2"], mode="lines+markers", name="ID HTML Elements",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.3"], mode="lines+markers", name="Navigate to Address Bar",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.8"], mode="lines+markers", name="ALT-TAB Focus",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.9"], mode="lines+markers", name="Toggle Screen Reader Mode",legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.10"], mode="lines+markers", name="Navigate a Table",legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.11"], mode="lines+markers", name="Navigation Sequence",legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.1"], mode="lines+markers", name="Save and Open Files",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.2"], mode="lines+markers", name="Create Folders",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.3"], mode="lines+markers", name="Navigate Cloud Storage",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.4"], mode="lines+markers", name="Download from Internet",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.5"], mode="lines+markers", name="UNZIP Folders",legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.6"], mode="lines+markers", name="Use Virtual Cursor",legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.7"], mode="lines+markers", name="Use Built-In OCR",legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=5, col=2)


fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])], row=1, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=1, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=2, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=4, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=5, col=1)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=5, col=2)

fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=2, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=4, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=5, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=5, col=2)

fig.update_layout(template="simple_white", title_text="Screen Reader Skills Progression")

fig.write_html("C:\\Users\\Ryan\\OneDrive\\Documents\\DSDSTUDENTS\\PMPLOTS\\ScreenReaderSkillsProgression.html")

#fig.show()

