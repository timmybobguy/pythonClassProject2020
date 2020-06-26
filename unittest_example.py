#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import unittest
from ppp_cmd import*
from strategy import *
from draw_UML import SvgSite, FigSite, DotSite

# Wu, Chieh-Ming (Jimmy's work)


class ExampleTest(unittest.TestCase):
    """Jimmy's unittest """
    def test_uml_diagram_svg(self):
        text = "/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -svg"
        result = CLI().do_uml_diagram(text)
        self.assertTrue(result)

    def test_uml_diagram_fig(self):
        text = "/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -fig"
        result = CLI().do_uml_diagram(text)
        self.assertTrue(result)

    def test_uml_diagram_dot(self):
        text = "/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -dot"
        result = CLI().do_uml_diagram(text)
        self.assertTrue(result)

    def test_uml_diagram_dot(self):
        text = "/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -png"
        result = CLI().do_uml_diagram(text)
        self.assertFalse(result)

    def test_chart(self):
        result = CLI().do_chart('/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py -b')
        self.assertTrue(result)





if __name__ == '__main__':
    unittest.main()
