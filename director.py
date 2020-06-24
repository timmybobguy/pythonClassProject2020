#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from builder import Builder
from concreteTable import ConcreteTable
from concreteBar import ConcreteBar


class Director:

    def __init__(self):
        pass

    def director(self):

        builder.get_inform()
        builder.draw()


    """def bar(self, cmd_file):
        builder1 = ConcreteBar()
        builder1.get_import(cmd_file)
        builder1.get_function(cmd_file)
        builder1.draw()

    def table(self, cmd_file):
        builder2 = ConcreteTable()
        builder2.get_inform(cmd_file)
        builder2.draw()"""