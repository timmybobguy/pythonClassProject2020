#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import re
import os
import plotly.graph_objects as go


class ExtractData:
    def __init__(self):
        pass

    def Get_file(self, cmd_file):
        filename = os.path.basename(cmd_file)
        file = open(cmd_file)
        file1 = file.read()
        obj = re.findall(r"def\sdo\w+", file1, re.S)
        all = []
        for i in obj:
            j = i.strip('def')
            print(j)
            all.append(j)
        fig = go.Figure(data=[go.Table(header=dict(values=[filename]), cells=dict(values=[all]))])
        fig.show()


if __name__ == '__main__':
    ExtractData().Get_file("run_cmd.py")







