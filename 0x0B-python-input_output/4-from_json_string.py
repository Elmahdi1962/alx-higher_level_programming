#!/usr/bin/python3
'''task 4 module'''


import json


def from_json_string(my_str):
    '''returns the str in the python nobject format'''
    return (json.loads(my_str))
