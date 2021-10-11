#!/usr/bin/python3
'''task 7 module'''


class BaseGeometry:
    '''empty class'''
    def __init__(self):
        '''empty init'''
        pass

    def area(self):
        '''stupid function'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''another useless function'''
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
