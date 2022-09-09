import wx
import os
import datetime
import sqlite3
from sqlite3 import Error
import wx.html2
import statistics
from csv import writer
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import wx.lib.scrolledpanel as scrolled
import numpy as np
from helpers import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = os.path.join(os.environ['USERPROFILE'], "Documents")
os.chdir(USER_DIR)
for name in students_all:
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase"):
        os.makedirs(f"{USER_DIR}\\StudentDatabase")
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles"):
        os.makedirs(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles")
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}"):
        os.makedirs(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}")
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\omnibusDatabase.csv"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\omnibusDatabase.csv", 'w')
        list_names = ['student', 'date', 'task', 'lesson', 'session', 'trial01', 'trial02', 'trial03', 'trial04',
                      'trial05', 'trial06', 'trial07', 'trial08', 'trial09', 'trial10', 'trial11', 'median', 'notes']
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\omnibusDatabase.csv", 'a',
                  newline='') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\BrailleSkillsProgression.csv"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\BrailleSkillsProgression.csv", 'w')
        list_names = ['date', 'P1_1', 'P1_2', 'P1_3', 'P1_4', 'P2_1', 'P2_2', 'P2_3', 'P2_4', 'P2_5', 'P2_6', 'P2_7',
                      'P2_8', 'P2_9', 'P2_10', 'P2_11', 'P2_12', 'P2_13', 'P2_14', 'P2_15', 'P3_1', 'P3_2', 'P3_3',
                      'P3_4', 'P3_5', 'P3_6', 'P3_7', 'P3_8', 'P3_9', 'P3_10', 'P3_11', 'P3_12', 'P3_13', 'P3_14',
                      'P3_15', 'P4_1', 'P4_2', 'P4_3', 'P4_4', 'P5_1', 'P5_2', 'P5_3', 'P5_4', 'P6_1', 'P6_2', 'P6_3',
                      'P6_4', 'P6_5', 'P6_6', 'P6_7', 'P7_1', 'P7_2', 'P7_3', 'P7_4', 'P7_5', 'P7_6', 'P7_7', 'P7_8',
                      'P8_1', 'P8_2', 'P8_3', 'P8_4', 'P8_5', 'P8_6', 'P8_7']
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\BrailleSkillsProgression.csv", 'a',
                  newline='') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\UEBLiterarySkillsProgression.html"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\UEBLiterarySkillsProgression.html",
                        'w')
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\UEBTechnicalSkillsProgression.html"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\UEBTechnicalSkillsProgression.html",
                        'w')
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\ScreenReaderSkillsProgression.csv"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\ScrenReaderSkillsProgression.csv", 'w')
        list_names = ['date', 'P1_1', 'P1_2', 'P1_3', 'P1_4', 'P1_5', 'P1_6', 'P2_1', 'P2_2', 'P2_3', 'P2_4', 'P3_1',
                      'P3_2', 'P3_3', 'P3_4', 'P3_5', 'P3_6', 'P3_7', 'P3_8', 'P3_9', 'P3_10', 'P3_11', 'P4_1', 'P4_2',
                      'P4_3', 'P4_4', 'P4_5', 'P4_6', 'P4_7']
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\ScrenReaderSkillsProgression.csv", 'a',
                  newline='') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\ScreenReaderSkillsProgression.html"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\ScreenReaderSkillsProgression.html",
                        'w')
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\AbacusSkillsProgression.csv"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\AbacusSkillsProgression.csv", 'w')
        list_names = ['date', 'P1_1', 'P1_2', 'P1_3', 'P1_4', 'P2_1', 'P2_2', 'P2_3', 'P3_1', 'P3_2', 'P3_3', 'P4_1',
                      'P4_2', 'P5_1', 'P5_2', 'P6_1', 'P6_2', 'P6_3', 'P6_4', 'P7_1', 'P7_2', 'P7_3', 'P7_4', 'P8_1',
                      'P8_2']
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\AbacusSkillsProgression.csv", 'a',
                  newline='') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not os.path.exists(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\AbacusSkillsProgression.html"):
        filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\AbacusSkillsProgression.html", 'w')


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
    create_connection(f"{USER_DIR}\\StudentDatabase\\students.db")


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql_create_sql_table):
    try:
        c = conn.cursor()
        c.execute(sql_create_sql_table)
    except Error as e:
        print(e)

    conn.close()


def main():
    sql_create_studentdata_table = "CREATE TABLE IF NOT EXISTS studentdata (id INTEGER PRIMARY KEY AUTOINCREMENT, studentname TEXT NOT NULL, date TEXT NOT NULL, task TEXT NOT NULL, lesson TEXT NOT NULL, session TEXT NOT NULL, trial01 INTEGER, trial02 INTEGER, trial03 INTEGER, trial04 INTEGER, trial05 INTEGER, trial06 INTEGER, trial07 INTEGER, trial08 INTEGER, trial09 INTEGER, trial10 INTEGER, trial11 INTEGER, median FLOAT, notes TEXT NOT NULL );"
    sql_create_brailledata_table = "CREATE TABLE IF NOT EXISTS brailleProgress (id INTEGER PRIMARY KEY AUTOINCREMENT, studentname TEXT NOT NULL, date TEXT NOT NULL,P1_1 INTEGER,P1_2 INTEGER,P1_3 INTEGER,P1_4 INTEGER,P2_1 INTEGER,P2_2 INTEGER,P2_3 INTEGER,P2_4 INTEGER,P2_5 INTEGER,P2_6 INTEGER,P2_7 INTEGER,P2_8 INTEGER,P2_9 INTEGER,P2_10 INTEGER,P2_11 INTEGER,P2_12 INTEGER,P2_13 INTEGER,P2_14 INTEGER,P2_15 INTEGER,P3_1 INTEGER,P3_2 INTEGER,P3_3 INTEGER,P3_4 INTEGER,P3_5 INTEGER,P3_6 INTEGER,P3_7 INTEGER,P3_8 INTEGER,P3_9 INTEGER,P3_10 INTEGER,P3_11 INTEGER,P3_12 INTEGER,P3_13 INTEGER,P3_14 INTEGER,P3_15 INTEGER,P4_1 INTEGER,P4_2 INTEGER,P4_3 INTEGER,P4_4 INTEGER,P5_1 INTEGER,P5_2 INTEGER,P5_3 INTEGER,P5_4 INTEGER,P6_1 INTEGER,P6_2 INTEGER,P6_3 INTEGER,P6_4 INTEGER,P6_5 INTEGER,P6_6 INTEGER,P6_7 INTEGER,P7_1 INTEGER,P7_2 INTEGER,P7_3 INTEGER,P7_4 INTEGER,P7_5 INTEGER,P7_6 INTEGER,P7_7 INTEGER,P7_8 INTEGER,P8_1 INTEGER,P8_2 INTEGER,P8_3 INTEGER,P8_4 INTEGER,P8_5 INTEGER,P8_6 INTEGER,P8_7 );"
    sql_create_screenreaderdata_table = "CREATE TABLE IF NOT EXISTS screenreaderProgress (id INTEGER PRIMARY KEY AUTOINCREMENT, studentname TEXT NOT NULL, date TEXT NOT NULL,P1_1 INTEGER,P1_2 INTEGER,P1_3 INTEGER,P1_4 INTEGER,P2_1 INTEGER,P2_2 INTEGER,P2_3 INTEGER,P2_4 INTEGER,P2_5 INTEGER,P2_6 INTEGER,P2_7 INTEGER,P2_8 INTEGER,P2_9 INTEGER,P2_10 INTEGER,P2_11 INTEGER,P2_12 INTEGER,P2_13 INTEGER,P2_14 INTEGER,P2_15 INTEGER,P3_1 INTEGER,P3_2 INTEGER,P3_3 INTEGER,P3_4 INTEGER,P3_5 INTEGER,P3_6 INTEGER,P3_7 INTEGER,P3_8 INTEGER,P3_9 INTEGER,P3_10 INTEGER,P3_11 INTEGER,P3_12 INTEGER,P3_13 INTEGER,P3_14 INTEGER,P3_15 INTEGER,P4_1 INTEGER,P4_2 INTEGER,P4_3 INTEGER,P4_4 INTEGER,P5_1 INTEGER,P5_2 INTEGER,P5_3 INTEGER,P5_4 INTEGER,P6_1 INTEGER,P6_2 INTEGER,P6_3 INTEGER,P6_4 INTEGER,P6_5 INTEGER,P6_6 INTEGER,P6_7 INTEGER,P7_1 INTEGER,P7_2 INTEGER,P7_3 INTEGER,P7_4 INTEGER,P7_5 INTEGER,P7_6 INTEGER,P7_7 INTEGER,P7_8 INTEGER,P8_1 INTEGER,P8_2 INTEGER,P8_3 INTEGER,P8_4 INTEGER,P8_5 INTEGER,P8_6 INTEGER,P8_7 );"
    sql_create_abacusdata_table = "CREATE TABLE IF NOT EXISTS abacusProgress (id INTEGER PRIMARY KEY AUTOINCREMENT, studentname TEXT NOT NULL, date TEXT NOT NULL,P1_1 INTEGER,P1_2 INTEGER,P1_3 INTEGER,P1_4 INTEGER,P2_1 INTEGER,P2_2 INTEGER,P2_3 INTEGER,P2_4 INTEGER,P2_5 INTEGER,P2_6 INTEGER,P2_7 INTEGER,P2_8 INTEGER,P2_9 INTEGER,P2_10 INTEGER,P2_11 INTEGER,P2_12 INTEGER,P2_13 INTEGER,P2_14 INTEGER,P2_15 INTEGER,P3_1 INTEGER,P3_2 INTEGER,P3_3 INTEGER,P3_4 INTEGER,P3_5 INTEGER,P3_6 INTEGER,P3_7 INTEGER,P3_8 INTEGER,P3_9 INTEGER,P3_10 INTEGER,P3_11 INTEGER,P3_12 INTEGER,P3_13 INTEGER,P3_14 INTEGER,P3_15 INTEGER,P4_1 INTEGER,P4_2 INTEGER,P4_3 INTEGER,P4_4 INTEGER,P5_1 INTEGER,P5_2 INTEGER,P5_3 INTEGER,P5_4 INTEGER,P6_1 INTEGER,P6_2 INTEGER,P6_3 INTEGER,P6_4 INTEGER,P6_5 INTEGER,P6_6 INTEGER,P6_7 INTEGER,P7_1 INTEGER,P7_2 INTEGER,P7_3 INTEGER,P7_4 INTEGER,P7_5 INTEGER,P7_6 INTEGER,P7_7 INTEGER,P7_8 INTEGER,P8_1 INTEGER,P8_2 INTEGER,P8_3 INTEGER,P8_4 INTEGER,P8_5 INTEGER,P8_6 INTEGER,P8_7 );"

    conn = create_connection(f"{USER_DIR}\\StudentDatabase\\students.db")
    if conn is not None:
        create_table(conn, sql_create_studentdata_table)
    else:
        print("Error! cannot create the database connection.")

    conn = create_connection(f"{USER_DIR}\\StudentDatabase\\students.db")
    if conn is not None:
        create_table(conn, sql_create_brailledata_table)
    else:
        print("Error! cannot create the database connection.")

    conn = create_connection(f"{USER_DIR}\\StudentDatabase\\students.db")
    if conn is not None:
        create_table(conn, sql_create_screenreaderdata_table)
    else:
        print("Error! cannot create the database connection.")

    conn = create_connection(f"{USER_DIR}\\StudentDatabase\\students.db")
    if conn is not None:
        create_table(conn, sql_create_abacusdata_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")


class dataPanel(wx.Panel):
    def __init__(self, parent):
        super(dataPanel, self).__init__(parent)
        self.ln = wx.StaticLine(self, -1, pos=(465, 0), style=wx.LI_VERTICAL)
        self.ln.SetSize((5, 900))
        self.ln.IsVertical()
        self.SetBackgroundColour(wx.Colour(241, 205, 234))
        wx.StaticText(self, -1, "Session Information", pos=(170, 20))
        wx.StaticText(self, -1, "Student Name", pos=(30, 50))
        self.studentname1 = wx.Choice(self, -1, choices=students_all, pos=(130, 50), size=(300, 20))
        wx.StaticText(self, -1, "Date", pos=(30, 80))
        self.date1 = wx.StaticText(self, -1, date, pos=(200, 80))
        wx.StaticText(self, -1, "Session Type", pos=(30, 110))
        self.session1 = wx.Choice(self, -1, choices=sessionType, pos=(130, 110), size=(300, 20))
        wx.StaticText(self, -1, "Domain and Lesson", pos=(30, 140))
        self.lesson1 = wx.TreeCtrl(self, 301, pos=(30, 170), size=(400, 650))
        self.root = self.lesson1.AddRoot('Lesson Type ')
        self.item1 = self.lesson1.AppendItem(self.root, 'Abacus')
        for name in abacusSkills:
            self.lesson1.AppendItem(self.item1, name)
        self.item2 = self.lesson1.AppendItem(self.root, 'ScreenReader')
        for name in screenreaderSkills:
            self.lesson1.AppendItem(self.item2, name)
        self.item3 = self.lesson1.AppendItem(self.root, 'Braille')
        for name in brailleSkills:
            self.lesson1.AppendItem(self.item3, name)
        self.item4 = self.lesson1.AppendItem(self.root, 'Magnification')
        for name in magnifierSkills:
            self.lesson1.AppendItem(self.item4, name)
        self.item5 = self.lesson1.AppendItem(self.root, 'iOS')
        for name in iOSSkills:
            self.lesson1.AppendItem(self.item5, name)
        self.item6 = self.lesson1.AppendItem(self.root, 'ECC_CompensatorySkills')
        for name in ECC_CompensatorySkills:
            self.lesson1.AppendItem(self.item6, name)
        self.item7 = self.lesson1.AppendItem(self.root, 'ECC_AssistiveTechnology')
        for name in ECC_AssistiveTechnology:
            self.lesson1.AppendItem(self.item7, name)
        self.item8 = self.lesson1.AppendItem(self.root, 'ECC_SensoryEfficiency')
        for name in ECC_SensoryEfficiency:
            self.lesson1.AppendItem(self.item8, name)
        self.item9 = self.lesson1.AppendItem(self.root, 'ECC_OrientationMobility')
        for name in magnifierSkills:
            self.lesson1.AppendItem(self.item9, name)
        self.item10 = self.lesson1.AppendItem(self.root, 'ECC_RecreationLeisure')
        for name in ECC_RecreationLeisure:
            self.lesson1.AppendItem(self.item10, name)
        self.item11 = self.lesson1.AppendItem(self.root, 'ECC_SelfDetermination')
        for name in ECC_SelfDetermination:
            self.lesson1.AppendItem(self.item11, name)
        self.item12 = self.lesson1.AppendItem(self.root, 'ECC_IndependentLivingSkills')
        for name in ECC_IndependentLivingSkills:
            self.lesson1.AppendItem(self.item12, name)
        self.item13 = self.lesson1.AppendItem(self.root, 'ECC_SocialInteractionSkills')
        for name in ECC_SocialInteractionSkills:
            self.lesson1.AppendItem(self.item13, name)
        self.item14 = self.lesson1.AppendItem(self.root, 'ECC_CareerEducation')
        for name in ECC_CareerEducation:
            self.lesson1.AppendItem(self.item14, name)
        wx.StaticText(self, -1, "Performance", pos=(665, 20))
        wx.StaticText(self, -1, "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent", pos=(490, 50))
        self.blank = wx.TextCtrl(self, -1, "0", pos=(490, 50), size=(0, 0))
        wx.StaticText(self, -1, "Trial 1", pos=(500, 80))
        self.trial011 = wx.TextCtrl(self, -1, "0", pos=(650, 80), size=(300, 20))
        wx.StaticText(self, -1, "Trial 2", pos=(500, 110))
        self.trial021 = wx.TextCtrl(self, -1, "0", pos=(650, 110), size=(300, 20))
        wx.StaticText(self, -1, "Trial 3", pos=(500, 140))
        self.trial031 = wx.TextCtrl(self, -1, "0", pos=(650, 140), size=(300, 20))
        wx.StaticText(self, -1, "Trial 4", pos=(500, 170))
        self.trial041 = wx.TextCtrl(self, -1, "0", pos=(650, 170), size=(300, 20))
        wx.StaticText(self, -1, "Trial 5", pos=(500, 200))
        self.trial051 = wx.TextCtrl(self, -1, "0", pos=(650, 200), size=(300, 20))
        wx.StaticText(self, -1, "Trial 6", pos=(500, 230))
        self.trial061 = wx.TextCtrl(self, -1, "0", pos=(650, 230), size=(300, 20))
        wx.StaticText(self, -1, "Trial 7", pos=(500, 260))
        self.trial071 = wx.TextCtrl(self, -1, "0", pos=(650, 260), size=(300, 20))
        wx.StaticText(self, -1, "Trial 8", pos=(500, 290))
        self.trial081 = wx.TextCtrl(self, -1, "0", pos=(650, 290), size=(300, 20))
        wx.StaticText(self, -1, "Trial 9", pos=(500, 320))
        self.trial091 = wx.TextCtrl(self, -1, "0", pos=(650, 320), size=(300, 20))
        wx.StaticText(self, -1, "Trial 10", pos=(500, 350))
        self.trial101 = wx.TextCtrl(self, -1, "0", pos=(650, 350), size=(300, 20))
        wx.StaticText(self, -1, "Trial 11", pos=(500, 380))
        self.trial111 = wx.TextCtrl(self, -1, "0", pos=(650, 380), size=(300, 20))
        wx.StaticText(self, -1, "Anecdotal Notes", pos=(500, 410))
        self.notes1 = wx.TextCtrl(self, -1, "0", pos=(650, 440), size=(300, 375), style=wx.TE_MULTILINE)
        self.btn = wx.Button(self, 201, "SAVE", pos=(625, 850), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(715, 850), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.exit, id=202)
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        os.chdir(USER_DIR)

    def exit(self, event):
        wx.Exit()

    def save(self, event):
        studentname = self.studentname1.GetString(self.studentname1.GetSelection())
        dateNow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S")
        simpleDate = datetime.datetime.now().strftime("%Y_%m_%d-%H%M")
        item = self.lesson1.GetSelection()
        task = self.lesson1.GetItemText(self.lesson1.GetItemParent(item))
        lesson = self.lesson1.GetItemText(self.lesson1.GetSelection())
        session = self.session1.GetString(self.session1.GetSelection())
        trial01 = self.trial011.GetValue()
        trial02 = self.trial021.GetValue()
        trial03 = self.trial031.GetValue()
        trial04 = self.trial041.GetValue()
        trial05 = self.trial051.GetValue()
        trial06 = self.trial061.GetValue()
        trial07 = self.trial071.GetValue()
        trial08 = self.trial081.GetValue()
        trial09 = self.trial091.GetValue()
        trial10 = self.trial101.GetValue()
        trial11 = self.trial111.GetValue()
        trials = [trial01, trial02, trial03, trial04, trial05, trial06, trial07, trial08, trial09, trial10, trial11]
        trialmedian = statistics.median(trials)
        notes = self.notes1.GetValue()
        if (len(studentname) and len(date) and len(task) and len(notes)) > 0:
            box = wx.TextEntryDialog(None, "Enter Address-Book name to save!", "Title",
                                     f"{studentname.title()}{dateNow}")
            if box.ShowModal() == wx.ID_OK:
                self.studentdatabasename = box.GetValue()
                if not os.path.exists(
                        f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\{self.studentdatabasename}.txt"):
                    self.filename = open(
                        f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\{self.studentdatabasename}.txt", 'w')
                    self.filename.write('studentname' + ',')
                    self.filename.write('simpleDate' + ',')
                    self.filename.write('task' + ',')
                    self.filename.write('lesson' + ',')
                    self.filename.write('session' + ',')
                    self.filename.write('trial01' + ',')
                    self.filename.write('trial02' + ',')
                    self.filename.write('trial03' + ',')
                    self.filename.write('trial04' + ',')
                    self.filename.write('trial05' + ',')
                    self.filename.write('trial06' + ',')
                    self.filename.write('trial07' + ',')
                    self.filename.write('trial08' + ',')
                    self.filename.write('trial09' + ',')
                    self.filename.write('trial10' + ',')
                    self.filename.write('trial11' + ',')
                    self.filename.write('median' + ',')
                    self.filename.write('notes' + ',\n')
                    self.filename.write(studentname + ',')
                    self.filename.write(dateNow + ',')
                    self.filename.write(task + ',')
                    self.filename.write(lesson + ',')
                    self.filename.write(session + ',')
                    self.filename.write(trial01 + ',')
                    self.filename.write(trial02 + ',')
                    self.filename.write(trial03 + ',')
                    self.filename.write(trial04 + ',')
                    self.filename.write(trial05 + ',')
                    self.filename.write(trial06 + ',')
                    self.filename.write(trial07 + ',')
                    self.filename.write(trial08 + ',')
                    self.filename.write(trial09 + ',')
                    self.filename.write(trial10 + ',')
                    self.filename.write(trial11 + ',')
                    self.filename.write(trialmedian + ',')
                    self.filename.write(notes + ',')
                    self.filename.close()
                    self.filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\Filenames.txt", 'a')
                    self.filename.write(
                        f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\{self.studentdatabasename}.txt" + '\n')
                    self.filename.close()
                    self.dial = wx.MessageDialog(None, 'Saved successfully!', 'Info', wx.OK)
                    self.dial.ShowModal()
                else:
                    self.dial = wx.MessageDialog(None, 'Name already exists', 'Info', wx.OK)
                    self.dial.ShowModal()
            else:
                self.dial = wx.MessageDialog(None, 'Save cancelled', 'Info', wx.OK)
                self.dial.ShowModal()
        else:
            self.dial = wx.MessageDialog(None, 'Fill Required Fields!', 'Info', wx.OK)
            self.dial.ShowModal()

        def data_entry():
            conn = sqlite3.connect(f"{USER_DIR}\\StudentDatabase\\students.db")
            c = conn.cursor()
            c.execute(
                "INSERT INTO studentdata (studentname, date, task, lesson, session, trial01, trial02, trial03, trial04, trial05, trial06, trial07, trial08, trial09, trial10, trial11, median, notes) VALUES (?,?,?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?)",
                (studentname, dateNow, task, lesson, session, trial01, trial02, trial03, trial04, trial05, trial06,
                 trial07, trial08, trial09, trial10, trial11, trialmedian, notes))
            conn.commit()
            c.close()
            conn.close()

        data_entry()

        list_data = [studentname, dateNow, task, lesson, session, trial01, trial02, trial03, trial04, trial05, trial06,
                     trial07, trial08, trial09, trial10, trial11, trialmedian, notes]
        os.chdir(USER_DIR)
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{name}\\omnibusDatabase.csv", 'a',
                  newline='') as f_setup:
            writer_setup = writer(f_setup)
            writer_setup.writerow(list_data)
            f_setup.close()

    def OnChoice(self, event):
        self.label.SetLabel(self.choice.GetString(self.choice.GetSelection()))


class braillePanel(scrolled.ScrolledPanel):
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
        self.studentname1 = wx.Choice(self, -1, choices=students_all, pos=(650, 50), size=(300, 20))
        wx.StaticText(self, -1, date, pos=(200, 50))
        wx.StaticText(self, -1, "1.1 Track Left to Right", pos=(30, 80))
        self.trial11 = wx.TextCtrl(self, -1, "0", pos=(650, 80), size=(300, 20))
        wx.StaticText(self, -1, "1.2 Track Top to Bottom", pos=(30, 110))
        self.trial12 = wx.TextCtrl(self, -1, "0", pos=(650, 110), size=(300, 20))
        wx.StaticText(self, -1, "1.3 Discriminate Shapes", pos=(30, 140))
        self.trial13 = wx.TextCtrl(self, -1, "0", pos=(650, 140), size=(300, 20))
        wx.StaticText(self, -1, "1.4 Discriminate Braille Characters", pos=(30, 170))
        self.trial14 = wx.TextCtrl(self, -1, "0", pos=(650, 170), size=(300, 20))
        wx.StaticText(self, -1, "2.1 G C L", pos=(30, 200))
        self.trial21 = wx.TextCtrl(self, -1, "0", pos=(650, 200), size=(300, 20))
        wx.StaticText(self, -1, "2.2 D Y", pos=(30, 230))
        self.trial22 = wx.TextCtrl(self, -1, "0", pos=(650, 230), size=(300, 20))
        wx.StaticText(self, -1, "2.3 A B", pos=(30, 260))
        self.trial23 = wx.TextCtrl(self, -1, "0", pos=(650, 260), size=(300, 20))
        wx.StaticText(self, -1, "2.4 S", pos=(30, 290))
        self.trial24 = wx.TextCtrl(self, -1, "0", pos=(650, 290), size=(300, 20))
        wx.StaticText(self, -1, "2.5 W", pos=(30, 320))
        self.trial25 = wx.TextCtrl(self, -1, "0", pos=(650, 320), size=(300, 20))
        wx.StaticText(self, -1, "2.6 P O", pos=(30, 350))
        self.trial26 = wx.TextCtrl(self, -1, "0", pos=(650, 350), size=(300, 20))
        wx.StaticText(self, -1, "2.7 K", pos=(30, 380))
        self.trial27 = wx.TextCtrl(self, -1, "0", pos=(650, 380), size=(300, 20))
        wx.StaticText(self, -1, "2.8 R", pos=(30, 410))
        self.trial28 = wx.TextCtrl(self, -1, "0", pos=(650, 410), size=(300, 20))
        wx.StaticText(self, -1, "2.9 M E", pos=(30, 440))
        self.trial29 = wx.TextCtrl(self, -1, "0", pos=(650, 440), size=(300, 20))
        wx.StaticText(self, -1, "2.10 H", pos=(30, 470))
        self.trial210 = wx.TextCtrl(self, -1, "0", pos=(650, 470), size=(300, 20))
        wx.StaticText(self, -1, "2.11 N X", pos=(30, 500))
        self.trial211 = wx.TextCtrl(self, -1, "0", pos=(650, 500), size=(300, 20))
        wx.StaticText(self, -1, "2.12 Z F", pos=(30, 530))
        self.trial212 = wx.TextCtrl(self, -1, "0", pos=(650, 530), size=(300, 20))
        wx.StaticText(self, -1, "2.13 U T", pos=(30, 560))
        self.trial213 = wx.TextCtrl(self, -1, "0", pos=(650, 560), size=(300, 20))
        wx.StaticText(self, -1, "2.14 Q I", pos=(30, 590))
        self.trial214 = wx.TextCtrl(self, -1, "0", pos=(650, 590), size=(300, 20))
        wx.StaticText(self, -1, "2.15 V J", pos=(30, 620))
        self.trial215 = wx.TextCtrl(self, -1, "0", pos=(650, 620), size=(300, 20))
        wx.StaticText(self, -1, "3.1 Alphabetic Wordsigns", pos=(30, 650))
        self.trial31 = wx.TextCtrl(self, -1, "0", pos=(650, 650), size=(300, 20))
        wx.StaticText(self, -1, "3.2 Braille Numbers", pos=(30, 680))
        self.trial32 = wx.TextCtrl(self, -1, "0", pos=(650, 680), size=(300, 20))
        wx.StaticText(self, -1, "3.3 Punctuation", pos=(30, 710))
        self.trial33 = wx.TextCtrl(self, -1, "0", pos=(650, 710), size=(300, 20))
        wx.StaticText(self, -1, "3.4 Strong Contractions - AND OF FOR WITH THE", pos=(30, 740))
        self.trial34 = wx.TextCtrl(self, -1, "0", pos=(650, 740), size=(300, 20))
        wx.StaticText(self, -1, "3.5 Strong Groupsigns - CH GH SH TH WH ED ER OU OW ST AR ING", pos=(30, 770))
        self.trial35 = wx.TextCtrl(self, -1, "0", pos=(650, 770), size=(300, 20))
        wx.StaticText(self, -1, "3.6 Strong Wordsigns - CH SH TH WH OU ST", pos=(30, 800))
        self.trial36 = wx.TextCtrl(self, -1, "0", pos=(650, 800), size=(300, 20))
        wx.StaticText(self, -1, "3.7 Lower Groupsigns - BE CON DIS", pos=(30, 830))
        self.trial37 = wx.TextCtrl(self, -1, "0", pos=(650, 830), size=(300, 20))
        wx.StaticText(self, -1, "3.8 Lower Groupsigns - EA BB CC FF GG", pos=(30, 860))
        self.trial38 = wx.TextCtrl(self, -1, "0", pos=(650, 860), size=(300, 20))
        wx.StaticText(self, -1, "3.9 Lower Group/Wordsigns - EN IN", pos=(30, 890))
        self.trial39 = wx.TextCtrl(self, -1, "0", pos=(650, 890), size=(300, 20))
        wx.StaticText(self, -1, "3.10 Lower Wordsigns - BE HIS WAS WERE", pos=(30, 920))
        self.trial310 = wx.TextCtrl(self, -1, "0", pos=(650, 920), size=(300, 20))
        wx.StaticText(self, -1, "3.11 Dot 5 Contractions", pos=(30, 950))
        self.trial311 = wx.TextCtrl(self, -1, "0", pos=(650, 950), size=(300, 20))
        wx.StaticText(self, -1, "3.12 Dot 45 Contractions", pos=(30, 980))
        self.trial312 = wx.TextCtrl(self, -1, "0", pos=(650, 980), size=(300, 20))
        wx.StaticText(self, -1, "3.13 Dot 456 Contractions", pos=(30, 1010))
        self.trial313 = wx.TextCtrl(self, -1, "0", pos=(650, 1010), size=(300, 20))
        wx.StaticText(self, -1, "3.14 Final Letter Groupsigns", pos=(30, 1040))
        self.trial314 = wx.TextCtrl(self, -1, "0", pos=(650, 1040), size=(300, 20))
        wx.StaticText(self, -1, "3.15 Shortform Words", pos=(30, 1070))
        self.trial315 = wx.TextCtrl(self, -1, "0", pos=(650, 1070), size=(300, 20))
        wx.StaticText(self, -1, "4.1 Grade 1 Indicators", pos=(30, 1100))
        self.trial41 = wx.TextCtrl(self, -1, "0", pos=(650, 1100), size=(300, 20))
        wx.StaticText(self, -1, "4.2 Capitals Indicators", pos=(30, 1130))
        self.trial42 = wx.TextCtrl(self, -1, "0", pos=(650, 1130), size=(300, 20))
        wx.StaticText(self, -1, "4.3 Numeric Mode and Spatial Math", pos=(30, 1160))
        self.trial43 = wx.TextCtrl(self, -1, "0", pos=(650, 1160), size=(300, 20))
        wx.StaticText(self, -1, "4.4 Typeform Indicators - ITALIC, SCRIPT, UNDERLINE, SCRIPT", pos=(30, 1190))
        self.trial44 = wx.TextCtrl(self, -1, "0", pos=(650, 1190), size=(300, 20))
        wx.StaticText(self, -1, "5.1 Page Numbering", pos=(30, 1220))
        self.trial51 = wx.TextCtrl(self, -1, "0", pos=(650, 1220), size=(300, 20))
        wx.StaticText(self, -1, "5.2 Headings", pos=(30, 1250))
        self.trial52 = wx.TextCtrl(self, -1, "0", pos=(650, 1250), size=(300, 20))
        wx.StaticText(self, -1, "5.3 Lists", pos=(30, 1280))
        self.trial53 = wx.TextCtrl(self, -1, "0", pos=(650, 1280), size=(300, 20))
        wx.StaticText(self, -1, "5.4 Poetry / Drama", pos=(30, 1310))
        self.trial54 = wx.TextCtrl(self, -1, "0", pos=(650, 1310), size=(300, 20))
        wx.StaticText(self, -1, "6.1 Operation and Comparison Signs", pos=(30, 1340))
        self.trial61 = wx.TextCtrl(self, -1, "0", pos=(650, 1340), size=(300, 20))
        wx.StaticText(self, -1, "6.2 Grade 1 Mode", pos=(30, 1370))
        self.trial62 = wx.TextCtrl(self, -1, "0", pos=(650, 1370), size=(300, 20))
        wx.StaticText(self, -1, "6.3 Special Print Symbols", pos=(30, 1400))
        self.trial63 = wx.TextCtrl(self, -1, "0", pos=(650, 1400), size=(300, 20))
        wx.StaticText(self, -1, "6.4 Omission Marks", pos=(30, 1430))
        self.trial64 = wx.TextCtrl(self, -1, "0", pos=(650, 1430), size=(300, 20))
        wx.StaticText(self, -1, "6.5 Shape Indicators", pos=(30, 1460))
        self.trial65 = wx.TextCtrl(self, -1, "0", pos=(650, 1460), size=(300, 20))
        wx.StaticText(self, -1, "6.6 Roman Numerals", pos=(30, 1490))
        self.trial66 = wx.TextCtrl(self, -1, "0", pos=(650, 1490), size=(300, 20))
        wx.StaticText(self, -1, "6.7 Fractions", pos=(30, 1520))
        self.trial67 = wx.TextCtrl(self, -1, "0", pos=(650, 1520), size=(300, 20))
        wx.StaticText(self, -1, "7.1 Grade 1 Mode and algebra", pos=(30, 1550))
        self.trial71 = wx.TextCtrl(self, -1, "0", pos=(650, 1550), size=(300, 20))
        wx.StaticText(self, -1, "7.2 Grade 1 Mode and Fractions", pos=(30, 1580))
        self.trial72 = wx.TextCtrl(self, -1, "0", pos=(650, 1580), size=(300, 20))
        wx.StaticText(self, -1, "7.3 Advanced Operation and Comparison Signs", pos=(30, 1610))
        self.trial73 = wx.TextCtrl(self, -1, "0", pos=(650, 1610), size=(300, 20))
        wx.StaticText(self, -1, "7.4 Indices", pos=(30, 1640))
        self.trial74 = wx.TextCtrl(self, -1, "0", pos=(650, 1640), size=(300, 20))
        wx.StaticText(self, -1, "7.5 Roots and Radicals", pos=(30, 1670))
        self.trial75 = wx.TextCtrl(self, -1, "0", pos=(650, 1670), size=(300, 20))
        wx.StaticText(self, -1, "7.6 Miscellaneous Shape Indicators", pos=(30, 1700))
        self.trial76 = wx.TextCtrl(self, -1, "0", pos=(650, 1700), size=(300, 20))
        wx.StaticText(self, -1, "7.7 Functions", pos=(30, 1730))
        self.trial77 = wx.TextCtrl(self, -1, "0", pos=(650, 1730), size=(300, 20))
        wx.StaticText(self, -1, "7.8 Greek Letters", pos=(30, 1760))
        self.trial78 = wx.TextCtrl(self, -1, "0", pos=(650, 1760), size=(300, 20))
        wx.StaticText(self, -1, "8.1 Functions", pos=(30, 1790))
        self.trial81 = wx.TextCtrl(self, -1, "0", pos=(650, 1790), size=(300, 20))
        wx.StaticText(self, -1, "8.2 Modifiers, Bars, and Dots", pos=(30, 1820))
        self.trial82 = wx.TextCtrl(self, -1, "0", pos=(650, 1820), size=(300, 20))
        wx.StaticText(self, -1, "8.3 Modifiers, Arrows, and Limits", pos=(30, 1850))
        self.trial83 = wx.TextCtrl(self, -1, "0", pos=(650, 1850), size=(300, 20))
        wx.StaticText(self, -1, "8.4 Probability", pos=(30, 1880))
        self.trial84 = wx.TextCtrl(self, -1, "0", pos=(650, 1880), size=(300, 20))
        wx.StaticText(self, -1, "8.5 Calculus: Differentiation", pos=(30, 1910))
        self.trial85 = wx.TextCtrl(self, -1, "0", pos=(650, 1910), size=(300, 20))
        wx.StaticText(self, -1, "8.6 Calculus: Integration", pos=(30, 1940))
        self.trial86 = wx.TextCtrl(self, -1, "0", pos=(650, 1940), size=(300, 20))
        wx.StaticText(self, -1, "8.7 Vertical Bars", pos=(30, 1970))
        self.trial87 = wx.TextCtrl(self, -1, "0", pos=(650, 1970), size=(300, 20))

        self.btn = wx.Button(self, 201, "SAVE", pos=(450, 2000), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(550, 2000), size=(70, 30))
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
                    f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt"):
                self.filename = open(
                    f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt",
                    'w')
                self.filename.write('studentname' + ',')
                self.filename.write('simpleDate' + ',')
                self.filename.write('trial11' + ',')
                self.filename.write('trial12' + ',')
                self.filename.write('trial13' + ',')
                self.filename.write('trial14' + ',')
                self.filename.write('trial21' + ',')
                self.filename.write('trial22' + ',')
                self.filename.write('trial23' + ',')
                self.filename.write('trial24' + ',')
                self.filename.write('trial25' + ',')
                self.filename.write('trial26' + ',')
                self.filename.write('trial27' + ',')
                self.filename.write('trial28' + ',')
                self.filename.write('trial29' + ',')
                self.filename.write('trial210' + ',')
                self.filename.write('trial211' + ',')
                self.filename.write('trial212' + ',')
                self.filename.write('trial213' + ',')
                self.filename.write('trial214' + ',')
                self.filename.write('trial215' + ',')
                self.filename.write('trial31' + ',')
                self.filename.write('trial32' + ',')
                self.filename.write('trial33' + ',')
                self.filename.write('trial34' + ',')
                self.filename.write('trial35' + ',')
                self.filename.write('trial36' + ',')
                self.filename.write('trial37' + ',')
                self.filename.write('trial38' + ',')
                self.filename.write('trial39' + ',')
                self.filename.write('trial310' + ',')
                self.filename.write('trial311' + ',')
                self.filename.write('trial312' + ',')
                self.filename.write('trial313' + ',')
                self.filename.write('trial314' + ',')
                self.filename.write('trial315' + ',')
                self.filename.write('trial41' + ',')
                self.filename.write('trial42' + ',')
                self.filename.write('trial43' + ',')
                self.filename.write('trial44' + ',')
                self.filename.write('trial51' + ',')
                self.filename.write('trial52' + ',')
                self.filename.write('trial53' + ',')
                self.filename.write('trial54' + ',')
                self.filename.write('trial61' + ',')
                self.filename.write('trial62' + ',')
                self.filename.write('trial63' + ',')
                self.filename.write('trial64' + ',')
                self.filename.write('trial65' + ',')
                self.filename.write('trial66' + ',')
                self.filename.write('trial67' + ',')
                self.filename.write('trial71' + ',')
                self.filename.write('trial72' + ',')
                self.filename.write('trial73' + ',')
                self.filename.write('trial74' + ',')
                self.filename.write('trial75' + ',')
                self.filename.write('trial76' + ',')
                self.filename.write('trial77' + ',')
                self.filename.write('trial78' + ',')
                self.filename.write('trial81' + ',')
                self.filename.write('trial82' + ',')
                self.filename.write('trial83' + ',')
                self.filename.write('trial84' + ',')
                self.filename.write('trial85' + ',')
                self.filename.write('trial86' + ',')
                self.filename.write('trial87' + ',')
                self.filename.write(studentname + ',')
                self.filename.write(dateNow + ',')
                self.filename.write(trial11 + ',')
                self.filename.write(trial12 + ',')
                self.filename.write(trial13 + ',')
                self.filename.write(trial14 + ',')
                self.filename.write(trial21 + ',')
                self.filename.write(trial22 + ',')
                self.filename.write(trial23 + ',')
                self.filename.write(trial24 + ',')
                self.filename.write(trial25 + ',')
                self.filename.write(trial26 + ',')
                self.filename.write(trial27 + ',')
                self.filename.write(trial28 + ',')
                self.filename.write(trial29 + ',')
                self.filename.write(trial210 + ',')
                self.filename.write(trial211 + ',')
                self.filename.write(trial212 + ',')
                self.filename.write(trial213 + ',')
                self.filename.write(trial214 + ',')
                self.filename.write(trial215 + ',')
                self.filename.write(trial31 + ',')
                self.filename.write(trial32 + ',')
                self.filename.write(trial33 + ',')
                self.filename.write(trial34 + ',')
                self.filename.write(trial35 + ',')
                self.filename.write(trial36 + ',')
                self.filename.write(trial37 + ',')
                self.filename.write(trial38 + ',')
                self.filename.write(trial39 + ',')
                self.filename.write(trial310 + ',')
                self.filename.write(trial311 + ',')
                self.filename.write(trial312 + ',')
                self.filename.write(trial313 + ',')
                self.filename.write(trial314 + ',')
                self.filename.write(trial315 + ',')
                self.filename.write(trial41 + ',')
                self.filename.write(trial42 + ',')
                self.filename.write(trial43 + ',')
                self.filename.write(trial44 + ',')
                self.filename.write(trial51 + ',')
                self.filename.write(trial52 + ',')
                self.filename.write(trial53 + ',')
                self.filename.write(trial54 + ',')
                self.filename.write(trial61 + ',')
                self.filename.write(trial62 + ',')
                self.filename.write(trial63 + ',')
                self.filename.write(trial64 + ',')
                self.filename.write(trial65 + ',')
                self.filename.write(trial66 + ',')
                self.filename.write(trial67 + ',')
                self.filename.write(trial71 + ',')
                self.filename.write(trial72 + ',')
                self.filename.write(trial73 + ',')
                self.filename.write(trial74 + ',')
                self.filename.write(trial75 + ',')
                self.filename.write(trial76 + ',')
                self.filename.write(trial77 + ',')
                self.filename.write(trial78 + ',')
                self.filename.write(trial81 + ',')
                self.filename.write(trial82 + ',')
                self.filename.write(trial83 + ',')
                self.filename.write(trial84 + ',')
                self.filename.write(trial85 + ',')
                self.filename.write(trial86 + ',')
                self.filename.write(trial87 + ',')
                self.filename.write(trial12 + ',')
                self.filename.write(trial13 + ',')
                self.filename.write(trial14 + ',')
                self.filename.write(trial21 + ',')
                self.filename.write(trial22 + ',')
                self.filename.write(trial23 + ',')
                self.filename.write(trial24 + ',')
                self.filename.write(trial25 + ',')
                self.filename.write(trial26 + ',')
                self.filename.write(trial27 + ',')
                self.filename.write(trial28 + ',')
                self.filename.write(trial29 + ',')
                self.filename.write(trial210 + ',')
                self.filename.write(trial211 + ',')
                self.filename.write(trial212 + ',')
                self.filename.write(trial213 + ',')
                self.filename.write(trial214 + ',')
                self.filename.write(trial215 + ',')
                self.filename.write(trial31 + ',')
                self.filename.write(trial32 + ',')
                self.filename.write(trial33 + ',')
                self.filename.write(trial34 + ',')
                self.filename.write(trial35 + ',')
                self.filename.write(trial36 + ',')
                self.filename.write(trial37 + ',')
                self.filename.write(trial38 + ',')
                self.filename.write(trial39 + ',')
                self.filename.write(trial310 + ',')
                self.filename.write(trial311 + ',')
                self.filename.write(trial312 + ',')
                self.filename.write(trial313 + ',')
                self.filename.write(trial314 + ',')
                self.filename.write(trial315 + ',')
                self.filename.write(trial41 + ',')
                self.filename.write(trial42 + ',')
                self.filename.write(trial43 + ',')
                self.filename.write(trial44 + ',')
                self.filename.write(trial51 + ',')
                self.filename.write(trial52 + ',')
                self.filename.write(trial53 + ',')
                self.filename.write(trial54 + ',')
                self.filename.write(trial61 + ',')
                self.filename.write(trial62 + ',')
                self.filename.write(trial63 + ',')
                self.filename.write(trial64 + ',')
                self.filename.write(trial65 + ',')
                self.filename.write(trial66 + ',')
                self.filename.write(trial67 + ',')
                self.filename.write(trial71 + ',')
                self.filename.write(trial72 + ',')
                self.filename.write(trial73 + ',')
                self.filename.write(trial74 + ',')
                self.filename.write(trial75 + ',')
                self.filename.write(trial76 + ',')
                self.filename.write(trial77 + ',')
                self.filename.write(trial78 + ',')
                self.filename.write(trial81 + ',')
                self.filename.write(trial82 + ',')
                self.filename.write(trial83 + ',')
                self.filename.write(trial84 + ',')
                self.filename.write(trial85 + ',')
                self.filename.write(trial86 + ',')
                self.filename.write(trial87 + ',')
                self.filename.close()
                self.filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\Filenames.txt", 'a')
                self.filename.write(
                    f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt" + '\n')
                self.filename.close()
                os.chdir(USER_DIR)
                with open(
                        f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\BrailleSkillsProgression.csv",
                        'a',
                        newline='') as f_setup:
                    list_data = [dateNow, trial11, trial12, trial13, trial14,
                                 trial21, trial22, trial23, trial24, trial25,
                                 trial26,  trial27, trial28, trial29, trial210, trial211,
                                 trial212, trial213, trial214, trial215,
                                 trial31,  trial32, trial33, trial34, trial35, trial36,
                                 trial37, trial38, trial39, trial310, trial311,
                                 trial312, trial313, trial314, trial315,  trial41,
                                 trial42, trial43, trial44, trial51, trial52,
                                 trial53, trial54, trial61, trial62, trial63,
                                 trial64, trial65, trial66, trial67, trial71,
                                 trial72,  trial73, trial74, trial75, trial76, trial77, trial78, trial81, trial82, trial83, trial84,  trial85,  trial86, trial87]
                    writer_setup = writer(f_setup)
                    writer_setup.writerow(list_data)
                    f_setup.close()

                self.dial = wx.MessageDialog(None, 'Saved successfully!', 'Info', wx.OK)
                self.dial.ShowModal()
            else:
                self.dial = wx.MessageDialog(None, 'Name already exists', 'Info', wx.OK)
                self.dial.ShowModal()
        else:
            self.dial = wx.MessageDialog(None, 'Save cancelled', 'Info', wx.OK)
            self.dial.ShowModal()

        def data_entry():
            conn = sqlite3.connect(f"{USER_DIR}\\StudentDatabase\\students.db")
            c = conn.cursor()
            c.execute(
                "INSERT INTO brailleProgress (studentname,date,P1_1 ,P1_2 ,P1_3 ,P1_4 ,P2_1 ,P2_2 ,P2_3 ,P2_4 ,P2_5 ,P2_6 ,P2_7 ,P2_8 ,P2_9 ,P2_10 ,P2_11 ,P2_12 ,P2_13 ,P2_14 ,P2_15 ,P3_1 ,P3_2 ,P3_3 ,P3_4 ,P3_5 ,P3_6 ,P3_7 ,P3_8 ,P3_9 ,P3_10 ,P3_11 ,P3_12 ,P3_13 ,P3_14 ,P3_15 ,P4_1 ,P4_2 ,P4_3 ,P4_4 ,P5_1 ,P5_2 ,P5_3 ,P5_4 ,P6_1 ,P6_2 ,P6_3 ,P6_4 ,P6_5 ,P6_6 ,P6_7 ,P7_1 ,P7_2 ,P7_3 ,P7_4 ,P7_5 ,P7_6 ,P7_7 ,P7_8 ,P8_1 ,P8_2 ,P8_3 ,P8_4 ,P8_5 ,P8_6 ,P8_7 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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





    def graph(self, event):
        studentname = self.studentname1.GetString(self.studentname1.GetSelection())
        df = pd.read_csv(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\BrailleSkillsProgression.csv",
                         sep=',', index_col=[0], parse_dates=[0])
        df = df.sort_values(by="date")
        mu, sigma = 0, 0.1
        noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
        df_noisy = df + noise
        fig = make_subplots(
            rows=7, cols=2,
            specs=[[{}, {"rowspan": 2}],
                   [{}, None],
                   [{"rowspan": 2}, {"rowspan": 2}],
                   [None, None],
                   [{"rowspan": 2}, {"rowspan": 2}],
                   [None, None],
                   [{}, {}]],
            subplot_titles=("Phase 1: Tracking Skills", "Phase 2: Braille Alphabet",
                            "Phase 1: Tracking Skills",
                            "Phase 3a: Wordsigns, Numbers,Punctuation",
                            "Phase 3b: Strong Contractions",
                            "Phase 3c: Lower Cell Contractions",
                            "Phase 3d: Multiple Cell Contractions",
                            "Phase 4a: Braille Mode Indicators",
                            "Phase 5: Document Formatting"),
            print_grid=True)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P1_1'], mode="lines+markers",
                       name="Track left to right", legendgroup="Phase 1",
                       legendgrouptitle_text="Phase 1"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P1_2'], mode="lines+markers",
                       name="Track top to bottom", legendgroup="Phase 1",
                       legendgrouptitle_text="Phase 1"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P1_3'].iloc[[-1]], mode="lines+markers",
                       name="Discriminate shapes", legendgroup="Phase 1",
                       legendgrouptitle_text="Phase 1"), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P1_4'], mode="lines+markers",
                       name="Discriminate braille characters", legendgroup="Phase 1",
                       legendgrouptitle_text="Phase 1"), row=2, col=1)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_1'], mode="lines+markers+text",
                       name="Alphabet", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=True), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_1'].iloc[[-1]],
                                 mode="text", text=[" G C L"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_2'], mode="lines+markers+text",
                       name="D Y", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_2'].iloc[[-1]],
                                 mode="text", text=[" D Y"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_3'], mode="lines+markers+text",
                       name="A B", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_3'].iloc[[-1]],
                                 mode="text", text=[" A B"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_4'], mode="lines+markers+text",
                       name="S", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                       showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_4'].iloc[[-1]],
                                 mode="text", text=[" S"], textposition="middle right",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                                 showlegend=False), row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_5'], mode="lines+markers+text",
                       name="W", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                       showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_5'].iloc[[-1]],
                                 mode="text", text=[" W"], textposition="middle right",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                                 showlegend=False), row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_6'], mode="lines+markers+text",
                       name="P O", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_6'].iloc[[-1]],
                                 mode="text", text=[" P O"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_7'], mode="lines+markers+text",
                       name="K", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                       showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_7'].iloc[[-1]],
                                 mode="text", text=[" K"], textposition="middle right",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                                 showlegend=False), row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_8'], mode="lines+markers+text",
                       name="R", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                       showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_8'].iloc[[-1]],
                                 mode="text", text=[" R"], textposition="middle right",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                                 showlegend=False), row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_9'], mode="lines+markers+text",
                       name="M E", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_9'].iloc[[-1]],
                                 mode="text", text=[" M E"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_10'], mode="lines+markers+text",
                       name="H", legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                       showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_10'].iloc[[-1]],
                                 mode="text", text=[" H"], textposition="middle right",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2",
                                 showlegend=False), row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_11'], mode="lines+markers+text",
                       name="N X", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_11'].iloc[[-1]],
                                 mode="text", text=[" N X"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_12'], mode="lines+markers+text",
                       name="Z F", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_12'].iloc[[-1]],
                                 mode="text", text=[" Z F"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_13'], mode="lines+markers+text",
                       name="U T", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_13'].iloc[[-1]],
                                 mode="text", text=[" U T"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_14'], mode="lines+markers+text",
                       name="Q I", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_14'].iloc[[-1]],
                                 mode="text", text=[" Q I"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_15'], mode="lines+markers+text",
                       name="V J ", legendgroup="Phase 2",
                       legendgrouptitle_text="Phase 2", showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P2_15'].iloc[[-1]],
                                 mode="text", text=[" V J"],
                                 textposition="middle right", legendgroup="Phase 2",
                                 legendgrouptitle_text="Phase 2", showlegend=False),
                      row=1, col=2)
        #
        fig.update_layout(showlegend=True)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_1'], mode="lines+markers",
                       name="Alphabetic Wordsigns", legendgroup="Phase 3a",
                       legendgrouptitle_text="Phase 3a"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_2'], mode="lines+markers",
                       name="Braille Numbers", legendgroup="Phase 3a",
                       legendgrouptitle_text="Phase 3a"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_3'], mode="lines+markers",
                       name="Punctuation", legendgroup="Phase 3a",
                       legendgrouptitle_text="Phase 3a"), row=3, col=1)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_4'], mode="lines+markers",
                       name="Strong Contractions <br>(AND OF FOR WITH THE)",
                       legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3,
            col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_5'], mode="lines+markers",
                       name="Strong Groupsigns <br>(CH GH SH TH WH ED ER OU OW ST AR ING)",
                       legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3,
            col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_6'], mode="lines+markers",
                       name="Strong Wordsigns <br>(CH SH TH WH OU ST)",
                       legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3,
            col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_7'], mode="lines+markers",
                       name="Lower Groupsigns <br>(BE CON DIS)", legendgroup="Phase 3c",
                       legendgrouptitle_text="Phase 3c"), row=5, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_8'], mode="lines+markers",
                       name="Lower Groupsigns <br>(EA BB CC FF GG)",
                       legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=5,
            col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_9'], mode="lines+markers",
                       name="Lower Groupsigns/Wordsigns <br>(EN IN)",
                       legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=5,
            col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_10'], mode="lines+markers",
                       name="Lower Wordsigns <br>(BE HIS WAS WERE)",
                       legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=5,
            col=1)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_11'], mode="lines+markers",
                       name="Dot 5 Contractions", legendgroup="Phase 3d",
                       legendgrouptitle_text="Phase 3d"), row=5, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_12'], mode="lines+markers",
                       name="Dot 45 Contractions", legendgroup="Phase 3d",
                       legendgrouptitle_text="Phase 3d"), row=5, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_13'], mode="lines+markers",
                       name="Dot 456 Contractions", legendgroup="Phase 3d",
                       legendgrouptitle_text="Phase 3d"), row=5, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_14'], mode="lines+markers",
                       name="Final Letter Groupsigns", legendgroup="Phase 3d",
                       legendgrouptitle_text="Phase 3d"), row=5, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P3_15'], mode="lines+markers",
                       name="Shortform Words", legendgroup="Phase 3d",
                       legendgrouptitle_text="Phase 3d"), row=5, col=2)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P4_1'], mode="lines+markers",
                       name="Grade 1 Indicators", legendgroup="Phase 4",
                       legendgrouptitle_text="Phase 4"), row=7, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P4_2'], mode="lines+markers",
                       name="Capitals Indicators", legendgroup="Phase 4",
                       legendgrouptitle_text="Phase 4"), row=7, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P4_3'], mode="lines+markers",
                       name="Numeric Mode and Spatial math", legendgroup="Phase 4",
                       legendgrouptitle_text="Phase 4"), row=7, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P4_4'], mode="lines+markers",
                       name="Typeform Indicators <br>(ITALIC, SCRIPT, UNDERLINE, BOLDFACE)",
                       legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=7,
            col=1)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P5_1'], mode="lines+markers",
                       name="Page Numbering", legendgroup="Phase 5",
                       legendgrouptitle_text="Phase 5"), row=7, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P5_2'], mode="lines+markers",
                       name="Headings", legendgroup="Phase 5",
                       legendgrouptitle_text="Phase 5"), row=7, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P5_3'], mode="lines+markers",
                       name="Lists", legendgroup="Phase 5",
                       legendgrouptitle_text="Phase 5"), row=7, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P5_4'], mode="lines+markers",
                       name="Poety / Drama", legendgroup="Phase 5",
                       legendgrouptitle_text="Phase 5"), row=7, col=2)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1,
                      col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=1, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=1, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=1, col=1)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1,
                      col=2)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=1, col=2)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=1, col=2)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=1, col=2)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2,
                      col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=2, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=2, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=2, col=1)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3,
                      col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=3, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=3, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=3, col=1)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3,
                      col=2)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=3, col=2)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=3, col=2)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=3, col=2)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5,
                      col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=5, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=5, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=5, col=1)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5,
                      col=2)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=5, col=2)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=5, col=2)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=5, col=2)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=7,
                      col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=7, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=7, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=7, col=1)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=7,
                      col=2)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=7, col=2)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=7, col=2)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=7, col=2)
        marker = '2022-01-01'
        fig.add_vline(x=marker, line_width=3, line_color="black", row=1, col=1)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=1, col=2)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=2, col=1)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=3, col=1)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=3, col=2)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=5, col=1)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=5, col=2)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=7, col=1)
        fig.add_vline(x=marker, line_width=3, line_color="black", row=7, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=1, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=1, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=2, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=3, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=3, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=5, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=5, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=7, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30"])], row=7, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=1, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=2, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=1, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=3, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=3, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=5, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=5, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=5, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=7, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=7, col=2)
        fig.update_layout(xaxis_tickformat='%d %b', xaxis2_tickformat='%d %b',
                          xaxis3_tickformat='%d %b', xaxis4_tickformat='%d %b',
                          xaxis5_tickformat='%d %b', xaxis6_tickformat='%d %b',
                          xaxis7_tickformat='%d %b', xaxis8_tickformat='%d %b',
                          xaxis9_tickformat='%d %b', template="simple_white",
                          title_text=f"{studentname}: Literary UEB Skills Progression",
                          legend=dict(font=dict(size=10)))

        fig.write_html(
            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\UEBLiterarySkillsProgression.html")
        fig.show()
        #
        fig = make_subplots(
            rows=3, cols=1,
            subplot_titles=(
                "Phase 6: UEB Technical Basics", "Phase 7: Advanced UEB Technical",
                "Phase 8: Accellerated UEB Technical"),
            print_grid=True
        )
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P6_1'], mode="lines+markers",
                       name=" Operation and Comparison Signs", legendgroup="Phase 6",
                       legendgrouptitle_text="Phase 6"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P6_2'], mode="lines+markers",
                       name="Grade 1 Mode", legendgroup="Phase 6",
                       legendgrouptitle_text="Phase 6"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P6_3'], mode="lines+markers",
                       name="Special Print Symbols", legendgroup="Phase 6",
                       legendgrouptitle_text="Phase 6"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P6_4'], mode="lines+markers",
                       name="Omission Marks", legendgroup="Phase 6",
                       legendgrouptitle_text="Phase 6"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P6_5'], mode="lines+markers",
                       name="Shape Indicators", legendgroup="Phase 6",
                       legendgrouptitle_text="Phase 6"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P6_6'], mode="lines+markers",
                       name="Roman Numerals", legendgroup="Phase 6",
                       legendgrouptitle_text="Phase 6"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P6_7'], mode="lines+markers",
                       name="Fractions", legendgroup="Phase 6",
                       legendgrouptitle_text="Phase 6"), row=1, col=1)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_1'], mode="lines+markers",
                       name="Grade 1 Mode and Algebra", legendgroup="Phase 7",
                       legendgrouptitle_text="Phase 7"), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_2'], mode="lines+markers",
                       name="Grade 1 Mode and Fractions", legendgroup="Phase 7",
                       legendgrouptitle_text="Phase 7"), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_3'], mode="lines+markers",
                       name="Advanced Operation and Comparison Signs",
                       legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=2,
            col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_4'], mode="lines+markers",
                       name="Indices", legendgroup="Phase 7",
                       legendgrouptitle_text="Phase 7"), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_5'], mode="lines+markers",
                       name="Roots and Radicals", legendgroup="Phase 7",
                       legendgrouptitle_text="Phase 7"), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_6'], mode="lines+markers",
                       name="Miscellaneous Shape Indicators", legendgroup="Phase 7",
                       legendgrouptitle_text="Phase 7"), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_7'], mode="lines+markers",
                       name="Functions", legendgroup="Phase 7",
                       legendgrouptitle_text="Phase 7"), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P7_8'], mode="lines+markers",
                       name="Greek letters", legendgroup="Phase 7",
                       legendgrouptitle_text="Phase 7"), row=2, col=1)
        #
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P8_1'], mode="lines+markers",
                       name="Functions", legendgroup="Phase 8",
                       legendgrouptitle_text="Phase 8"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P8_2'], mode="lines+markers",
                       name="Modifiers, Bars, and Dots", legendgroup="Phase 8",
                       legendgrouptitle_text="Phase 8"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P8_3'], mode="lines+markers",
                       name="Modifiers, Arrows, and Limits", legendgroup="Phase 8",
                       legendgrouptitle_text="Phase 8"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P8_4'], mode="lines+markers", name="Probability",
                       legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P8_5'], mode="lines+markers", name="Calculus: Differentiation",
                       legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P8_6'], mode="lines+markers", name="Calculus: Integration",
                       legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy['P8_7'], mode="lines+markers", name="Vertical Bars",
                       legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=3, col=1)
        #
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30", "2021-12-31",
                    "2022-01-01", "2022-01-02"])], row=1, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30", "2021-12-31",
                    "2022-01-01", "2022-01-02"])], row=2, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19",
                    "2021-12-20", "2021-12-21", "2021-12-22", "2021-12-23",
                    "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27",
                    "2021-12-28", "2021-12-29", "2021-12-30", "2021-12-31",
                    "2022-01-01", "2022-01-02"])], row=3, col=1)
        #
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=1, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=2, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True,
                         ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=3, col=1)
        #
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=1)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2,
                      col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=2, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=2, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=2, col=1)
        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3,
                      col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2,
                      row=3, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2,
                      row=3, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2,
                      row=3, col=1)

        fig.update_layout(xaxis_tickformat='%d %b', xaxis2_tickformat='%d %b',
                          xaxis3_tickformat='%d %b', template="simple_white",
                          title_text=f"{studentname}: Technical UEB Skills Progression",
                          legend=dict(font=dict(size=10)))
        fig.write_html(
            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\UEBTechnicalSkillsProgression.html")
        fig.show()
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
        wx.StaticText(self, -1, "Student Name", pos=(30, 50))
        self.studentname1 = wx.Choice(self, -1, choices=students_all, pos=(650, 50), size=(300, 20))
        wx.StaticText(self, -1, date, pos=(200, 50))
        wx.StaticText(self, -1, "1.1 turn on and off the screen reader", pos=(30, 80))
        self.trial11 = wx.TextCtrl(self, -1, "0", pos=(650, 80), size=(300, 20))
        wx.StaticText(self, -1,
                      "1.2 utilize modifier keys such as ctrl, alt and shift to enter a modified key command. eg: Ctrl + Left Arrow",
                      pos=(30, 110))
        self.trial12 = wx.TextCtrl(self, -1, "0", pos=(650, 110), size=(300, 20))
        wx.StaticText(self, -1, "1.3 read text using a variety of reading commands", pos=(30, 140))
        self.trial13 = wx.TextCtrl(self, -1, "0", pos=(650, 140), size=(300, 20))
        wx.StaticText(self, -1, "1.4 identify the titles and section titles of documents with Headings", pos=(30, 170))
        self.trial14 = wx.TextCtrl(self, -1, "0", pos=(650, 170), size=(300, 20))
        wx.StaticText(self, -1,
                      "1.5 access documents, open and close programs, and will be able to navigate easily to the desktop.",
                      pos=(30, 200))
        self.trial15 = wx.TextCtrl(self, -1, "0", pos=(650, 200), size=(300, 20))
        wx.StaticText(self, -1, "1.6 switch program focus", pos=(30, 230))
        self.trial16 = wx.TextCtrl(self, -1, "0", pos=(650, 230), size=(300, 20))
        wx.StaticText(self, -1, "2.1 type with all alphanumeric keys on the keyboard.", pos=(30, 260))
        self.trial21 = wx.TextCtrl(self, -1, "0", pos=(650, 260), size=(300, 20))
        wx.StaticText(self, -1, "2.2 navigate to and change screen reader settings", pos=(30, 290))
        self.trial22 = wx.TextCtrl(self, -1, "0", pos=(650, 290), size=(300, 20))
        wx.StaticText(self, -1, "2.3 write and edit documents using a basic understanding of cursor placement.",
                      pos=(30, 320))
        self.trial23 = wx.TextCtrl(self, -1, "0", pos=(650, 320), size=(300, 20))
        wx.StaticText(self, -1, "2.4. select, copy and paste text.", pos=(30, 350))
        self.trial24 = wx.TextCtrl(self, -1, "0", pos=(650, 350), size=(300, 20))
        wx.StaticText(self, -1,
                      "3.1 define common element types on the internet such as Headings, Buttons, Links, Tables as well as text.",
                      pos=(30, 380))
        self.trial31 = wx.TextCtrl(self, -1, "0", pos=(650, 380), size=(300, 20))
        wx.StaticText(self, -1, "3.2 identify each element by type.", pos=(30, 410))
        self.trial32 = wx.TextCtrl(self, -1, "0", pos=(650, 410), size=(300, 20))
        wx.StaticText(self, -1, "3.3 navigate to the address bar", pos=(30, 440))
        self.trial33 = wx.TextCtrl(self, -1, "0", pos=(650, 440), size=(300, 20))
        wx.StaticText(self, -1,
                      "3.4 Use the “Tab” key to navigate to the next clickable object (Shift Tab for previous) (METHOD 1) ",
                      pos=(30, 470))
        self.trial34 = wx.TextCtrl(self, -1, "0", pos=(650, 470), size=(300, 20))
        wx.StaticText(self, -1,
                      "3.5 navigate by “Quick Keys” (h for heading, b for button, v, and u for link) (METHOD 2)",
                      pos=(30, 500))
        self.trial35 = wx.TextCtrl(self, -1, "0", pos=(650, 500), size=(300, 20))
        wx.StaticText(self, -1, "3.6 use Elements Lists on a website to navigate by element type (METHOD 3)",
                      pos=(30, 530))
        self.trial36 = wx.TextCtrl(self, -1, "0", pos=(650, 530), size=(300, 20))
        wx.StaticText(self, -1, "3.7 justify why he/she/they selected a particular method for the situation.",
                      pos=(30, 560))
        self.trial37 = wx.TextCtrl(self, -1, "0", pos=(650, 560), size=(300, 20))
        wx.StaticText(self, -1, "3.8 switch tab focus", pos=(30, 590))
        self.trial38 = wx.TextCtrl(self, -1, "0", pos=(650, 590), size=(300, 20))
        wx.StaticText(self, -1,
                      "3.9 switch between screen reader modes. (Forms Mode in JAWS or Browse/Focus Mode in NVDA)",
                      pos=(30, 620))
        self.trial39 = wx.TextCtrl(self, -1, "0", pos=(650, 620), size=(300, 20))
        wx.StaticText(self, -1, "3.10 navigate a table.", pos=(30, 650))
        self.trial310 = wx.TextCtrl(self, -1, "0", pos=(650, 650), size=(300, 20))
        wx.StaticText(self, -1, "3.11 develop a navigation sequence to access an unfamiliar website.", pos=(30, 680))
        self.trial311 = wx.TextCtrl(self, -1, "0", pos=(650, 680), size=(300, 20))
        wx.StaticText(self, -1, "4.1 be able to save and open files using File Explorer.", pos=(30, 710))
        self.trial41 = wx.TextCtrl(self, -1, "0", pos=(650, 710), size=(300, 20))
        wx.StaticText(self, -1, "4.2 create folders and move files in File Explorer.", pos=(30, 740))
        self.trial42 = wx.TextCtrl(self, -1, "0", pos=(650, 740), size=(300, 20))
        wx.StaticText(self, -1,
                      "4.3 navigate a cloud-based file management system (eg: Google Drive, Microsoft OneDrive)",
                      pos=(30, 770))
        self.trial43 = wx.TextCtrl(self, -1, "0", pos=(650, 770), size=(300, 20))
        wx.StaticText(self, -1,
                      "4.4 download material from the internet and place that material in a location on the computer.",
                      pos=(30, 800))
        self.trial44 = wx.TextCtrl(self, -1, "0", pos=(650, 800), size=(300, 20))
        wx.StaticText(self, -1, "4.5 extract zipped folders.", pos=(30, 830))
        self.trial45 = wx.TextCtrl(self, -1, "0", pos=(650, 830), size=(300, 20))
        wx.StaticText(self, -1,
                      "4.6 utilize the virtual cursor and mouse keys as a backup to access inaccessible elements.",
                      pos=(30, 860))
        self.trial46 = wx.TextCtrl(self, -1, "0", pos=(650, 860), size=(300, 20))
        wx.StaticText(self, -1, "4.7 to use OCR features to read inaccessible material.", pos=(30, 890))
        self.trial47 = wx.TextCtrl(self, -1, "0", pos=(650, 890), size=(300, 20))

        self.btn = wx.Button(self, 201, "SAVE", pos=(450, 930), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(550, 930), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.exit, id=202)
        self.btn = wx.Button(self, 203, "PRINT GRAPHS", pos=(450, 970), size=(170, 30))
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
        trial15 = self.trial15.GetValue()
        trial16 = self.trial16.GetValue()
        trial21 = self.trial21.GetValue()
        trial22 = self.trial22.GetValue()
        trial23 = self.trial23.GetValue()
        trial24 = self.trial24.GetValue()
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
        trial41 = self.trial41.GetValue()
        trial42 = self.trial42.GetValue()
        trial43 = self.trial43.GetValue()
        trial44 = self.trial44.GetValue()
        trial45 = self.trial45.GetValue()
        trial46 = self.trial46.GetValue()
        trial47 = self.trial47.GetValue()

        box = wx.TextEntryDialog(None, "Enter Address-Book name to save!", "Title",
                                 f"screenreader{studentname.title()}{dateNow}")
        if box.ShowModal() == wx.ID_OK:
            self.studentdatabasename = box.GetValue()
            if not os.path.exists(
                    f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt"):
                if box.ShowModal() == wx.ID_OK:
                    self.studentdatabasename = box.GetValue()
                    if not os.path.exists(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt"):
                        self.filename = open(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt",
                            'w')
                        self.filename.write('studentname' + ',')
                        self.filename.write('simpleDate' + ',')
                        self.filename.write('trial11' + ',')
                        self.filename.write('trial12' + ',')
                        self.filename.write('trial13' + ',')
                        self.filename.write('trial14' + ',')
                        self.filename.write('trial15' + ',')
                        self.filename.write('trial16' + ',')
                        self.filename.write('trial21' + ',')
                        self.filename.write('trial22' + ',')
                        self.filename.write('trial23' + ',')
                        self.filename.write('trial24' + ',')
                        self.filename.write('trial31' + ',')
                        self.filename.write('trial32' + ',')
                        self.filename.write('trial33' + ',')
                        self.filename.write('trial34' + ',')
                        self.filename.write('trial35' + ',')
                        self.filename.write('trial36' + ',')
                        self.filename.write('trial37' + ',')
                        self.filename.write('trial38' + ',')
                        self.filename.write('trial39' + ',')
                        self.filename.write('trial310' + ',')
                        self.filename.write('trial311' + ',')
                        self.filename.write('trial41' + ',')
                        self.filename.write('trial42' + ',')
                        self.filename.write('trial43' + ',')
                        self.filename.write('trial44' + ',')
                        self.filename.write('trial45' + ',')
                        self.filename.write('trial46' + ',')
                        self.filename.write('trial47' + ',')
                        self.filename.write(studentname + ',')
                        self.filename.write(dateNow + ',')
                        self.filename.write(trial11 + ',')
                        self.filename.write(trial12 + ',')
                        self.filename.write(trial13 + ',')
                        self.filename.write(trial14 + ',')
                        self.filename.write(trial15 + ',')
                        self.filename.write(trial16 + ',')
                        self.filename.write(trial21 + ',')
                        self.filename.write(trial22 + ',')
                        self.filename.write(trial23 + ',')
                        self.filename.write(trial24 + ',')
                        self.filename.write(trial31 + ',')
                        self.filename.write(trial32 + ',')
                        self.filename.write(trial33 + ',')
                        self.filename.write(trial34 + ',')
                        self.filename.write(trial35 + ',')
                        self.filename.write(trial36 + ',')
                        self.filename.write(trial37 + ',')
                        self.filename.write(trial38 + ',')
                        self.filename.write(trial39 + ',')
                        self.filename.write(trial310 + ',')
                        self.filename.write(trial311 + ',')
                        self.filename.write(trial41 + ',')
                        self.filename.write(trial42 + ',')
                        self.filename.write(trial43 + ',')
                        self.filename.write(trial44 + ',')
                        self.filename.write(trial45 + ',')
                        self.filename.write(trial46 + ',')
                        self.filename.write(trial47 + ',')
                        self.filename.close()
                        self.filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\Filenames.txt", 'a')
                        self.filename.write(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt" + '\n')
                        self.filename.close()
                        self.dial = wx.MessageDialog(None, 'Saved successfully!', 'Info', wx.OK)
                        self.dial.ShowModal()
                    else:
                        self.dial = wx.MessageDialog(None, 'Name already exists', 'Info', wx.OK)
                        self.dial.ShowModal()
                else:
                    self.dial = wx.MessageDialog(None, 'Save cancelled', 'Info', wx.OK)
                    self.dial.ShowModal()
        else:
            self.dial = wx.MessageDialog(None, 'Fill Required Fields!', 'Info', wx.OK)
            self.dial.ShowModal()

        def data_entry():
            conn = sqlite3.connect(f"{USER_DIR}\\StudentDatabase\\students.db")
            c = conn.cursor()
            c.execute(
                "INSERT INTO brailleProgress (studentname,date,P1_1,P1_2,P1_3,P1_4,P1_5,P1_6,P2_1,P2_2,P2_3,P2_4,P3_1,P3_2,P3_3,P3_4,P3_5,P3_6,P3_7,P3_8,P3_9,P3_10,P3_11,P4_1,P4_2,P4_3,P4_4,P4_5,P4_6,P4_7) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (studentname, dateNow, trial11, trial12, trial13, trial14, trial15, trial16, trial21, trial22, trial23,
                 trial24,
                 trial31, trial32, trial33, trial34, trial35, trial36, trial37, trial38, trial39, trial310, trial311,
                 trial41, trial42, trial43, trial44, trial45, trial46, trial47))
            conn.commit()

        data_entry()

        # list_names = ['date','P1_1','P1_2','P1_3','P1_4','P1_5','P1_6','P2_1','P2_2','P2_3','P2_4','P3_1','P3_2','P3_3','P3_4','P3_5','P3_6','P3_7','P3_8','P3_9','P3_10','P3_11','P4_1','P4_2','P4_3','P4_4','P4_5','P4_6','P4_7']

        list_data = [studentname, dateNow, trial11, trial12, trial13, trial14, trial15, trial16, trial21, trial22,
                     trial23, trial24,
                     trial31, trial32, trial33, trial34, trial35, trial36, trial37, trial38, trial39, trial310,
                     trial311,
                     trial41, trial42, trial43, trial44, trial45, trial46, trial47]

        os.chdir(USER_DIR)
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\ScreenReaderSkillsProgression.csv",
                  'a',
                  newline='') as f_setup:
            writer_setup = writer(f_setup)
            writer_setup.writerow(list_data)
            f_setup.close()

    def graph(self, event):
        studentname = self.studentname1.GetString(self.studentname1.GetSelection())
        df = pd.read_csv(
            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\ScreenReaderSkillsProgression.csv",
            sep=',', index_col=[0], parse_dates=[0])
        df = df.sort_values(by="date")
        mu, sigma = 0, 0.1
        noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
        df_noisy = df + noise

        fig = make_subplots(
            rows=5, cols=2,
            specs=[[{}, {"rowspan": 2}],
                   [{}, None],
                   [{"rowspan": 2}, {}],
                   [None, {}],
                   [{}, {}]],
            subplot_titles=(
                "Phase 1a: Reading", "Phase 2: Writing", "Phase 1b: Reading", "Phase 3a: Internet",
                "Phase 3b: Internet",
                "Phase 3c: Internet", "Phase 4a: File Management", "Phase 4b: File Management"),
            # print_grid=True
        )

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.1"], mode="lines+markers", name="Turn ON/OFF",
                                 legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.2"], mode="lines+markers", name="Use Modifier Keys",
                                 legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.3"], mode="lines+markers", name="Use Reading Commands",
                       legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.4"], mode="lines+markers", name="ID Titles",
                                 legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.5"], mode="lines+markers", name="Access Documents",
                                 legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.6"], mode="lines+markers", name="Switch Program Focus",
                       legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P2.1"], mode="lines+markers", name="Type with all keys",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P2.2"], mode="lines+markers", name="Change Screen Reader Settings",
                       legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P2.3"], mode="lines+markers", name="Write documents",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P2.4"], mode="lines+markers", name="Copy/Paste Text",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.4"], mode="lines+markers", name="TAB Navigation",
                                 legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.5"], mode="lines+markers", name="Quick Key Navigation",
                       legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.6"], mode="lines+markers", name="Elements List Navigation",
                       legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.7"], mode="lines+markers", name="Justify Navigation Method",
                       legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)

        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.1"], mode="lines+markers", name="Define HTML Elements",
                       legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.2"], mode="lines+markers", name="ID HTML Elements",
                                 legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.3"], mode="lines+markers", name="Navigate to Address Bar",
                       legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.8"], mode="lines+markers", name="ALT-TAB Focus",
                                 legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)

        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.9"], mode="lines+markers", name="Toggle Screen Reader Mode",
                       legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.10"], mode="lines+markers", name="Navigate a Table",
                                 legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.11"], mode="lines+markers", name="Navigation Sequence",
                       legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.1"], mode="lines+markers", name="Save and Open Files",
                                 legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.2"], mode="lines+markers", name="Create Folders",
                                 legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.3"], mode="lines+markers", name="Navigate Cloud Storage",
                       legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
        fig.add_trace(
            go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.4"], mode="lines+markers", name="Download from Internet",
                       legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.5"], mode="lines+markers", name="UNZIP Folders",
                                 legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.6"], mode="lines+markers", name="Use Virtual Cursor",
                                 legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.7"], mode="lines+markers", name="Use Built-In OCR",
                                 legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)

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

        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=1, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=1, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=2, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=3, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=3, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=3, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=4, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=5, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=5, col=2)

        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=1, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=2, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=1, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=3, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=3, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=4, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=5, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=5, col=2)

        fig.update_layout(template="simple_white", title_text=f"{studentname}: Screen Reader Skills Progression")

        fig.write_html(
            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\ScreenReaderSkillsProgression.html")
class abacusPanel(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(wx.StaticLine(self, -1, size=(1500, -1)), 0, wx.ALL, 5)
        vbox.Add(wx.StaticLine(self, -1, size=(-1, 2100)), 0, wx.ALL, 5)
        vbox.Add((20, 20))
        self.SetSizer(vbox)
        self.SetupScrolling()
        self.SetBackgroundColour(wx.Colour(241, 205, 234))
        wx.StaticText(self, -1, "Student Name", pos=(30, 50))
        self.studentname1 = wx.Choice(self, -1, choices=students_all, pos=(650, 50), size=(300, 20))
        wx.StaticText(self, -1, date, pos=(200, 50))

        wx.StaticText(self, -1, "1.1 Setting NumbersNumbers", pos=(30, 80))
        self.trial11 = wx.TextCtrl(self, -1, "0", pos=(650, 80), size=(300, 20))
        wx.StaticText(self, -1, "1.2 Clearing Beads", pos=(30, 110))
        self.trial12 = wx.TextCtrl(self, -1, "0", pos=(650, 110), size=(300, 20))
        wx.StaticText(self, -1, "1.3 Place Value", pos=(30, 140))
        self.trial13 = wx.TextCtrl(self, -1, "0", pos=(650, 140), size=(300, 20))
        wx.StaticText(self, -1, "1.4 Vocabulary", pos=(30, 170))
        self.trial14 = wx.TextCtrl(self, -1, "0", pos=(650, 170), size=(300, 20))
        wx.StaticText(self, -1, "2.1 Addition of Single Digit Numbers", pos=(30, 200))
        self.trial21 = wx.TextCtrl(self, -1, "0", pos=(650, 200), size=(300, 20))
        wx.StaticText(self, -1, "2.2 Addition of Multiple Digit Numbers – Direct", pos=(30, 230))
        self.trial22 = wx.TextCtrl(self, -1, "0", pos=(650, 230), size=(300, 20))
        wx.StaticText(self, -1, "2.3 Addition of Multiple Digit Numbers – Indirect", pos=(30, 260))
        self.trial23 = wx.TextCtrl(self, -1, "0", pos=(650, 260), size=(300, 20))
        wx.StaticText(self, -1, "3.1 Subtraction", pos=(30, 290))
        self.trial31 = wx.TextCtrl(self, -1, "0", pos=(650, 290), size=(300, 20))
        wx.StaticText(self, -1, "3.2 Subtraction of Multiple Digit Numbers – Direct", pos=(30, 320))
        self.trial32 = wx.TextCtrl(self, -1, "0", pos=(650, 320), size=(300, 20))
        wx.StaticText(self, -1, "3.3 Subtraction of Multiple Digit Numbers – Indirect", pos=(30, 350))
        self.trial33 = wx.TextCtrl(self, -1, "0", pos=(650, 350), size=(300, 20))
        wx.StaticText(self, -1, "4.1 Multiplication – 2+ Digit Multiplicand, 1 Digit Multiplier", pos=(30, 380))
        self.trial41 = wx.TextCtrl(self, -1, "0", pos=(650, 380), size=(300, 20))
        wx.StaticText(self, -1, "4.2 Multiplication – 2+ Digit Multiplicand AND Multiplier", pos=(30, 410))
        self.trial42 = wx.TextCtrl(self, -1, "0", pos=(650, 410), size=(300, 20))
        wx.StaticText(self, -1, "5.1 Division – 2+ Digit Dividend, 1 Digit Divisor ", pos=(30, 440))
        self.trial51 = wx.TextCtrl(self, -1, "0", pos=(650, 440), size=(300, 20))
        wx.StaticText(self, -1, "5.2 Division – 2+ Digit Dividend AND 1 Digit Divisor ", pos=(30, 470))
        self.trial52 = wx.TextCtrl(self, -1, "0", pos=(650, 470), size=(300, 20))
        wx.StaticText(self, -1, "6.1 Addition of Decimals", pos=(30, 500))
        self.trial61 = wx.TextCtrl(self, -1, "0", pos=(650, 500), size=(300, 20))
        wx.StaticText(self, -1, "6.2 Subtraction of Decimals", pos=(30, 530))
        self.trial62 = wx.TextCtrl(self, -1, "0", pos=(650, 530), size=(300, 20))
        wx.StaticText(self, -1, "6.3 Multiplication of Decimals", pos=(30, 560))
        self.trial63 = wx.TextCtrl(self, -1, "0", pos=(650, 560), size=(300, 20))
        wx.StaticText(self, -1, "6.4 Division of Decimals", pos=(30, 590))
        self.trial64 = wx.TextCtrl(self, -1, "0", pos=(650, 590), size=(300, 20))
        wx.StaticText(self, -1, "7.1 Addition of Fractions", pos=(30, 620))
        self.trial71 = wx.TextCtrl(self, -1, "0", pos=(650, 620), size=(300, 20))
        wx.StaticText(self, -1, "7.2 Subtraction of Fractions", pos=(30, 650))
        self.trial72 = wx.TextCtrl(self, -1, "0", pos=(650, 650), size=(300, 20))
        wx.StaticText(self, -1, "7.3 Multiplication of Fractions", pos=(30, 680))
        self.trial73 = wx.TextCtrl(self, -1, "0", pos=(650, 680), size=(300, 20))
        wx.StaticText(self, -1, "7.4 Division of Fractions", pos=(30, 710))
        self.trial74 = wx.TextCtrl(self, -1, "0", pos=(650, 710), size=(300, 20))
        wx.StaticText(self, -1, "8.1 Percent", pos=(30, 740))
        self.trial81 = wx.TextCtrl(self, -1, "0", pos=(650, 740), size=(300, 20))
        wx.StaticText(self, -1, "8.2 Square Root", pos=(30, 770))
        self.trial82 = wx.TextCtrl(self, -1, "0", pos=(650, 770), size=(300, 20))
        self.btn = wx.Button(self, 201, "SAVE", pos=(450, 830), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(550, 830), size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.exit, id=202)
        self.btn = wx.Button(self, 203, "PRINT GRAPHS", pos=(450, 870), size=(170, 30))
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
        trial31 = self.trial31.GetValue()
        trial32 = self.trial32.GetValue()
        trial33 = self.trial33.GetValue()
        trial41 = self.trial41.GetValue()
        trial42 = self.trial42.GetValue()
        trial51 = self.trial51.GetValue()
        trial52 = self.trial52.GetValue()
        trial61 = self.trial61.GetValue()
        trial62 = self.trial62.GetValue()
        trial63 = self.trial63.GetValue()
        trial64 = self.trial64.GetValue()
        trial71 = self.trial71.GetValue()
        trial72 = self.trial72.GetValue()
        trial73 = self.trial73.GetValue()
        trial74 = self.trial74.GetValue()
        trial81 = self.trial81.GetValue()
        trial82 = self.trial82.GetValue()

        box = wx.TextEntryDialog(None, "Enter Address-Book name to save!", "Title",
                                 f"abacus{studentname.title()}{dateNow}")
        if box.ShowModal() == wx.ID_OK:
            self.studentdatabasename = box.GetValue()
            if not os.path.exists(
                    f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt"):
                if box.ShowModal() == wx.ID_OK:
                    self.studentdatabasename = box.GetValue()
                    if not os.path.exists(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt"):
                        self.filename = open(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt",
                            'w')
                        self.filename.write('studentname' + ',')
                        self.filename.write('simpleDate' + ',')
                        self.filename.write('trial11' + ',')
                        self.filename.write('trial12' + ',')
                        self.filename.write('trial13' + ',')
                        self.filename.write('trial14' + ',')
                        self.filename.write('trial21' + ',')
                        self.filename.write('trial22' + ',')
                        self.filename.write('trial23' + ',')
                        self.filename.write('trial31' + ',')
                        self.filename.write('trial32' + ',')
                        self.filename.write('trial33' + ',')
                        self.filename.write('trial41' + ',')
                        self.filename.write('trial42' + ',')
                        self.filename.write('trial51' + ',')
                        self.filename.write('trial52' + ',')
                        self.filename.write('trial61' + ',')
                        self.filename.write('trial62' + ',')
                        self.filename.write('trial63' + ',')
                        self.filename.write('trial64' + ',')
                        self.filename.write('trial71' + ',')
                        self.filename.write('trial72' + ',')
                        self.filename.write('trial73' + ',')
                        self.filename.write('trial74' + ',')
                        self.filename.write('trial81' + ',')
                        self.filename.write('trial82' + ',')
                        self.filename.write(studentname + ',')
                        self.filename.write(trial11 + ',')
                        self.filename.write(trial12 + ',')
                        self.filename.write(trial13 + ',')
                        self.filename.write(trial14 + ',')
                        self.filename.write(trial21 + ',')
                        self.filename.write(trial22 + ',')
                        self.filename.write(trial23 + ',')
                        self.filename.write(trial31 + ',')
                        self.filename.write(trial32 + ',')
                        self.filename.write(trial33 + ',')
                        self.filename.write(trial41 + ',')
                        self.filename.write(trial42 + ',')
                        self.filename.write(trial51 + ',')
                        self.filename.write(trial52 + ',')
                        self.filename.write(trial61 + ',')
                        self.filename.write(trial62 + ',')
                        self.filename.write(trial63 + ',')
                        self.filename.write(trial64 + ',')
                        self.filename.write(trial71 + ',')
                        self.filename.write(trial72 + ',')
                        self.filename.write(trial73 + ',')
                        self.filename.write(trial74 + ',')
                        self.filename.write(trial81 + ',')
                        self.filename.write(trial82 + ',')
                        self.filename.close()
                        self.filename = open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\Filenames.txt", 'a')
                        self.filename.write(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{self.studentdatabasename}.txt" + '\n')
                        self.filename.close()
                        self.dial = wx.MessageDialog(None, 'Saved successfully!', 'Info', wx.OK)
                        self.dial.ShowModal()
                    else:
                        self.dial = wx.MessageDialog(None, 'Name already exists', 'Info', wx.OK)
                        self.dial.ShowModal()
                else:
                    self.dial = wx.MessageDialog(None, 'Save cancelled', 'Info', wx.OK)
                    self.dial.ShowModal()
        else:
            self.dial = wx.MessageDialog(None, 'Fill Required Fields!', 'Info', wx.OK)
            self.dial.ShowModal()

        def data_entry():
            conn = sqlite3.connect(f"{USER_DIR}\\StudentDatabase\\students.db")
            c = conn.cursor()
            c.execute(
                "INSERT INTO abacusProgress (studentname, date,P1_1,P1_2,P1_3,P1_4,P2_1,P2_2,P2_3,P3_1,P3_2,P3_3,P4_1,P4_2,P5_1,P5_2,P6_1,P6_2,P6_3,P6_4,P7_1,P7_2,P7_3,P7_4,P8_1,P8_2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (studentname, dateNow, trial11, trial12, trial13, trial14, trial21, trial22, trial23, trial31, trial32,
                 trial33, trial41, trial42, trial51, trial52, trial61, trial62, trial63, trial64, trial71, trial72,
                 trial73, trial74, trial81, trial82))
            conn.commit()

        data_entry()
        list_names = ['date', 'P1_1', 'P1_2', 'P1_3', 'P1_4', 'P2_1', 'P2_2', 'P2_3', 'P3_1', 'P3_2', 'P3_3', 'P4_1',
                      'P4_2', 'P5_1', 'P5_2', 'P6_1', 'P6_2', 'P6_3', 'P6_4', 'P7_1', 'P7_2', 'P7_3', 'P7_4', 'P8_1',
                      'P8_2']
        list_data = [dateNow, trial11, trial12, trial13, trial14, trial21, trial22, trial23, trial31, trial32, trial33,
                     trial41, trial42, trial51, trial52, trial61, trial62, trial63, trial64, trial71, trial72,
                     trial73, trial74, trial81, trial82]
        os.chdir(USER_DIR)
        with open(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\AbacusSkillsProgression.csv", 'a',
                  newline='') as f_setup:
            writer_setup = writer(f_setup)
            writer_setup.writerow(list_data)
            f_setup.close()

    def graph(self, event):
        studentname = self.studentname1.GetString(self.studentname1.GetSelection())
        df = pd.read_csv(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\AbacusSkillsProgression.csv",
                         sep=',', index_col=[0], parse_dates=[0])
        df = df.sort_values(by="date")
        mu, sigma = 0, 0.1
        noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
        df_noisy = df + noise

        fig = make_subplots(
            rows=4, cols=2,
            subplot_titles=(
                "Phase 1: Foundation", "Phase 2: Addition", "Phase 3: Subtraction", "Phase 4: Multiplication",
                "Phase 5: Division", "Phase 6: Decimals", "Phase 7: Fractions", "Phase 8: Special Functions"),
            # print_grid=True
        )

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.1"], mode="lines+markers", name="Setting Numbers",
                                 legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.2"], mode="lines+markers", name="Clearing Beads",
                                 legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.3"], mode="lines+markers", name="Place Value",
                                 legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P1.4"], mode="lines+markers", name="Vocabulary",
                                 legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P2.1"], mode="lines+markers", name="Setting Numbers",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P2.2"], mode="lines+markers", name="Clearing Beads",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P2.3"], mode="lines+markers", name="Place Value",
                                 legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.1"], mode="lines+markers", name="Setting Numbers",
                                 legendgroup="Phase 3", legendgrouptitle_text="Phase 3"), row=2, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.2"], mode="lines+markers", name="Clearing Beads",
                                 legendgroup="Phase 3", legendgrouptitle_text="Phase 3"), row=2, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P3.3"], mode="lines+markers", name="Place Value",
                                 legendgroup="Phase 3", legendgrouptitle_text="Phase 3"), row=2, col=1)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.1"], mode="lines+markers", name="Setting Numbers",
                                 legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=2, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P4.2"], mode="lines+markers", name="Clearing Beads",
                                 legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=2, col=2)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P5.1"], mode="lines+markers", name="Place Value",
                                 legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=3, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P5.2"], mode="lines+markers", name="Vocabulary",
                                 legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=3, col=1)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P6.1"], mode="lines+markers", name="Setting Numbers",
                                 legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P6.2"], mode="lines+markers", name="Clearing Beads",
                                 legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P6.3"], mode="lines+markers", name="Place Value",
                                 legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P6.4"], mode="lines+markers", name="Vocabulary",
                                 legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P7.1"], mode="lines+markers", name="Setting Numbers",
                                 legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P7.2"], mode="lines+markers", name="Clearing Beads",
                                 legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P7.3"], mode="lines+markers", name="Place Value",
                                 legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P7.4"], mode="lines+markers", name="Vocabulary",
                                 legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)

        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P8.1"], mode="lines+markers", name="Setting Numbers",
                                 legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=4, col=2)
        fig.add_trace(go.Scatter(x=df_noisy.index[[-1]], y=df_noisy["P8.2"], mode="lines+markers", name="Clearing Beads",
                                 legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=4, col=2)

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

        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=2)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=2)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=2)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=2)

        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=1)

        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=2)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=2)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=2)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=2)

        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=4, col=1)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=4, col=1)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=4, col=1)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=4, col=1)

        fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=4, col=2)
        fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=4, col=2)
        fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=4, col=2)
        fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=4, col=2)

        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=1, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=1, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=2, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=2, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=3, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=3, col=2)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=4, col=1)
        fig.update_xaxes(rangebreaks=[dict(
            values=["2021-12-16", "2021-12-17", "2021-12-18", "2021-12-19", "2021-12-20", "2021-12-21", "2021-12-22",
                    "2021-12-23", "2021-12-24", "2021-12-25", "2021-12-26", "2021-12-27", "2021-12-28", "2021-12-29",
                    "2021-12-30", "2021-12-31", "2022-01-01", "2022-01-02"])], row=4, col=2)

        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=1, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=1, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=2, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=2, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=3, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=3, col=2)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=4, col=1)
        fig.update_yaxes(range=[-.5, 3.5], fixedrange=True, ticktext=["Unable", "Prompted", "Hesitated", "Independent"],
                         tickvals=[0.1, 1, 2, 3], row=4, col=2)

        fig.update_layout(template="simple_white", title_text=f"{studentname}: Abacus Skills Progression")

        fig.write_html(f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\AbacusSkillsProgression.html")

        # fig.show()
class StudentDataBook(wx.Frame, wx.Accessible):
    def __init__(self, parent, title):
        super(StudentDataBook, self).__init__(parent, title="Data Entry Form", size=(1130, 1000))
        self.InitUI()

    def InitUI(self):
        nb = wx.Notebook(self)
        nb.AddPage(dataPanel(nb), "Data Entry Form")
        nb.AddPage(braillePanel(nb), "Braille Progression")
        nb.AddPage(screenreaderPanel(nb), "ScreenReader Progression")
        nb.AddPage(abacusPanel(nb), "Abacus Progression")
        self.Centre()
        self.Show(True)


app = wx.App()
frame = StudentDataBook(None, 'Student Data Entry')
frame.Centre()
frame.Show()
app.MainLoop()
