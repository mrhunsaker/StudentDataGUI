class braillePanel(scrolled.ScrolledPanel):
    """

    """

    def __init__(
            self,
            parent
            ):
        scrolled.ScrolledPanel.__init__(
                self,
                parent,
                -1
                )
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(
                wx.StaticLine(
                        self,
                        -1,
                        size = (
                                1500,
                                -1
                                )
                        ),
                0,
                wx.ALL,
                5
                )
        vbox.Add(
                wx.StaticLine(
                        self,
                        -1,
                        size = (-1,
                                2100
                                )
                        ),
                0,
                wx.ALL,
                5
                )
        vbox.Add(
                (20,
                 20
                 )
                )
        self.SetSizer(vbox)
        self.SetupScrolling()
        self.SetBackgroundColour(
                random.choice(
                        colorList
                        )
                )
        self.SetFont(
                wx.Font(
                        10,
                        wx.MODERN,
                        wx.NORMAL,
                        wx.NORMAL,
                        False,
                        u'Atkinson Hyperlegible'
                        )
                )
        wx.StaticText(
                self,
                -1,
                "BRAILLE SKILLS PROGRESSION",
                pos = (
                        200,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "Student Name",
                pos = (
                        30,
                        50
                        )
                )
        self.studentname1 = wx.Choice(
                self,
                -1,
                choices = students,
                pos = (
                        130,
                        50
                        ),
                size = (
                        300,
                        30
                        )
                )
        wx.StaticText(
                self,
                -1,
                "RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent",
                pos = (
                        550,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "1.1 Track Left to Right" + '.' * (200 - len("1.1 Track Left to Right")),
                pos = (
                        30,
                        80
                        )
                )
        self.trial11 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        80
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "1.2 Track Top to Bottom" + '.' * (200 - len("1.2 Track Top to Bottom")),
                pos = (
                        30,
                        110
                        )
                )
        self.trial12 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        110
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "1.3 Discriminate Shapes" + '.' * (200 - len("1.3 Discriminate Shapes")),
                pos = (
                        30,
                        140
                        )
                )
        self.trial13 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        140
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "1.4 Discriminate Braille Characters" + '.' * (200 - len("1.4 Discriminate Braille Characters")),
                pos = (
                        30,
                        170
                        )
                )
        self.trial14 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        170
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.1 Mangold Progression: G C L" + '.' * (200 - len("2.1 Mangold Progression: G C L")),
                pos = (
                        30,
                        200
                        )
                )
        self.trial21 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        200
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.2 Mangold Progression: D Y" + '.' * (200 - len("2.2 Mangold Progression: D Y")),
                pos = (
                        30,
                        230
                        )
                )
        self.trial22 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        230
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.3 Mangold Progression: A B" + '.' * (200 - len("2.3 Mangold Progression: A B")),
                pos = (
                        30,
                        260
                        )
                )
        self.trial23 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        260
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.4 Mangold Progression: S" + '.' * (200 - len("2.4 Mangold Progression: S")),
                pos = (
                        30,
                        290
                        )
                )
        self.trial24 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        290
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.5 Mangold Progression: W" + '.' * (200 - len("2.5 Mangold Progression: W")),
                pos = (
                        30,
                        320
                        )
                )
        self.trial25 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        320
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.6 Mangold Progression: P O" + '.' * (200 - len("2.6 Mangold Progression: P O")),
                pos = (
                        30,
                        350
                        )
                )
        self.trial26 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        350
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.7 Mangold Progression: K" + '.' * (200 - len("2.7 Mangold Progression: K")),
                pos = (
                        30,
                        380
                        )
                )
        self.trial27 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        380
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.8 Mangold Progression: R" + '.' * (200 - len("2.8 Mangold Progression: R")),
                pos = (
                        30,
                        410
                        )
                )
        self.trial28 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        410
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.9 Mangold Progression: M E" + '.' * (200 - len("2.9 Mangold Progression: M E")),
                pos = (
                        30,
                        440
                        )
                )
        self.trial29 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        440
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.10 Mangold Progression: H" + '.' * (200 - len("2.10 Mangold Progression: H")),
                pos = (
                        30,
                        470
                        )
                )
        self.trial210 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        470
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.11 Mangold Progression: N X" + '.' * (200 - len("2.11 Mangold Progression: N X")),
                pos = (
                        30,
                        500
                        )
                )
        self.trial211 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        500
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.12 Mangold Progression: Z F" + '.' * (200 - len("2.12 Mangold Progression: Z F")),
                pos = (
                        30,
                        530
                        )
                )
        self.trial212 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        530
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.13 Mangold Progression: U T" + '.' * (200 - len("2.13 Mangold Progression: U T")),
                pos = (
                        30,
                        560
                        )
                )
        self.trial213 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        560
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.14 Mangold Progression: Q I" + '.' * (200 - len("2.14 Mangold Progression: Q I")),
                pos = (
                        30,
                        590
                        )
                )
        self.trial214 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        590
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "2.15 Mangold Progression: V J" + '.' * (200 - len("2.15 Mangold Progression: V J")),
                pos = (
                        30,
                        620
                        )
                )
        self.trial215 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        620
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.1 Alphabetic Wordsigns" + '.' * (200 - len("3.1 Alphabetic Wordsigns")),
                pos = (
                        30,
                        650
                        )
                )
        self.trial31 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        650
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.2 Braille Numbers" + '.' * (200 - len("3.2 Braille Numbers")),
                pos = (
                        30,
                        680
                        )
                )
        self.trial32 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        680
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.3 Punctuation" + '.' * (200 - len("3.3 Punctuation")),
                pos = (
                        30,
                        710
                        )
                )
        self.trial33 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        710
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.4 Strong Contractions - AND OF FOR WITH THE" + '.' * (200 - len("3.4 Strong Contractions - AND OF FOR WITH THE")),
                pos = (
                        30,
                        740
                        )
                )
        self.trial34 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        740
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.5 Strong Groupsigns - CH GH SH TH WH ED ER OU OW ST AR ING" + '.' * (200 - len("3.5 Strong Groupsigns - CH GH SH TH WH ED ER OU OW ST AR ING")),
                pos = (
                        30,
                        770
                        )
                )
        self.trial35 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        770
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.6 Strong Wordsigns - CH SH TH WH OU ST" + '.' * (200 - len("3.6 Strong Wordsigns - CH SH TH WH OU ST")),
                pos = (
                        30,
                        800
                        )
                )
        self.trial36 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        800
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.7 Lower Groupsigns - BE CON DIS" + '.' * (200 - len("3.7 Lower Groupsigns - BE CON DIS")),
                pos = (
                        30,
                        830
                        )
                )
        self.trial37 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        830
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.8 Lower Groupsigns - EA BB CC FF GG" + '.' * (200 - len("3.8 Lower Groupsigns - EA BB CC FF GG")),
                pos = (
                        30,
                        860
                        )
                )
        self.trial38 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        860
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.9 Lower Group/Wordsigns - EN IN" + '.' * (200 - len("3.9 Lower Group/Wordsigns - EN IN")),
                pos = (
                        30,
                        890
                        )
                )
        self.trial39 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        890
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.10 Lower Wordsigns - BE HIS WAS WERE" + '.' * (200 - len("3.10 Lower Wordsigns - BE HIS WAS WERE")),
                pos = (
                        30,
                        920
                        )
                )
        self.trial310 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        920
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.11 Dot 5 Contractions" + '.' * (200 - len("3.11 Dot 5 Contractions")),
                pos = (
                        30,
                        950
                        )
                )
        self.trial311 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        950
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.12 Dot 45 Contractions" + '.' * (200 - len("3.12 Dot 45 Contractions")),
                pos = (
                        30,
                        980
                        )
                )
        self.trial312 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        980
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.13 Dot 456 Contractions" + '.' * (200 - len("3.13 Dot 456 Contractions")),
                pos = (
                        30,
                        1010
                        )
                )
        self.trial313 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1010
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.14 Final Letter Groupsigns" + '.' * (200 - len("3.14 Final Letter Groupsigns")),
                pos = (
                        30,
                        1040
                        )
                )
        self.trial314 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1040
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "3.15 Shortform Words" + '.' * (200 - len("3.15 Shortform Words")),
                pos = (
                        30,
                        1070
                        )
                )
        self.trial315 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1070
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "4.1 Grade 1 Indicators" + '.' * (200 - len("4.1 Grade 1 Indicators")),
                pos = (
                        30,
                        1100
                        )
                )
        self.trial41 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1100
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "4.2 Capitals Indicators" + '.' * (200 - len("4.2 Capitals Indicators")),
                pos = (
                        30,
                        1130
                        )
                )
        self.trial42 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1130
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "4.3 Numeric Mode and Spatial Math" + '.' * (200 - len("4.3 Numeric Mode and Spatial Math")),
                pos = (
                        30,
                        1160
                        )
                )
        self.trial43 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1160
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "4.4 Typeform Indicators - ITALIC BOLD UNDERLINE SCRIPT" + '.' * (200 - len("4.4 Typeform Indicators - ITALIC BOLD UNDERLINE SCRIPT")),
                pos = (
                        30,
                        1190
                        )
                )
        self.trial44 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1190
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "5.1 Page Numbering" + '.' * (200 - len("5.1 Page Numbering")),
                pos = (
                        30,
                        1220
                        )
                )
        self.trial51 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1220
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "5.2 Headings" + '.' * (200 - len("5.2 Headings")),
                pos = (
                        30,
                        1250
                        )
                )
        self.trial52 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1250
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "5.3 Lists" + '.' * (200 - len("5.3 Lists")),
                pos = (
                        30,
                        1280
                        )
                )
        self.trial53 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1280
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "5.4 Poetry / Drama" + '.' * (200 - len("5.4 Poetry / Drama")),
                pos = (
                        30,
                        1310
                        )
                )
        self.trial54 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1310
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "6.1 Operation and Comparison Signs" + '.' * (200 - len("6.1 Operation and Comparison Signs")),
                pos = (
                        30,
                        1340
                        )
                )
        self.trial61 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1340
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "6.2 Grade 1 Mode" + '.' * (200 - len("6.2 Grade 1 Mode")),
                pos = (
                        30,
                        1370
                        )
                )
        self.trial62 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1370
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "6.3 Special Print Symbols" + '.' * (200 - len("6.3 Special Print Symbols")),
                pos = (
                        30,
                        1400
                        )
                )
        self.trial63 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1400
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "6.4 Omission Marks" + '.' * (200 - len("6.4 Omission Marks")),
                pos = (
                        30,
                        1430
                        )
                )
        self.trial64 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1430
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "6.5 Shape Indicators" + '.' * (200 - len("6.5 Shape Indicators")),
                pos = (
                        30,
                        1460
                        )
                )
        self.trial65 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1460
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "6.6 Roman Numerals" + '.' * (200 - len("6.6 Roman Numerals")),
                pos = (
                        30,
                        1490
                        )
                )
        self.trial66 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1490
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "6.7 Fractions" + '.' * (200 - len("6.7 Fractions")),
                pos = (
                        30,
                        1520
                        )
                )
        self.trial67 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1520
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.1 Grade 1 Mode and algebra" + '.' * (200 - len("7.1 Grade 1 Mode and algebra")),
                pos = (
                        30,
                        1550
                        )
                )
        self.trial71 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1550
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.2 Grade 1 Mode and Fractions" + '.' * (200 - len("7.2 Grade 1 Mode and Fractions")),
                pos = (
                        30,
                        1580
                        )
                )
        self.trial72 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1580
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.3 Advanced Operation and Comparison Signs" + '.' * (200 - len("7.3 Advanced Operation and Comparison Signs")),
                pos = (
                        30,
                        1610
                        )
                )
        self.trial73 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1610
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.4 Indices" + '.' * (200 - len("7.4 Indices")),
                pos = (
                        30,
                        1640
                        )
                )
        self.trial74 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1640
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.5 Roots and Radicals" + '.' * (200 - len("7.5 Roots and Radicals")),
                pos = (
                        30,
                        1670
                        )
                )
        self.trial75 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1670
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.6 Miscellaneous Shape Indicators" + '.' * (200 - len("7.6 Miscellaneous Shape Indicators")),
                pos = (
                        30,
                        1700
                        )
                )
        self.trial76 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1700
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.7 Functions" + '.' * (200 - len("7.7 Functions")),
                pos = (
                        30,
                        1730
                        )
                )
        self.trial77 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1730
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "7.8 Greek Letters" + '.' * (200 - len("7.8 Greek Letters")),
                pos = (
                        30,
                        1760
                        )
                )
        self.trial78 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1760
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "8.1 Functions" + '.' * (200 - len("8.1 Functions")),
                pos = (
                        30,
                        1790
                        )
                )
        self.trial81 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1790
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "8.2 Modifiers: Bars and Dots" + '.' * (200 - len("8.2 Modifiers: Bars and Dots")),
                pos = (
                        30,
                        1820
                        )
                )
        self.trial82 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1820
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "8.3 Modifiers: Arrows and Limits" + '.' * (200 - len("8.3 Modifiers: Arrows and Limits")),
                pos = (
                        30,
                        1850
                        )
                )
        self.trial83 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1850
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "8.4 Probability" + '.' * (200 - len("8.4 Probability")),
                pos = (
                        30,
                        1880
                        )
                )
        self.trial84 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1880
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "8.5 Calculus: Differentiation" + '.' * (200 - len("8.5 Calculus: Differentiation")),
                pos = (
                        30,
                        1910
                        )
                )
        self.trial85 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1910
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "8.6 Calculus: Integration" + '.' * (200 - len("8.6 Calculus: Integration")),
                pos = (
                        30,
                        1940
                        )
                )
        self.trial86 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1940
                        ),
                size = (
                        500,
                        20
                        )
                )
        wx.StaticText(
                self,
                -1,
                "8.7 Vertical Bars" + '.' * (200 - len("8.7 Vertical Bars")),
                pos = (
                        30,
                        1970
                        )
                )
        self.trial87 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (
                        650,
                        1970
                        ),
                size = (
                        500,
                        20
                        )
                )
        self.btn = wx.Button(
                self,
                201,
                "SAVE",
                pos = (
                        450,
                        2000
                        ),
                size = (
                        70,
                        30
                        )
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.save,
                id = 201
                )
        self.btn = wx.Button(
                self,
                203,
                "PRINT GRAPHS",
                pos = (
                        450,
                        2040
                        ),
                size = (
                        170,
                        30
                        )
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.graph,
                id = 203
                )
        self.btn1 = wx.Button(
                self,
                202,
                "EXIT",
                pos = (
                        550,
                        2000
                        ),
                size = (
                        70,
                        30
                        )
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.exit,
                id = 202
                )

    @staticmethod
    def exit(event):
        """

        :param event:
        :type event:
        """
        wx.Exit()

    def save(
            self,
            event
            ):
        """

        :param event:
        :type event:
        """
        studentname = self.studentname1.GetString(
                self.studentname1.GetSelection()
                )
        datenow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S")
        simpledate = datetime.datetime.now().strftime("%Y_%m_%d-%H%M")
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
        box = wx.TextEntryDialog(
                None,
                "Enter File Name",
                "Title",
                f"braille{studentname.title()}{datenow}"
                )
        if box.ShowModal() == wx.ID_OK:
            self.studentdatabasename = box.GetValue()
            if not Path(USER_DIR).joinpath(
                    'StudentDatabase',
                    'StudentDataFiles',
                    studentname,
                    self.studentdatabasename + '.txt'
                    ).exists():
                tmppath = Path(USER_DIR).joinpath(
                        'StudentDatabase',
                        'StudentDataFiles',
                        studentname,
                        self.studentdatabasename + '.txt'
                        )
                Path.touch(tmppath)
                self.filename = open(
                        tmppath,
                        'w'
                        )
                self.filename.write('studentname' + ', ')
                self.filename.write('simpledate' + ', ')
                self.filename.write('trial11' + ', ')
                self.filename.write('trial12' + ', ')
                self.filename.write('trial13' + ', ')
                self.filename.write('trial14' + ', ')
                self.filename.write('trial21' + ', ')
                self.filename.write('trial22' + ', ')
                self.filename.write('trial23' + ', ')
                self.filename.write('trial24' + ', ')
                self.filename.write('trial25' + ', ')
                self.filename.write('trial26' + ', ')
                self.filename.write('trial27' + ', ')
                self.filename.write('trial28' + ', ')
                self.filename.write('trial29' + ', ')
                self.filename.write('trial210' + ', ')
                self.filename.write('trial211' + ', ')
                self.filename.write('trial212' + ', ')
                self.filename.write('trial213' + ', ')
                self.filename.write('trial214' + ', ')
                self.filename.write('trial215' + ', ')
                self.filename.write('trial31' + ', ')
                self.filename.write('trial32' + ', ')
                self.filename.write('trial33' + ', ')
                self.filename.write('trial34' + ', ')
                self.filename.write('trial35' + ', ')
                self.filename.write('trial36' + ', ')
                self.filename.write('trial37' + ', ')
                self.filename.write('trial38' + ', ')
                self.filename.write('trial39' + ', ')
                self.filename.write('trial310' + ', ')
                self.filename.write('trial311' + ', ')
                self.filename.write('trial312' + ', ')
                self.filename.write('trial313' + ', ')
                self.filename.write('trial314' + ', ')
                self.filename.write('trial315' + ', ')
                self.filename.write('trial41' + ', ')
                self.filename.write('trial42' + ', ')
                self.filename.write('trial43' + ', ')
                self.filename.write('trial44' + ', ')
                self.filename.write('trial51' + ', ')
                self.filename.write('trial52' + ', ')
                self.filename.write('trial53' + ', ')
                self.filename.write('trial54' + ', ')
                self.filename.write('trial61' + ', ')
                self.filename.write('trial62' + ', ')
                self.filename.write('trial63' + ', ')
                self.filename.write('trial64' + ', ')
                self.filename.write('trial65' + ', ')
                self.filename.write('trial66' + ', ')
                self.filename.write('trial67' + ', ')
                self.filename.write('trial71' + ', ')
                self.filename.write('trial72' + ', ')
                self.filename.write('trial73' + ', ')
                self.filename.write('trial74' + ', ')
                self.filename.write('trial75' + ', ')
                self.filename.write('trial76' + ', ')
                self.filename.write('trial77' + ', ')
                self.filename.write('trial78' + ', ')
                self.filename.write('trial81' + ', ')
                self.filename.write('trial82' + ', ')
                self.filename.write('trial83' + ', ')
                self.filename.write('trial84' + ', ')
                self.filename.write('trial85' + ', ')
                self.filename.write('trial86' + ', ')
                self.filename.write('trial87' + ', ')
                self.filename.write(studentname + ', ')
                self.filename.write(simpledate + ', ')
                self.filename.write(trial11 + ', ')
                self.filename.write(trial12 + ', ')
                self.filename.write(trial13 + ', ')
                self.filename.write(trial14 + ', ')
                self.filename.write(trial21 + ', ')
                self.filename.write(trial22 + ', ')
                self.filename.write(trial23 + ', ')
                self.filename.write(trial24 + ', ')
                self.filename.write(trial25 + ', ')
                self.filename.write(trial26 + ', ')
                self.filename.write(trial27 + ', ')
                self.filename.write(trial28 + ', ')
                self.filename.write(trial29 + ', ')
                self.filename.write(trial210 + ', ')
                self.filename.write(trial211 + ', ')
                self.filename.write(trial212 + ', ')
                self.filename.write(trial213 + ', ')
                self.filename.write(trial214 + ', ')
                self.filename.write(trial215 + ', ')
                self.filename.write(trial31 + ', ')
                self.filename.write(trial32 + ', ')
                self.filename.write(trial33 + ', ')
                self.filename.write(trial34 + ', ')
                self.filename.write(trial35 + ', ')
                self.filename.write(trial36 + ', ')
                self.filename.write(trial37 + ', ')
                self.filename.write(trial38 + ', ')
                self.filename.write(trial39 + ', ')
                self.filename.write(trial310 + ', ')
                self.filename.write(trial311 + ', ')
                self.filename.write(trial312 + ', ')
                self.filename.write(trial313 + ', ')
                self.filename.write(trial314 + ', ')
                self.filename.write(trial315 + ', ')
                self.filename.write(trial41 + ', ')
                self.filename.write(trial42 + ', ')
                self.filename.write(trial43 + ', ')
                self.filename.write(trial44 + ', ')
                self.filename.write(trial51 + ', ')
                self.filename.write(trial52 + ', ')
                self.filename.write(trial53 + ', ')
                self.filename.write(trial54 + ', ')
                self.filename.write(trial61 + ', ')
                self.filename.write(trial62 + ', ')
                self.filename.write(trial63 + ', ')
                self.filename.write(trial64 + ', ')
                self.filename.write(trial65 + ', ')
                self.filename.write(trial66 + ', ')
                self.filename.write(trial67 + ', ')
                self.filename.write(trial71 + ', ')
                self.filename.write(trial72 + ', ')
                self.filename.write(trial73 + ', ')
                self.filename.write(trial74 + ', ')
                self.filename.write(trial75 + ', ')
                self.filename.write(trial76 + ', ')
                self.filename.write(trial77 + ', ')
                self.filename.write(trial78 + ', ')
                self.filename.write(trial81 + ', ')
                self.filename.write(trial82 + ', ')
                self.filename.write(trial83 + ', ')
                self.filename.write(trial84 + ', ')
                self.filename.write(trial85 + ', ')
                self.filename.write(trial86 + ', ')
                self.filename.write(trial87 + ', ')
                self.filename.write(trial12 + ', ')
                self.filename.write(trial13 + ', ')
                self.filename.write(trial14 + ', ')
                self.filename.write(trial21 + ', ')
                self.filename.write(trial22 + ', ')
                self.filename.write(trial23 + ', ')
                self.filename.write(trial24 + ', ')
                self.filename.write(trial25 + ', ')
                self.filename.write(trial26 + ', ')
                self.filename.write(trial27 + ', ')
                self.filename.write(trial28 + ', ')
                self.filename.write(trial29 + ', ')
                self.filename.write(trial210 + ', ')
                self.filename.write(trial211 + ', ')
                self.filename.write(trial212 + ', ')
                self.filename.write(trial213 + ', ')
                self.filename.write(trial214 + ', ')
                self.filename.write(trial215 + ', ')
                self.filename.write(trial31 + ', ')
                self.filename.write(trial32 + ', ')
                self.filename.write(trial33 + ', ')
                self.filename.write(trial34 + ', ')
                self.filename.write(trial35 + ', ')
                self.filename.write(trial36 + ', ')
                self.filename.write(trial37 + ', ')
                self.filename.write(trial38 + ', ')
                self.filename.write(trial39 + ', ')
                self.filename.write(trial310 + ', ')
                self.filename.write(trial311 + ', ')
                self.filename.write(trial312 + ', ')
                self.filename.write(trial313 + ', ')
                self.filename.write(trial314 + ', ')
                self.filename.write(trial315 + ', ')
                self.filename.write(trial41 + ', ')
                self.filename.write(trial42 + ', ')
                self.filename.write(trial43 + ', ')
                self.filename.write(trial44 + ', ')
                self.filename.write(trial51 + ', ')
                self.filename.write(trial52 + ', ')
                self.filename.write(trial53 + ', ')
                self.filename.write(trial54 + ', ')
                self.filename.write(trial61 + ', ')
                self.filename.write(trial62 + ', ')
                self.filename.write(trial63 + ', ')
                self.filename.write(trial64 + ', ')
                self.filename.write(trial65 + ', ')
                self.filename.write(trial66 + ', ')
                self.filename.write(trial67 + ', ')
                self.filename.write(trial71 + ', ')
                self.filename.write(trial72 + ', ')
                self.filename.write(trial73 + ', ')
                self.filename.write(trial74 + ', ')
                self.filename.write(trial75 + ', ')
                self.filename.write(trial76 + ', ')
                self.filename.write(trial77 + ', ')
                self.filename.write(trial78 + ', ')
                self.filename.write(trial81 + ', ')
                self.filename.write(trial82 + ', ')
                self.filename.write(trial83 + ', ')
                self.filename.write(trial84 + ', ')
                self.filename.write(trial85 + ', ')
                self.filename.write(trial86 + ', ')
                self.filename.write(trial87 + ', ')
                self.filename.close()
                tmppath = Path(USER_DIR).joinpath(
                        'StudentDatabase',
                        'StudentDataFiles',
                        'Filenames.txt'
                        )
                self.filename = open(
                        tmppath,
                        'a'
                        )
                tmppath = Path(USER_DIR).joinpath(
                        'StudentDatabase',
                        'StudentDataFiles',
                        studentname,
                        self.studentdatabasename + '.txt'
                        )
                self.filename.write(f"'{tmppath}'" + '\n')
                self.filename.close()
                os.chdir(USER_DIR)
                tmppath = Path(USER_DIR).joinpath(
                        'StudentDatabase',
                        'StudentDataFiles',
                        studentname,
                        'BrailleSkillsProgression.csv'
                        )
                with open(
                        tmppath,
                        'a',
                        newline = ''
                        ) as f_setup:
                    list_data = [
                            datenow,
                            trial11,
                            trial12,
                            trial13,
                            trial14,
                            trial21,
                            trial22,
                            trial23,
                            trial24,
                            trial25,
                            trial26,
                            trial27,
                            trial28,
                            trial29,
                            trial210,
                            trial211,
                            trial212,
                            trial213,
                            trial214,
                            trial215,
                            trial31,
                            trial32,
                            trial33,
                            trial34,
                            trial35,
                            trial36,
                            trial37,
                            trial38,
                            trial39,
                            trial310,
                            trial311,
                            trial312,
                            trial313,
                            trial314,
                            trial315,
                            trial41,
                            trial42,
                            trial43,
                            trial44,
                            trial51,
                            trial52,
                            trial53,
                            trial54,
                            trial61,
                            trial62,
                            trial63,
                            trial64,
                            trial65,
                            trial66,
                            trial67,
                            trial71,
                            trial72,
                            trial73,
                            trial74,
                            trial75,
                            trial76,
                            trial77,
                            trial78,
                            trial81,
                            trial82,
                            trial83,
                            trial84,
                            trial85,
                            trial86,
                            trial87
                            ]
                    writer_setup = writer(f_setup)
                    writer_setup.writerow(list_data)
                    f_setup.close()
                self.dial = wx.MessageDialog(
                        None,
                        'Saved successfully!',
                        'Info',
                        wx.OK
                        )
                self.dial.ShowModal()
                self.trial11.Clear()
                self.trial12.Clear()
                self.trial13.Clear()
                self.trial14.Clear()
                self.trial21.Clear()
                self.trial22.Clear()
                self.trial23.Clear()
                self.trial24.Clear()
                self.trial25.Clear()
                self.trial26.Clear()
                self.trial27.Clear()
                self.trial28.Clear()
                self.trial29.Clear()
                self.trial210.Clear()
                self.trial211.Clear()
                self.trial212.Clear()
                self.trial213.Clear()
                self.trial214.Clear()
                self.trial215.Clear()
                self.trial31.Clear()
                self.trial32.Clear()
                self.trial33.Clear()
                self.trial34.Clear()
                self.trial35.Clear()
                self.trial36.Clear()
                self.trial37.Clear()
                self.trial38.Clear()
                self.trial39.Clear()
                self.trial310.Clear()
                self.trial311.Clear()
                self.trial312.Clear()
                self.trial313.Clear()
                self.trial314.Clear()
                self.trial315.Clear()
                self.trial41.Clear()
                self.trial42.Clear()
                self.trial43.Clear()
                self.trial44.Clear()
                self.trial51.Clear()
                self.trial52.Clear()
                self.trial53.Clear()
                self.trial54.Clear()
                self.trial61.Clear()
                self.trial62.Clear()
                self.trial63.Clear()
                self.trial64.Clear()
                self.trial65.Clear()
                self.trial66.Clear()
                self.trial67.Clear()
                self.trial71.Clear()
                self.trial72.Clear()
                self.trial73.Clear()
                self.trial74.Clear()
                self.trial75.Clear()
                self.trial76.Clear()
                self.trial77.Clear()
                self.trial78.Clear()
                self.trial81.Clear()
                self.trial82.Clear()
                self.trial83.Clear()
                self.trial84.Clear()
                self.trial85.Clear()
                self.trial86.Clear()
                self.trial87.Clear()
            else:
                self.dial = wx.MessageDialog(
                        None,
                        'Name already exists',
                        'Info',
                        wx.OK
                        )
                self.dial.ShowModal()
        else:
            self.dial = wx.MessageDialog(
                    None,
                    'Save cancelled'  'Info',
                    wx.OK
                    )
            self.dial.ShowModal()

        def data_entry():
            """

            """
            conn = sqlite3.connect(dataBasePath)
            c = conn.cursor()
            c.execute(
                    """INSERT INTO BRAILLEPROGRESS (
                STUDENTNAME,
                DATE,
                P1_1,
                P1_2,
                P1_3,
                P1_4,
                P2_1,
                P2_2,
                P2_3,
                P2_4,
                P2_5,
                P2_6,
                P2_7,
                P2_8,
                P2_9,
                P2_10,
                P2_11,
                P2_12,
                P2_13,
                P2_14,
                P2_15,
                P3_1,
                P3_2,
                P3_3,
                P3_4,
                P3_5,
                P3_6,
                P3_7,
                P3_8,
                P3_9,
                P3_10,
                P3_11,
                P3_12,
                P3_13,
                P3_14,
                P3_15,
                P4_1,
                P4_2,
                P4_3,
                P4_4,
                P5_1,
                P5_2,
                P5_3,
                P5_4,
                P6_1,
                P6_2,
                P6_3,
                P6_4,
                P6_5,
                P6_6,
                P6_7,
                P7_1,
                P7_2,
                P7_3,
                P7_4,
                P7_5,
                P7_6,
                P7_7,
                P7_8,
                P8_1,
                P8_2,
                P8_3,
                P8_4,
                P8_5,
                P8_6,
                P8_7
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
                ?)""",
                    (studentname,
                     datenow,
                     trial11,
                     trial12,
                     trial13,
                     trial14,
                     trial21,
                     trial22,
                     trial23,
                     trial24,
                     trial25,
                     trial26,
                     trial27,
                     trial28,
                     trial29,
                     trial210,
                     trial211,
                     trial212,
                     trial213,
                     trial214,
                     trial215,
                     trial31,
                     trial32,
                     trial33,
                     trial34,
                     trial35,
                     trial36,
                     trial37,
                     trial38,
                     trial39,
                     trial310,
                     trial311,
                     trial312,
                     trial313,
                     trial314,
                     trial315,
                     trial41,
                     trial42,
                     trial43,
                     trial44,
                     trial51,
                     trial52,
                     trial53,
                     trial54,
                     trial61,
                     trial62,
                     trial63,
                     trial64,
                     trial65,
                     trial66,
                     trial67,
                     trial71,
                     trial72,
                     trial73,
                     trial74,
                     trial75,
                     trial76,
                     trial77,
                     trial78,
                     trial81,
                     trial82,
                     trial83,
                     trial84,
                     trial85,
                     trial86,
                     trial87
                     )
                    )
            conn.commit()

        data_entry()

    def graph(
            self,
            event
            ):
        """

        Graphing

        """
        studentname = self.studentname1.GetString(self.studentname1.GetSelection())
        conn = sqlite3.connect(dataBasePath)
        dfSQL = pd.read_sql_query(f"SELECT * FROM BRAILLEPROGRESS", conn)
        dfStudent = dfSQL[dfSQL.STUDENTNAME == studentname]
        print(dfStudent)
        conn.close()
        df = ""
        df = dfStudent.drop(columns = ['ID', 'STUDENTNAME'])
        print(df)
        df = df.rename(columns = {'DATE': 'date'})
        df = df.set_index('date')
        print(df)

        # tmppath=Path(USER_DIR).joinpath(
        #        'StudentDatabase',
        #        'StudentDataFiles',
        #        studentname,
        #        'BrailleSkillsProgression.csv'
        #        )

        # df=pd.read_csv(
        #        tmppath,
        #        sep=',',
        #        index_col=[0],
        #        parse_dates=[0]
        #        )
        df = df.sort_values(by = "date")
        mu, sigma = 0, 0.1
        noise = np.random.normal(
                mu,
                sigma,
                [len(df.index), len(df.columns)]
                )
        df_noisy = df + noise

        fig = make_subplots(
                rows = 7,
                cols = 2,
                specs = [[{}, {"rowspan": 2}], [{}, None],
                         [{"rowspan": 2}, {"rowspan": 2}],
                         [None, None],
                         [{"rowspan": 2}, {"rowspan": 2}],
                         [None, None], [{}, {}]],
                subplot_titles = (
                        "Phase 1: Tracking Skills",
                        "Phase 2: Braille Alphabet",
                        "Phase 1: Tracking Skills",
                        "Phase 3a: Wordsigns, Numbers, Punctuation",
                        "Phase 3b: Strong Contractions",
                        "Phase 3c: Lower Cell Contractions",
                        "Phase 3d: Multiple Cell Contractions",
                        "Phase 4a: Braille Mode Indicators",
                        "Phase 5: Document Formatting"),
                print_grid = True
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P1_1'],
                        mode = "lines+markers",
                        name = "Track left to right",
                        legendgroup = "Phase 1",
                        legendgrouptitle_text = "Phase 1"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P1_2'],
                        mode = "lines+markers",
                        name = "Track top to bottom",
                        legendgroup = "Phase 1",
                        legendgrouptitle_text = "Phase 1"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P1_3'].iloc[[-1]],
                        mode = "lines+markers",
                        name = "Discriminate shapes",
                        legendgroup = "Phase 1",
                        legendgrouptitle_text = "Phase 1"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P1_4'],
                        mode = "lines+markers",
                        name = "Discriminate braille characters",
                        legendgroup = "Phase 1",
                        legendgrouptitle_text = "Phase 1"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_1'],
                        mode = "lines+markers+text",
                        name = "Alphabet",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = True
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_1'].iloc[[-1]],
                        mode = "text",
                        text = [" G C L"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_2'],
                        mode = "lines+markers+text",
                        name = "D Y",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_2'].iloc[[-1]],
                        mode = "text",
                        text = [" D Y"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_3'],
                        mode = "lines+markers+text",
                        name = "A B",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_3'].iloc[[-1]],
                        mode = "text",
                        text = [" A B"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_4'],
                        mode = "lines+markers+text",
                        name = "S",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_4'].iloc[[-1]],
                        mode = "text",
                        text = [" S"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_5'],
                        mode = "lines+markers+text",
                        name = "W",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_5'].iloc[[-1]],
                        mode = "text",
                        text = [" W"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_6'],
                        mode = "lines+markers+text",
                        name = "P O",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_6'].iloc[[-1]],
                        mode = "text",
                        text = [" P O"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_7'],
                        mode = "lines+markers+text",
                        name = "K",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_7'].iloc[[-1]],
                        mode = "text",
                        text = [" K"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_8'],
                        mode = "lines+markers+text",
                        name = "R",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_8'].iloc[[-1]],
                        mode = "text",
                        text = [" R"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_9'],
                        mode = "lines+markers+text",
                        name = "M E",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_9'].iloc[[-1]],
                        mode = "text",
                        text = [" M E"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_10'],
                        mode = "lines+markers+text",
                        name = "H",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_10'].iloc[[-1]],
                        mode = "text",
                        text = [" H"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_11'],
                        mode = "lines+markers+text",
                        name = "N X",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_11'].iloc[[-1]],
                        mode = "text",
                        text = [" N X"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_12'],
                        mode = "lines+markers+text",
                        name = "Z F",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_12'].iloc[[-1]],
                        mode = "text",
                        text = [" Z F"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_13'],
                        mode = "lines+markers+text",
                        name = "U T",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_13'].iloc[[-1]],
                        mode = "text",
                        text = [" U T"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_14'],
                        mode = "lines+markers+text",
                        name = "Q I",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_14'].iloc[[-1]],
                        mode = "text",
                        text = [" Q I"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_15'],
                        mode = "lines+markers+text",
                        name = "V J ",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P2_15'].iloc[[-1]],
                        mode = "text",
                        text = [" V J"],
                        textposition = "middle right",
                        legendgroup = "Phase 2",
                        legendgrouptitle_text = "Phase 2",
                        showlegend = False
                        ),
                row = 1,
                col = 2
                )
        fig.update_layout(showlegend = True)
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_1'],
                        mode = "lines+markers",
                        name = "Alphabetic Wordsigns",
                        legendgroup = "Phase 3a",
                        legendgrouptitle_text = "Phase 3a"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_2'],
                        mode = "lines+markers",
                        name = "Braille Numbers",
                        legendgroup = "Phase 3a",
                        legendgrouptitle_text = "Phase 3a"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_3'],
                        mode = "lines+markers",
                        name = "Punctuation",
                        legendgroup = "Phase 3a",
                        legendgrouptitle_text = "Phase 3a"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_4'],
                        mode = "lines+markers",
                        name = "Strong Contractions <br>(AND OF FOR WITH THE)",
                        legendgroup = "Phase 3b",
                        legendgrouptitle_text = "Phase 3b"
                        ),
                row = 3,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_5'],
                        mode = "lines+markers",
                        name = "Strong Groupsigns <br>(CH GH SH TH WH ED ER OU OW ST AR ING)",
                        legendgroup = "Phase 3b",
                        legendgrouptitle_text = "Phase 3b"
                        ),
                row = 3,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_6'],
                        mode = "lines+markers",
                        name = "Strong Wordsigns <br>(CH SH TH WH OU ST)",
                        legendgroup = "Phase 3b",
                        legendgrouptitle_text = "Phase 3b"
                        ),
                row = 3,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_7'],
                        mode = "lines+markers",
                        name = "Lower Groupsigns <br>(BE CON DIS)",
                        legendgroup = "Phase 3c",
                        legendgrouptitle_text = "Phase 3c"
                        ),
                row = 5,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_8'],
                        mode = "lines+markers",
                        name = "Lower Groupsigns <br>(EA BB CC FF GG)",
                        legendgroup = "Phase 3c",
                        legendgrouptitle_text = "Phase 3c"
                        ),
                row = 5,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_9'],
                        mode = "lines+markers",
                        name = "Lower Groupsigns/Wordsigns <br>(EN IN)",
                        legendgroup = "Phase 3c",
                        legendgrouptitle_text = "Phase 3c"
                        ),
                row = 5,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_10'],
                        mode = "lines+markers",
                        name = "Lower Wordsigns <br>(BE HIS WAS WERE)",
                        legendgroup = "Phase 3c",
                        legendgrouptitle_text = "Phase 3c"
                        ),
                row = 5,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_11'],
                        mode = "lines+markers",
                        name = "Dot 5 Contractions",
                        legendgroup = "Phase 3d",
                        legendgrouptitle_text = "Phase 3d"
                        ),
                row = 5,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_12'],
                        mode = "lines+markers",
                        name = "Dot 45 Contractions",
                        legendgroup = "Phase 3d",
                        legendgrouptitle_text = "Phase 3d"
                        ),
                row = 5,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_13'],
                        mode = "lines+markers",
                        name = "Dot 456 Contractions",
                        legendgroup = "Phase 3d",
                        legendgrouptitle_text = "Phase 3d"
                        ),
                row = 5,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_14'],
                        mode = "lines+markers",
                        name = "Final Letter Groupsigns",
                        legendgroup = "Phase 3d",
                        legendgrouptitle_text = "Phase 3d"
                        ),
                row = 5,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P3_15'],
                        mode = "lines+markers",
                        name = "Shortform Words",
                        legendgroup = "Phase 3d",
                        legendgrouptitle_text = "Phase 3d"
                        ),
                row = 5,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P4_1'],
                        mode = "lines+markers",
                        name = "Grade 1 Indicators",
                        legendgroup = "Phase 4",
                        legendgrouptitle_text = "Phase 4"
                        ),
                row = 7,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index,
                        y = df_noisy['P4_2'],
                        mode = "lines+markers",
                        name = "Capitals Indicators",
                        legendgroup = "Phase 4",
                        legendgrouptitle_text = "Phase 4"
                        ),
                row = 7,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P4_3'],
                        mode = "lines+markers",
                        name = "Numeric Mode and Spatial math",
                        legendgroup = "Phase 4",
                        legendgrouptitle_text = "Phase 4"
                        ),
                row = 7,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P4_4'],
                        mode = "lines+markers",
                        name = "Typeform Indicators <br>(ITALIC, SCRIPT, UNDERLINE, BOLDFACE)",
                        legendgroup = "Phase 4",
                        legendgrouptitle_text = "Phase 4"
                        ),
                row = 7,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P5_1'],
                        mode = "lines+markers",
                        name = "Page Numbering",
                        legendgroup = "Phase 5",
                        legendgrouptitle_text = "Phase 5"
                        ),
                row = 7,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P5_2'],
                        mode = "lines+markers",
                        name = "Headings",
                        legendgroup = "Phase 5",
                        legendgrouptitle_text = "Phase 5"
                        ),
                row = 7,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P5_3'],
                        mode = "lines+markers",
                        name = "Lists",
                        legendgroup = "Phase 5",
                        legendgrouptitle_text = "Phase 5"
                        ),
                row = 7,
                col = 2
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P5_4'],
                        mode = "lines+markers",
                        name = "Poety / Drama",
                        legendgroup = "Phase 5",
                        legendgrouptitle_text = "Phase 5"
                        ),
                row = 7,
                col = 2
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 1,
                col = 2
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 1,
                col = 2
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 1,
                col = 2
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 1,
                col = 2
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 3,
                col = 2
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 3,
                col = 2
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 3,
                col = 2
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 3,
                col = 2
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 5,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 5,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 5,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 5,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 5,
                col = 2
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 5,
                col = 2
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 5,
                col = 2
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 5,
                col = 2
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 7,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 7,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 7,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 7,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 7,
                col = 2
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 7,
                col = 2
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 7,
                col = 2
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 7,
                col = 2
                )
        '''marker = '2022-01-01'
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 1,
                col = 1
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 1,
                col = 2
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 2,
                col = 1
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 3,
                col = 1
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 3,
                col = 2
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 5,
                col = 1
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 5,
                col = 2
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 7,
                col = 1
                )
        fig.add_vline(
                x = marker,
                line_width = 3,
                line_color = "black",
                row = 7,
                col = 2
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 1,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 1,
                col = 2
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 2,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 3,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 3,
                col = 2
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 5,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 5,
                col = 2
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 7,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [" "])],
                row = 7,
                col = 2
                )'''
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 1,
                col = 1
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 2,
                col = 1
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 1,
                col = 2
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 3,
                col = 1
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 3,
                col = 2
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 5,
                col = 1
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 5,
                col = 2
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 5,
                col = 2
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 7,
                col = 2
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 7,
                col = 2
                )
        fig.update_layout(
                xaxis_tickformat = '%d %b', xaxis2_tickformat = '%d %b',
                xaxis3_tickformat = '%d %b',
                xaxis4_tickformat = '%d %b', xaxis5_tickformat = '%d %b',
                xaxis6_tickformat = '%d %b',
                xaxis7_tickformat = '%d %b', xaxis8_tickformat = '%d %b',
                xaxis9_tickformat = '%d %b',
                template = "simple_white",
                title_text = f"{studentname}: Literary UEB Skills Progression",
                legend = dict(
                        font = dict(
                                size = 10
                                )
                        )
                )
        tmppath = Path(USER_DIR).joinpath(
                'StudentDatabase',
                'StudentDataFiles', studentname,
                'UEBLiterarySkillsProgression.html'
                )
        fig.write_html(tmppath)
        fig.show()
        fig = make_subplots(
                rows = 3,
                cols = 1, subplot_titles = (
                        "Phase 6: UEB Technical Basics", "Phase 7: Advanced UEB Technical",
                        "Phase 8: Accelerated UEB Technical"),
                print_grid = True
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P6_1'],
                        mode = "lines+markers",
                        name = " Operation and Comparison Signs",
                        legendgroup = "Phase 6",
                        legendgrouptitle_text = "Phase 6"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P6_2'],
                        mode = "lines+markers",
                        name = "Grade 1 Mode",
                        legendgroup = "Phase 6",
                        legendgrouptitle_text = "Phase 6"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P6_3'],
                        mode = "lines+markers",
                        name = "Special Print Symbols",
                        legendgroup = "Phase 6",
                        legendgrouptitle_text = "Phase 6"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P6_4'],
                        mode = "lines+markers",
                        name = "Omission Marks",
                        legendgroup = "Phase 6",
                        legendgrouptitle_text = "Phase 6"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P6_5'],
                        mode = "lines+markers",
                        name = "Shape Indicators",
                        legendgroup = "Phase 6",
                        legendgrouptitle_text = "Phase 6"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P6_6'],
                        mode = "lines+markers",
                        name = "Roman Numerals",
                        legendgroup = "Phase 6",
                        legendgrouptitle_text = "Phase 6"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P6_7'],
                        mode = "lines+markers",
                        name = "Fractions",
                        legendgroup = "Phase 6",
                        legendgrouptitle_text = "Phase 6"
                        ),
                row = 1,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_1'],
                        mode = "lines+markers",
                        name = "Grade 1 Mode and Algebra",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_2'],
                        mode = "lines+markers",
                        name = "Grade 1 Mode and Fractions",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_3'],
                        mode = "lines+markers",
                        name = "Advanced Operation and Comparison Signs",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_4'],
                        mode = "lines+markers",
                        name = "Indices",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_5'],
                        mode = "lines+markers",
                        name = "Roots and Radicals",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_6'],
                        mode = "lines+markers",
                        name = "Miscellaneous Shape Indicators",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_7'],
                        mode = "lines+markers",
                        name = "Functions",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P7_8'],
                        mode = "lines+markers",
                        name = "Greek letters",
                        legendgroup = "Phase 7",
                        legendgrouptitle_text = "Phase 7"
                        ),
                row = 2,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P8_1'],
                        mode = "lines+markers",
                        name = "Functions",
                        legendgroup = "Phase 8",
                        legendgrouptitle_text = "Phase 8"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P8_2'],
                        mode = "lines+markers",
                        name = "Modifiers, Bars, and Dots",
                        legendgroup = "Phase 8",
                        legendgrouptitle_text = "Phase 8"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P8_3'],
                        mode = "lines+markers",
                        name = "Modifiers, Arrows, and Limits",
                        legendgroup = "Phase 8",
                        legendgrouptitle_text = "Phase 8"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P8_4'],
                        mode = "lines+markers",
                        name = "Probability",
                        legendgroup = "Phase 8",
                        legendgrouptitle_text = "Phase 8"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P8_5'],
                        mode = "lines+markers",
                        name = "Calculus: Differentiation",
                        legendgroup = "Phase 8",
                        legendgrouptitle_text = "Phase 8"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P8_6'],
                        mode = "lines+markers",
                        name = "Calculus: Integration",
                        legendgroup = "Phase 8",
                        legendgrouptitle_text = "Phase 8"
                        ),
                row = 3,
                col = 1
                )
        fig.add_trace(
                go.Scatter(
                        x = df_noisy.index, y = df_noisy['P8_7'],
                        mode = "lines+markers",
                        name = "Vertical Bars",
                        legendgroup = "Phase 8",
                        legendgrouptitle_text = "Phase 8"
                        ),
                row = 3,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                row = 1,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                row = 2,
                col = 1
                )
        fig.update_xaxes(
                rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                row = 3,
                col = 1
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 1,
                col = 1
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 2,
                col = 1
                )
        fig.update_yaxes(
                range = [-.5, 3.5], fixedrange = True,
                ticktext = ["Unable", "Prompted", "Hesitated",
                            "Independent"],
                tickvals = [0.1, 1, 2, 3],
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 1,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 2,
                col = 1
                )
        fig.add_hrect(
                y0 = -.5,
                y1 = .5,
                line_width = 0,
                fillcolor = "red",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = .5,
                y1 = 1.5,
                line_width = 0,
                fillcolor = "orange",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = 1.5,
                y1 = 2.5,
                line_width = 0,
                fillcolor = "yellow",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.add_hrect(
                y0 = 2.5,
                y1 = 3.5,
                line_width = 0,
                fillcolor = "green",
                opacity = 0.2,
                row = 3,
                col = 1
                )
        fig.update_layout(
                xaxis_tickformat = '%d %b', xaxis2_tickformat = '%d %b',
                xaxis3_tickformat = '%d %b',
                template = "simple_white",
                title_text = f"{studentname}: Technical UEB Skills Progression",
                legend = dict(
                        font = dict(
                                size = 10
                                )
                        )
                )
        tmppath = Path(USER_DIR).joinpath(
                'StudentDatabase',
                'StudentDataFiles', studentname,
                'UEBTechnicalSkillsProgression.html'
                )
        fig.write_html(tmppath)

        dfAsString = df.to_html(index = True)

        dialog = MyBrowser(
                None, -1
                )
        dialog.browser.SetPage(dfAsString, "")
        dialog.Show()
        fig.show()