# StudentDataGUI

Student Data Input GUI designed in wxPython and sqlite3

To use this package open 'helpers.py' and edit the names for the **students** variable, following the pattern of surrounding text with single quotes (' ') and separating entries with commas. 

I recommend leaving the first entry as it is, unless of course you have a student with that name. It is just a cheeky reference to one of the inventors of SQL and a faux student I can use to test settings without accidentally inserting data into a database that I later would have to remove.

This is designed to be used by Teachers for Students with Visual Impairments, and any Tasks, Domains, and Lessons can be edited as you desire. Just do not change any variable names without editing the 'main.py' file
accordingly

At present, all file paths use pathlib and check your system in order to be OS-agnostic

This program will create a StudentDatabase folder in you ./Documents folder for a sqlite database file and resulting data. It will student folders and populate the folders with the necessary files. I have also added the ability to import files as desired. 
