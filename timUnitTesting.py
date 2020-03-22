import unittest
import ppp_cmd
import mysql
from sqlite import MySqlite
import jsonTesting


class UnitTests(unittest.TestCase):

    # Sqlite tests

    def test_sqlite_createConnection(self):
        pass

    def test_sqlite_createConnectionFail(self):
        conn = MySqlite
        self.assertEqual(conn.connection(), None)

    def test_sqlite_createCursor(self):
        pass

    def test_sqlite_createCursorFail(self):
        conn = MySqlite
        self.assertEqual(conn.cursor(), None)

    def test_sqlite_executeQuery(self):
        conn = MySqlite
        conn.create_connection(r"pythonsqlite.db")
        conn.create_cursor()
        result = conn.fetch_one("""SELECT fileSaveDate from testData WHERE fileName = "test.png" """)
        self.assertEqual(result, "2020-03-17 22:49:20.890304")

    # MySql tests

    def test_mysql_createConnection(self):
        pass

    def test_mysql_createCursor(self):
        pass

    def test_mysql_executeQuery(self):
        pass


if __name__ == '__main__':

    pass
