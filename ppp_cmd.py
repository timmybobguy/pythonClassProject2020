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

#os.environ["PATH"] += os.pathsep + './graphviz/release/bin'


class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "==>>>"
        self.intro = "This program can generate class diagrams from your source codes, type help for a list of commands"

    def do_choose_system(self, arg):
        """ please imput -w or -m  to tell us your operation system, Windows or Mac"""
        if arg == "-w":
            print('Windows lover')
        elif arg == "-m":
            print('Mac lover')

    def do_exit(self, args):
        """Exits from the console"""
        exit()

        ## Command definitions to support Cmd object functionality ##

    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(args)


    def do_uml_diagram(self, args):
        """PLASE input full path and can have
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

    def do_ValidateData(self,args):
        "input a full path of your file, then the programme can check your file weather pass pep8 or not"
        ValidateData().check_file(args)

    def do_bar_chart(self, args):
        """input a full path of your file, then the programme can generate a bar chart
        which shows a number of package used and  a numbe of features in your cmd file """
        ExtractData().get_data(args)
        ExtractData().draw_bar_chart()

    def do_link_MySql(self):
        link_db().check_link_db()

    def do_save_data(self):
        link_db().get_file(args)
        link_db().link_mysql_save()


    def do_load_data(self):
         link_db().load_mysql_data()


if __name__ == '__main__':
    CLI().cmdloop()
