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

    def __init__(self):
        pass

    def get_inform(self, cmd_file):
        file_name = CheckDirectory.check_file(self, cmd_file)
        print(file_name)
        file = open(file_name)
        file1 = file.read()
        imp = re.findall(r"import\s\w+", file1, re.S)
        func = re.findall(r"def\sdo\w+", file1, re.S)

        for i in func:
            j = i.strip('def')
            self.func_all.append(j)
        print(self.func_all)

        for i in imp:
            j = i.strip('import')
            self.imp_arr.append(j)
        print(self.imp_arr)

    def draw(self):
        fig = go.Figure(data=[go.Table(header=dict(values=['Functions']),


                                       cells=dict(values=[[95, 85, 75, 95]]))
                              ])
        fig.show()