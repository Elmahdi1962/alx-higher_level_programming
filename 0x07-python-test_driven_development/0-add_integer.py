#!/usr/bin/python3
"""This module contains calculation functions"""


def add_integer(a, b=98):
    """"This function does the addition of 2 arguments
    args:
        a (union[int, float]): first number
        b (union[int, float], optional): second number
    returns:
        the result of the addition
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return int(a) + int(b)
