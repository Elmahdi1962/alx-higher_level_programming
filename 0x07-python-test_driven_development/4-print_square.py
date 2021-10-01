#!/usr/bin/python3
'''This module for printing squares'''


def print_square(size):
    '''This function prints a square of size size
    args:
        size (int): size of the square
    returns:
        None
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for n in range(size):
            print('#', end='')
        print()
