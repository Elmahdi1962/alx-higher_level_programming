#!/usr/bin/python3
'''task 6 module'''


import json


def load_from_json_file(filename):
    '''loads json from file and convert it to pyobject'''
    with open(filename, mode='r', encoding='utf-8') as f:
        my_object = json.load(f)
    return my_object
