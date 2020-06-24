#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from abc import abstractmethod

class Builder:

    def __init__(self):
        pass

    @abstractmethod
    def get_inform(self, cmd_file):
        pass

    @abstractmethod
    def draw(self):
        pass





