#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import os
import cmd
import ast
import pylint
import graphviz
import subprocess


class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "===>>>>>> "
        self.intro = "This program can generate class diagrams from your source codes, type help for a list of commands"

    def do_hello(self, arg):
        """Greets user"""
        print("hello again", arg, "!")

    def do_printFile(self, path):
        """Takes one parameter: file path. Takes a file and then prints it to the console"""
        try:

            fileObj = open(path, 'r')
            print(fileObj.read())

        except FileNotFoundError:

            print("No file found at: '" + path + "'")

    def do_generateDOT(self, args):
        """Takes two parameters: source code file path, and output (dot) file path. This command turns the source
        code file into a dot file of the program structure"""

        arguments = args.split()

        if len(arguments) == 2:

            print("correct number")
            print(arguments[0])
            print(arguments[1])

            command = 'pyreverse dot ' + arguments[0] + ' -p componentplain -o ' + arguments[1]
            subprocess.call(command)

        else:

            print("Wrong num of args, please try again")


if __name__ == '__main__':
    CLI().cmdloop()
