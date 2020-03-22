#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import doctest
from checkfiles import CheckDirectory
# Wu, Chieh-Ming (Jimmy's work)


def CheckDirectory(path):
    """ add two number or string
    >>> add(1, 2)
    3

    >>> add("hello", " world")
    'hello world'

    >>> add(1, 2)
    5

    """
    return x+y


if __name__ == '__main__':
        doctest.testmod()