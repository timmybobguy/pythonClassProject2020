#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess


class Check_directory():

    def __init__(self):
        pass

    def check_file(self, input_file, file_type):
        if os.path.isfile(input_file):
            work_dir = os.path.dirname(input_file)
            file = input_file[len(work_dir)+1:]
            #output_file = "componentplain"
        else:
            work_dir = input_file
            file = "*.py"
            #output_file = "componentplain"

        command = "pyreverse {0} -o {1} -p test2".format(file, file_type)
        print("input_dir:{0} input_file:{1}".format(work_dir, file))
        print("command:" + command)

        subprocess.run(command, cwd=work_dir, shell=True)


if __name__ == '__main__':
    Check_directory().check_file("/Users/jimmy/py/pythonClassProject2020/test2.py", "svg")




