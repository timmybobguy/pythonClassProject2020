#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import os
import subprocess


class Site(metaclass=ABCMeta):

    def __init__(self, file):
        self.file = file

    def get_file(self):
        name = os.path.basename(self.file)
        return name


    @abstractmethod
    def get_diagram(self):
        pass

    def run(self):
        p = self.get_diagram()
        subprocess.run(p, cwd= os.path.dirname(self.file), shell=True)


class SvgSite(Site):
    def __init__(self, file):
        super().__init__(file)

    def get_diagram(self):
        command = "pyreverse {0} -o svg -p diagram".format(self.file)
        return command
    


if __name__ == '__main__':
    svg = SvgSite("/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py")
    svg.get_diagram()
    svg.run()


