#!/usr/bin/python3
"""this module defines a class Square."""


from typing import Type


class Square:
    """class for Square."""

    def __init__(self, size=0):
        """Initialize class and check if it's an integer and if less than 0."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
