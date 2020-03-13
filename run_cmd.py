#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import os
import cmd
import sys


class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "===>>>>>> "
        self.intro = "This programme can generate class diagrams from your source codes"

    def do_hello(self, arg):
        print( "hello again", arg, "!")


    def do_run(args):
    # get the file name/path
        file_name = args.read['/Users/jimmy/py/pythonClassProject2020/sample1.txt']

    # validate the file name/path
        validate_file(file_name)
    # read and print the file content
        with open(file_name, 'r') as f:
          print(f.read())




cli = CLI()
cli.cmdloop()