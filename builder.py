#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def get_inform(self):
        pass

    @abstractmethod
    def draw(self):
        pass





