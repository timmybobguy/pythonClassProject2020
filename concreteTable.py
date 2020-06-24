#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from builder import Builder
from checkfiles import CheckDirectory
from checkfiles import CheckDirectory
import re
import os
import plotly.graph_objects as go


class ConcreteTable(Builder):
    func_all = []
    imp_arr = []
    imp = []
    func = []
    all = []

    def __init__(self):
        pass

    def get_inform(self, cmd_file):
        file_name = CheckDirectory.check_file(self, cmd_file)
        file = open(file_name)
        file1 = file.read()
        obj = re.findall(r"def\sdo\w+", file1, re.S)
        for i in obj:
            j = i.strip('def')
            print(j)

            self.all.append(j)

    def draw(self):
        fig = go.Figure(data=[go.Table(header=dict(values=['Functions']), cells=dict(values=[self.all]))])
        fig.show()

if __name__ == '__main__':
    Table = ConcreteTable()
    Table.get_inform("/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py")
    Table.draw()