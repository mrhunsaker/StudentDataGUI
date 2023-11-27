# FILEPATH: /c:/Users/RYHUNSAKER/GitHubRepos/StudentDataGUI/tests/test_braillenote.py

import unittest
import json
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
from appPages.braillenote import save

class Testbraillenote(unittest.TestCase):
    def setUp(self):
        # Mocking the UI elements
        self.u_studentname = MagicMock()
        self.u_today_date = MagicMock()
        self.u_braillenote_trial11 = MagicMock()
        # ... repeat for all the other UI elements

    @patch('appPages.braillenote.datetime')
    @patch('appPages.braillenote.Path')
    @patch('appPages.braillenote.json')
    def test_save(self, mock_json, mock_path, mock_datetime):
        # Setting up the mock values
        self.u_studentname.value = "TestStudent"
        self.u_today_date.value = "2023-01-01"
        self.u_braillenote_trial11.value = 1
        # ... repeat for all the other UI elements

        mock_datetime.datetime.strptime.return_value.strftime.return_value = "2023_01_01-000000_AM"
        mock_path.return_value.joinpath.return_value = Path("/path/to/student/data")

        # Call the function to test
        save(None)

        # Check that the json dump was called with the correct data
        mock_json.dump.assert_called_once_with({
            "studentname": "TestStudent",
            "date": "2023_01_01-000000_AM",
            "braillenote_trial11": 1,
            # ... repeat for all the other UI elements
        }, mock_path.return_value.joinpath.return_value.open.return_value.__enter__.return_value)

        # Check that the file was opened in write mode
        mock_path.return_value.joinpath.return_value.open.assert_called_once_with('w')

if __name__ == "__main__":
    unittest.main()