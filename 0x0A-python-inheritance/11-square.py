#!/usr/bin/python3
'''task 9 module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''classy class'''
    def __init__(self, size):
        '''initialization of squar'''
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        '''get that number'''
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
