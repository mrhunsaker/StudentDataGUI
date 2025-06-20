# StudentDataGUI

Student Data Input GUI using NiceGUI and SQLite3 designed be platform-independent.

To use this package, first create a file called "roster.txt" in your ~/Documents on linux/MacOS or %userprofile%\Documents in Windows. Add student names following the pattern below. Surround text with single quotes (' ') and separating entries with commas. The program will use this file to create a roster.py file in the correct location and use these student names.

I recommend leaving the first entry as it is, unless of course you have a student with that name. It is just a cheeky reference to one of the inventors of SQL and a fake student I can use to test settings without accidentally inserting data into a database that I later would have to remove.

If you need to add students, you can alter the roster.py file in the program directory inside the appHelpers folder. 

```txt
students = [
    'DonaldChamberlain',
    'StudentOne', 
    'StudentTwo', 
    'StudentN'
]
```

Also create a file called "workingdirectory" in the same ~/Documents (/home/<username>/Documents) on linux/MacOS or %userprofile%\Documents in windows. 

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


At present, all file paths use pathlib and check your system in order to be OS-agnostic

This program will create a */StudentDatabase* folder in your *<path - to - folder>/Documents* folder for a SQLite3 database file and resulting data. It will create folders for each student and populate each of these folders with all necessary files. I have also added the
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

I this program using Poetry on Python 3.12 because it allows me to keep my system python installation streamlined and allows me to install everything with precision across multiple computers. 

I include a requirements.txt file as well for those who just want to install required modules globally. This requirements.txt file will work with the more traditional virtualenv or pipenv pipelines.

By preference, I install either [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to manage multiple python versions and virtual environments. 

### How to set up project using Poetry

#### Install Poetry

Linux/MacOS
```bash
python3 -m pip install --user poetry
```

Windows
```bash
python -m pip install --user poetry
```

Enter the project repository and set up the virtual environment using the information in pyproject.toml. The program currenty works with python 3.10-3.12

```bash
poetry env 3.12
poetry update
```

This will create a poetry.lock file in the folder.

## Clone the project 

Point your terminal to the folder you want to store the source code for the program in (I use a GithubRepos/ folder inside my home folder)

```bash
cd ~/GitHubRepos # cd ~\GitHubRepos on Windows
git clone https://github.com/mrhunsaker/StudentDataGUI 
git pull #to update
```
This makes a folder named StudentDataGUI inside the GitHubRepos folder 

#### To run program

```bash
cd </path/to/project> # cd ~/GitHubRepos/StudentDataGUI on my WIidows system
poetry run python main.py # poetry run python3 main.py for *nix systems
```

### How to set up project using Pipenv

#### Install Pipenv

Linux/MacOS
```bash
python3 -m pip install --user pipenv
```

Windows
```bash
python -m pip install --user pipenv
```

Enter the project repository and set up the virtual environment using the information inrequirements.txt. The program currenty works with python3 versions 3.10-3.12

```bash
pipenv --python 3.12
pipenv install ./requirements.txt
```

This will create a Pipfile and Pipfile.lock 

## Clone the project 

Point your terminal to the folder you want to store the source code for the program in (I use a GithubRepos/ folder inside my home folder)

```bash
cd ~/GitHubRepos # cd ~\GitHubRepos on Windows
git clone https://github.com/mrhunsaker/StudentDataGUI 
git pull #to update
```


if you want to do any development, then fork the repository by checking out a branch
```bash
# To checkout a branch after having cloned the repository
cd ~/GitHubRepos/StudentDataGUI
git checkout -b my_branch 
# To checkout a new branch when initially cloning the repository
git clone -b my_branch https://github.com/mrhunsaker/StudentDataGUI 
```

This makes a folder named StudentDataGUI inside the GitHubRepos folder 

#### To run program

```bash
cd </path/to/project> # cd ~/GitHubRepos/StudentDataGUI on my WIidows system
poetry run python main.py # poetry run python3 main.py for *nix systems
```

## Development

### Getting Started
1. Fork the repository on GitHub.

2. Clone your fork locally:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
3. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature-or-bugfix-branch
```
4. Make your changes and test thoroughly.

### Submitting Changes
1. Commit your changes:

```bash
git commit -m "Your descriptive commit message"
```
2. Push to your fork:

```bash
git push origin feature-or-bugfix-branch
```
3. Submit a pull request:
    - Go to the Pull Requests tab on GitHub.
    - Click the "New Pull Request" button.
    - Select the branch with your changes.
4. Describe your changes in detail, providing context and reasons for the changes.

#### Code Style
I try my best to follow the styles enforced by the [Black](https://black.readthedocs.io/en/stable/) code formatter [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black).  Please do your best to follow our coding style guidelines to maintain consistency across the project.

### Reporting Issues
If you encounter any issues or have suggestions, please [open an issue on GitHub](https://github.com/mrhunsaker/StudentDataGUI/issues). Provide as much detail as possible, including your operating system and relevant configuration.

### Development Workflow
- Before starting to work on an issue, make sure it's not already assigned or being worked on.
- If you plan major changes, it's a good idea to open an issue for discussion first.

### Code of Conduct
Everyone participating in the Black project, and in particular in the issue tracker, pull requests, and social media activity, is expected to treat other people with respect and more generally to follow the guidelines articulated in the [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

---

# Container Support

This project provides both Docker and Podman support with dedicated Dockerfiles optimized for each container runtime.

## Docker vs Podman

- **Docker**: Uses `Dockerfile` with traditional root-based container setup
- **Podman**: Uses `Dockerfile.podman` optimized for rootless containers with virtual environment isolation

## Quick Start

### Create local directories first
```bash
mkdir -p ~/Documents/StudentDatabase/StudentDataFiles
mkdir -p ~/Documents/StudentDatabase/errorLogs
mkdir -p ~/Documents/StudentDatabase/backups
chmod -R 755 ~/Documents/StudentDatabase
```

### For Docker users:
```bash
# Build the image
docker build -f Dockerfile -t student-data-app .

# Run the container
docker run -d \
  --name student-data \
  -p 8080:8080 \
  -v ~/Documents/StudentDatabase:/app/data \
  student-data-app
```

### For Podman users:
```bash
# Build the image
podman build -f Dockerfile.podman -t student-data-app .

# Run the container
podman run -d \
  --name student-data \
  -p 8080:8080 \
  -v ~/Documents/StudentDatabase:/app/data:Z \
  student-data-app
```

## Using Docker Compose

### For Docker:
```bash
docker-compose up -d
```

### For Podman:
```bash
podman-compose up -d
```

## Container Features

- **Ubuntu 24.04** base image with Python 3.12
- **Updated GObject Introspection** support (girepository-2.0)
- **Rootless-friendly** Podman configuration
- **Health checks** for container monitoring
- **Persistent data** storage via volume mounts

## Data Directory Structure

The mounted volume will contain:
```
~/Documents/StudentDatabase/
  ├── StudentDataFiles/
  ├── errorLogs/
  ├── backups/
  └── students.db
```

## Access the Application

Once running, open your browser and navigate to:
```
http://localhost:8080
```

