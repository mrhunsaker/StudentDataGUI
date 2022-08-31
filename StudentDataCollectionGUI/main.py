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
from helpers import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = os.path.join(os.environ['USERPROFILE'], "Documents")

os.chdir(USER_DIR)

if not os.path.exists('StudentDatabase'):
    os.makedirs('StudentDatabase')

if not os.path.exists(USER_DIR + '\\' + 'StudentDatabase'):
    os.makedirs(USER_DIR + '\\' + 'StudentDatabase')

if not os.path.exists(
        USER_DIR + '\\' + 'StudentDatabase' '\\' 'omnibusDatabase.csv'):
        filename = open(
        USER_DIR + '\\' + 'StudentDatabase' '\\' 'omnibusDatabase.csv', 'w')

if not os.path.exists(
        USER_DIR + '\\' 'StudentDatabase' + '\\' + 'StudentDataFiles'):
    os.makedirs(USER_DIR + '\\' 'StudentDatabase' + '\\' + 'StudentDataFiles')
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
    create_connection(USER_DIR + '\\' + 'StudentDatabase' '\\' 'students.db')


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
    sql_create_studentdata_table = "CREATE TABLE IF NOT EXISTS studentdata (id INTEGER PRIMARY KEY AUTOINCREMENT, studentname TEXT NOT NULL,  date TEXT NOT NULL,  task TEXT NOT NULL, lesson TEXT NOT NULL, session TEXT NOT NULL,  trial01 INTEGER,  trial02 INTEGER,  trial03 INTEGER,  trial04 INTEGER,  trial05 INTEGER,  trial06 INTEGER,  trial07 INTEGER,  trial08 INTEGER,  trial09 INTEGER,  trial10 INTEGER,  trial11 INTEGER,  median FLOAT, notes TEXT NOT NULL );"
    conn = create_connection(USER_DIR + '\\' + 'StudentDatabase' '\\' 'students.db')
    if conn is not None:
        create_table(conn, sql_create_studentdata_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")


class StudentDataBook(wx.Frame,wx.Accessible):
    def __init__(self, parent, title):
        super(StudentDataBook, self).__init__(parent, title="Data Entry Form",
                                              size=(1550, 1000))
        self.InitUI()

    def InitUI(self):
        nb = wx.Notebook(self)
        nb.AddPage(dataPanel(nb), "Data Entry Form")
        nb.AddPage(explorePanel(nb), "Explore Data")
        #nb.AddPage(braillePanel(nb), "Braille Graphs")
        #nb.AddPage(screenreaderPanel(nb), "ScreenReader Graphs")
        #nb.AddPage(abacusPanel(nb), "Abacus Graphs")
        self.Centre()
        self.Show(True)

class dataPanel(wx.Panel):
    def __init__(self, parent):
        super(dataPanel, self).__init__(parent)
        self.ln = wx.StaticLine(self, -1, pos=(465, 0), style=wx.LI_VERTICAL)
        self.ln.SetSize((5, 900))
        self.ln.IsVertical()
        self.ln = wx.StaticLine(self, -1, pos=(950, 0), style=wx.LI_VERTICAL)
        self.ln.SetSize((5, 900))
        self.ln.IsVertical()
        self.SetBackgroundColour(wx.Colour(241,205,234))
        wx.StaticText(self, -1, "Session Information", pos=(170, 20))
        wx.StaticText(self, -1, "Student Name", pos=(30, 50))
        self.studentname1 = wx.Choice(self, -1, choices=students_all, pos=(130, 50),
                                      size=(300, 20))
        wx.StaticText(self, -1, "Date", pos=(30, 80))
        self.date1 = wx.StaticText(self, -1, date, pos=(200, 80))
        wx.StaticText(self, -1, "Session Type", pos=(30, 110))
        self.session1 = wx.Choice(self, -1, choices=sessionType, pos=(130, 110),
                                  size=(300, 20))
        wx.StaticText(self,-1, "Domain and Lesson", pos=(30,140))
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
        self.item6 = self.lesson1.AppendItem(self.root,
                                             'ECC_CompensatorySkills')
        for name in ECC_CompensatorySkills:
            self.lesson1.AppendItem(self.item6, name)
        self.item7 = self.lesson1.AppendItem(self.root,
                                             'ECC_AssistiveTechnology')
        for name in ECC_AssistiveTechnology:
            self.lesson1.AppendItem(self.item7, name)
        self.item8 = self.lesson1.AppendItem(self.root, 'ECC_SensoryEfficiency')
        for name in ECC_SensoryEfficiency:
            self.lesson1.AppendItem(self.item8, name)
        self.item9 = self.lesson1.AppendItem(self.root,
                                             'ECC_OrientationMobility')
        for name in magnifierSkills:
            self.lesson1.AppendItem(self.item9, name)
        self.item10 = self.lesson1.AppendItem(self.root,
                                              'ECC_RecreationLeisure')
        for name in ECC_RecreationLeisure:
            self.lesson1.AppendItem(self.item10, name)
        self.item11 = self.lesson1.AppendItem(self.root,
                                              'ECC_SelfDetermination')
        for name in ECC_SelfDetermination:
            self.lesson1.AppendItem(self.item11, name)
        self.item12 = self.lesson1.AppendItem(self.root,
                                              'ECC_IndependentLivingSkills')
        for name in ECC_IndependentLivingSkills:
            self.lesson1.AppendItem(self.item12, name)
        self.item13 = self.lesson1.AppendItem(self.root,
                                              'ECC_SocialInteractionSkills')
        for name in ECC_SocialInteractionSkills:
            self.lesson1.AppendItem(self.item13, name)
        self.item14 = self.lesson1.AppendItem(self.root, 'ECC_CareerEducation')
        for name in ECC_CareerEducation:
            self.lesson1.AppendItem(self.item14, name)
        wx.StaticText(self, -1, "Performance", pos=(665, 20))
        wx.StaticText(self, -1,
                      "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent",
                      pos=(490, 50))
        self.blank=wx.TextCtrl(self,-1,"",pos=(0,0),size=(0,0))
        wx.StaticText(self, -1, "Trial 1", pos=(500, 80))
        self.trial011 = wx.TextCtrl(self, -1, "", pos=(550, 80),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 2", pos=(500, 110))
        self.trial021 = wx.TextCtrl(self, -1, "", pos=(550, 110),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 3", pos=(500, 140))
        self.trial031 = wx.TextCtrl(self, -1, "", pos=(550, 140),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 4", pos=(500, 170))
        self.trial041 = wx.TextCtrl(self, -1, "", pos=(550, 170),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 5", pos=(500, 200))
        self.trial051 = wx.TextCtrl(self, -1, "", pos=(550, 200),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 6", pos=(500, 230))
        self.trial061 = wx.TextCtrl(self, -1, "", pos=(550, 230),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 7", pos=(500, 260))
        self.trial071 = wx.TextCtrl(self, -1, "", pos=(550, 260),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 8", pos=(500, 290))
        self.trial081 = wx.TextCtrl(self, -1, "", pos=(550, 290),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 9", pos=(500, 320))
        self.trial091 = wx.TextCtrl(self, -1, "", pos=(550, 320),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 10", pos=(500, 350))
        self.trial101 = wx.TextCtrl(self, -1, "", pos=(550, 350),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Trial 11", pos=(500, 380))
        self.trial111 = wx.TextCtrl(self, -1, "", pos=(550, 380),
                                    size=(300, 20))
        wx.StaticText(self, -1, "Anecdotal Notes", pos=(500, 410))
        self.notes1 = wx.TextCtrl(self, -1, "", pos=(550, 440), size=(300, 375),
                                  style=wx.TE_MULTILINE)
        self.btn = wx.Button(self, 201, "SAVE", pos=(625, 850),
                             size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(715, 850),
                              size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.exit, id=202)
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        os.chdir(USER_DIR)
        self.filename = 'StudentDatabase'
        if not os.path.exists(self.filename):
            os.makedirs('StudentDatabase')

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
        trials = [trial01,
                  trial02,
                  trial03,
                  trial04,
                  trial05,
                  trial06,
                  trial07,
                  trial08,
                  trial09,
                  trial10,
                  trial11]
        trialmedian = statistics.median(trials)
        notes = self.notes1.GetValue()
        if (len(studentname) and len(date) and len(task) and len(notes)) > 0:
            box = wx.TextEntryDialog(None, "Enter Address-Book name to save!",
                                     "Title", f"{studentname.title()}{dateNow}")
            if box.ShowModal() == wx.ID_OK:
                self.studentdatabasename = box.GetValue()
                if not os.path.exists(USER_DIR + '\\' 'StudentDataBase' + '\\' + 'StudentDataFiles' + '\\' + self.studentdatabasename + '.txt'):
                    self.filename = open(USER_DIR + '\\' 'StudentDataBase' +'\\' + 'StudentDataFiles' + '\\' + self.studentdatabasename + '.txt', 'w')
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
                    self.filename = open(USER_DIR + '\\' + 'StudentDatabase\\Filenames.txt', 'a')
                    self.filename.write(self.studentdatabasename + '\n')
                    self.filename.close()
                    self.dial = wx.MessageDialog(None, 'Saved successfully!',
                                                 'Info', wx.OK)
                    self.dial.ShowModal()
                else:
                    self.dial = wx.MessageDialog(None,
                                                 'Name already exists',
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
                'students.db')
        c = conn.cursor()

        def data_entry():
            c.execute(
                    "INSERT INTO studentdata (studentname, date, task, lesson, session, trial01, trial02, trial03, trial04, trial05, trial06, trial07, trial08, trial09, trial10, trial11, median, notes) VALUES (?,?,?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?)",
                    (studentname,
                     dateNow,
                     task,
                     lesson,
                     session,
                     trial01,
                     trial02,
                     trial03,
                     trial04,
                     trial05,
                     trial06,
                     trial07,
                     trial08,
                     trial09,
                     trial10,
                     trial11,
                     trialmedian,
                     notes))
            conn.commit()

        data_entry()
        dataView = pd.read_sql(
                f"SELECT date,median,notes FROM studentdata WHERE studentname = '{studentname}' AND lesson = '{lesson}'",
                conn)
        c.close()
        conn.close()

        self.dataWindow = wx.html2.WebView.New(self, pos=(975, 20), size=(500,400))
        df = dataView.to_html()
        html = f"<h3>{studentname}<br /><br />{task.title()}: {lesson.title()}<br /></h3><br /><br />{df} "
        self.dataWindow.SetPage(html,"")


        fig=go.Figure()
        fig.add_trace(go.Scatter(x=dataView.date,y=dataView["median"], mode="lines+markers"))
        fig.write_image('temp.png')

        self.dataPlot = wx.StaticBitmap(self,-1,wx.Bitmap("temp.png", wx.BITMAP_TYPE_ANY),pos=(975, 400),
                                             size=(500,400))
        list_names=['student',
                     'date',
                     'task',
                     'lesson',
                     'session',
                     'trial01',
                     'trial02',
                     'trial03',
                     'trial04',
                     'trial05',
                     'trial06',
                     'trial07',
                     'trial08',
                     'trial09',
                     'trial10',
                     'trial11',
                     'median',
                     'notes']
        list_data=[studentname,
                     dateNow,
                     task,
                     lesson,
                     session,
                     trial01,
                     trial02,
                     trial03,
                     trial04,
                     trial05,
                     trial06,
                     trial07,
                     trial08,
                     trial09,
                     trial10,
                     trial11,
                     trialmedian,
                     notes]
        os.chdir(USER_DIR)
        with open(USER_DIR + '\\' + 'StudentDatabase' '\\' 'omnibusDatabase.csv', 'a',newline='') as f_setup:
            writer_setup=writer(f_setup)
            writer_setup.writerow(list_names)
            f_setup.close()
        with open(USER_DIR + '\\' + 'StudentDatabase' '\\' 'omnibusDatabase.csv', 'a',newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list_data)
            f_object.close()
    def OnChoice(self, event):
        self.label.SetLabel(self.choice.GetString(self.choice.GetSelection()))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class explorePanel(wx.Panel):
    def __init__(self, parent):
        super(explorePanel, self).__init__(parent)
        conn = sqlite3.connect(USER_DIR + '\\' + 'StudentDatabase' '\\' 'students.db')
        c = conn.cursor()
        dataView = pd.read_sql(f"SELECT date,median,notes FROM studentdata", conn)
        c.close()
        conn.close()
        self.dataWindow = wx.html2.WebView.New(self, pos=(975, 20), size=(500, 400))
        df = dataView.to_html()
        self.dataWindow.SetPage(df, "")

#################################
app = wx.App()
frame = StudentDataBook(None, 'title')
frame.Centre()
frame.Show()
app.MainLoop()
