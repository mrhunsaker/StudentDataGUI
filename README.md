# StudentDataGUI

Student Data Input GUI using NiceGUI and SQLite designed be platform-independent.

To use this package, first create a file called "roster.txt" in your ~/Documents on linux/MacOS or %userprofile%\Documents in Windows Add student names following the pattern of surrounding text with single quotes (' ') and separating entries with commas. The program will use this file to create a roster.py file in the correct location and use these student names.
ex:

```txt
students = [
    'DonaldChamberlain',
    'StudentOne', 
    'StudentTwo', 
    'StudentN'
]
```

Also create a file called "workingdirectory" in your ~/Documents (/home/<username>/Documents) on linux/MacOS or %userprofile%\Documents in windows. 

Copy the following code into the file, changing <path - to - folder> to where you want to store the documents created by this program. The program will place files in <path - to - folder> in a Documents folder. So if you want to place it in the ~/Documents folder the <path - to -folder> would be "/home/<username>"
```txt
    if os.name == "nt":
        try:
            tmp_path = Path(os.environ["USERPROFILE"]).joinpath(
                "<path - to - folder>", "Documents"
            )
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            USER_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find %USERPROFILE")
    elif os.name == "posix":
        try:
            tmp_path = Path(os.environ["HOME"]).joinpath(
                "OneDrive - Davis School District", "Documents"
            )
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            USER_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find $HOME")
    return USER_DIR

```

I recommend leaving the first entry as it is, unless of course you have a student with that name. It is just a cheeky reference to one of the inventors of SQL and a fake student I can use to test settings without accidentally inserting data into a database that I later would have to remove.

If you need to add students, you can alter the roster.py file in the program directory inside the appHelpers folder. 

At present, all file paths use pathlib and check your system in order to be OS-agnostic

This program will create a *StudentDatabase* folder in your *~/Documents* folder for a SQLite database file and resulting data. It will create folders for each student and populate each of these folders with all necessary files. I have also added the
ability for you to import files into each student folder as desired.

Here is the tree view of this file structure:

```bash
 <path - to -folder>/Documents # or <path - to -folder>\Documents on Windows
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

I set up and run this program using Poetry on Python3.12 because it allows me to keep my system python3 installation streamlined and allows me to install everything with precision on multiple computers, but I am including a requirements.txt file as well for those who just want to install required modules globally.

By preference, I install either [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to manage multiple python/python3 installations.

### To Use Poetry

#### Install Poetry

```bash
$ python3 -m pip install --user poetry
```

Enter the project repository and set up the virtual environment using the information in pyproject.toml. The program currenty works with python 3.10-3.12

```bash
$ poetry env 3.12
$ poetry update
```

## Clone the project 

Point your terminal to the folder you want to store the source code for the program in (I use a GithubRepos/ folder inside my home folder)

```bash
$ cd ~/GitHubRepos # cd ~\GitHubRepos on Windows
$ git clone https://github.com/mrhunsaker/StudentDataGUI 
```

This makes a folder named StudentDataGUI inside the GitHubRepos folder (I use %userprofile%/GitHubRepos/StudentDataGUI)

#### To run program

```bash
$ cd </path/to/project> # cd ~/GitHubRepos/StudentDataGUI on my WIndows system
$ poetry run python main.py # poetry run python3 main.py for *nix systems
```

