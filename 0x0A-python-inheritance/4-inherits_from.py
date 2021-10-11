#!/usr/bin/python3
'''module for task 4'''


def inherits_from(obj, a_class):
    '''
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False
    '''
    return type(obj) != a_class and issubclass(type(obj), a_class)
