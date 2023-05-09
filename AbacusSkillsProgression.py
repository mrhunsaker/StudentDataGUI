#############################################################################
# Begin Classes
############################################################################
with ui.header().classes(replace='row items-center') as header:
        ui.button(on_click=lambda: left_drawer.toggle()).props('flat color=white icon=menu')
with ui.tabs() as tabs:
        ui.tab('BRAILLE SKILLS PROGRESSION')
        ui.tab('SCREENREADER SKILLS PROGRESSION')
        ui.tab('ABACUS SKILLS PROGRESSION')

with ui.tab_panels(tabs, value='ABACUS SKILLS PROGRESSION'):
        with ui.tab_panel('ABACUS SKILLS PROGRESSION'):
            u_studentname = ui.select(options=students, value='DonaldChamberlain').classes('hidden')
            date = ui.date().classes('hidden')
            u_trial11 = ui.number().classes('hidden')
            u_trial12 = ui.number().classes('hidden')
            u_trial13 = ui.number().classes('hidden')
            u_trial14 = ui.number().classes('hidden')
            u_trial21 = ui.number().classes('hidden')
            u_trial22 = ui.number().classes('hidden')
            u_trial23 = ui.number().classes('hidden')
            u_trial31 = ui.number().classes('hidden')
            u_trial32 = ui.number().classes('hidden')
            u_trial33 = ui.number().classes('hidden')
            u_trial41 = ui.number().classes('hidden')
            u_trial42 = ui.number().classes('hidden')
            u_trial51 = ui.number().classes('hidden')
            u_trial52 = ui.number().classes('hidden')
            u_trial61 = ui.number().classes('hidden')
            u_trial62 = ui.number().classes('hidden')
            u_trial63 = ui.number().classes('hidden')
            u_trial64 = ui.number().classes('hidden')
            u_trial71 = ui.number().classes('hidden')
            u_trial72 = ui.number().classes('hidden')
            u_trial73 = ui.number().classes('hidden')
            u_trial74 = ui.number().classes('hidden')
            u_trial81 = ui.number().classes('hidden')
            u_trial82 = ui.number().classes('hidden')

            def save(event):
                """
                :param event:
                :type event:
                """
                studentname = u_studentname.value
                date = datenow
                trial11 = int(u_trial11.value)
                trial12 = int(u_trial12.value)
                trial13 = int(u_trial13.value)
                trial14 = int(u_trial14.value)
                trial21 = int(u_trial21.value)
                trial22 = int(u_trial22.value)
                trial23 = int(u_trial23.value)
                trial31 = int(u_trial31.value)
                trial32 = int(u_trial32.value)
                trial33 = int(u_trial33.value)
                trial41 = int(u_trial41.value)
                trial42 = int(u_trial42.value)
                trial51 = int(u_trial51.value)
                trial52 = int(u_trial52.value)
                trial61 = int(u_trial61.value)
                trial62 = int(u_trial62.value)
                trial63 = int(u_trial63.value)
                trial64 = int(u_trial64.value)
                trial71 = int(u_trial71.value)
                trial72 = int(u_trial72.value)
                trial73 = int(u_trial73.value)
                trial74 = int(u_trial74.value)
                trial81 = int(u_trial81.value)
                trial82 = int(u_trial82.value)
                
                studentdatabasename = f"screenreader{studentname.title()}{datenow}"
                with open(
                        f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\{studentdatabasename}.txt",
                        'w'
                        ) as filename:
                    filename.write('studentname' + ', ')
                    filename.write('simpledate' + ', ')
                    filename.write('trial11' + ', ')
                    filename.write('trial12' + ', ')
                    filename.write('trial13' + ', ')
                    filename.write('trial14' + ', ')
                    filename.write('trial21' + ', ')
                    filename.write('trial22' + ', ')
                    filename.write('trial23' + ', ')
                    filename.write('trial31' + ', ')
                    filename.write('trial32' + ', ')
                    filename.write('trial33' + ', ')
                    filename.write('trial41' + ', ')
                    filename.write('trial42' + ', ')
                    filename.write('trial51' + ', ')
                    filename.write('trial52' + ', ')
                    filename.write('trial61' + ', ')
                    filename.write('trial62' + ', ')
                    filename.write('trial63' + ', ')
                    filename.write('trial64' + ', ')
                    filename.write('trial71' + ', ')
                    filename.write('trial72' + ', ')
                    filename.write('trial73' + ', ')
                    filename.write('trial74' + ', ')
                    filename.write('trial81' + ', ')
                    filename.write('trial82' + ', ')
                    filename.write(studentname + ', ')
                    filename.write(date + ', ')
                    filename.write(str(trial11) + ', ')
                    filename.write(str(trial12) + ', ')
                    filename.write(str(trial13) + ', ')
                    filename.write(str(trial14) + ', ')
                    filename.write(str(trial21) + ', ')
                    filename.write(str(trial22) + ', ')
                    filename.write(str(trial23) + ', ')
                    filename.write(str(trial31) + ', ')
                    filename.write(str(trial32) + ', ')
                    filename.write(str(trial33) + ', ')
                    filename.write(str(trial41) + ', ')
                    filename.write(str(trial42) + ', ')
                    filename.write(str(trial51) + ', ')
                    filename.write(str(trial52) + ', ')
                    filename.write(str(trial61) + ', ')
                    filename.write(str(trial62) + ', ')
                    filename.write(str(trial63) + ', ')
                    filename.write(str(trial64) + ', ')
                    filename.write(str(trial71) + ', ')
                    filename.write(str(trial72) + ', ')
                    filename.write(str(trial73) + ', ')
                    filename.write(str(trial74) + ', ')
                    filename.write(str(trial81) + ', ')
                    filename.write(str(trial82) + ', ')
                    filename.close()
                            
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
                    self.filename.write(f"{tmppath}" + '\n')
                    self.filename.close()
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
                    list_data = [
                        datenow,
                        trial11,
                        trial12,
                        trial13,
                        trial14,
                        trial21,
                        trial22,
                        trial23,
                        trial31,
                        trial32,
                        trial33,
                        trial41,
                        trial42,
                        trial51,
                        trial52,
                        trial61,
                        trial62,
                        trial63,
                        trial64,
                        trial71,
                        trial72,
                        trial73,
                        trial74,
                        trial81,
                        trial82
                        ]
                    os.chdir(USER_DIR)
                    with open(
                            f"{USER_DIR}\\StudentDatabase\\StudentDataFiles\\{studentname}\\ScreenReaderSkillsProgression.csv",
                            'a',
                            newline = ''
                            ) as f_setup:
                            writer_setup = writer(f_setup)
                            writer_setup.writerow(list_data)
                            f_setup.close()
                    ui.notify('Saved successfully!', close_button='OK')
                def data_entry():
                    """

                    """
                    conn = sqlite3.connect(dataBasePath)
                    c = conn.cursor()
                    c.execute(
                            """INSERT INTO ABACUSPROGRESS (
                        STUDENTNAME,
                        DATE,
                        P1_1,
                        P1_2,
                        P1_3,
                        P1_4,
                        P2_1,
                        P2_2,
                        P2_3,
                        P3_1,
                        P3_2,
                        P3_3,
                        P4_1,
                        P4_2,
                        P5_1,
                        P5_2,
                        P6_1,
                        P6_2,
                        P6_3,
                        P6_4,
                        P7_1,
                        P7_2,
                        P7_3,
                        P7_4,
                        P8_1,
                        P8_2
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
                             trial31,
                             trial32,
                             trial33,
                             trial41,
                             trial42,
                             trial51,
                             trial52,
                             trial61,
                             trial62,
                             trial63,
                             trial64,
                             trial71,
                             trial72,
                             trial73,
                             trial74,
                             trial81,
                             trial82
                             )
                            )
                    conn.commit()

                data_entry()
            
            def graph(
                        self,
                        event
                        ):
                """

                :param event:
                :type event:
                """
                studentname = u_studentname.value
                conn = sqlite3.connect(dataBasePath)
                dfSQL = pd.read_sql_query(f"SELECT * FROM ABACUSPROGRESS", conn)
                dfStudent = dfSQL[dfSQL.STUDENTNAME == studentname]
                print(dfStudent)
                conn.close()
                df = dfStudent.drop(columns = ['ID', 'STUDENTNAME'])
                print(df)
                df = df.rename(columns = {'DATE': 'date'})
                df = df.set_index('date')
                print(df)
                df = df.sort_values(by = "date")
                mu, sigma = 0, 0.1
                noise = np.random.normal(mu, sigma, [len(df.index), len(df.columns)])
                df_noisy = df + noise
                fig = make_subplots(
                        rows = 4,
                        cols = 2,
                        subplot_titles = (
                                "Phase 1: Foundation",
                                "Phase 2: Addition",
                                "Phase 3: Subtraction",
                                "Phase 4: Multiplication",
                                "Phase 5: Division",
                                "Phase 6: Decimals",
                                "Phase 7: Fractions",
                                "Phase 8: Special Functions"),
                        print_grid = True
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P1_1"],
                                mode = "lines+markers",
                                name = "Setting Numbers",
                                legendgroup = "Phase 1",
                                legendgrouptitle_text = "Phase 1"
                                ),
                        row = 1,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P1_2"],
                                mode = "lines+markers",
                                name = "Clearing Beads",
                                legendgroup = "Phase 1",
                                legendgrouptitle_text = "Phase 1"
                                ),
                        row = 1,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P1_3"],
                                mode = "lines+markers",
                                name = "Place Value",
                                legendgroup = "Phase 1",
                                legendgrouptitle_text = "Phase 1"
                                ),
                        row = 1,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P1_4"],
                                mode = "lines+markers",
                                name = "Vocabulary",
                                legendgroup = "Phase 1",
                                legendgrouptitle_text = "Phase 1"
                                ),
                        row = 1,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P2_1"],
                                mode = "lines+markers",
                                name = "Setting Numbers",
                                legendgroup = "Phase 2",
                                legendgrouptitle_text = "Phase 2"
                                ),
                        row = 1,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P2_2"],
                                mode = "lines+markers",
                                name = "Clearing Beads",
                                legendgroup = "Phase 2",
                                legendgrouptitle_text = "Phase 2"
                                ),
                        row = 1,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P2_3"],
                                mode = "lines+markers",
                                name = "Place Value",
                                legendgroup = "Phase 2",
                                legendgrouptitle_text = "Phase 2"
                                ),
                        row = 1,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P3_1"],
                                mode = "lines+markers",
                                name = "Setting Numbers",
                                legendgroup = "Phase 3",
                                legendgrouptitle_text = "Phase 3"
                                ),
                        row = 2,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P3_2"],
                                mode = "lines+markers",
                                name = "Clearing Beads",
                                legendgroup = "Phase 3",
                                legendgrouptitle_text = "Phase 3"
                                ),
                        row = 2,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P3_3"],
                                mode = "lines+markers",
                                name = "Place Value",
                                legendgroup = "Phase 3",
                                legendgrouptitle_text = "Phase 3"
                                ),
                        row = 2,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P4_1"],
                                mode = "lines+markers",
                                name = "Setting Numbers",
                                legendgroup = "Phase 4",
                                legendgrouptitle_text = "Phase 4"
                                ),
                        row = 2,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P4_2"],
                                mode = "lines+markers",
                                name = "Clearing Beads",
                                legendgroup = "Phase 4",
                                legendgrouptitle_text = "Phase 4"
                                ),
                        row = 2,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P5_1"],
                                mode = "lines+markers",
                                name = "Place Value",
                                legendgroup = "Phase 5",
                                legendgrouptitle_text = "Phase 5"
                                ),
                        row = 3,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P5_2"],
                                mode = "lines+markers",
                                name = "Vocabulary",
                                legendgroup = "Phase 5",
                                legendgrouptitle_text = "Phase 5"
                                ),
                        row = 3,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P6_1"],
                                mode = "lines+markers",
                                name = "Setting Numbers",
                                legendgroup = "Phase 6",
                                legendgrouptitle_text = "Phase 6"
                                ),
                        row = 3,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P6_2"],
                                mode = "lines+markers",
                                name = "Clearing Beads",
                                legendgroup = "Phase 6",
                                legendgrouptitle_text = "Phase 6"
                                ),
                        row = 3,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P6_3"],
                                mode = "lines+markers",
                                name = "Place Value",
                                legendgroup = "Phase 6",
                                legendgrouptitle_text = "Phase 6"
                                ),
                        row = 3,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P6_4"],
                                mode = "lines+markers",
                                name = "Vocabulary",
                                legendgroup = "Phase 6",
                                legendgrouptitle_text = "Phase 6"
                                ),
                        row = 3,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P7_1"],
                                mode = "lines+markers",
                                name = "Setting Numbers",
                                legendgroup = "Phase 7",
                                legendgrouptitle_text = "Phase 7"
                                ),
                        row = 4,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P7_2"],
                                mode = "lines+markers",
                                name = "Clearing Beads",
                                legendgroup = "Phase 7",
                                legendgrouptitle_text = "Phase 7"
                                ),
                        row = 4,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P7_3"],
                                mode = "lines+markers",
                                name = "Place Value",
                                legendgroup = "Phase 7",
                                legendgrouptitle_text = "Phase 7"
                                ),
                        row = 4,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P7_4"],
                                mode = "lines+markers",
                                name = "Vocabulary",
                                legendgroup = "Phase 7",
                                legendgrouptitle_text = "Phase 7"
                                ),
                        row = 4,
                        col = 1
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P8_1"],
                                mode = "lines+markers",
                                name = "Setting Numbers",
                                legendgroup = "Phase 8",
                                legendgrouptitle_text = "Phase 8"
                                ),
                        row = 4,
                        col = 2
                        )
                fig.add_trace(
                        go.Scatter(
                                x = df_noisy.index, y = df_noisy["P8_2"],
                                mode = "lines+markers",
                                name = "Clearing Beads",
                                legendgroup = "Phase 8",
                                legendgrouptitle_text = "Phase 8"
                                ),
                        row = 4,
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
                        row = 2,
                        col = 2
                        )
                fig.add_hrect(
                        y0 = .5,
                        y1 = 1.5,
                        line_width = 0,
                        fillcolor = "orange",
                        opacity = 0.2,
                        row = 2,
                        col = 2
                        )
                fig.add_hrect(
                        y0 = 1.5,
                        y1 = 2.5,
                        line_width = 0,
                        fillcolor = "yellow",
                        opacity = 0.2,
                        row = 2,
                        col = 2
                        )
                fig.add_hrect(
                        y0 = 2.5,
                        y1 = 3.5,
                        line_width = 0,
                        fillcolor = "green",
                        opacity = 0.2,
                        row = 2,
                        col = 2
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
                        row = 4,
                        col = 1
                        )
                fig.add_hrect(
                        y0 = .5,
                        y1 = 1.5,
                        line_width = 0,
                        fillcolor = "orange",
                        opacity = 0.2,
                        row = 4,
                        col = 1
                        )
                fig.add_hrect(
                        y0 = 1.5,
                        y1 = 2.5,
                        line_width = 0,
                        fillcolor = "yellow",
                        opacity = 0.2,
                        row = 4,
                        col = 1
                        )
                fig.add_hrect(
                        y0 = 2.5,
                        y1 = 3.5,
                        line_width = 0,
                        fillcolor = "green",
                        opacity = 0.2,
                        row = 4,
                        col = 1
                        )
                fig.add_hrect(
                        y0 = -.5,
                        y1 = .5,
                        line_width = 0,
                        fillcolor = "red",
                        opacity = 0.2,
                        row = 4,
                        col = 2
                        )
                fig.add_hrect(
                        y0 = .5,
                        y1 = 1.5,
                        line_width = 0,
                        fillcolor = "orange",
                        opacity = 0.2,
                        row = 4,
                        col = 2
                        )
                fig.add_hrect(
                        y0 = 1.5,
                        y1 = 2.5,
                        line_width = 0,
                        fillcolor = "yellow",
                        opacity = 0.2,
                        row = 4,
                        col = 2
                        )
                fig.add_hrect(
                        y0 = 2.5,
                        y1 = 3.5,
                        line_width = 0,
                        fillcolor = "green",
                        opacity = 0.2,
                        row = 4,
                        col = 2
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 1,
                        col = 1
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 1,
                        col = 2
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 2,
                        col = 1
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 2,
                        col = 2
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 3,
                        col = 1
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 3,
                        col = 2
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 4,
                        col = 1
                        )
                fig.update_xaxes(
                        rangebreaks = [dict(bounds = ["sat", "mon"]), dict(values = [])],
                        row = 4,
                        col = 2
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
                        row = 1,
                        col = 2
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
                        row = 2,
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
                        row = 4,
                        col = 1
                        )
                fig.update_yaxes(
                        range = [-.5, 3.5], fixedrange = True,
                        ticktext = ["Unable", "Prompted", "Hesitated",
                                    "Independent"],
                        tickvals = [0.1, 1, 2, 3],
                        row = 4,
                        col = 2
                        )
                fig.update_layout(
                template = "simple_white",
                title_text = f"{studentname}: Abacus Skills Progression"
                )

                tmppath = Path(USER_DIR).joinpath(
                            'StudentDatabase',
                            'StudentDataFiles', studentname,
                            'ScreenReaderSkillsProgression.html'
                            )
                fig.write_html(tmppath)
                fig.show()
            # ABACUS SKILLS PROGRESSION TAB
            with ui.row().classes('w-full no-wrap'):
                ui.label('ABACUS SKILLS PROGRESSION').classes('justify-center items-center')
            with ui.row().classes('w-full no-wrap py-4'):
                ui.select(options=students, with_input=True, on_change=lambda e: ui.notify(e.value)).bind_value(u_studentname, 'value').classes('w-1/4').props('aria-label="Select Student from the Dropdown. It will autocomplete as you type"').tooltip("Select Student from the Dropdown. It will autocomplete as you type")
                with ui.input('Date') as date:
                    with date.add_slot('append'):
                        ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                        with ui.menu() as menu:
                            ui.date().bind_value(date)
            with ui.row().classes('w-full no-wrap py-4 justify-center items-center'):   
                ui.label('RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent').props('aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center').tooltip("RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent")
            with ui.row().classes('w-full no-wrap py4 justify-center items-center'):
                ui.label('PHASE 1: ').classes('justify-center items-center')
                ui.number(label="1.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="1.1 Setting Numbers"')
                ui.number(label="1.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="1.2 Clearing Numbers"')
                ui.number(label="1.3", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="1.3 Place Value"')
                ui.number(label="1.4", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="1.4 Vocabulary"')
                
                ui.number(label="2.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="2.1 Addition of Single Digit Numbers"')
                ui.number(label="2.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="2.2 Addition of Multiple Digit Numbers – Direct"')
                ui.number(label="2.3", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="2.3 Addition of Multiple Digit Numbers – Indirect"')
                ui.number(label="3.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="3.1 Subtraction"')
                ui.number(label="3.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="3.2 Subtraction of Multiple Digit Numbers – Direct"')
                ui.number(label="3.3", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="3.3 Subtraction of Multiple Digit Numbers – Indirect"')
                ui.number(label="4.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="4.1 Multiplication – 2+ Digit Multiplicand 1-Digit Multiplier"')
                ui.number(label="4.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="4.2 Multiplication – 2+ Digit Multiplicand AND Multiplier"')
                ui.number(label="5.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="5.1 Division – 2+ Digit Dividend 1-Digit Divisor"')
                ui.number(label="5.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="5.2 Division – 2+ Digit Dividend AND 1 Digit Divisor"')
                ui.number(label="6.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="6.1 Addition of Decimals"')
                ui.number(label="6.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="6.2 Subtraction of Decimals"')
                ui.number(label="6.3", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="6.3 Multiplication of Decimals"')
                ui.number(label="6.4", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="6.4 Division of Decimals"')
                ui.number(label="7.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="7.1 Addition of Fractions"')
                ui.number(label="7.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="7.2 Subtraction of Fractions"')
                ui.number(label="7.3", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="7.3 Multiplication of Fractions"')
                ui.number(label="7.4", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="7.4 Division of Fractions"')
                ui.number(label="8.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="8.1 Percent"')
                ui.number(label="8.2", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="8.2 Square Root"')
            with ui.row().classes('w-full no-wrap py-4'):
                ui.button('SAVE', on_click=save)
                ui.button('GRAPH', on_click=graph)
                ui.button('EXIT', on_click=app.shutdown)   
                    
                # SCREENREADER SKILLS PROGRESSION TAB
                with ui.row().classes('w-full no-wrap'):
                        ui.label('SCREENREADER SKILLS PROGRESSION').classes('justify-center items-center')
                with ui.row().classes('w-full no-wrap py-4'):
                        ui.select(options=students, with_input=True, on_change=lambda e: ui.notify(e.value)).bind_value(u_studentname, 'value').classes('w-1/4').props('aria-label="Select Student from the Dropdown. It will autocomplete as you type"').tooltip("Select Student from the Dropdown. It will autocomplete as you type")
                        with ui.input('Date') as date:
                                        with date.add_slot('append'):
                                                ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
                                        with ui.menu() as menu:
                                                ui.date().bind_value(date)
                with ui.row().classes('w-full no-wrap py-4 justify-center items-center'):   
                        ui.label('RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent').props('aria-label="RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent" content-center').tooltip("RUBRIC: 0=No attempt 1=Required Assistance 2=Hesitated 3=Independent")
                with ui.row().classes('w-full no-wrap py4 justify-center items-center'):
                        ui.label('PHASE 1: READING').classes('justify-center items-center')
                with ui.row().classes('w-full no-wrap py-4'):      
                        ui.number(label="1.1", value="", on_change=lambda e: u_trial11.set_value(e.value)).classes('w-1/7').props('aria-label="1.1 Turn on and off the screen reader"').tooltip("1.1 Turn on and off the screen reader")
                        ui.number(label="1.2", value="", on_change=lambda e: u_trial12.set_value(e.value)).classes('w-1/7').props('aria-label="1.2 Utilize modifier keys such as ctrl alt and shift"').tooltip("1.2 Utilize modifier keys such as ctrl alt and shift")
                        ui.number(label="1.3", value="", on_change=lambda e: u_trial13.set_value(e.value)).classes('w-1/7').props('aria-label="1.3 Read text using a variety of reading commands"').tooltip("1.3 Read text using a variety of reading commands")
                        ui.number(label="1.4", value="", on_change=lambda e: u_trial14.set_value(e.value)).classes('w-1/7').props('aria-label="1.4 Identify the titles and section titles of documents with Headings"').tooltip("1.4 Identify the titles and section titles of documents with Headings")
                        ui.number(label='1.5', value="", on_change=lambda e: u_trial15.set_value(e.value)).classes('w-1/7').props('aria-label="1.5 Access documents open and close programs  navigate to the  desktop"').tooltip("1.5 Access documents open and close programs  navigate to the  desktop")
                        ui.number(label='1.6', value="", on_change=lambda e: u_trial16.set_value(e.value)).classes('w-1/7').props('aria-label="1.6 Switch Program Focus"').tooltip("1.6 Switch Program Focus")
                        ui.label(' ').classes('w-1/7')
                with ui.row().classes('w-full no-wrap py-4 justify-center items-center'):
                        ui.label('PHASE 2: WRITING').classes('justify-center items-center')
                with ui.row().classes('w-full no-wrap py-4'): 
                        ui.number(label="2.1", value="", on_change=lambda e: u_trial21.set_value(e.value)).classes('w-1/7').props('aria-label="2.1 Type with all alphanumeric keys on the keyboard."').tooltip("2.1 Type with all alphanumeric keys on the keyboard.")
                        ui.number(label="2.2", value="", on_change=lambda e: u_trial22.set_value(e.value)).classes('w-1/7').props('aria-label="2.2 Navigate to and change screen reader settings"').tooltip("2.2 Navigate to and change screen reader settings")
                        ui.number(label="2.3", value="", on_change=lambda e: u_trial23.set_value(e.value)).classes('w-1/7').props('aria-label="2.3 Write and edit documents using a basic understanding of cursor placement"').tooltip("2.3 Write and edit documents using a basic understanding of cursor placement")
                        ui.number(label="2.4", value="", on_change=lambda e: u_trial24.set_value(e.value)).classes('w-1/7').props('aria-label="2.4. Select copy and paste text"').tooltip("2.4. Select copy and paste text")
                        ui.label(' ').classes('w-1/7')
                        ui.label(' ').classes('w-1/7')
                        ui.label(' ').classes('w-1/7')            
                with ui.row().classes('w-full no-wrap py-4 justify-center items-center'):
                        ui.label('PHASE 3: USING THE INTERNET').classes('justify-center items-center')
                with ui.row().classes('w-full no-wrap py-4'):       
                        ui.number(label="3.1", value="", on_change=lambda e: u_trial31.set_value(e.value)).classes('w-1/7').props('aria-label="3.1 Define common element types on the internet such as Headings Buttons"').tooltip("3.1 Define common element types on the internet such as Headings Buttons")
                        ui.number(label="3.2", value="", on_change=lambda e: u_trial32.set_value(e.value)).classes('w-1/7').props('aria-label="3.2 identify each element by type."').tooltip("3.2 identify each element by type.")
                        ui.number(label="3.3", value="", on_change=lambda e: u_trial33.set_value(e.value)).classes('w-1/7').props('aria-label="3.3 navigate to the address bar"').tooltip("3.3 navigate to the address bar")
                        ui.number(label="3.4", value="", on_change=lambda e: u_trial34.set_value(e.value)).classes('w-1/7').props('aria-label="3.4 Use the “Tab” key to navigate to the next clickable object"').tooltip("3.4 Use the “Tab” key to navigate to the next clickable object")
                        ui.number(label="3.5", value="", on_change=lambda e: u_trial35.set_value(e.value)).classes('w-1/7').props('aira-label="3.5 Navigate by “Quick Keys” (h for heading b for button and u for link"').tooltip("3.5 Navigate by “Quick Keys” (h for heading b for button and u for link")
                        ui.number(label="3.6", value="", on_change=lambda e: u_trial36.set_value(e.value)).classes('w-1/7').props('aria-label="3.6 Use Elements Lists on a website to navigate by element type"').tooltip("3.6 Use Elements Lists on a website to navigate by element type")             
                        ui.number(label="3.7", value="", on_change=lambda e: u_trial37.set_value(e.value)).classes('w-1/7').props('aria-label="3.7 Justify why he/she/they selected a particular method for the situation"').tooltip("3.7 Justify why he/she/they selected a particular method for the situation")
                with ui.row().classes('w-full no-wrap py-4'):
                        ui.number(label="3.8", value="", on_change=lambda e: u_trial38.set_value(e.value)).classes('w-1/7').props('aria-label="3.8 Switch tab focus"').tooltip("3.8 Switch tab focus")
                        ui.number(label="3.9", value="", on_change=lambda e: u_trial39.set_value(e.value)).classes('w-1/7').props('aria-label="3.9 Switch between screen reader modes"').tooltip("3.9 Switch between screen reader modes")
                        ui.number(label="3.10", value="", on_change=lambda e: u_trial310.set_value(e.value)).classes('w-1/7').props('aria-label="3.10 Navigate a table"').tooltip("3.10 Navigate a table")
                        ui.number(label="3.11", value="", on_change=lambda e: u_trial311.set_value(e.value)).classes('w-1/7').props('aria-label="3.11 Develop a navigation sequence to access an unfamiliar website"').tooltip("3.11 Develop a navigation sequence to access an unfamiliar website")
                        ui.label(' ').classes('w-1/7')
                        ui.label(' ').classes('w-1/7')
                        ui.label(' ').classes('w-1/7')
                with ui.row().classes('w-full no-wrap py-4 justify-center items-center'): 
                        ui.label('PHASE 4: NAVIGATING AND FILE MANAGEMENT').classes('justify-center items-center')
                with ui.row().classes('w-full no-wrap py-4'):
                        ui.number(label="4.1", value="", on_change=lambda e: u_trial41.set_value(e.value)).classes('w-1/7').props('aria-label="4.1 Be able to save and open files using File Explorer."').tooltip("4.1 Be able to save and open files using File Explorer.")
                        ui.number(label="4.2", value="", on_change=lambda e: u_trial42.set_value(e.value)).classes('w-1/7').props('aria-label="4.2 Create folders and move files in File Explorer"').tooltip("4.2 Create folders and move files in File Explorer")
                        ui.number(label="4.3", value="", on_change=lambda e: u_trial43.set_value(e.value)).classes('w-1/7').props('aria-label="4.3 Navigate a cloud-based file management system (eg: Google Drive)"').tooltip("4.3 Navigate a cloud-based file management system (eg: Google Drive)")
                        ui.number(label="4.4", value="", on_change=lambda e: u_trial44.set_value(e.value)).classes('w-1/7').props('aria-label="4.4 Download and save material from the internet"').tooltip("4.4 Download and save material from the internet")
                        ui.number(label="4.5", value="", on_change=lambda e: u_trial45.set_value(e.value)).classes('w-1/7').props('aria-label="4.5 Extract zipped folders"').tooltip("4.5 Extract zipped folders")
                        ui.number(label="4.6", value="", on_change=lambda e: u_trial46.set_value(e.value)).classes('w-1/7').props('aria-label="4.6 Utilize the virtual cursor and mouse keys"').tooltip("4.6 Utilize the virtual cursor and mouse keys")
                        ui.number(label="4.7", value="", on_change=lambda e: u_trial47.set_value(e.value)).classes('w-1/7').props('aria-label="4.7 To use OCR features to read inaccessible material"').tooltip("4.7 To use OCR features to read inaccessible material")
                with ui.row().classes('w-full no-wrap py-4'):
                        ui.button('SAVE', on_click=save)
                        ui.button('GRAPH', on_click=graph)
                        ui.button('EXIT', on_click=app.shutdown)   

with ui.footer(value=False) as footer:
        ui.label('Footer')
with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        ui.label('Side menu')
with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle).props('fab icon=contact_support')
ui.run(native=True, reload=False, dark=None, title='Screen Reader Skills Progression', fullscreen=False, window_size=(1550,1500))
