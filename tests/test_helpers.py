import unittest
import os
from pathlib import Path
from StudentDataGUI.appHelpers.helpers import (
    set_start_dir,
    working_dir,
    create_roster,
    createFolderHierarchy,
)


class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.original_dir = os.getcwd()

    def tearDown(self):
        os.chdir(self.original_dir)

    def test_set_start_dir(self):
        start_dir = set_start_dir()
        self.assertIsInstance(start_dir, Path)
        self.assertTrue(start_dir.exists())

    def test_working_dir(self):

        # Call working_dir which should set CWD to the project's app_home and create StudentDataFiles
        working_dir()
        cwd = Path(os.getcwd())
        # StudentDataFiles should exist under the working directory
        self.assertTrue(cwd.joinpath("StudentDataFiles").exists())

    def test_create_roster(self):
        create_roster()
        self.assertTrue(Path(os.getcwd()).joinpath("appHelpers", "roster.py").exists())

    def test_createFolderHierarchy(self):
        createFolderHierarchy()
        # Pick any created student folder under StudentDataFiles to validate structure
        # The application stores data under the project's app_home; use set_start_dir()
        base = set_start_dir().joinpath("StudentDatabase", "StudentDataFiles")
        self.assertTrue(base.exists())
        # find any student directory
        student_dirs = [p for p in base.iterdir() if p.is_dir()]
        self.assertTrue(len(student_dirs) > 0, "No student directories were created")
        student_dir = student_dirs[0]
        self.assertTrue(student_dir.exists())
        self.assertTrue(student_dir.joinpath("StudentDataSheets").exists())
        self.assertTrue(student_dir.joinpath("StudentInstructionMaterials").exists())
        self.assertTrue(student_dir.joinpath("StudentVisionAssessments").exists())
        self.assertTrue(student_dir.joinpath("omnibusDatabase.csv").exists())
        self.assertTrue(student_dir.joinpath("BrailleSkillsProgression.csv").exists())


if __name__ == "__main__":
    unittest.main()
