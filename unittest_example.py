#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import unittest
from checkfiles import CheckDirectory
from validate_data import ValidateData
from mysql_example import LinkDb
from ppp_cmd import *
# Wu, Chieh-Ming (Jimmy's work)


class ExampleTest(unittest.TestCase):
    """Jimmy's unittest """

    def test_checkdirectory(self):
        self.assertEqual(CheckDirectory().check_file('/Users/jimmy/py/pythonClassProject2020/test4.py'), 'test4.py')

    def test_correct_input_path(self):
        try:
            result = CheckDirectory().check_file('/Users/jimmy/py/pythonClassProject2020/test4.py')
            self.assertIsInstance(result, str)
        except WrongInputException:
            self.fail()

    def test_mydb_link(self):
        self.assertRaises(FileNotFoundError, ValidateData().check_file, "FileNotFoundError")

    def test_correct_path_validate_data(self):

        result = CLI().do_ValidateData('/Users/jimmy/py/pythonClassProject2020/test3.py')
        self.assertTrue(result)

    def test_wrong_path_validate_data(self):

        result = CLI().do_ValidateData('This is Jimmy')
        self.assertFalse(result)

    def test_correct_do_bar_chart(self):
        result = CLI().do_bar_chart('/Users/jimmy/py/pythonClassProject2020/run_cmd.py')
        self.assertTrue(result)

    def test_wrong_do_bar_chart(self):
        result = CLI().do_bar_chart('LoveYou')
        self.assertFalse(result)

    def test_correct_input_do_bar_chart(self):
        try:
            result = CheckDirectory().check_file('/Users/jimmy/py/pythonClassProject2020/run_cmd.py')
            self.assertIsInstance(result, str)
        except WrongInputException:
            self.fail()

    def test_do_exit(self):
        result = CLI().do_exit()
        self.assertIsInstance(result, bool)

    def test_return_do_exit(self):
        result = CLI().do_exit()
        self.assertTrue(result)

    def test_throw_raise(self):
        self.assertRaises(FileNotFoundError, ValidateData().check_file, "You should input a correct path")

    def test_false_do_save_data(self):
        result = CLI().do_save_data('1234')
        self.assertFalse(result)

    def test_true_do_save_data(self):
        result = CLI().do_save_data('/Users/jimmy/py/pythonClassProject2020/run_cmd.py')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
