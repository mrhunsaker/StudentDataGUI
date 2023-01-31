# StudentDataGUI

*Student Data Input GUI using wxPython and SQLite*

To use this package open *helpers.py* and edit the names for the *students* variable, following the pattern of surrounding text with single quotes (' ') and separating entries with commas.

ex:

```python
students = (
        'DonaldChamberlain',
        'StudentOne',
        'StudentTwo',
        'StudentThree'
        )   
```

I recommend leaving the first entry as it is, unless of course you have a student with that name. It is just a cheeky reference to one of the inventors of SQL and a fake student I can use to test settings without
accidentally inserting data into a database that I later would have to remove.

This is designed to be used by Teachers for Students with Visual Impairments, and any Tasks, Domains, and Lessons can be edited as you desire. Just do not change any variable names without editing the 'main.py' file
accordingly

At present, all file paths use pathlib and check your system in order to be OS-agnostic

This program will create a *StudentDatabase* folder in your *~/Documents* folder for a SQLite database file and resulting data. It will create folders for each student and populate each of these folders with all
necessary files. I have also added the ability for you to import files into each student folder as desired.

## Set up the Program

I set up and run this program using pipenv because it allows me to keep my system python3 installation streamlined and allows me to install everything with precision on multiple computers, but I am including a
requirements.txt file as well for those who just want to install required modules globally.

### To Use pipenv

#### Install Pipenv

```bash
$ python3 -m pip install --user pipenv
```

Enter the project repository and install from Pipfile and Pipfile.lock

```bash
$ cd </path/to/project>
$ pipenv install
```

It will create the virtual environment and install all modules and necessary dependencies

#### To run program

```bash
$ cd </path/to/project>
$ pipenv run python3 main.py
```
