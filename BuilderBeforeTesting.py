import ppp_cmd
import os
import io
import sys
import unittest


class BranchCoverageTests(unittest.TestCase):
    # baseDir = os.path.join(os.path.dirname(__file__))
    baseDir = "C:/Users/TimDesk/PycharmProjects/pythonClassProject2020"

    def test_1(self):
        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "{0}/sqlite.py svg".format(self.baseDir)

        cli.do_uml_diagram(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = 'input_dir:{0} input_file:sqlite.py\ncommand:pyreverse ' \
                   'sqlite.py -o svg -p diagram\n'.format(self.baseDir)

        self.assertEqual(actual, expected)  # Assert

    def test_2(self):
        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "{0}/sqlite.py fig".format(self.baseDir)

        cli.do_uml_diagram(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = 'input_dir:{0} input_file:sqlite.py\ncommand:pyreverse ' \
                   'sqlite.py -o fig -p diagram\n'.format(self.baseDir)

        self.assertEqual(actual, expected)  # Assert

    def test_3(self):
        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "{0}/sqlite.py dot".format(self.baseDir)

        cli.do_uml_diagram(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = 'input_dir:{0} input_file:sqlite.py\ncommand:pyreverse ' \
                   'sqlite.py -o dot -p diagram\n'.format(self.baseDir)

        self.assertEqual(actual, expected)  # Assert

    def test_4(self):
        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "{0}/sqlite.py fake".format(self.baseDir)

        cli.do_uml_diagram(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = ' You only have 3 options which are svg, ' \
                   'dot and fig in the file types\n'

        self.assertEqual(actual, expected)  # Assert

    def test_5(self):
        cli = ppp_cmd.CLI()

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        command = "{0}/fakeFile.py fake".format(self.baseDir)

        cli.do_uml_diagram(command)  # Do the thing

        sys.stdout = sys.__stdout__  # Reset redirect.

        actual = capturedOutput.getvalue()

        expected = 'wrong path, try again\n'

        self.assertEqual(actual, expected)  # Assert

    def tearDown(self):
        print("This test case is done!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
