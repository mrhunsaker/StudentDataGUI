# StudentDataGUI

*Student Data Input GUI using NiceGUI and SQLite*

To use this package, first go to you Documents folder, create a text file names *roster.txt* and type in the names of your students using the below formatting. 


```txt
students = (
        'DonaldChamberlain',
        'StudentOne',
        'StudentTwo',
        'StudentThree'
        )   
```

I recommend leaving the first entry as it is, unless of course you have a student with that name. It is just a cheeky reference to one of the inventors of SQL and a fake student I can use to test settings without
accidentally inserting data into a database that I later would have to remove.

At present, all file paths use pathlib and check your system in order to be OS-agnostic

This program will create a *StudentDatabase* folder in your *~/Documents* folder for a SQLite database file and resulting data. It will create folders for each student and populate each of these folders with all
necessary files. I have also added the ability for you to import files into each student folder as desired.

## Set up the Program

I set up and run this program using Poetry because it allows me to keep my system python3 installation streamlined and allows me to install everything with precision on multiple computers, but I am including a
requirements.txt file as well for those who just want to install required modules globally.

### To Use Poetry

#### Install Poetry

(Linux or Mac)
```bash
$ python3 -m pip install --user poetry
```
(Windows)
```powershell
$ python -m pip install --user poetry
```

Enter the project repository and set up the virtual environment using the information in pyproject.toml. At present, due to some required modules, Python 3,8-3.10 are supported. 

```bash
$ cd </path/to/project>
$ poetry env use 3.10
```

#### To run program

(Linux and Mac OS)
```bash
$ cd </path/to/project>
$ poetry run python3 ./main.py
```
(Windows)
```powershell
$ cd <path\to\project>
$ poetry run python .\main.py
```