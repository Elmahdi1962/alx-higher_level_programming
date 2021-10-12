#!/usr/bin/python3
'''task 9 module'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''Initialization of the student object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return a dictionary representation of a Student instance'''
        return self.__dict__
