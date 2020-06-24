#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from builder import Builder
from concreteTable import ConcreteTable
from concreteBar import ConcreteBar


class Director(object):

    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.get_inform()
        self.builder.draw()


if __name__ == '__main__':
 table = ConcreteTable("/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py")
 director = Director(table)
 director.construct()