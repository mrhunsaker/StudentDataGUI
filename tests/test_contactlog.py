# FILEPATH: /c:/Users/RYHUNSAKER/GitHubRepos/StudentDataGUI/tests/test_contactlog.py

from unittest.mock import MagicMock, call
from appPages.contactlog import create_ui

class TestContactLog(unittest.TestCase):
    @patch('appPages.contactlog.ui')
    def test_create_ui(self, mock_ui):
        # Mocking the UI elements
        u_studentname = MagicMock()
        u_today_date = MagicMock()
        u_guardianName = MagicMock()
        u_phoneNumber = MagicMock()
        u_emailAddress = MagicMock()
        u_contactMethod = MagicMock()
        u_contactResponse = MagicMock()
        u_contactGeneral = MagicMock()
        u_contactSpecific = MagicMock()
        u_contactNotes = MagicMock()

        # Call the function to test
        create_ui()

        # Check that the ui methods were called with the correct arguments
        calls = [
            call.row().classes("w-screen no-wrap py-4").style('font-style:normal, font-family: "Atkinson Hyperlegible"'),
            call.label().classes("w-[150px]").style('font-style:normal, font-family: "Atkinson Hyperlegible"'),
            call.label("STUDENT INFORMATION").classes("w-full justify-center items-center font-bold"),
            # ... repeat for all the other UI elements
        ]
        mock_ui.assert_has_calls(calls, any_order=True)

        # Check that the on_change functions were set correctly
        u_studentname.set_value.assert_not_called()
        u_today_date.set_value.assert_not_called()
        u_guardianName.set_value.assert_not_called()
        u_phoneNumber.set_value.assert_not_called()
        u_emailAddress.set_value.assert_not_called()
        u_contactMethod.set_value.assert_not_called()
        u_contactResponse.set_value.assert_not_called()
        u_contactGeneral.set_value.assert_not_called()
        u_contactSpecific.set_value.assert_not_called()
        u_contactNotes.set_value.assert_not_called()

if __name__ == "__main__":
    unittest.main()