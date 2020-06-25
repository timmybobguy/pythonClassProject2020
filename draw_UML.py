#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import os
import subprocess


class Site(metaclass=ABCMeta):

    def __init__(self, file):
        self.file = file
        self.p = ""

    @abstractmethod
    def get_diagram(self):
        pass

    def run(self):
        subprocess.run(self.p, cwd=os.path.dirname(self.file), shell=True)

    def run_all(self):
        self.get_diagram()
        self.run()


class SvgSite(Site):
    def __init__(self, file):
        super().__init__(file)

    def get_diagram(self):
        self.p = "pyreverse {0} -o svg -p diagram".format(self.file)


class FigSite(Site):
    def __init__(self, file):
        super().__init__(file)

    def get_diagram(self):
        self.p = "pyreverse {0} -o fig -p diagram".format(self.file)


class DotSite(Site):
    def __init__(self, file):
        super().__init__(file)

    def get_diagram(self):
        self.p = "pyreverse {0} -o dot -p diagram".format(self.file)


if __name__ == '__main__':
    svg = SvgSite("/Users/jimmy/py/pythonClassProject2020/ppp_cmd.py")
    svg.run_all()




