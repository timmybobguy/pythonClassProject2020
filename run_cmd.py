#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import os
import cmd
import ast
import pylint

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "===>>>>>> "
        self.intro = "This programme can generate class diagrams from your source codes"

    def do_hello(self, arg):
        print( "hello again", arg, "!")


    def do_run(self, arg):
    # get the file name/path
       fileObj = open('./test1.py', 'r')
       print(fileObj.read())







cli = CLI()
cli.cmdloop()