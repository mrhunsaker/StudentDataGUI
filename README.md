# StudentDataGUI

Student Data Input GUI using NiceGUI and SQLite designed be platform-independent.

To use this package open *helpers.py* and edit the names for the *students* variable, following the pattern of surrounding text with single quotes (' ') and separating entries with commas.

ex:

```txt
students = ('DonaldChamberlain', 'StudentOne', 'StudentTwo', 'StudentN')   
```

I recommend leaving the first entry as it is, unless of course you have a student with that name. It is just a cheeky reference to one of the inventors of SQL and a fake student I can use to test settings without accidentally inserting data into a database that I later would have to remove.

This is designed to be used by Teachers for Students with Visual Impairments, and any Tasks, Domains, and Lessons can be edited as you desire. Just do not change any variable names without editing the 'main.py' file accordingly

At present, all file paths use pathlib and check your system in order to be OS-agnostic

This program will create a *StudentDatabase* folder in your *~/Documents* folder for a SQLite database file and resulting data. It will create folders for each student and populate each of these folders with all necessary files. I have also added the
ability for you to import files into each student folder as desired.

Here is the tree view of this file structure:

```bash
 HOME/Documents
 +---StudentDatabase
   +-- errorLogs
   +-- StudentDataFiles
   ¦   +--Filenames.txt
   ¦   +--Student 1
   ¦   ¦   +-- AbacusSkillsProgression.csv
   ¦   ¦   +-- AbacusSkillsProgression.html
   ¦   ¦   +-- BrailleSkillsProgression.csv
   ¦   ¦   +-- cviProgression.csv
   ¦   ¦   +-- cviProgression.html
   ¦   ¦   +-- omnibusDatabase.csv
   ¦   ¦   +-- ScreenReaderSkillsProgression.csv
   ¦   ¦   +-- ScreenReaderSkillsProgression.html
   ¦   ¦   +-- StudentDataSheets
   ¦   ¦   +-- BlankVisionTemplate.pdf
   ¦   ¦   +-- GenericDataSheets.pdf
   ¦   ¦   +-- ProgressMonitoring.pdf
   ¦   ¦   +-- StudentInstructionMaterials
   ¦   ¦   +-- StudentVisionAssessments
   ¦   ¦   +-- EducationVisionAssessments.pdf
   ¦   ¦   +-- UEBLiterarySkillsProgression.html
   ¦   ¦   +-- UEBTechnicalSkillsProgression.html
  ...  ...
   ¦   +-- Student n
   ¦   ¦   +-- AbacusSkillsProgression.csv
   ¦   ¦   +-- AbacusSkillsProgression.html
   ¦   ¦   +-- BrailleSkillsProgression.csv
   ¦   ¦   +-- cviProgression.csv
   ¦   ¦   +-- cviProgression.html
   ¦   ¦   +-- omnibusDatabase.csv
   ¦   ¦   +-- ScreenReaderSkillsProgression.csv
   ¦   ¦   +-- ScreenReaderSkillsProgression.html
   ¦   ¦   +-- StudentDataSheets
   ¦   ¦   +-- BlankVisionTemplate.pdf
   ¦   ¦   +-- GenericDataSheets.pdf
   ¦   ¦   +-- ProgressMonitoring.pdf
   ¦   ¦   +-- StudentInstructionMaterials
   ¦   ¦   +-- StudentVisionAssessments
   ¦   ¦   +-- EducationVisionAssessments.pdf
   ¦   ¦   +-- UEBLiterarySkillsProgression.html
   ¦   ¦   +-- UEBTechnicalSkillsProgression.html
   students.db
```

## Set up the Program

I set up and run this program using Poetry on Python3.11 because it allows me to keep my system python3 installation streamlined and allows me to install everything with precision on multiple computers, but I am including a requirements.txt file as well for those who just want to install required modules globally.

By preference, I install either [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to manage multiple python3 installations.

### To Use Poetry

#### Install Poetry

```bash
$ python3 -m pip install --user poetry
```

Enter the project repository and set up the virtual environment using the information in pyproject.toml 

```bash
$ poetry env 3.10.11
$ poetry install
```

#### To run program

```bash
$ cd </path/to/project>
$ poetry run python main.py # poetry run python3 main.py for *nix systems
```
