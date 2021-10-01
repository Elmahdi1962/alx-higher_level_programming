#!/usr/bin/python3
'''This module for printing stuff'''


def say_my_name(first_name, last_name=""):
    '''This function print the string "My name is <first name> <last name>"
    args:
        first_name (str): first name
        last_name (str): last name
    returns:
        None
    '''

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
