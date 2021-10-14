#!/usr/bin/python3
'''Base Module / Task 1'''


import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization of the Base instance
        args:
            id (int): id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # ***************** Static Methods *****************

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the Json string reprisentaion
        of the argument list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    # ***************** End of Static Methods *****************

    # ***************** Class Methods *****************

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.json'
        else:
            file_name = 'Square.json'

        if list_objs is None:
            list_objs = []
        else:
            list_objs = list(map(lambda obj: obj.to_dictionary(), list_objs))

        json_list_objs = Base.to_json_string(list_objs)

        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write(json_list_objs)

    # ***************** End of Class Methods *****************
