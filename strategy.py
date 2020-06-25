#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from checkfiles import CheckDirectory
import re
import re
import os
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import doctest



class Strategy(metaclass=ABCMeta):

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def get_inform(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Bar(Strategy):
    func_all = []
    imp_arr = []
    imp = []
    func = []

    def __init__(self, file):
        super().__init__(file)

    def get_inform(self):
        """
        >>> a = Bar('/Users/jimmy/py/pythonClassProject2020/cmd_test.py')
        >>> a.get_inform()
        [' do_exit']
        """
        file_name = CheckDirectory.check_file(self, self.file)
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

    def draw(self):
        num1 = len(self.func_all)
        num2 = len(self.imp_arr)
        data = [num1, num2]
        plt.bar(['Features', 'packages used'], data)
        plt.show()


class Table(Strategy):
    all = []

    def __init__(self, file):
        super().__init__(file)

    def get_inform(self):
        """
        >>> a = Table('/Users/jimmy/py/pythonClassProject2020/cmd_test.py')
        >>> a.get_inform()
         do_exit
        """
        file_name = CheckDirectory.check_file(self, self.file)
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


class Context(object):
    def __init__(self, strategy):
        self.strategy = strategy

    def chart(self):
        """
        >>> a = Bar('/Users/jimmy/py/pythonClassProject2020/cmd_test.py')
        >>> con = Context(a)
        >>> con.chart()
        [' do_exit', ' do_exit']
        """
        self.strategy.get_inform()
        self.strategy.draw()


if __name__ == '__main__':
    doctest.testmod()


# if __name__ == '__main__':
#     con = Context(Table('/Users/jimmy/py/pythonClassProject2020/cmd_test.py'))
#     con.chart()
#
#     con2 = Context(Bar('/Users/jimmy/py/pythonClassProject2020/cmd_test.py'))
#     con2.chart()





