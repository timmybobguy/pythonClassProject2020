#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import unittest
from example import func1, func2
from checkfiles import Check_directory
from validate_data import ValidateData

class ExampleTest(unittest.TestCase):
    """Test example
    """

    def test_checkdirectory(self):
        self.assertEqual(Check_directory().check_file('/Users/jimmy/py/pythonClassProject2020/test4.py'), 'test4.py')

    def test_validate_function(self):
        self.assertEqual(ValidateData().check_file('/Users/jimmy/py/pythonClassProject2020/test4.py'),)




if __name__ == '__main__':
    unittest.main()