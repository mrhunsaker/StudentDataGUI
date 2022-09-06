import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import argparse
import numpy as np
import pdfkit
import wx
import os
import datetime
import sqlite3
from sqlite3 import Error
import wx.html2
from csv import writer
###################
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = os.path.join(os.environ['USERPROFILE'], "Documents")
###################
os.chdir(USER_DIR)

if not os.path.exists('StudentDatabase'):
    os.makedirs('StudentDatabase')

if not os.path.exists(USER_DIR + '\\' + 'StudentDatabase'):
    os.makedirs(USER_DIR + '\\' + 'StudentDatabase')

if not os.path.exists(
        USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'omnibusDatabase.csv'):
    filename = open(
            USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'omnibusDatabase.csv',
            'w')

if not os.path.exists(
        USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'StudentDataFiles'):
    os.makedirs(USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'StudentDataFiles')

###################
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(
        USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'students.db')

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql_create_studentdata_table):
    try:
        c = conn.cursor()
        c.execute(sql_create_studentdata_table)
    except Error as e:
        print(e)
    conn.close()

def main():
    sql_create_studentdata_table = "CREATE TABLE IF NOT EXISTS brailleProgression (id INTEGER PRIMARY KEY AUTOINCREMENT, studentname TEXT NOT NULL,  date TEXT NOT NULL, P1.1, P1.2, P1.3, P1.4, P2.1, P2.2, P2.3, P2.4, P2.5, P2.6, P2.7, P2.8, P2.9, P2.10, P2.11, P2.12, P2.13, P2.14, P2.15, P3.1, P3.2, P3.3, P3.4, P3.5, P3.6, P3.7, P3.8, P3.9, P3.10, P3.11, P3.12, P3.13, P3.14, P3.15, P4.1, P4.2, P4.3, P4.4, P5.1, P5.2, P5.3, P5.4, P6.1, P6.2, P6.3, P6.4, P6.5, P6.6, P6.7, P7.1, P7.2, P7.3, P7.4, P7.5, P7.6, P7.7, P7.8, P8.1, P8.2, P8.3, P8.4, P8.5, P8.6, P8.7 );"
    conn = create_connection(
            USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'students.db')
    if conn is not None:
        create_table(conn, sql_create_studentdata_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
###################
date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")

###################

class braillePanel(wx.Panel):
    def __init__(self, parent):
        super(braillePanel,self).__init__(parent)
        wx.StaticText(self, -1, "Student Name", pos=(30, 50))
        self.studentname1 = wx.Choice(self, -1, choices=students_all,
                                      pos=(130, 50), size=(300, 20))
        wx.StaticText(self, -1, "Date", pos=(30, 80))
        self.date = wx.StaticText(self, -1, date, pos=(200, 80))
        wx.StaticText(self, -1, "1.1 Track Left to Right", pos=(500, 80))
        self.trial11 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "1.2 Track Top to Bottom", pos=(500, 110))
        self.trial12 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "1.3 Discriminate Shapes", pos=(500, 140))
        self.trial13 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "1.4 Discriminate Braille Characters", pos=(500, 170))
        self.trial14 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.1 G C L", pos=(500, 200))
        self.trial21 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.2 D Y", pos=(500, 230))
        self.trial22 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.3 A B", pos=(500, 260))
        self.trial23 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.4 S", pos=(500, 290))
        self.trial24 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.5 W", pos=(500, 80))
        self.trial25 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.6 P O", pos=(500, 110))
        self.trial26 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.7 K", pos=(500, 140))
        self.trial27 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.8 R", pos=(500, 170))
        self.trial28 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.9 M E", pos=(500, 200))
        self.trial29 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.10 H", pos=(500, 230))
        self.trial210 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.11 N X", pos=(500, 260))
        self.trial211 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.12 Z F", pos=(500, 290))
        self.trial212 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.13 U T", pos=(500, 80))
        self.trial213 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.14 Q I", pos=(500, 110))
        self.trial214 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "2.15 V J", pos=(500, 140))
        self.trial215 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.1 Alphabetic Wordsigns", pos=(500, 170))
        self.trial31 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.2 Braille Numbers", pos=(500, 200))
        self.trial32 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.3 Punctuation", pos=(500, 230))
        self.trial33 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.4 Strong Contractions - AND OF FOR WITH THE", pos=(500, 260))
        self.trial34 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.5 Strong Groupsigns - CH GH SH TH WH ED ER OU OW ST AR ING", pos=(500, 290))
        self.trial35 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.6 Strong Wordsigns - CH SH TH WH OU ST", pos=(500, 80))
        self.trial36 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.7 Lower Groupsigns - BE CON DIS", pos=(500, 110))
        self.trial37 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.8 Lower Groupsigns - EA BB CC FF GG", pos=(500, 140))
        self.trial38 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.9 Lower Group/Wordsigns - EN IN", pos=(500, 170))
        self.trial39 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.10 Lower Wordsigns - BE HIS WAS WERE", pos=(500, 200))
        self.trial310 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.11 Dot 5 Contractions", pos=(500, 230))
        self.trial311 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.12 Dot 45 Contractions", pos=(500, 260))
        self.trial312 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.13 Dot 456 Contractions", pos=(500, 290))
        self.trial313 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.14 Final Letter Groupsigns", pos=(500, 80))
        self.trial314 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "3.15 Shortform Words", pos=(500, 110))
        self.trial315 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "4.1 Grade 1 Indicators", pos=(500, 140))
        self.trial41 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "4.2 Capitals Indicators", pos=(500, 170))
        self.trial42 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "4.3 Numeric Mode and Spatial Math", pos=(500, 200))
        self.trial43 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "4.4 Typeform Indicators - ITALIC, SCRIPT, UNDERLINE, SCRIPT", pos=(500, 230))
        self.trial44 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "5.1 Page Numbering", pos=(500, 260))
        self.trial51 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "5.2 Headings", pos=(500, 290))
        self.trial52 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "5.3 Lists", pos=(500, 80))
        self.trial53 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "5.4 Poetry / Drama", pos=(500, 110))
        self.trial54 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "6.1 Operation and Comparison Signs", pos=(500, 140))
        self.trial61 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "6.2 Grade 1 Mode", pos=(500, 170))
        self.trial62 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "6.3 Special Print Symbols", pos=(500, 200))
        self.trial63 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "6.4 Omission Marks", pos=(500, 230))
        self.trial64 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "6.5 Shape Indicators", pos=(500, 260))
        self.trial65 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "6.6 Roman Numerals", pos=(500, 290))
        self.trial66 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "6.7 Fractions", pos=(500, 80))
        self.trial67 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.1 Grade 1 Mode and algebra", pos=(500, 110))
        self.trial71 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.2 Grade 1 Mode and Fractions", pos=(500, 140))
        self.trial72 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.3 Advanced Operation and COmparison Signs", pos=(500, 170))
        self.trial73 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.4 Indices", pos=(500, 200))
        self.trial74 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.5 Roots and Radicals", pos=(500, 230))
        self.trial75 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.6 Miscellaneous Shape Indicators", pos=(500, 260))
        self.trial76 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.7 Functions", pos=(500, 290))
        self.trial77 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "7.8 Greek Letters", pos=(500, 80))
        self.trial78 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "8.1 Functions", pos=(500, 110))
        self.trial81 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "8.2 Modifiers, Bars, and Dots", pos=(500, 140))
        self.trial82 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "8.3 Modifiers, Arrows, and Limits", pos=(500, 170))
        self.trial83 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "8.4 Probability", pos=(500, 200))
        self.trial84 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "8.5 Calculus: Differentiation", pos=(500, 230))
        self.trial85 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "8.6 Calculus: Integration", pos=(500, 260))
        self.trial86 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "8.7 Vertical Bars", pos=(500, 290))
        self.trial87 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))


        self.btn = wx.Button(self, 201, "SAVE", pos=(625, 850), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(715, 850), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.exit, id=202)
        self.Bind(wx.EVT_BUTTON, self.save, id=201)


 def exit(self, event):
        wx.Exit()

    def save(self, event):
        studentname = self.studentname1.GetString(
                self.studentname1.GetSelection())
        dateNow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S")
        simpleDate = datetime.datetime.now().strftime("%Y_%m_%d-%H%M")
        item = self.lesson1.GetSelection()
        task = self.lesson1.GetItemText(self.lesson1.GetItemParent(item))
        lesson = self.lesson1.GetItemText(self.lesson1.GetSelection())
        session = self.session1.GetString(self.session1.GetSelection())
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
        notes = self.notes1.GetValue()

        box = wx.TextEntryDialog(None, "Enter Address-Book name to save!",
                                     "Title", f"{studentname.title()}{dateNow}")
            if box.ShowModal() == wx.ID_OK:
                self.studentdatabasename = box.GetValue()
                if not os.path.exists(
                        USER_DIR + '\\' 'StudentDatabase' + '\\' + 'StudentDataFiles' + '\\' + self.studentdatabasename + '.txt'):
                            conn = sqlite3.connect(
                USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'students.db')
                
        c = conn.cursor()

        def data_entry():
            c.execute(
                    "INSERT INTO studentdata (studentname, date, task, lesson, session, trial01, trial02, trial03, trial04, trial05, trial06, trial07, trial08, trial09, trial10, trial11, median, notes) VALUES (?,?,?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?)",
                    (studentname, dateNow, task, lesson, session, trial01,
                     trial02, trial03, trial04, trial05, trial06, trial07,
                     trial08, trial09, trial10, trial11, trialmedian, notes))
            conn.commit()
                    self.dial = wx.MessageDialog(None, 'Saved successfully!',
                                                 'Info', wx.OK)
                    self.dial.ShowModal()
                else:
                    self.dial = wx.MessageDialog(None, 'Name already exists',
                                                 'Info', wx.OK)
                    self.dial.ShowModal()
            else:
                self.dial = wx.MessageDialog(None, 'Save cancelled', 'Info',
                                             wx.OK)
                self.dial.ShowModal()
        else:
            self.dial = wx.MessageDialog(None, 'Fill Required Fields!', 'Info',
                                         wx.OK)
            self.dial.ShowModal()

        conn = sqlite3.connect(
                USER_DIR + '\\' + 'StudentDatabase' + '\\' + 'students.db')
        c = conn.cursor()

        def data_entry():
            c.execute(
                    "INSERT INTO studentdata (studentname, date, task, lesson, session, trial01, trial02, trial03, trial04, trial05, trial06, trial07, trial08, trial09, trial10, trial11, median, notes) VALUES (?,?,?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?)",
                    (studentname, dateNow, task, lesson, session, trial01,
                     trial02, trial03, trial04, trial05, trial06, trial07,
                     trial08, trial09, trial10, trial11, trialmedian, notes))
            conn.commit()

        data_entry()
        dataView = pd.read_sql(
                f"SELECT date,median,notes FROM studentdata WHERE studentname = '{studentname}' AND lesson = '{lesson}'",
                conn)
        c.close()
        conn.close()
















































df = pd.read_sql(f"SELECT date P1.1, P1.2, P1.3, P1.4, P2.1, P2.2, P2.3, P2.4, P2.5, P2.6, P2.7, P2.8, P2.9, P2.10, P2.11, P2.12, P2.13, P2.14, P2.15, P3.1, P3.2, P3.3, P3.4, P3.5, P3.6, P3.7, P3.8, P3.9, P3.10, P3.11, P3.12, P3.13, P3.14, P3.15, P4.1, P4.2, P4.3, P4.4, P5.1, P5.2, P5.3, P5.4, P6.1, P6.2, P6.3, P6.4, P6.5, P6.6, P6.7, P7.1, P7.2, P7.3, P7.4, P7.5, P7.6, P7.7, P7.8, P8.1, P8.2, P8.3, P8.4, P8.5, P8.6, P8.7 WHERE studentname={studentname}")
# Generate Jitter in Dataframe columns since all data are 0,1,2, or 3
mu, sigma = 0, 0.1 
noise = np.random.normal(mu, sigma, [len(df.index),len(df.columns)])
df_noisy=df + noise
print(df_noisy) #df_noisy is used for all plotting. Replace df_noisy with df in all fig.add_trace below for unadjusted raw data






###################
# Line Plots
###################

fig = make_subplots(
    rows=7, cols=2,
    specs=[[{}, {"rowspan": 2}],
        [{}, None],
        [{"rowspan": 2}, {"rowspan": 2}],
        [None, None],
        [{"rowspan": 2}, {"rowspan": 2}],
        [None, None],
        [{},{}]],
    subplot_titles=("Phase 1: Tracking Skills",  "Phase 2: Braille Alphabet", "Phase 1: Tracking Skills", "Phase 3a: Wordsigns, Numbers, Punctuation", "Phase 3b: Strong Contractions", "Phase 3c: Lower Cell Contractions", "Phase 3d: Multiple Cell Contractions", "Phase 4a: Braille Mode Indicators", "Phase 5: Document Formatting"),
    print_grid=True
    )
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.1"], mode="lines+markers", name="Track left to right", legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.2"], mode="lines+markers", name="Track top to bottom", legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.3"], mode="lines+markers", name="Discriminate shapes", legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.4"], mode="lines+markers", name="Discriminate braille characters", legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=2, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.1"], mode="lines+markers+text", name="Alphabet", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=True), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.1"].iloc[[-1]], mode="text", text=["  G C L"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.2"], mode="lines+markers+text", name="D Y", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.2"].iloc[[-1]], mode="text", text=["  D Y"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.3"], mode="lines+markers+text", name="A B", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.3"].iloc[[-1]], mode="text", text=["  A B"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.4"], mode="lines+markers+text", name="S", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.4"].iloc[[-1]], mode="text", text=["  S"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.5"], mode="lines+markers+text", name="W", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.5"].iloc[[-1]], mode="text", text=["  W"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.6"], mode="lines+markers+text", name="P O", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.6"].iloc[[-1]], mode="text", text=["  P O"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.7"], mode="lines+markers+text", name="K", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.7"].iloc[[-1]], mode="text", text=["  K"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.8"], mode="lines+markers+text", name="R", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.8"].iloc[[-1]], mode="text", text=["  R"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.9"], mode="lines+markers+text", name="M E", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.9"].iloc[[-1]], mode="text", text=["  M E"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.10"], mode="lines+markers+text", name="H", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.10"].iloc[[-1]], mode="text", text=["  H"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.11"], mode="lines+markers+text", name="N X", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.11"].iloc[[-1]], mode="text", text=["  N X"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.12"], mode="lines+markers+text", name="Z F", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.12"].iloc[[-1]], mode="text", text=["  Z F"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.13"], mode="lines+markers+text", name="U T", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.13"].iloc[[-1]], mode="text", text=["  U T"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.14"], mode="lines+markers+text", name="Q I", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.14"].iloc[[-1]], mode="text", text=["  Q I"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.15"], mode="lines+markers+text", name="V J ", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index[[-1]],y=df_noisy["P2.15"].iloc[[-1]], mode="text", text=["  V J"], textposition="middle right",legendgroup="Phase 2", legendgrouptitle_text="Phase 2",showlegend=False), row=1, col=2)

fig.update_layout(showlegend=True)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.1"], mode="lines+markers", name="Alphabetic Wordsigns", legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.2"], mode="lines+markers", name="Braille Numbers", legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.3"], mode="lines+markers", name="Punctuation", legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.4"], mode="lines+markers", name="Strong Contractions <br>(AND OF FOR WITH THE)", legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.5"], mode="lines+markers", name="Strong Groupsigns <br>(CH GH SH TH WH ED ER OU OW ST AR ING)", legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.6"], mode="lines+markers", name="Strong Wordsigns <br>(CH SH TH WH OU ST)", legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.7"], mode="lines+markers", name="Lower Groupsigns <br>(BE CON DIS)", legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.8"], mode="lines+markers", name="Lower Groupsigns <br>(EA BB CC FF GG)", legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.9"], mode="lines+markers", name="Lower Groupsigns/Wordsigns <br>(EN IN)", legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.10"], mode="lines+markers", name="Lower Wordsigns <br>(BE HIS WAS WERE)", legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=5, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.11"], mode="lines+markers", name="Dot 5 Contractions", legendgroup="Phase 3d", legendgrouptitle_text="Phase 3d"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.12"], mode="lines+markers", name="Dot 45 Contractions", legendgroup="Phase 3d", legendgrouptitle_text="Phase 3d"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.13"], mode="lines+markers", name="Dot 456 Contractions", legendgroup="Phase 3d", legendgrouptitle_text="Phase 3d"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.14"], mode="lines+markers", name="Final Letter Groupsigns", legendgroup="Phase 3d", legendgrouptitle_text="Phase 3d"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.15"], mode="lines+markers", name="Shortform Words", legendgroup="Phase 3d", legendgrouptitle_text="Phase 3d"), row=5, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.1"], mode="lines+markers", name="Grade 1 Indicators", legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=7, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.2"], mode="lines+markers", name="Capitals Indicators", legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=7, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.3"], mode="lines+markers", name="Numeric Mode and Spatial math", legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=7, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.4"], mode="lines+markers", name="Typeform Indicators <br>(ITALIC, SCRIPT, UNDERLINE, BOLDFACE)", legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=7, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P5.1"], mode="lines+markers", name="Page Numbering", legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=7, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P5.2"], mode="lines+markers", name="Headings", legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=7, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P5.3"], mode="lines+markers", name="Lists", legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=7, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P5.4"], mode="lines+markers", name="Poety / Drama", legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=7, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=7, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=7, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=7, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=7, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=7, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=7, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=7, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=7, col=2)
marker='2022-01-01'
fig.add_vline(x=marker, line_width=3, line_color="black",row=1, col=1)
fig.add_vline(x=marker, line_width=3, line_color="black",row=1, col=2)
fig.add_vline(x=marker, line_width=3, line_color="black",row=2, col=1)
fig.add_vline(x=marker, line_width=3, line_color="black",row=3, col=1)
fig.add_vline(x=marker, line_width=3, line_color="black",row=3, col=2)
fig.add_vline(x=marker, line_width=3, line_color="black",row=5, col=1)
fig.add_vline(x=marker, line_width=3, line_color="black",row=5, col=2)
fig.add_vline(x=marker, line_width=3, line_color="black",row=7, col=1)
fig.add_vline(x=marker, line_width=3, line_color="black",row=7, col=2)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])], row=1, col=1)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=1, col=2)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=2, col=1)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=3, col=1)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=3, col=2)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=5, col=1)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=5, col=2)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=7, col=1)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30"])],row=7, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=2, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=5, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=5, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=5, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=7, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=7, col=2)
fig.update_layout(xaxis_tickformat = '%d %b',xaxis2_tickformat = '%d %b',xaxis3_tickformat = '%d %b',xaxis4_tickformat = '%d %b',xaxis5_tickformat = '%d %b',xaxis6_tickformat = '%d %b',xaxis7_tickformat = '%d %b',xaxis8_tickformat = '%d %b',xaxis9_tickformat = '%d %b',template="simple_white", title_text="Literary UEB Skills Progression",legend = dict(font = dict(size = 10)))
fig.write_html("C:\\Users\\hunsa\\Downloads\\TechScreenReader_DSD\\DSDSTUDENTS\\PMPLOTS\\UEBLiterarySkillsProgression.html")
fig.show()

fig = make_subplots(
    rows=3, cols=1,
    subplot_titles=("Phase 6: UEB Technical Basics", "Phase 7: Advanced UEB Technical","Phase 8: Accellerated UEB Technical"),
    #print_grid=True
    )

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.1"], mode="lines+markers", name=" Operation and Comparison Signs", legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.2"], mode="lines+markers", name="Grade 1 Mode", legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.3"], mode="lines+markers", name="Special Print Symbols", legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.4"], mode="lines+markers", name="Omission Marks", legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.5"], mode="lines+markers", name="Shape Indicators", legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.6"], mode="lines+markers", name="Roman Numerals", legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.7"], mode="lines+markers", name="Fractions", legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=1, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.1"], mode="lines+markers", name="Grade 1 Mode and Algebra", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.2"], mode="lines+markers", name="Grade 1 Mode and Fractions", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.3"], mode="lines+markers", name="Advanced Operation and Comparison Signs", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.4"], mode="lines+markers", name="Indices", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.5"], mode="lines+markers", name="Roots and Radicals", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.6"], mode="lines+markers", name="Miscellaneous Shape Indicators", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.7"], mode="lines+markers", name="Functions", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.8"], mode="lines+markers", name="Greek letters", legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.1"], mode="lines+markers", name="Functions", legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.2"], mode="lines+markers", name="Modifiers, Bars, and Dots", legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.3"], mode="lines+markers", name="Modifiers, Arrows, and Limits", legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.4"], mode="lines+markers", name="Probability", legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.5"], mode="lines+markers", name="Calculus: Differentiation", legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.6"], mode="lines+markers", name="Calculus: Integration", legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.7"], mode="lines+markers", name="Vertical Bars", legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)

fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])], row=1, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=2, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=1)

fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=2, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=1)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=1)

fig.update_layout(xaxis_tickformat = '%d %b',xaxis2_tickformat = '%d %b',xaxis3_tickformat = '%d %b', template="simple_white", title_text="Technical UEB Skills Progression",legend = dict(font = dict(size = 10)))
fig.write_html("C:\\Users\\hunsa\\Downloads\\TechScreenReader_DSD\\DSDSTUDENTS\\PMPLOTS\\UEBTechnicalSkillsProgression.html")
fig.show()


