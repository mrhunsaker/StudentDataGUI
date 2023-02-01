# coding=utf-8
#################################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                         #
#                                                                               #
#    Licensed under the Apache License, Version 2.0 (the "License");            #
#    you may not use this file except in compliance with the License.           #
#    You may obtain a copy of the License at                                    #
#                                                                               #
#        http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                               #
#    Unless required by applicable law or agreed to in writing, software        #
#    distributed under the License is distributed on an "AS IS" BASIS,          #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#    See the License for the specific language governing permissions and        #
#    limitations under the License.                                             #
#################################################################################

import datetime

date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")

##############################################################################
# Current Students for Project
##############################################################################
students = [
        'DonaldChamberlain',
        'AustinDenney',
        'AddisonBooker',
        'AmiRito',
        'AshlynneNelson',
        'CarstonTalbot',
        'CarterCostello',
        'CelestialNeilson',
        'ColeCooper',
        'DylanPenalozaDiaz',
        'GrantChristensen',
        'KayleeVimahi',
        'MadelineCostello',
        'NoahPalmer',
        'PaulaSackett',
        'SuttonBuell'
        ]
##############################################################################
# Current Student IEPs
##############################################################################
addisonbbookeriep = """Addison Booker  	20 min / quarter
    • When Addi is read a short story from a book with pictures, she will use eye gaze or touch to identify people or objects from the story or answer yes/no comprehension questions with 60% accuracy 2x
    weekly, across 3/5 data sessions.
        ◦ When Addi is read a short story from a book with pictures, she will use eye gaze or touch to identify people or objects from the story or answer yes/no comprehension questions with 20% accuracy
        2x weekly, across 3/5 data sessions.
        ◦ When Addi is read a short story from a book with pictures, she will use eye gaze or touch to identify people or objects from the story or answer yes/no comprehension questions with 40% accuracy
        2x weekly, across 3/5 data sessions.
    """
amiritoiep = """Ami Rito    20 min / month
    • When presented with a 3D household or classroom item, Ami will find its match using eye gaze or touch selection, matching a total of 3 items, on 4/5 daily trials, over 3 consecutive weeks.
        ◦ When presented with a 3D household or classroom item, Ami will find its match using eye gaze or touch selection, matching a total of 1 item, on 4/5 daily trials, over 3 consecutive weeks.
        ◦ When presented with a 3D household or classroom item, Ami will find its match using eye gaze or touch selection, matching a total of 2 items, on 4/5 daily trials, over 3 consecutive weeks.
    """
ashlynnenelsoniep = """Ashlynn Nelson  	20 min / month
    • When given partial physical support, Ashylnn will be shown a selected musical instrument (xylophone, bells, drum, tambourine), and be shown a video (4-6ft away) of someone playing the selected
    musical instrument, then will focus her attention on the video for 3 seconds or more on 4/5 twice weekly trials, over 3 consecutive weeks.
        ◦ When given partial physical support, Ashylnn will be shown a selected musical instrument (xylophone, bells, drum, tambourine), and be shown a video (4-6ft away) of someone playing the selected
        musical instrument, then will focus her attention on the video for 1 second on 4/5 twice weekly trials, over 3 consecutive weeks.
        ◦ When given partial physical support, Ashylnn will be shown a selected musical instrument (xylophone, bells, drum, tambourine), and be shown a video (4-6ft away) of someone playing the selected
        musical instrument, then will focus her attention on the video for 2 second or more on 4/5 twice weekly trials, over 3 consecutive weeks.
    """
austindenneyiep = """Austin Denney  60 min/month
    •  Within one year Austin will independently utilize 10 keyboard shortcuts 8/10 times at 80% accuracy over 4 data sessions as observed by the teacher of students with visual impairments.
    • Within one year Austin will independently type 30wpm 4/5 times at 80% accuracy over 4 data sessions as observed by the teacher of students with visual impairments.
        """
cartercostelloiep = """Carter Costello	    	120 min / month
    • Carter will identify the braille letters of his name with 80% accuracy in 4/5 trials as measured by classroom data. (EE.RF.1.3)
        ◦ Carter will identify 2/6 braille letters of his name with 80% accuracy in 4/5 trials as measured by classroom data.
        ◦ Carter will identify 4/6 braille letters of his name with 80% accuracy in 4/5 trails as measured by classroom data.
    • Carter will independently indicate the number that results when adding one more using manipulatives and/or the abacus with 80% accuracy in 4/5 trials as measured by classroom data. (EE.1.OA.5.a)
        ◦ With assistance from staff, Carter will indicate the number that results when adding one more using manipulatives or the abacus with 80% accuracy in 4/5 trials as measured by classroom data
        ◦ Carter will independently identify the different parts of the abacus: the one beads, five beads and the reckoning bar with 80% accuracy unprompted in 4/5 trials as measured by classroom data.
    • Carter will braille his name independently with 80% accuracy and no more than one prompt per probe on 5 probes as measured by classroom data. (EE.W.1.6)
        ◦ Carter will independently learn to braille the letters in his name with 60% accuracy with less than 3 physical prompts as measured by classroom data.
        ◦ Carter will use a braille writer to braille his name with limited physical assistance with 60% accuracy and no more than one prompt per probe on 5 probes as measured by classroom data.
    """
carstontalbotiep = """Carston Talbot  	30 min / month
    • When given a choice between two pictures, Carston will visually locate and chose the picture that represents the object/activity he would like with 4 out of 5 trials over 3 consecutive data sessions
    as evidenced by vision and classroom data.
        ◦ Carston will visually locate and chose the picture that represents the activity he would like with 4 out of 5 trials over 3 consecutive data sessions as evidenced by vision and classroom data.
        ◦ Carston will visually locate and chose a picture that represents a preferred object that he would like with 4 out of 5 trials over 3 consecutive data sessions as evidenced by vision and
        classroom data.
    """
celestialneilsoniep = """Celestial  Nelson   	30 min / month
    • Given the opportunity, in a variety of school-based locations, CD will, with minimal prompting, using her vision, make choices about academic and preferred activities within a class period in
    addition to 2 topics of conversation per location with a variety of people 70% of opportunities across 3 consecutive data session, as measured by classroom data and observation.
        ◦ Given the opportunity, in a variety of school-based locations, CD will, with maximum prompting, using her vision, make choices about academic and preferred activities within a class period in
        addition to 1 topic of conversation per location with a variety of people 70% of opportunities across 3 consecutive data session, as measured by classroom data and observation.
        ◦ Given the opportunity, in a variety of school-based locations, CD will, with maximum prompting, using her vision, make choices about academic and preferred activities within a class period in
        addition to 2 topics of conversation per location with a variety of people 70% of opportunities across 3 consecutive data session, as measured by classroom data and observation.
    """
colecooperiep = """Cole  Cooper    30 min/month
    • When presented with 2 objects, Cole will be able to utilize his central vision to locate an object with 70% accuracy as measured by the TVI and classroom teacher over 3 consecutive data sessions.
        ◦ When presented with 2 objects, Cole will be able to utilize his central vision to locate an object with 50% accuracy as measured by the TVI and classroom teacher over 3 consecutive data sessions.
        ◦ When presented with 2 objects, Cole will be able to utilize his central vision to locate an object with 60% accuracy as measured by the TVI and classroom teacher over 3 consecutive data sessions.
    """
diegopenalozadiaziep = """Dylan Penaloza-Diaz	    	40 min / month
    • Dylan will independently complete eye-hand coordination matching activities and/or locating a specific letter, word, or icon on a communication board with 70% accuracy on by completing 4/5 requests
    across 3 data sessions.
        ◦ Dylan will independently complete eye-hand coordination matching activities and/or locating a specific letter, word, or icon on a communication board with 30% accuracy on by completing 4/5
        requests across 3 data sessions.
        ◦ Dylan will independently complete eye-hand coordination matching activities and/or locating a specific letter, word, or icon on a communication board with 50% accuracy on by completing 4/5
        requests across 3 data sessions.
    """
grantchristenseniep = """Grant Christensen	    	800 min/month
    • Grant, through monthly assessments, will read braille at grade level text with a consistent speed of 65 cwpm with 95% accuracy or better with 100% comprehension in 4/5 trials as measured by his TVI.
    • Grant, through monthly assessments, will produce complete sentences and passages using UEB contractions and proper braille writing techniques with 3 errors or less per writing assignment in 4 of 5
    trials as measured by his TVI.
    • Grant, through monthly assessments, will demonstrate proficiency in technology for the visually impaired with at least 95% accuracy on required tasks indicated on a checklist of skills from a
    Teacher's rubric in 3 of 4 evaluated sessions.
    """
kayleevimahiiep = """Kaylee Vimahi	    	60 min/month
    • When given access to an accessible reading library, Kaylee will independently download 3 audio/eBooks and increase her reading speed and stamina from 143wpm and 10 minutes, to 200wpm and 30 minutes
    in 3 of 4 probes and measured by TVI created data sheets.
    """
madelinecostelloiep = """Madeline Costello	    	120 min / month
    • Maddie will, with guidance and support, use a QWERTY keyboard with screenreader, to type her name with 80% accuracy in 4/5 trials as measured by classroom data.
    • Maddie will explore, locate and identify a tactile object or tactile drawing, based on being read to or listening to instructions, during one on one instruction or small group instruction in 4/5 
    tries with decreasing amount of physical assistance, for 3 consecutive days. ELA.EE.RI.5.3 C
    • Maddie will, follow a tactile sequenced schedule, with objects that are different but have similar attributes, in order to anticipate transitions , with full physical assistance fading to 
    independent, 4 out of 5 tries per day, 4 out of 5 days per week. This goal is done in conjunction with the TVI specialist.
    """
noahpalmeriep = """Noah Palmer	    	20 min / month
    • Given verbal support, Noah will solve math money problems using the dollar more strategy for amounts up to $20.00 dollars using 1, 5 and 10 dollar bills, on 4/5 daily trials over 3 consecutive weeks.
        ◦ Given verbal support, Noah will solve math money problems using the dollar more strategy for amounts up to $15.00 dollars using 1, 5 and 10 dollar bills, on 4/5 daily trials over 3 consecutive
        weeks.
        ◦ Given verbal support, Noah will solve math money problems using the dollar more strategy for amounts up to $17.00 dollars using 1, 5 and 10 dollar bills, on 4/5 daily trials over 3 consecutive
        weeks.
    """
paulasackettiep = """Paula Sackett      30 min / month
    • When given moderate support, Paula will participate in two separate leisure skill activities (crafts,games, books, etc.) throughout the school week, then when shown a 3D item associated with each
    activity, she will choose (by looking at and grabbing) the 3D item associated with the activity that she preferred, on 2x weekly trials, as measured over 12 consecutive weeks (staff will keep a
    running list of activities she enjoys to add to her interest inventory).
        ◦ When given maximal support, Paula will participate in two separate leisure skill activities (crafts, games, books, etc.) throughout the school week, then when shown a 3D item associated with
        each activity, she will choose (by looking at and grabbing) the 3D item associated with the activity that she preferred, on 2x weekly trials, as measured over 12 consecutive weeks (staff will keep
        a running list of activities she enjoys to add to her interest inventory)..
    """
suttonbuelliep = """Sutton Buell    	20 min / month
    • Sutton will independently point to and label shapes, numbers, and count by rote and objects to 10, with a 80% accuracy over 3 consecutive data sessions.
    • Sutton will recognize and label 15 letters and sounds starting with those in her name with 100% accuracy across 4 data sessions as recorded by teacher collected data.
    """

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
        'Write letters  numbers  punctuation',
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
        'Olfactory (smell) function: localization of smells discrimination of odors and recognition of pleasant and unpleasant odors.'
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
        'Mobility skills: noticing and negotiating unexpected drop-offs  using systematic search techniques  and knowing built elements such as block distances  corners  intersection types streets and road '
        'structures.',
        'Orientation skills: knowing routes and understanding layouts',
        'Interpersonal skills: requesting directions  arranging for rides; soliciting information from individuals such as dispatchers  drivers  and store personnel; and using appropriate telephone manners',
        'Decision-making skills: altering travel in response to inclement weather choosing appropriate clothing and gear choosing between routes knowing the advantage and disadvantage of different modes of travel '
        'and making back up plans.'
        ]

ECC_RecreationLeisure = [
        'Play: interacting through play with peers and siblings  entertaining oneself for various periods of time',
        'Physical activity: participating in physical education or other active play activities  taking part in recreation and leisure activities enjoyed by the family',
        'Health  fitness and individual sports: developing a regimen of physical exercise that leads to improvement or maintenance of strength  stamina and endurance; developing skills for engaging in such '
        'activities as track  wrestling and weight-lifting.',
        'Team and spectator sports: learning  to enjoy competitive and noncompetitive sports activities such as football  baseball  soccer  golf baseball or goalball  as a participant or as a spectator',
        'Leisure activities and hobbies: being exposed to opportunities for choosing a favorite game or book experiencing arts and crafts activities appreciating and enjoying fine arts in such forms as museum  '
        'visits theater dance opera and music.'
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
        'Cooking: preparing and cooking meals pouring liquids retrieving utensils  stirring and mixing  spreading and spooning  helping with dishes  using a stove  cleaning up  learning food-related concepts '
        'involved in gardening  visiting grocery stores  applying food nutrition  and opening and closing different kinds of packages.',
        'Cleaning and general household tasks: participating in responsibilities at home and school  retrieving and replacing toys and games  and using cleaning supplies and equipment.',
        'Telephone use: calling friends  knowing how to make emergency calls and having a system of phone number retrieval',
        'Money management: identifying coins and bills using ATMs writing checks and managing money.'
        ]

ECC_SocialInteractionSkills = [
        'Appropriate body language: knowing when to lean forward to hear a secret from a friend  maintaining appropriate eye contact  facing a person who is speaking  standing up to greet a new friend keeping '
        'hands to oneself during a group conversation',
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

needformovement = ("""
NEED FOR MOVEMENT
0.........Range 1-2:  Objects viewed generally have movement/reflective properties
1.........Range 3-4:  More consistent localization, brief fixations on movement & reflective materials
2.........Range 5-6:  Movement continues to be an important factor to initiate visual attention
3.........Range 7-8:  Movement not required for attention at near
4.........Range 9-10: Typical responses to moving targets
""")
visuallatency = ("""
VISUAL LATENCY
0.........Range 1-2:  Prolonged periods of visual latency
1.........Range 3-4:  Latency slightly decreases after periods of consistent viewing
2.........Range 5-6:  Latency present only when student is tired, stressed, or over stimulated
3.........Range 7-8:  Latency rarely present
4.........Range 9-10: Latency resolved
""")
visualfieldpreference = ("""
VISUAL FIELD LATENCY
0.........Range 1-2:  Distinct field dependency
1.........Range 3-4:  Shows visual field preferences
2.........Range 5-6:  Field preferences decreasing with familiar inputs
3.........Range 7-8:  May alternate use of right and left fields
4.........Range 9-10: Visual fields unrestricted
""")
visualcomplexity = ("""
DIFFICULTY WITH VISUAL COMPLEXITY
0.........Range 1-2:  Responds only in strictly controlled environments
1.........Range 3-4:  Visually fixates when environment is controlled
2.........Range 5-6:  Student tolerates low levels of familiar background noise
                         Regards familiar faces when voice does not compete
3.........Range 7-8:  Competing auditory stimuli tolerated during periods of viewing
                         Views simple books/ symbols & Smiles at/regards familiar and new faces
4.........Range 9-10: Only the most complex visual environments affect visual response
                         Views books or other 2-dimensional materials & Typical visual- social responses
""")
nonpurposefulgaze = ("""
LIGHT GAZING AND NONPURPOSEFUL GAZE
0.........Range 1-2:  May localize briefly but no prolonged fixations on objects or faces
                         Overly attentive to lights or perhaps ceiling fans
1.........Range 3-4:  Less attracted to lights - can be redirected to other targets
2.........Range 5-6:  Light is no longer a distractor
3.........Range 7-8:  Light is no longer a distractor
4.........Range 9-10: Light is no longer a distractor
""")
distanceviewing = ("""
DIFFICULTY WITH DISTANCE VIEWING
0.........Range 1-2:  Visually attends in near space only
1.........Range 3-4:  Occasional visual attention on familiar, moving or large targets at 2-3 feet
2.........Range 5-6:  Visual attention extends beyond near space, up to 4-6 feet
3.........Range 7-8:  Visual attention extends to 10 feet with targets that produce movement
4.........Range 9-10: Visual attention extends beyond 20 feet & Demonstrates memory of visual events
""")
visualreflexes = ("""
ATYPICAL VISUAL REFLEXES
0......... Range 1-2:  No blink in response to touch and/or visual threat
1.........Range 3-4:  Blinks in response to touch but response may be latent
2.........Range 5-6:  Blink response to touch consistently present
                         Visual threat response intermittently present
3.........Range 7-8:  Visual threat response consistently present (both near 90% resolved)
4.........Range 9-10: Visual reflexes always present, resolved
""")
visualnovelty = ("""
DIFFICULTY WITH VISUAL NOVELTY
0.........Range 1-2:  Only favorite or known objects solicit visual attention
1.........Range 3-4:  May tolerate novel objects if the novel objects share characteristics of familiar objects
2.........Range 5-6:  Use of “known” objects to initiate looking sequence
3.........Range 7-8:  Selection of objects less restricted, requires 1-2 sessions of “warm up” time
4.........Range 9-10: Selection of objects not restricted
""")
visuallyguidedreach = ("""
ABSENCE OF VISUALLY GUIDED REACH
0.........Range 1-2:  Look & touch occur as separate functions
                     Large &/or moving targets
1.........Range 3-4:  Look & touch on smaller objects that are familiar, lighted, or reflective
                     Look and touch are still separate
2.........Range 5-6:  Visually guided reach with familiar objects or “favorite” color
3.........Range 7-8:  Look and touch occur in rapid sequence but not always together
4.........Range 9-10: Look and touch consistently
""")
colorpreference = ("""
COLOR PREFERENCE
0.........Range 1-2:  Objects viewed are generally single color
1.........Range 3-4:  Has “favorite” color
2.........Range 5-6:  Objects may have 2- 3 colors
3.........Range 7-8:  More colors, familiar patterns regarded
4.........Range 9-10: No color or pattern preference
""")

##############################################################################
# End Variables
##############################################################################
