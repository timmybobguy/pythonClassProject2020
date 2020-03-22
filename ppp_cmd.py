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
from mysql_example import LinkDb
from checkfiles import CheckDirectory
import re
import shelve
from mysql import MySQL
import cmdAdapter
import asyncio
from jsonTesting import JsonData


class CustomStream(object):
    async def readline(self):
        return await sys.stdin.readline()

    def write(self, msg):
        sys.stdout.write(msg)

    def flush(self):
        pass


MyAsyncShell = type('MyAsyncShell', (cmd.Cmd,), {
    'cmdloop': cmdAdapter.adapter_cmdloop,
    'use_rawinput': False,
    'stdin': CustomStream(),
    'stdout': CustomStream()
})


class CLI(cmd.Cmd):  # MyAsyncShell - This is not working bugged

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "==>>>"
        self.intro = "This program can generate class diagrams from your source codes, type help for a list of commands"
        json = JsonData('helpfiledata.json')
        json.open_file()
        self.__json = json

    def do_shelve(self,cmd_file):
        file_name = CheckDirectory.check_file(self, cmd_file)
        print(file_name)
        file = open(file_name)
        file1 = file.read()
        imp = re.findall(r"import\s\w+", file1, re.S)
        s = shelve.open("test")
        s['package'] = imp
        print(s['package'])
        s.close()


    def do_choose_system(self, arg):
        """ please input -w or -m  to tell us your operation system, Windows or Mac"""
        if arg == "-w":
            print('Windows lover')
        elif arg == "-m":
            print('Mac lover')

    def help_choose_system(self):
        print(self.__json.get_help_text('choose_system'))

    def do_exit(self, *args):
        """leave the programme"""
        return True


    def do_uml_diagram(self, args):
        """PLEASE input full path and can have
         options on two different diagram types """
        raw_data = args.split()
        input_file = raw_data[0]
        file_type = raw_data[1]
        try:
            os.path.isdir(input_file)
            os.path.isfile(input_file)
            work_dir = os.path.dirname(input_file)
            file = input_file[len(work_dir) + 1:]

        except FileNotFoundError:
            print("wrong path, try again")

        else:

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

    def help_uml_diagram(self):
        print(self.__json.get_help_text('uml_diagram'))

    def do_extractData(self, args):
        """This can load a cmd interface file and extract data from it"""

        ExtractData().get_data(args)

    def help_extractData(self):
        print(self.__json.get_help_text('extractData'))

    def do_ValidateData(self, args):
        try:
            path = True
            ValidateData().check_file(args)
        except:
            print("wrong path, try again")
            path = False
        return path

    def help_ValidateData(self):
        print(self.__json.get_help_text('ValidateData'))

    def do_bar_chart(self, args):
        """input a full path of your file, then the programme can generate a bar chart
        which shows a number of package used and  a numbe of features in your cmd file """
        try:
            path = True
            ExtractData().get_data(args)
            ExtractData().draw_bar_chart()
        except:
            print("wrong path, try again")
            path = False
        return path

    def help_bar_chart(self):
        print(self.__json.get_help_text('bar_chart'))

    def do_mySql(self, arg):
        """this can check weather the db links.
        please make sure your Mysql have a database which is
        host="127.0.0.1", user="root", passwd="1234", database="class """

        LinkDb().check_link_db()

        return True


    def do_save_data(self, args):
        """this can save data to MySql database.
        please make sure your Mysql have a database which is
        host="127.0.0.1", user="root", passwd="1234", database="class"""
        try:
            path = True
            LinkDb().get_file(args)
            LinkDb().link_mysql_save()
        except:
            print("wrong path, try again")
            path = False
        return path


    def do_load_data(self, args):
        """This can laod data from MySql database.
         please make sure your Mysql have a database which is host="127.0.0.1", user="root",
         passwd="1234", database="class"""
        try:
            LinkDb().load_mysql_data()
        except:
            raise FileNotFoundError("cannot load data from the database")


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

    async def do_testSaveToDatabaseServer(self, args):
        loop = asyncio.get_event_loop()

        result = loop.run_until_complete(saveServer())
        print(result)

        loop.close()


async def saveServer():
    await saveFileToDatabaseServer("Components.txt")


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


async def saveFileToDatabaseServer(path):
    conn = MySQL()
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root'
    }
    try:

        await conn.create_connection(db_config)
        fileData = convertToBinaryData(path)

    except FileNotFoundError:

        print("File path not found...")

    except Exception as err:

        print(err)

    else:

        await conn.create_cursor()
        sql = """INSERT INTO testData (fileName, fileData, fileSaveDate) VALUES ("{}", ?, "{}")""".format(path,
                                                                                                          datetime.now())
        await conn.execute_blob(sql, fileData)
        await conn.commit()
        await conn.close_cursor()
        await conn.close_connection()


if __name__ == '__main__':
    # CLI().cmdloop()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(CLI().cmdloop())
    loop.close()
