import unittest
import ppp_cmd
from mysql import MySQL
from sqlite import MySqlite
from jsonTesting import JsonData
import subprocess
import asyncio
import io
import sys
import os


class UnitTests(unittest.TestCase):

    # Sqlite tests

    def test_sqlite_createConnection(self):
        conn = MySqlite()
        conn.create_connection(r"pythonsqlite.db")
        self.assertNotEqual(conn.connection(), None)

    def test_sqlite_createConnectionFail(self):
        conn = MySqlite()
        self.assertEqual(conn.connection(), None)

    def test_sqlite_createCursor(self):
        conn = MySqlite()
        conn.create_connection(r"pythonsqlite.db")
        conn.create_cursor()
        self.assertNotEqual(conn.cursor(), None)

    def test_sqlite_createCursorFail(self):
        conn = MySqlite()
        self.assertEqual(conn.cursor(), None)

    def test_sqlite_executeQuery(self):
        conn = MySqlite()
        conn.create_connection(r"pythonsqlite.db")
        conn.create_cursor()
        result = conn.fetch_one("""SELECT fileSaveDate from testData WHERE fileName = "test.png" """)
        self.assertEqual(result, ('2020-03-17 22:49:20.890304',))

    # JsonTesting tests

    def test_jsonTesting_open_file(self):
        model = JsonData("helpfiledata.json")
        model.open_file()
        self.assertIsInstance(model.helpTextDict(), dict)

    def test_jsonTesting_open_fileFail(self):
        model = JsonData("helpfiledata.json")
        self.assertEqual(model.helpTextDict(), None)

    def test_jsonTesting_get_help_text(self):
        model = JsonData("helpfiledata.json")
        model.open_file()
        self.assertEqual(model.get_help_text("TESTING"), "TESTING TEXT")

    def test_jsonTesting_get_help_textFail(self):
        model = JsonData("helpfiledata.json")
        model.open_file()
        self.assertNotEqual(model.get_help_text("TESTING NOT VALID"), "TESTING TEXT")

    # File directory tests

    def test_directory_goodDay(self):
        baseDir = os.path.join(os.path.dirname(__file__))
        testCommand = os.path.join(baseDir, "timDBCode")

        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        cli.do_get_all_source_files(testCommand)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()
        expected = testCommand + "\\mysql.py\n" + testCommand + "\\sqlite.py\n"
        self.assertEqual(actual, expected)

    def test_directory_badDirectory(self):
        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        cli.do_get_all_source_files("This is a bad directory")  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()
        self.assertEqual(actual, "Directory not valid\n")

    def test_directory_badOutputFormat(self):
        baseDir = os.path.join(os.path.dirname(__file__))
        testCommand = os.path.join(baseDir, "timDBCode")

        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        cli.do_get_all_source_files(testCommand + " -a NOTAFILETYPE")  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()
        expected = testCommand + "\\mysql.py\n" + testCommand + "\\sqlite.py\n" + "Incorrect output format entered\n"
        self.assertEqual(actual, expected)

    # MySql tests

    async def test_mysql_createConnection(self):
        conn = MySQL()
        await conn.create_connection({
            'host': 'localhost',
            'user': 'root',
            'password': 'root'
        })
        await self.assertNotEqual(conn.connection(), None)

    async def test_mysql_createConnectionFail(self):
        conn = MySQL()
        await conn.create_connection({
            'host': '',
            'user': '',
            'password': ''
        })
        self.assertEqual(conn.connection(), None)

    async def test_mysql_createCursor(self):
        conn = MySQL()
        await conn.create_connection({
            'host': 'localhost',
            'user': 'root',
            'password': 'root'
        })
        await conn.create_cursor()
        self.assertNotEqual(conn.cursor(), None)

    async def test_mysql_executeQuery(self):
        conn = MySQL()
        await conn.create_connection({
            'host': 'localhost',
            'user': 'root',
            'password': 'root'
        })
        await conn.create_cursor()
        result = await conn.fetch_one("""SELECT fileSaveDate from testData WHERE fileName = "test.png" """)
        self.assertEqual(result, ('2020-03-17 22:49:20.890304',))


if __name__ == '__main__':
    unittest.main()
