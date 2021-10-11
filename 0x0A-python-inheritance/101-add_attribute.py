#!/usr/bin/python3
'''task 13 module'''


def add_attribute(object, name, value):
    '''this function adds new attr to the obj if possible'''
    if '__dict__' in dir(object) and type(object.__dict__) is dict:
        object.name = value
    else:
        raise TypeError("can't add new attribute")
