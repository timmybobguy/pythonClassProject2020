#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import unittest
from strategy import *

# Wu, Chieh-Ming (Jimmy's work)


class ExampleTest(unittest.TestCase):
    """Jimmy's unittest for strategy pattern"""

    def test_bar_get_inforam(self):
        self.assertEqual(Bar('/Users/jimmy/py/pythonClassProject2020/cmd_test.py').get_inform(),[' do_exit'])

    def test_bar_draw(self):
        self.assertEqual(Bar('/Users/jimmy/py/pythonClassProject2020/cmd_test.py').draw(),)


if __name__ == '__main__':
    unittest.main()
