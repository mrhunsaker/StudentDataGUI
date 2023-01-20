# StudentDataGUI

Student Data Input GUI designed in wxPython and sqlite

To use this package open 'helpers.py' and edit the names for the **students_all** variable, following the pattern of surrounding text with single quotes (' ') and separating entries with commas.

This is designed to be used by Teachers for Students with Visual Impairments, and any Tasks, Domains, and Lessons can be edited as you desire. Just do not change any variable names without editing the 'main.py' file
accordingly

At present, all file paths use pathlib to be OS-agnostic

This program will create a StudentDatabase folder in you ./Documents folder for a sqlite database file and resulting data. 
