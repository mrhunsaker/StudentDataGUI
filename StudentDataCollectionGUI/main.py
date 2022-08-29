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

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
USER_DIR = os.path.join(os.environ['USERPROFILE'], "Documents")
print(USER_DIR)

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
    create_connection("students.db")


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
    conn = create_connection(
            "students.db")
    if conn is not None:
        create_table(conn, sql_create_studentdata_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

students = ['CCooper',
            'LGraham',
            'TLewis',
            'DPenaloza-Diaz',
            'CCostello',
            'MCostello',
            'SBuell',
            'MWalker',
            'TGraham',
            'ABooker',
            'ARito',
            'ANelson',
            'CTalbot',
            'CNelson',
            'LLee',
            'NPalmer',
            'PSackett'
            ]

students_all =['AddisonBooker',
                'AlaijahValdez',
                'AlessaPurcel',
                'AlexRoylance',
                'AmiRito',
                'AmmonOlsen',
                'AshlynnNelson',
                'AustinDenney',
                'AvaWilson',
                'BaraahAlArbid',
                'BelleOsborn',
                'BrightonTingey',
                'BryceClark',
                'CallumDavis',
                'CarstonTalbot',
                'CarterCostello',
                'CasonHemphill',
                'CelestialNelson',
                'CharlieChristensen',
                'ChaseCreer',
                'ChristiGriffin',
                'ColbieBlodgett',
                'ColeCooper',
                'ColeHalbasch',
                'ConnorDenney',
                'CristianPerez',
                'CruAnderson',
                'DaltonCarter',
                'DylanPenaloza-Diaz',
                'EleanorParson',
                'EllaLechtenberg',
                'ElliotWhite',
                'ElyseStephensen',
                'EmmaThompson',
                'EmmaTorres',
                'EvieCompton',
                'FrancisAnwar',
                'FrancisLeyva',
                'GenevieveBriceno',
                'GraceDavis',
                'GrantChristensen',
                'HalleGallacher',
                'HannahHadean',
                'HillaryWheeler',
                'HunterHaskell',
                'HunterTrevino',
                'IsaacChiakis',
                'JacksonJohnson',
                'JacksonWhitear',
                'JainaKarakusis',
                'JakeHeairld',
                'JayceAbles',
                'JaydenSmith',
                'JeffreyLeishman',
                'JonathanChesnovar',
                'JulieMartin',
                'JustinBadham',
                'KahvonFord',
                'KaitlinStott',
                'KatelynChamberlain',
                'KayleeVimahi',
                'KaysonWallwork',
                'KenzieBybee',
                'KinisouElimo',
                'KiraAgamez',
                'KiyrahMiller',
                'LandonGraham',
                'LandonUlrich',
                'LanedanLee',
                'LaurenArnesen',
                'LeonaMizera',
                'LillyVanwagoner',
                'LincolnHoke',
                'LucasKirby',
                'LukeMontgomery',
                'MackenzieMcclean',
                'MadelineCostello',
                'MagnusWilson',
                'MallieMartin',
                'MargaretWalker',
                'MarilynParker',
                'MaryJaneBlack',
                'MayaHegoas',
                'MeelaZendejas',
                'MentorAngela',
                'MichelleCorrea',
                'MilesWebster',
                'MillieBeckstead',
                'NadiaBurns',
                'NoahPalmer',
                'NoraBarton',
                'OliverPage',
                'OliviaEvershed',
                'PaulaSackett',
                'PrestonPage',
                'RachelBallard',
                'RachelScott',
                'RyderReddig',
                'RykerWeight',
                'SamuelWilliam',
                'SaraHill',
                'SavannahWinegar',
                'ShelbySteed',
                'SpencerCostello',
                'SuttonBuell',
                'TalmageTingey',
                'TarelLewis',
                'TaylorTroxel',
                'TheodoreLloyd',
                'TjGutierrez',
                'TyGoddard',
                'TylerAshby',
                'TysonGraham',
                'WestonHemphill',
                'WilliamHayes',
                'WilliamJackson',
                'WilliamMacKay',
                'ZoeyFerguson']

taskType = ['braille',
            'screenreader',
            'abacus',
            'iOS',
            'magnifierSkills',
            'Expanded Core Curriculum']

sessionType = ['ProgressMonitor',
               'Instruction',
               'Assessment']

magnifierSkills = ['Concept of "in focus" and how to bring the image into focus.',
                    'Change the image size and then focus. Provide the students with materials of various print sizes and practice adjusting the image appropriately.',
                    'Spot or locate an image on the page and then focus.',
                    'Follow a line of text, and then track down to locate the next line of text.',
                    'Use various features of the electronic magnifier and when it is adventitious to use those features.',
                    'Become accustomed to writing and drawing while looking at the monitor.',
                    'Care for the video magnifier and demonstrate safe use.',]

iOSSkills = ['Select and speak an item',
             'Select the previous / next item',
             'Move into / out of a group of items',
             'Select the first / last item on the screen',
             'Speak the entire screen from the top',
             'Speak the entire screen from the selected item',
             'Pause or continue speaking',
             'Speak additional information, such as the position within a list or whether text is selected',
             'Drag over the screen',
             'Scroll up /down one page',
             'Scroll left / right  one page',
             'Activate the selected item',
             'Double-tap the selected item',
             'Drag a slider',
             'Dismiss an alert or return to the previous screen',
             'Edit an item label to make it easier to find',
             'Navigate forms',
             'Help with current element',
             'Toggle screen curtain on/off',
             'Split tap quick activation',
             'Double-press button',
             'Speak words/characters typed',
             'Access control center',
             'Backspace',
             'Write letters, numbers, punctation',
             'Change case, punctuation, numbers',
             'Insert space',
             'Choose a rotor setting',
             'Change keyboard mode',
             ]

ECC_CompensatorySkills = [
        'Concept development: developing mental ideas about the environment and the objects, people and processes and interactions taking place in the world.',
        'Spatial understanding:  understanding the physical location of objects in relation to one’s self and to other objects',
        'Communication modes: developing facility with techniques and tools needed to access information presented in print and to write or communicate thoughts',
        'Speaking and listening skills: learning appropriate methods of addressing others in conversation and comprehending what is said.',
        'Study and organization skills: developing methods that allow a student to maintain order in the use of materials and time and to set priorities for such activities as they completion of school work.',
        'Use of adapted and specialized educational materials: independently using tools and devices that provide compensatory access.']

ECC_SensoryEfficiency = [
        'Visual function: fixating, orienting, tracking and recognizing objects and using optical devices',
        'Auditory function: localization, aural discrimination and presentation, and sound pattern use',
        'Tactile function: tactile discrimination, scanning, manipulation and dexterity',
        'Gustatory (taste) function: appreciation for food, discrimination of food types and recognition of various tastes',
        'Olfactory (smell) function: localization of smells, discrimination of odors, and recognition of pleasant and unpleasant odors.']

ECC_AssistiveTechnology = [
        'Access to information: developing facility with general applications and basic technology skills such as inputting information and producing documents',
        ' Communication: developing awareness of electronic communication modes and the ability to conduct research and written assignments.',
        ' Personal productivity: practicing the use of basic applications in activities related to learning and daily living ']

ECC_OrientationMobility = [
        'Body concepts: understanding body parts and function',
        'Environmental concepts:  understanding concepts related to the home environment (such as windows and doors) and to buildings, residential and business areas, schools, and streets and intersections.',
        'Spatial concepts: understanding self-to-object relationships, spatial terminology (such as right, left and next to), landmarks and cues and cardinal directions',
        'Perceptual/sensory skills: interpreting environmental sounds, applying meaning to tasks and determining the nature of sensory information',
        'Mobility skills: noticing and negotiating unexpected drop-offs, using systematic search techniques, and knowing built elements such as block distances, corners, intersection types, streets and road structures.',
        'Orientation skills: knowing routes and understanding layouts',
        'Interpersonal skills: requesting directions, arranging for rides; soliciting information from individuals such as dispatchers, drivers, and store personnel; and using appropriate telephone manners',
        'Decision-making skills: altering travel in response to inclement weather, choosing appropriate clothing and gear, choosing between routes, knowing the advantage and disadvantage of different modes of travel and making back up plans.']

ECC_RecreationLeisure = [
        'Play: interacting through play with peers and siblings, entertaining oneself for various periods of time',
        'Physical activity: participating in physical education or other active play activities, taking part in recreation and leisure activities enjoyed by the family',
        'Health, fitness and individual sports: developing a regimen of physical exercise that leads to improvement or maintenance of strength, stamina and endurance; developing skills for engaging in such activities  as track, wrestling and weight-lifting.',
        'Team and spectator sports: learning  to enjoy competitive and noncompetitive sports activities such as football, baseball, soccer, golf baseball or goalball, as a participant or as a spectator',
        'Leisure activities and hobbies: being exposed to opportunities for choosing a favorite game or book, experiencing arts and crafts activities, appreciating and enjoying fine arts in such forms as museum visits, theater, dance, opera and music.']

ECC_SelfDetermination = [
        'Self-knowledge: developing personal preferences, needs and desires',
        'Awareness of individual right and responsibilities: possessing knowledge of laws protecting people with disabilities',
        'Capacity to make informed choices: knowing what to do in an emergency, being able to express one’s likes and dislikes',
        'Problem-solving and goal-setting skills: making personal and educational goals and interacting with others to obtain assistance',
        'Ability to engage in self-regulated and self-directed behavior: developing negotiation skills and skills involved in interacting with others and the public at large',
        'Self-advocacy and empowerment: choosing favorite or desired activities and being able to evaluate one’s own behavior or progress',
        'Assertiveness skills: being able to advocate for one’s needs and wants.']

ECC_IndependentLivingSkills = [
        'Organization: Maintaining school notes and materials where can be accessed easily, prioritizing daily demands of everyday life and of school and work, and keeping personal objects in a specific location',
        'Personal hygiene and grooming:bathing, maintaining feminine and masculine hygiene and understanding and ensuring privacy',
        'Dressing: participating in dressing oneself with independence, and determining appropriate clothing for the weather',
        'Clothing care: labeling, clothing, selecting appropriate clothing for events, doing laundry and performing related tasks',
        'Time management: establishing a routine of sleeping at appropriate times, recognizing how long it takes to complete a task, using watches and clocks and maintaining a calendar',
        'Eating: eating with utensils,  locating food on a plate, using condiments and using tableware',
        'Cooking: preparing and cooking meals, pouring liquids, retrieving utensils, stirring and mixing, spreading and spooning, helping with dishes, using a stove, cleaning up, learning food-related concepts involved in gardening, visiting grocery stores, applying food nutrition, and opening and closing different kinds of packages.',
        'Cleaning and general household tasks: participating in responsibilities at home and school, retrieving and replacing toys and games, and using cleaning supplies and equipment.',
        'Telephone use: calling friends, knowing how to make emergency calls and having a system of phone number retrieval',
        'Money management: identifying coins and bills, using ATMs, writing checks, and managing money.']

ECC_SocialInteractionSkills = [
        'Appropriate body language: knowing when to lean forward to hear a secret from a friend, maintaining appropriate eye contact, facing a person who is speaking, standing up to greet a new friend, keeping hands to oneself during a group conversation',
        'Social communication: engaging in appropriate verbal and nonverbal interaction with others, initiating conversations, expressing needs and wants',
        'Effective conversation patterns:  asking for help; initiating, maintaining and end ending conversations; extending invitations',
        'Cooperative skills: working  with another to accomplish a goal, volunteering to help in the classroom, helping with home chores',
        'Interactions with others:  knowing how to react to humor, identify the person in charge in a given situation and respond  to the presence of a peer; develop dating skills',
        'Social etiquette: demonstrate courteous behavior, thanking a friend for a gift, sharing a seat with another on the bus, smiling at others.',
        'Development of relationships and friendships: taking turns, seeking friendships with others, working effectively in groups',
        'Knowledge of self: knowing one’s likes and dislikes, taking responsibility for actions, understanding the concept of personal body space, showing pride in accomplished tasks, stating one’s point of view',
        'Interpretation and monitoring of social behavior: knowing when to disobey an adult, understanding the appropriate time to ask questions, developing problem solving skills, recognizing sarcasm in a conversation, understanding the difference between reacting to requests from strangers and familiar people.']

ECC_CareerEducation = [
        'Career awareness: differentiating between work and play, understanding the value of work',
        'Career exploration: developing awareness of careers, researching careers of interest',
        'Career preparation: reading and understanding want ads, recognizing typical job adaptations make by workers with visual impairments, developing prevocationals skills (such as work habits, attitudes, and motivation), and having vocational interests',
        'Career placement: preparing resumes, completing applications, participating in interviews, participating in work',
        'Listen and attend to others', 'Follow directions', 'Stay on task',
        'Complete tasks',
        'Play make believe and dress-up activities to imitate adult roles',
        'Have responsibilities at home and school',
        'Recognize different school & community workers',
        'Participate in problem solving (locating lost items independently, for example)',
        'React appropriately to unexpected changes or events',
        'Learn to work individually and in a group',
        'Learn to be responsible for actions',
        'Recognize that workers get paid', 'Develop good communication skills',
        'Understand the rewards of work',
        'Organize resources such as time and money',
        'Meet increased responsibilities at home, school and the community',
        'Show well-developed academic, thinking and work behavior skills',
        'Participate in work activities and jobs and possibly work part time',
        'Show an understanding  of work performed by adults and what is involved in being successful in multiple areas of work',
        'Show interest in particular areas of work',
        'Plan for life beyond high school']

abacusSkills = ['1.1. Setting Numbers',
                '1.2. Clearing Beads',
                '1.3. Place Value',
                '1.4. Vocabulary',
                '2.1. Addition of Single Digit Numbers',
                '2.2. Addition of Multiple Digit Numbers – Direct',
                '2.3. Addition of Multiple Digit Numbers – Indirect',
                '3.1 Subtraction',
                '3.2. Subtraction of Multiple Digit Numbers – Direct',
                '3.3. Subtraction of Multiple Digit Numbers – Indirect',
                '4.1. Multiplication – 2+ Digit Multiplicand, 1 Digit Multiplier',
                '4.2. Multiplication – 2+ Digit Multiplicand AND Multiplier',
                '5.1. Division – 2+ Digit Dividend, 1 Digit Divisor ',
                '5.2. Division – 2+ Digit Dividend AND 1 Digit Divisor ',
                '6.1. Addition of Decimals',
                '6.2. Subtraction of Decimals',
                '6.3. Multiplication of Decimals',
                '6.4. Division of Decimals',
                '7.1. Addition of Fractions',
                '7.2. Subtraction of Fractions',
                '7.3. Multiplication of Fractions',
                '7.4. Division of Fractions', '8.1. Percent',
                '8.2. Square Root']

screenreaderSkills = ['1.1. Turn on and off the screen reader',
                      '1.2 Utilize modifier keys ',
                      '1.3. Read text ',
                      '1.4. Identify the titles with headings',
                      '1.5. Access documents, open programs, navigate to desktop',
                      '1.6 Switch program focus',
                      '2.1. Type with all keys',
                      '2.2. Change screen reader settings',
                      '2.3. Cursor Placement',
                      '2.4. Select, copy and paste text',
                      '3.1. Define common element types',
                      '3.2. Identify each element by type.',
                      '3.3 Navigate to the address bar',
                      '3.4. Method 1 - Navigate by Clickable Object',
                      '3.5. Method 2 - Quick Keys',
                      '3.6. Method 3 - Elements Lists',
                      '3.7. Justify Why they used a method',
                      '3.8 Switch tab focus',
                      '3.9. Switch between screen reader modes',
                      '3.10. Navigate a table',
                      '3.11. Develop a navigation sequence',
                      '4.1. Save and open files',
                      '4.2. Create and move folders',
                      '4.3. navigate a cloud-based file management system',
                      '4.4. Download material from the internet',
                      '4.5. Extract zipped folders',
                      '4.6. Utilize virtual cursors',
                      '4.7. Use OCR']

brailleSkills = ['1.1. Track left to right',
                 '1.2. Track top to bottom',
                 '1.3. Discriminate shapes',
                 '1.4. Discriminate braille characters',
                 '2.1. G C L',
                 '2.2. D Y',
                 '2.3. A B',
                 '2.4. S',
                 '2.5. W',
                 '2.6. P O',
                 '2.7. K',
                 '2.8. R',
                 '2.9. M E',
                 '2.10. H',
                 '2.11. N X',
                 '2.12. Z F',
                 '2.13. U T',
                 '2.14. Q I',
                 '2.15. V J ',
                 '3.1. Alphabetic Wordsigns',
                 '3.2. Braille Numbers',
                 '3.3. Punctuation',
                 '3.4. Strong Contractions (AND OF FOR WITH THE)',
                 '3.5. Strong Groupsigns (CH GH SH TH WH ED ER OU OW ST AR ING)',
                 '3.6. Strong Wordsigns (CH SH TH WH OU ST)',
                 '3.7. Lower Groupsigns (BE CON DIS)',
                 '3.8. Lower Groupsigns (EA BB CC FF GG)',
                 '3.9. Lower Groupsigns/Wordsigns (EN IN)',
                 '3.10. Lower Wordsigns (BE HIS WAS WERE)',
                 '3.11. Dot 5 Contractions',
                 '3.12. Dot 45 Contractions',
                 '3.13. Dot 456 Contractions',
                 '3.14. Final Letter Groupsigns',
                 '3.15. Shortform Words',
                 '4.1. Grade 1 Indicators',
                 '4.2. Capitals Indicators',
                 '4.3. Numeric Mode and Spatial math',
                 '4.4. Typeform Indicators (ITALIC, SCRIPT, UNDERLINE, BOLDFACE)',
                 '5.1. Page Numbering',
                 '5.2. Headings',
                 '5.3. Lists',
                 '5.4. Poety / Drama',
                 '6.1.  Operation and Comparison Signs',
                 '6.2. Grade 1 Mode',
                 '6.3. Special Print Symbols',
                 '6.4. Omission Marks',
                 '6.5. Shape Indicators',
                 '6.6. Roman Numerals',
                 '6.7. Fractions',
                 '7.1. Grade 1 Mode and Algebra',
                 '7.2. Grade 1 Mode and Fractions',
                 '7.3. Advanced Operation and Comparison Signs',
                 '7.4. Indices',
                 '7.5. Roots and Radicals',
                 '7.6. Miscellaneous Shape Indicators',
                 '7.7. Functions',
                 '7.8. Greek letters',
                 '8.1. Functions',
                 '8.2. Modifiers, Bars, and Dots',
                 '8.3. Modifiers, Arrows, and Limits',
                 '8.4. Probability',
                 '8.5. Calculus: Differentiation',
                 '8.6. Calculus: Integration',
                 '8.7. Vertical Bars']
date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")


class StudentDataBook(wx.Frame):
    def __init__(self, parent, title):
        super(StudentDataBook, self).__init__(parent, title="Data Entry Form",
                                              size=(1500, 1000))
        self.InitUI()

    def InitUI(self):
        nb = wx.Notebook(self)
        nb.AddPage(dataPanel(nb), "Data Entry")
        # nb.AddPage(explorePanel(nb), "Explore Data")
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
        wx.StaticText(self, -1, "Anecodatal Notes", pos=(500, 410))
        self.notes1 = wx.TextCtrl(self, -1, "", pos=(550, 440), size=(300, 375),
                                  style=wx.TE_MULTILINE)
        self.btn = wx.Button(self, 201, "SAVE", pos=(625, 850),
                             size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.btn1 = wx.Button(self, 202, "EXIT", pos=(715, 850),
                              size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.exit, id=202)
        self.Bind(wx.EVT_BUTTON, self.save, id=201)
        self.filename = 'StudentDataBase'
        if not os.path.exists(self.filename):
            os.makedirs('StudentDataBase')

    def exit(self, event):
        wx.Exit()

    def save(self, event):
        studentname = self.studentname1.GetString(
                self.studentname1.GetSelection())
        dateNow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S")
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
                if not os.path.exists(ROOT_DIR + '\\' 'StudentDataBase' + '\\' + self.studentdatabasename + '.txt'):
                    self.filename = open(ROOT_DIR + '\\' 'StudentDataBase' + '\\' + self.studentdatabasename + '.txt', 'w')
                    self.filename.write('studentname' + ',')
                    self.filename.write('date' + ',')
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
                    self.filename = open(ROOT_DIR + '\\' + 'StudentDataBase\\Filenames.txt', 'a')
                    self.filename.write(self.studentdatabasename + '\n')
                    self.filename.close()
                    self.dial = wx.MessageDialog(None, 'Saved successfully!',
                                                 'Info', wx.OK)
                    self.dial.ShowModal()
                else:
                    self.dial = wx.MessageDialog(None,
                                                 'Address-Book name already exists. Enter another name to save!',
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
        if not os.path.exists('StudentDataBase'):
            os.makedirs('StudentDataBase')
        if not os.path.exists( USER_DIR + '\\' + 'StudentDatabase' '\\' 'omnibusDatabase.csv'):
            self.filename = open(USER_DIR + '\\' + 'StudentDatabase' '\\' 'omnibusDatabase.csv', 'w')
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
#################################
app = wx.App()
frame = StudentDataBook(None, 'title')
frame.Centre()
frame.Show()
app.MainLoop()
