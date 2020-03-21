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
        get_file_name = os.path.dirname(input_file)
        command = "pycodestyle " + input_file
        subprocess.run(command, cwd=get_file_name, shell=True)
"""
if __name__ == '__main__':
    ValidateData().check_file("/Users/jimmy/py/pythonClassProject2020/test4.py")

"""














