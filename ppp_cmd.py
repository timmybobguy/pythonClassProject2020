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
from extractData import ExtractData
from validate_data import ValidateData
from mysql_example import link_db
from mysql import MySQL

os.environ["PATH"] += os.pathsep + './graphviz/release/bin'


class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "==>>>"
        self.intro = "This program can generate class diagrams from your source codes, type help for a list of commands"

    def do_choose_system(self, arg):
        """ please input -w or -m  to tell us your operation system, Windows or Mac"""
        if arg == "-w":
            print('Windows lover')
        elif arg == "-m":
            print('Mac lover')

    def do_exit(self, args):
        """Exits from the console"""
        exit()

    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(args)

    def do_uml_diagram(self, args):
        """PLEASE input full path and can have
         options on two different diagram types """
        raw_data = args.split()
        input_file = raw_data[0]
        file_type = raw_data[1]
        os.path.isfile(input_file)
        work_dir = os.path.dirname(input_file)
        file = input_file[len(work_dir) + 1:]
        if file_type == 'svg':
            command = "pyreverse {0} -o svg -p diagram".format(file)
            print("input_dir:{0} input_file:{1}".format(work_dir, file))
            print("command:" + command)
            subprocess.run(command, cwd=work_dir, shell=True)
        elif file_type == 'fig':
            command = "pyreverse {0} -o fig -p diagram".format(file)
            print("input_dir:{0} input_file:{1}".format(work_dir, file))
            print("command:" + command)
            subprocess.run(command, cwd=work_dir, shell=True)
        elif file_type == 'dot':
            command = "pyreverse {0} -o dot -p diagram".format(file)
            print("input_dir:{0} input_file:{1}".format(work_dir, file))
            print("command:" + command)
            subprocess.run(command, cwd=work_dir, shell=True)

        else:
            print(" You only have 3 options which are svg, dot and fig in the file types")

    def do_extractData(self, args):
        """This can load a cmd interface file and extract data from it"""

        ExtractData().get_data(args)

    def do_ValidateData(self, args):
        """input a full path of your file, then the programme can check your file weather pass pep8 or not"""
        ValidateData().check_file(args)

    def do_bar_chart(self, args):
        """input a full path of your file, then the programme can generate a bar chart
        which shows a number of package used and  a number of features in your cmd file """
        ExtractData().get_data(args)
        ExtractData().draw_bar_chart()

    def do_mySql(self, arg):
        """this can check weather the db links """
        link_db().check_link_db()

    def do_save_data(self, args):
        """this can save data to MySql database"""
        link_db().get_file(args)
        link_db().link_mysql_save()

    def do_load_data(self, arg):
        """this can laod data from MySql database"""
        link_db().load_mysql_data()

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

            try:
                open(arguments[0], 'r').read()

            except FileNotFoundError:

                print("No file found at: '" + arguments[0] + "'")

            command = 'pyreverse -o dot ' + arguments[0] + ' -p componentplain '
            subprocess.call(command)

        else:

            print("Wrong num of args, please try again")

    def do_saveDOTtoDatabase(self, args):
        """Saves a file to the database server"""
        saveFileToLocalDatabase("Components.txt")

    def do_getFileFromLocalDatabase(self, args):
        getFileFromLocalDatabase(args)

    def do_testGraph(self, args):
        # This is hard coded at the moment, need to change paths etc.
        command = 'dot -Tpng classes_componentplain.dot -o ' + args
        subprocess.call(command)


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def saveFileToLocalDatabase(path):
    conn = MySqlite()
    conn.create_connection(r"pythonsqlite.db")
    conn.create_cursor()

    try:

        fileData = convertToBinaryData(path)
        sql = """INSERT INTO testData (fileName, fileData, fileSaveDate) VALUES ("{}", ?, "{}")""".format(path,
                                                                                                          datetime.now())
        conn.execute_blob(sql, fileData)
        print("File inserted into db...")

    except FileNotFoundError:

        print("File path does not exist")

    conn.commit_changes()
    conn.close_cursor()
    conn.close_connection()


def getFileFromLocalDatabase(filename):
    conn = MySqlite()
    try:
        conn.create_connection(r"pythonsqlite.db")
    except Exception as err:
        print("Cannot connect to local db: " + err)
    conn.create_cursor()
    sql = """SELECT fileData FROM testData WHERE fileName = "{}" """.format(filename)
    result = conn.fetch_all(sql)
    print(result)


if __name__ == '__main__':
    CLI().cmdloop()
