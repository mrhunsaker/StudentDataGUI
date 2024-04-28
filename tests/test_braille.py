# FILEPATH: /c:/Users/RYHUNSAKER/GitHubRepos/StudentDataGUI/tests/test_braille.py

import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
from appPages.braille import save


class Testbraille(unittest.TestCase):
    def setUp(self):
        # Mocking the UI elements
        self.u_studentname = MagicMock()
        self.u_today_date = MagicMock()
        self.u_braille_trial11 = MagicMock()
        # ... repeat for all the other UI elements

    @patch("appPages.braille.datetime")
    @patch("appPages.braille.Path")
    @patch("appPages.braille.json")
    def test_save(self, mock_json, mock_path, mock_datetime):
        # Setting up the mock values
        self.u_studentname.value = "TestStudent"
        self.u_today_date.value = "2023-01-01"
        self.u_braille_trial11.value = 1
        # ... repeat for all the other UI elements

        mock_datetime.datetime.strptime.return_value.strftime.return_value = (
            "2023_01_01-000000_AM"
        )
        mock_path.return_value.joinpath.return_value = Path("/path/to/student/data")

        # Call the function to test
        save(None)

        # Check that the json dump was called with the correct data
        mock_json.dump.assert_called_once_with(
            {
                "studentname": "TestStudent",
                "date": "2023_01_01-000000_AM",
                "braille_trial11": 1,
                # ... repeat for all the other UI elements
            },
            mock_path.return_value.joinpath.return_value.open.return_value.__enter__.return_value,
        )

        # Check that the file was opened in write mode
        mock_path.return_value.joinpath.return_value.open.assert_called_once_with("w")

    @patch("appPages.braille.sqlite3")
    @patch("appPages.braille.pd")
    @patch("appPages.braille.np")
    @patch("appPages.braille.go")
    @patch("appPages.braille.make_subplots")
    def test_graph(self, mock_make_subplots, mock_go, mock_np, mock_pd, mock_sqlite3):
        # Mocking the UI elements
        self.u_studentname = MagicMock()
        self.u_studentname.value = "TestStudent"

        # Mocking the global variables
        global USER_DIR
        USER_DIR = "/path/to/user/dir"

        # Mocking the database connection and query
        mock_conn = MagicMock()
        mock_sqlite3.connect.return_value = mock_conn
        mock_df_sql = MagicMock()
        mock_pd.read_sql_query.return_value = mock_df_sql
        mock_df_student = MagicMock()
        mock_df_sql.__getitem__.return_value = mock_df_student

        # Mocking the DataFrame operations
        mock_df = MagicMock()
        mock_df_student.drop.return_value = mock_df
        mock_df.rename.return_value = mock_df
        mock_df.astype.return_value = mock_df
        mock_pd.to_datetime.return_value = mock_df
        mock_df.set_index.return_value = mock_df
        mock_df.sort_values.return_value = mock_df
        mock_df.describe.return_value = mock_df
        mock_df.diff.return_value = mock_df

        # Mocking the numpy operations
        mock_np.random.normal.return_value = MagicMock()

        # Mocking the plotly operations
        mock_fig = MagicMock()
        mock_make_subplots.return_value = mock_fig
        mock_trace = MagicMock()
        mock_go.Scatter.return_value = mock_trace

        # Call the function to test
        graph(None)

        # Check that the database connection and query were called correctly
        mock_sqlite3.connect.assert_called_once_with(
            Path(USER_DIR).joinpath("StudentDatabase", "students.db")
        )
        mock_pd.read_sql_query.assert_called_once_with(
            "SELECT * FROM BRAILLEPROGRESS", mock_conn
        )
        mock_df_sql.__getitem__.assert_called_once_with(
            mock_df_sql.STUDENTNAME == "TestStudent"
        )

        # Check that the DataFrame operations were called correctly
        mock_df_student.drop.assert_called_once_with(columns=["ID", "STUDENTNAME"])
        mock_df.rename.assert_called_once_with(columns={"DATE": "date"})
        mock_df.astype.assert_called_once_with("string")
        mock_pd.to_datetime.assert_called_once_with(mock_df, format=date_fmt)
        mock_df.set_index.assert_called_once_with("date")
        mock_df.sort_values.assert_called_once_with(by="date")
        mock_df.describe.assert_called_once()
        mock_df.diff.assert_called_once_with(periods=3)

        # Check that the numpy operations were called correctly
        mock_np.random.normal.assert_called_once()

        # Check that the plotly operations were called correctly
        mock_make_subplots.assert_called_once()
        assert mock_go.Scatter.call_count == 22
        assert mock_fig.add_trace.call_count == 22


if __name__ == "__main__":
    unittest.main()
