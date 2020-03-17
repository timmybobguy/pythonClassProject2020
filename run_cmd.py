#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import os
import cmd
import ast
import pylint
import subprocess
from os import environ, pathsep
from sqlite import MySqlite
from datetime import datetime

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

            command = 'pyreverse -o dot ' + arguments[0] + ' -p ' + arguments[0]

            try:

                open(arguments[0], 'r')
                subprocess.call(command)

            except FileNotFoundError:

                print("No file found at: '" + arguments[0] + "'")

        else:

            print("You have entered an incorrect number of arguments for this command, please try again or type 'help "
                  "generateDOT' for more info")

    def do_saveDOTtoDatabase(self, args):
        """Saves the dot file to the database server"""
        saveFileToMySqliteDatabase("test.png")

    def do_generateGraph(self, args):
        """Takes two parameters: .dot file path, output file path. This command takes the .dot file and outputs a
        graphical representation of the file in the specified format."""
        # Add functionality which allows the user to choose the output file type, this would mean the command has
        # another parameter/option. These options could be retrieved from database?

        arguments = args.split()

        if len(args) == 2:

            print("correct num of args")

        command = 'dot -Tpng classes_componentplain.dot -o ' + args
        subprocess.call(command)


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def saveFileToMySqliteDatabase(path):
    conn = MySqlite()
    try:
        conn.create_connection(r"pythonsqlite.db")
    except Exception as err:
        print(err)
        print("Cannot connect to local database file")

    conn.create_cursor()
    fileData = convertToBinaryData(path)
    sql = """INSERT INTO testData (fileName, fileData, fileSaveDate) VALUES ("{}", ?, "{}")""".format(path, datetime.now())
    conn.execute_blob(sql, fileData)
    print("File inserted into database")
    conn.commit_changes()
    conn.close_cursor()
    conn.close_connection()


if __name__ == '__main__':
    CLI().cmdloop()
