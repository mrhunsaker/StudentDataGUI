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

                        # list_names = ['date','P1_1','P1_2','P1_3','P1_4','P1_5','P1_6','P2_1','P2_2','P2_3','P2_4','P3_1','P3_2','P3_3','P3_4','P3_5','P3_6','P3_7','P3_8','P3_9','P3_10','P3_11','P4_1','P4_2','P4_3','P4_4','P4_5','P4_6','P4_7']

                        list_data = [studentname, dateNow, trial11, trial12,
                                     trial13, trial14, trial15, trial16,
                                     trial21, trial22,
                                     trial23, trial24,
                                     trial31, trial32, trial33, trial34,
                                     trial35, trial36, trial37, trial38,
                                     trial39, trial310,
                                     trial311,
                                     trial41, trial42, trial43, trial44,
                                     trial45, trial46, trial47]
                        os.chdir(USER_DIR)
                        with open(
                                f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\ScreenReaderSkillsProgression.csv",
                                'a',
                                newline='') as f_setup:
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

        fig.update_layout(template="simple_white", title_text="Screen Reader Skills Progression")

        fig.write_html(
            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\ScreenReaderSkillsProgression.html")
