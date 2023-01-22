# coding=utf-8
import datetime
import os
import sqlite3
from csv import writer
from pathlib import Path
from sqlite3 import Error

##############################################################################
# Current Students for Project
##############################################################################
students = [
    'ColeCooper',
    'DylanPenalozaDiaz',
    'GrantChristensen',
    'AustinDenney',
    'KayleeVimahi',
    'CarterCostello',
    'MadelineCostello',
    'SuttonBuell',
    'AddisonBooker',
    'AmiRito',
    'AshlynneNelson',
    'CarstonTalbot',
    'CelestialNeilson',
    'NoahPalmer',
    'PaulaSackett'
    ]
##############################################################################
# All DSD Students
##############################################################################
students_all = [
    'AddisonBooker',
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
    'CelestialNeilson',
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
    'DylanPenalozaDiaz',
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
    'HadleyKelleher',
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
    'Kenzie Bybee',
    'KenzieBybee',
    'KinisouElimo',
    'KiraAgamez',
    'KiyrahMiller',
    'LandonGraham',
    'LandonUlrich',
    'LanedanLee',
    'LaurenArnesen',
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
    'SamuelWilliams',
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
    'ZoeyFerguson'
    ]
##############################################################################
# Session and Task Definitions
##############################################################################
taskType = [
    'braille',
    'screenreader',
    'abacus',
    'iOS',
    'magnifierSkills',
    'Expanded Core Curriculum'
    ]

sessionType = [
    'ProgressMonitor',
    'Instruction',
    'Assessment'
    ]

magnifierSkills = [
    'Concept of "in focus" and how to bring the image into focus.',
    'Change the image size and then focus. Provide the students with materials of various print sizes and practice adjusting the image appropriately.',
    'Spot or locate an image on the page and then focus.',
    'Follow a line of text  and then track down to locate the next line of text.',
    'Use various features of the electronic magnifier and when it is adventitious to use those features.',
    'Become accustomed to writing and drawing while looking at the monitor.',
    'Care for the video magnifier and demonstrate safe use.'
    ]

iOSSkills = [
    'Select and speak an item',
    'Select the previous / next item',
    'Move into / out of a group of items',
    'Select the first / last item on the screen',
    'Speak the entire screen from the top',
    'Speak the entire screen from the selected item',
    'Pause or continue speaking',
    'Speak additional information  such as the position within a list or whether text is selected',
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
    'Write letters  numbers  punctation',
    'Change case  punctuation  numbers',
    'Insert space',
    'Choose a rotor setting',
    'Change keyboard mode'
    ]

ECC_CompensatorySkills = [
    'Concept development: developing mental ideas about the environment and the objects  people and processes and interactions taking place in the world.',
    'Spatial understanding:  understanding the physical location of objects in relation to one’s self and to other objects',
    'Communication modes: developing facility with techniques and tools needed to access information presented in print and to write or communicate thoughts',
    'Speaking and listening skills: learning appropriate methods of addressing others in conversation and comprehending what is said.',
    'Study and organization skills: developing methods that allow a student to maintain order in the use of materials and time and to set priorities for such activities as they completion of school work.',
    'Use of adapted and specialized educational materials: independently using tools and devices that provide compensatory access.'
    ]

ECC_SensoryEfficiency = [
    'Visual function: fixating  orienting  tracking and recognizing objects and using optical devices',
    'Auditory function: localization  aural discrimination and presentation  and sound pattern use',
    'Tactile function: tactile discrimination  scanning  manipulation and dexterity',
    'Gustatory (taste) function: appreciation for food  discrimination of food types and recognition of various tastes',
    'Olfactory (smell) function: localization of smellsdiscrimination of odors and recognition of pleasant and unpleasant odors.'
    ]

ECC_AssistiveTechnology = [
    'Access to information: developing facility with general applications and basic technology skills such as inputting information and producing documents',
    'Communication: developing awareness of electronic communication modes and the ability to conduct research and written assignments.',
    'Personal productivity: practicing the use of basic applications in activities related to learning and daily living'
    ]

ECC_OrientationMobility = [
    'Body concepts: understanding body parts and function',
    'Environmental concepts:  understanding concepts related to the home environment (such as windows and doors) and to buildings  residential and business areas  schools  and streets and intersections.',
    'Spatial concepts: understanding self-to-object relationships  spatial terminology (such as right  left and next to)  landmarks and cues and cardinal directions',
    'Perceptual/sensory skills: interpreting environmental sounds  applying meaning to tasks and determining the nature of sensory information',
    'Mobility skills: noticing and negotiating unexpected drop-offs  using systematic search techniques  and knowing built elements such as block distances  corners  intersection types',
    'streets and road structures.',
    'Orientation skills: knowing routes and understanding layouts',
    'Interpersonal skills: requesting directions  arranging for rides; soliciting information from individuals such as dispatchers  drivers  and store personnel; and using appropriate telephone manners',
    'Decision-making skills: altering travel in response to inclement weather choosing appropriate clothing and gear choosing between routes knowing the advantage and disadvantage of different modes of travel and '
    'making back up plans.'
    ]

ECC_RecreationLeisure = [
    'Play: interacting through play with peers and siblings  entertaining oneself for various periods of time',
    'Physical activity: participating in physical education or other active play activities  taking part in recreation and leisure activities enjoyed by the family',
    'Health  fitness and individual sports: developing a regimen of physical exercise that leads to improvement or maintenance of strength  stamina and endurance; developing skills for engaging in such activities',
    ' as track  wrestling and weight-lifting.',
    'Team and spectator sports: learning  to enjoy competitive and noncompetitive sports activities such as football  baseball  soccer  golf baseball or goalball  as a participant or as a spectator',
    'Leisure activities and hobbies: being exposed to opportunities for choosing a favorite game or book experiencing arts and crafts activities appreciating and enjoying fine arts in such forms as museum visits '
    'theater dance opera and music.'
    ]

ECC_SelfDetermination = [
    'Self-knowledge: developing personal preferences  needs and desires',
    'Awareness of individual right and responsibilities: possessing knowledge of laws protecting people with disabilities',
    'Capacity to make informed choices: knowing what to do in an emergency  being able to express one’s likes and dislikes',
    'Problem-solving and goal-setting skills: making personal and educational goals and interacting with others to obtain assistance',
    'Ability to engage in self-regulated and self-directed behavior: developing negotiation skills and skills involved in interacting with others and the public at large',
    'Self-advocacy and empowerment: choosing favorite or desired activities and being able to evaluate one’s own behavior or progress',
    'Assertiveness skills: being able to advocate for one’s needs and wants.'
    ]

ECC_IndependentLivingSkills = [
    'Organization: Maintaining school notes and materials where can be accessed easily  prioritizing daily demands of everyday life and of school and work  and keeping personal objects in a specific location',
    'Personal hygiene and grooming:bathing  maintaining feminine and masculine hygiene and understanding and ensuring privacy',
    'Dressing: participating in dressing oneself with independence  and determining appropriate clothing for the weather',
    'Clothing care: labeling  clothing  selecting appropriate clothing for events  doing laundry and performing related tasks',
    'Time management: establishing a routine of sleeping at appropriate times  recognizing how long it takes to complete a task  using watches and clocks and maintaining a calendar',
    'Eating: eating with utensils   locating food on a plate  using condiments and using tableware',
    'Cooking: preparing and cooking meals pouring liquids retrieving utensils  stirring and mixing  spreading and spooning  helping with dishes  using a stove  cleaning up  learning food-related concepts',
    'involved in gardening  visiting grocery stores  applying food nutrition  and opening and closing different kinds of packages.',
    'Cleaning and general household tasks: participating in responsibilities at home and school  retrieving and replacing toys and games  and using cleaning supplies and equipment.',
    'Telephone use: calling friends  knowing how to make emergency calls and having a system of phone number retrieval',
    'Money management: identifying coins and bills using ATMs writing checks and managing money.'
    ]

ECC_SocialInteractionSkills = [
    'Appropriate body language: knowing when to lean forward to hear a secret from a friend  maintaining appropriate eye contact  facing a person who is speaking  standing up to greet a new friend',
    'keeping hands to oneself during a group conversation',
    'Social communication: engaging in appropriate verbal and nonverbal interaction with others  initiating conversations  expressing needs and wants',
    'Effective conversation patterns:  asking for help; initiating  maintaining and end ending conversations; extending invitations',
    'Cooperative skills: working  with another to accomplish a goal  volunteering to help in the classroom  helping with home chores',
    'Interactions with others:  knowing how to react to humor  identify the person in charge in a given situation and respond  to the presence of a peer; develop dating skills',
    'Social etiquette: demonstrate courteous behavior  thanking a friend for a gift  sharing a seat with another on the bus  smiling at others.',
    'Development of relationships and friendships: taking turns  seeking friendships with others  working effectively in groups',
    'Knowledge of self: knowing one’s likes and dislikes  taking responsibility for actions  understanding the concept of personal body space  showing pride in accomplished tasks  stating one’s point of view',
    'Interpretation and monitoring of social behavior: knowing when to disobey an adult understanding the appropriate time to ask questions developing problem solving skills, recognizing sarcasm in a '
    'conversation, understanding the difference between reacting to requests from strangers and familiar people.'
    ]

ECC_CareerEducation = [
    'Career awareness: differentiating between work and play  understanding the value of work',
    'Career exploration: developing awareness of careers  researching careers of interest',
    'Career preparation: reading and understanding want ads  recognizing typical job adaptations make by workers with visual impairments  developing prevocationals skills (such as work habits  attitudes  and '
    'motivation)  and having vocational interests',
    'Career placement: preparing resumes  completing applications  participating in interviews  participating in work',
    'Listen and attend to others',
    'Follow directions',
    'Stay on task',
    'Complete tasks',
    'Play make believe and dress-up activities to imitate adult roles',
    'Have responsibilities at home and school',
    'Recognize different school & community workers',
    'Participate in problem solving (locating lost items independently  for example)',
    'React appropriately to unexpected changes or events',
    'Learn to work individually and in a group',
    'Learn to be responsible for actions',
    'Recognize that workers get paid',
    'Develop good communication skills',
    'Understand the rewards of work',
    'Organize resources such as time and money',
    'Meet increased responsibilities at home  school and the community',
    'Show well-developed academic  thinking and work behavior skills',
    'Participate in work activities and jobs and possibly work part time',
    'Show an understanding  of work performed by adults and what is involved in being successful in multiple areas of work',
    'Show interest in particular areas of work',
    'Plan for life beyond high school'
    ]

abacusSkills = [
    '1.1. Setting Numbers',
    '1.2. Clearing Beads',
    '1.3. Place Value',
    '1.4. Vocabulary',
    '2.1. Addition of Single Digit Numbers',
    '2.2. Addition of Multiple Digit Numbers – Direct',
    '2.3. Addition of Multiple Digit Numbers – Indirect',
    '3.1. Subtraction',
    '3.2. Subtraction of Multiple Digit Numbers – Direct',
    '3.3. Subtraction of Multiple Digit Numbers – Indirect',
    '4.1. Multiplication – 2+ Digit Multiplicand  1 Digit Multiplier',
    '4.2. Multiplication – 2+ Digit Multiplicand AND Multiplier',
    '5.1. Division – 2+ Digit Dividend  1 Digit Divisor ',
    '5.2. Division – 2+ Digit Dividend AND 1 Digit Divisor ',
    '6.1. Addition of Decimals',
    '6.2. Subtraction of Decimals',
    '6.3. Multiplication of Decimals',
    '6.4. Division of Decimals',
    '7.1. Addition of Fractions',
    '7.2. Subtraction of Fractions',
    '7.3. Multiplication of Fractions',
    '7.4. Division of Fractions',
    '8.1. Percent',
    '8.2. Square Root'
    ]

screenreaderSkills = [
    '1.1. Turn on and off the screen reader',
    '1.2 Utilize modifier keys ',
    '1.3. Read text ',
    '1.4. Identify the titles with headings',
    '1.5. Access documents  open programs  navigate to desktop',
    '1.6. Switch program focus',
    '2.1. Type with all keys',
    '2.2. Change screen reader settings',
    '2.3. Cursor Placement',
    '2.4. Select  copy and paste text',
    '3.1. Define common element types',
    '3.2. Identify each element by type.',
    '3.3. Navigate to the address bar',
    '3.4. Method 1 - Navigate by Clickable Object',
    '3.5. Method 2 - Quick Keys',
    '3.6. Method 3 - Elements Lists',
    '3.7. Justify Why they used a method',
    '3.8. Switch tab focus',
    '3.9. Switch between screen reader modes',
    '3.10. Navigate a table',
    '3.11. Develop a navigation sequence',
    '4.1. Save and open files',
    '4.2. Create and move folders',
    '4.3. navigate a cloud-based file management system',
    '4.4. Download material from the internet',
    '4.5. Extract zipped folders',
    '4.6. Utilize virtual cursors',
    '4.7. Use OCR'
    ]

brailleSkills = [
    '1.1. Track left to right',
    '1.2. Track top to bottom',
    '1.3. Discriminate shapes',
    '1.4. Discriminate braille characters',
    '2.1. Mangold Progression: G C L',
    '2.2. Mangold Progression: D Y',
    '2.3. Mangold Progression: A B',
    '2.4. Mangold Progression: S',
    '2.5. Mangold Progression: W',
    '2.6. Mangold Progression: P O',
    '2.7. Mangold Progression: K',
    '2.8. Mangold Progression: R',
    '2.9. Mangold Progression: M E',
    '2.10. Mangold Progression: H',
    '2.11. Mangold Progression: N X',
    '2.12. Mangold Progression: Z F',
    '2.13. Mangold Progression: U T',
    '2.14. Mangold Progression: Q I',
    '2.15. Mangold Progression: V J ',
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
    '4.4. Typeform Indicators (ITALIC  SCRIPT  UNDERLINE  BOLDFACE)',
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
    '8.2. Modifiers  Bars  and Dots',
    '8.3. Modifiers  Arrows  and Limits',
    '8.4. Probability',
    '8.5. Calculus: Differentiation',
    '8.6. Calculus: Integration',
    '8.7. Vertical Bars'
    ]

cviDomains = [
    'colorPreference',
    'needForMovement',
    'visualLatency',
    'visualFieldPreference',
    'visualComplexity',
    'nonpurposefulGaze',
    'distanceViewing',
    'visualReflexes',
    'visualNovelty',
    'visuallyGuidedReach'
    ]

##############################################################################
# End Variables
##############################################################################

##############################################################################
# Define Paths
##############################################################################
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = ""

##############################################################################
# Set User Directory based on OS
##############################################################################

if os.name == 'nt':
    tmpPath = Path(os.environ['USERPROFILE']).joinpath('Documents')
    Path.mkdir(tmpPath, parents = True, exist_ok = True)
    USER_DIR = Path(tmpPath)
elif os.name == 'posix':
    tmpPath = Path(os.environ['HOME']).joinpath('Documents')
    Path.mkdir(tmpPath, parents = True, exist_ok = True)
    USER_DIR = Path(tmpPath)
else:
    print("Error! Cannot find HOME directory")

os.chdir(USER_DIR)

##############################################################################
# Set User Folders in ~/Documents for each Student
##############################################################################

for name in students:
    if not Path(USER_DIR).joinpath('StudentDatabase').exists():
        tmpPath = Path(USER_DIR).joinpath('StudentDatabase')
        Path.mkdir(
            tmpPath,
            parents = True,
            exist_ok = True
            )
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath('StudentDatabase/StudentDataFiles')
        Path.mkdir(
            tmpPath,
            parents = True,
            exist_ok = True
            )
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase/StudentDataFiles',
            name
            )
        Path.mkdir(tmpPath, parents = True, exist_ok = True)
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'omnibusDatabase.csv'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase/StudentDataFiles',
            name,
            'omnibusDatabase.csv'
            )
        Path.touch(tmpPath)
        list_names = [
            'student',
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
            'notes'
            ]
        with open(tmpPath, 'a', newline = '') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'BrailleSkillsProgression.csv'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'BrailleSkillsProgression.csv'
            )
        Path.touch(tmpPath)
        list_names = [
            'date',
            'P1_1',
            'P1_2',
            'P1_3',
            'P1_4',
            'P2_1',
            'P2_2',
            'P2_3',
            'P2_4',
            'P2_5',
            'P2_6',
            'P2_7',
            'P2_8',
            'P2_9',
            'P2_10',
            'P2_11',
            'P2_12',
            'P2_13',
            'P2_14',
            'P2_15',
            'P3_1',
            'P3_2',
            'P3_3',
            'P3_4',
            'P3_5',
            'P3_6',
            'P3_7',
            'P3_8',
            'P3_9',
            'P3_10',
            'P3_11',
            'P3_12',
            'P3_13',
            'P3_14',
            'P3_15',
            'P4_1',
            'P4_2',
            'P4_3',
            'P4_4',
            'P5_1',
            'P5_2',
            'P5_3',
            'P5_4',
            'P6_1',
            'P6_2',
            'P6_3',
            'P6_4',
            'P6_5',
            'P6_6',
            'P6_7',
            'P7_1',
            'P7_2',
            'P7_3',
            'P7_4',
            'P7_5',
            'P7_6',
            'P7_7',
            'P7_8',
            'P8_1',
            'P8_2',
            'P8_3',
            'P8_4',
            'P8_5',
            'P8_6',
            'P8_7'
            ]
        with open(tmpPath, 'a', newline = '') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'UEBLiterarySkillsProgression.html'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'UEBLiterarySkillsProgression.html'
            )
        Path.touch(tmpPath)
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'UEBTechnicalSkillsProgression.html'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'UEBTechnicalSkillsProgression.html'
            )
        Path.touch(tmpPath)
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'ScreenReaderSkillsProgression.csv'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'ScreenReaderSkillsProgression.csv'
            )
        Path.touch(tmpPath)
        list_names = [
            'date',
            'P1_1',
            'P1_2',
            'P1_3',
            'P1_4',
            'P1_5',
            'P1_6',
            'P2_1',
            'P2_2',
            'P2_3',
            'P2_4',
            'P3_1',
            'P3_2',
            'P3_3',
            'P3_4',
            'P3_5',
            'P3_6',
            'P3_7',
            'P3_8',
            'P3_9',
            'P3_10',
            'P3_11',
            'P4_1',
            'P4_2',
            'P4_3',
            'P4_4',
            'P4_5',
            'P4_6',
            'P4_7'
            ]
        with open(tmpPath, 'a', newline = '') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'ScreenReaderSkillsProgression.html'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'ScreenReaderSkillsProgression.html'
            )
        Path.touch(tmpPath)
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'AbacusSkillsProgression.csv'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'AbacusSkillsProgression.csv'
            )
        Path.touch(tmpPath)
        list_names = [
            'date',
            'P1_1',
            'P1_2',
            'P1_3',
            'P1_4',
            'P2_1',
            'P2_2',
            'P2_3',
            'P3_1',
            'P3_2',
            'P3_3',
            'P4_1',
            'P4_2',
            'P5_1',
            'P5_2',
            'P6_1',
            'P6_2',
            'P6_3',
            'P6_4',
            'P7_1',
            'P7_2',
            'P7_3',
            'P7_4',
            'P8_1',
            'P8_2'
            ]
        with open(tmpPath, 'a', newline = '') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'AbacusSkillsProgression.html'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'AbacusSkillsProgression.html'
            )
        Path.touch(tmpPath)
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'cviProgression.csv'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'cviProgression.csv'
            )
        Path.touch(tmpPath)
        list_names = [
            'date',
            'P1_1',
            'P1_2',
            'P1_3',
            'P1_4',
            'P1_5',
            'P1_6',
            'P2_1',
            'P2_2',
            'P2_3',
            'P2_4'
            ]
        with open(tmpPath, 'a', newline = '') as f_object:
            writer_setup = writer(f_object)
            writer_setup.writerow(list_names)
            f_object.close()
    if not Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'cviProgression.html'
            ).exists():
        tmpPath = Path(USER_DIR).joinpath(
            'StudentDatabase',
            'StudentDataFiles',
            name,
            'cviProgression.html'
            )
        Path.touch(tmpPath)


##############################################################################
# Create SQL database with SQLite and create data tables
##############################################################################

def create_connection(db_file):
    """

    :param db_file:
    :type db_file:
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


dataBasePath = Path(USER_DIR).joinpath('StudentDatabase/students.db')
if __name__ == '__main__':
    create_connection(dataBasePath)


def create_connection(db_file):
    """

    :param db_file:
    :type db_file:
    :return:
    :rtype:
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql_create_sql_table):
    """

    :param conn:
    :type conn:
    :param sql_create_sql_table:
    :type sql_create_sql_table:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_sql_table)
    except Error as e:
        print(e)
    conn.close()


def main():
    """

    """
    sql_create_studentdata_table = """CREATE TABLE IF NOT EXISTS studentdata (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        studentname TEXT NOT NULL, 
        date TEXT NOT NULL, 
        task TEXT NOT NULL, 
        lesson TEXT NOT NULL, 
        session TEXT NOT NULL, 
        trial01 INTEGER, 
        trial02 INTEGER, 
        trial03 INTEGER, 
        trial04 INTEGER, 
        trial05 INTEGER, 
        trial06 INTEGER, 
        trial07 INTEGER, 
        trial08 INTEGER, 
        trial09 INTEGER, 
        trial10 INTEGER, 
        trial11 INTEGER, 
        median FLOAT, 
        notes TEXT NOT NULL 
    );"""

    sql_create_brailledata_table = """CREATE TABLE IF NOT EXISTS brailleProgress (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        studentname TEXT NOT NULL, 
        date TEXT NOT NULL, 
        P1_1 INTEGER, 
        P1_2 INTEGER, 
        P1_3 INTEGER, 
        P1_4 INTEGER, 
        P2_1 INTEGER, 
        P2_2 INTEGER, 
        P2_3 INTEGER, 
        P2_4 INTEGER, 
        P2_5 INTEGER, 
        P2_6 INTEGER, 
        P2_7 INTEGER, 
        P2_8 INTEGER, 
        P2_9 INTEGER, 
        P2_10 INTEGER, 
        P2_11 INTEGER, 
        P2_12 INTEGER, 
        P2_13 INTEGER, 
        P2_14 INTEGER, 
        P2_15 INTEGER, 
        P3_1 INTEGER, 
        P3_2 INTEGER, 
        P3_3 INTEGER, 
        P3_4 INTEGER, 
        P3_5 INTEGER, 
        P3_6 INTEGER, 
        P3_7 INTEGER, 
        P3_8 INTEGER, 
        P3_9 INTEGER, 
        P3_10 INTEGER, 
        P3_11 INTEGER, 
        P3_12 INTEGER, 
        P3_13 INTEGER, 
        P3_14 INTEGER, 
        P3_15 INTEGER, 
        P4_1 INTEGER, 
        P4_2 INTEGER, 
        P4_3 INTEGER, 
        P4_4 INTEGER, 
        P5_1 INTEGER, 
        P5_2 INTEGER, 
        P5_3 INTEGER, 
        P5_4 INTEGER, 
        P6_1 INTEGER, 
        P6_2 INTEGER, 
        P6_3 INTEGER, 
        P6_4 INTEGER, 
        P6_5 INTEGER, 
        P6_6 INTEGER, 
        P6_7 INTEGER, 
        P7_1 INTEGER, 
        P7_2 INTEGER, 
        P7_3 INTEGER, 
        P7_4 INTEGER, 
        P7_5 INTEGER, 
        P7_6 INTEGER, 
        P7_7 INTEGER, 
        P7_8 INTEGER, 
        P8_1 INTEGER, 
        P8_2 INTEGER, 
        P8_3 INTEGER, 
        P8_4 INTEGER,
        P8_5 INTEGER, 
        P8_6 INTEGER, 
        P8_7 INTEGER
    );"""

    sql_create_screenreaderdata_table = """CREATE TABLE IF NOT EXISTS screenreaderProgress (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        studentname TEXT NOT NULL, 
        date TEXT NOT NULL, 
        P1_1 INTEGER, 
        P1_2 INTEGER, 
        P1_3 INTEGER, 
        P1_4 INTEGER, 
        P1_5 INTEGER, 
        P1_6 INTEGER, 
        P2_1 INTEGER, 
        P2_2 INTEGER, 
        P2_3 INTEGER, 
        P2_4 INTEGER, 
        P3_1 INTEGER, 
        P3_2 INTEGER, 
        P3_3 INTEGER, 
        P3_4 INTEGER, 
        P3_5 INTEGER,
        P3_6 INTEGER, 
        P3_7 INTEGER, 
        P3_8 INTEGER, 
        P3_9 INTEGER, 
        P3_10 INTEGER, 
        P3_11 INTEGER, 
        P4_1 INTEGER, 
        P4_2 INTEGER, 
        P4_3 INTEGER, 
        P4_4 INTEGER, 
        P4_5 INTEGER, 
        P4_6 INTEGER, 
        P4_7 INTEGER
    );"""

    sql_create_abacusdata_table = """CREATE TABLE IF NOT EXISTS abacusProgress (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        studentname TEXT NOT NULL, 
        date TEXT NOT NULL, 
        P1_1 INTEGER, 
        P1_2 INTEGER, 
        P1_3 INTEGER, 
        P1_4 INTEGER, 
        P2_1 INTEGER, 
        P2_2 INTEGER, 
        P2_3 INTEGER, 
        P3_1 INTEGER, 
        P3_2 INTEGER, 
        P3_3 INTEGER, 
        P4_1 INTEGER, 
        P4_2 INTEGER, 
        P5_1 INTEGER, 
        P5_2 INTEGER, 
        P6_1 INTEGER, 
        P6_2 INTEGER, 
        P6_3 INTEGER, 
        P6_4 INTEGER, 
        P7_1 INTEGER, 
        P7_2 INTEGER, 
        P7_3 INTEGER, 
        P7_4 INTEGER, 
        P8_1 INTEGER, 
        P8_2 INTEGER 
    );"""

    sql_create_cvidata_table = """CREATE TABLE IF NOT EXISTS cviProgress (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        studentname TEXT NOT NULL, 
        date TEXT NOT NULL, 
        P1_1 INTEGER, 
        P1_2 INTEGER, 
        P1_3 INTEGER, 
        P1_4 INTEGER, 
        P1_5 INTEGER, 
        P1_6 INTEGER, 
        P2_1 INTEGER, 
        P2_2 INTEGER, 
        P2_3 INTEGER, 
        P2_4 INTEGER 
    );"""

    conn = create_connection(dataBasePath)
    if conn is not None:
        create_table(conn, sql_create_studentdata_table)
    else:
        print("Error! cannot create the database connection.")
    conn = create_connection(dataBasePath)

    if conn is not None:
        create_table(conn, sql_create_brailledata_table)
    else:
        print("Error! cannot create the database connection.")
    conn = create_connection(dataBasePath)

    if conn is not None:
        create_table(conn, sql_create_screenreaderdata_table)
    else:
        print("Error! cannot create the database connection.")
    conn = create_connection(dataBasePath)

    if conn is not None:
        create_table(conn, sql_create_abacusdata_table)
    else:
        print("Error! cannot create the database connection.")
    conn = create_connection(dataBasePath)

    if conn is not None:
        create_table(conn, sql_create_cvidata_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")
