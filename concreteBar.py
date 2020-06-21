#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from builder import Builder
from checkfiles import CheckDirectory
import re
import os
import matplotlib.pyplot as plt
from checkfiles import CheckDirectory
import plotly.graph_objects as go


class ConcreteBar(Builder):
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
        num1 = len(self.func_all)
        num2 = len(self.imp_arr)
        data = [num1, num2]
        plt.bar(['Features', 'packages used'], data)
        plt.show()

if __name__ == '__main__':
    Bar = ConcreteBar()
    Bar.get_inform("/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py")
    Bar.draw()
