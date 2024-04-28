import unittest
import os
from pathlib import Path
from appHelpers.helpers import (
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
        working_dir()
        self.assertTrue(Path(os.getcwd()).joinpath("workingdirectory.py").exists())

    def test_create_roster(self):
        create_roster()
        self.assertTrue(Path(os.getcwd()).joinpath("appHelpers", "roster.py").exists())

    def test_createFolderHierarchy(self):
        createFolderHierarchy()
        # Test for a specific student, replace 'StudentName' with a real student name from your students list
        student_dir = Path(os.getcwd()).joinpath(
            "StudentDatabase", "StudentDataFiles", "StudentName"
        )
        self.assertTrue(student_dir.exists())
        self.assertTrue(student_dir.joinpath("StudentDataSheets").exists())
        self.assertTrue(student_dir.joinpath("StudentInstructionMaterials").exists())
        self.assertTrue(student_dir.joinpath("StudentVisionAssessments").exists())
        self.assertTrue(student_dir.joinpath("omnibusDatabase.csv").exists())
        self.assertTrue(student_dir.joinpath("BrailleSkillsProgression.csv").exists())


if __name__ == "__main__":
    unittest.main()
