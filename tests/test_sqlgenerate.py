import unittest
import sqlite3
from sqlite3 import Error
from appHelpers.sqlgenerate import createTables

class TestCreateTables(unittest.TestCase):
    def setUp(self):
        # Setup a temporary database for testing
        self.db = ":memory:"
        self.conn = sqlite3.connect(self.db)

    def tearDown(self):
        # Close the connection after each test
        self.conn.close()

    def test_create_keyboarding_table(self):
        # Test the creation of the keyboarding table
        try:
            createTables(self.conn, "KEYBOARDING")
            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='KEYBOARDING'")
            self.assertIsNotNone(cursor.fetchone())
        except Error as e:
            self.fail(f"Test failed with error: {e}")

    # Repeat the above test method for each table you want to test

if __name__ == "__main__":
    unittest.main()