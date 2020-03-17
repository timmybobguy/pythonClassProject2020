#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import os
import cmd
import ast
import pylint
import subprocess
from os import environ, pathsep
from sqlite import MySqlite

os.environ["PATH"] += os.pathsep + './graphviz/release/bin'


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
        """Takes one parameter: source code file path. This command turns the source
        code file into a dot file of the program structure"""

        arguments = args.split()

        if len(arguments) == 1:

            print("correct number")
            print(arguments[0])

            command = 'pyreverse -o dot ' + arguments[0] + ' -p componentplain '
            subprocess.call(command)

        else:

            print("Wrong num of args, please try again")

    def do_saveDOTtoDatabase(self, args):
        """Saves the dot file to the database server"""
        conn = MySqlite()
        conn.create_connection(r"pythonsqlite.db")
        conn.create_cursor()
        fileData = convertToBinaryData('test.png')

        sql = "INSERT INTO testData (fileData) VALUES (?)"
        conn.execute_blob(sql, fileData)
        print("file inserted")
        conn.commit_changes()
        conn.close_cursor()
        conn.close_connection()

    def do_testGraph(self, args):
        # This is hard coded at the moment, need to change paths etc.
        command = 'dot -Tpng classes_componentplain.dot -o ' + args
        subprocess.call(command)


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


if __name__ == '__main__':
    CLI().cmdloop()
