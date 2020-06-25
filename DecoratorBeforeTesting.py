import ppp_cmd
import os
import io
import sys
import unittest


class BranchCoverageTests2(unittest.TestCase):

    baseDir = "C:/Users/TimDesk/PycharmProjects/" \
              "pythonClassProject2020/ppp_cmd.py"

    def test_1(self):
        cli = ppp_cmd.CLI()
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "{0} Classes Functions Attributes".format(self.baseDir)

        cli.do_generate_pie_chart(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = 'Classes\nFunctions\nAttributes\n11\n35\n1\n'

        self.assertEqual(actual, expected)  # Assert

    def test_2(self):
        # Testing for non .py extension
        cli = ppp_cmd.CLI()
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "C:/Users/TimDesk/PycharmProjects/pythonClassProject2020" \
                  "/TimComponents.txt Classes Functions Attributes"

        cli.do_generate_pie_chart(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = 'Unsupported file extension, only accepts .py files\n'

        self.assertEqual(actual, expected)

    def test_3(self):
        # Testing non-existent file

        cli = ppp_cmd.CLI()
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "C:/Users/TimDesk/PycharmProjects/pythonClassProject2020" \
                  "/FAKEFILE.py Classes Functions Attributes"

        cli.do_generate_pie_chart(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = 'No such file found\n'

        self.assertEqual(actual, expected)

    def tearDown(self):
        print("This test case is done!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
