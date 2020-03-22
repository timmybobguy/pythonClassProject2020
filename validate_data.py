#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import pycodestyle
import pep8
import subprocess
import os


class ValidateData:

    def __init__(self):
        pass

    def check_file(self, input_file):
        try:
            get_file_name = os.path.dirname(input_file)
            command = "pycodestyle " + input_file
            subprocess.run(command, cwd=get_file_name, shell=True)
        except:
            raise FileNotFoundError("You should input a correct path")





if __name__ == '__main__':
    ValidateData().check_file("fihguhfidu")
















