#!/usr/bin/python3
""" this module defines a class Square"""


from typing import Type


class Square:
    """ class for Square"""
    def __init__(self, size=0):
        """ Initialize class and check if it's an integer and if less than 0
        args:
            size (int, optional): size of the square
        Raises:
            TypeError: raised when the arg size is not integer
            ValueError: raised when the arg size is lees than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
