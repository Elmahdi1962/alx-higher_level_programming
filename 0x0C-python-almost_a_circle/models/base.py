#!/usr/bin/python3
'''Base Module / Task 1'''


import json
from os import path


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

    def from_json_string(json_string):
        '''returns a list object of the json string
        represenation json_string
        '''
        if json_string is None or len(json_string) <= 0:
            return []
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        '''creates new object of type cls and
        initialized with values in dictionary
        '''
        # creating dummy instance
        new_obj = cls(1, 1, 1, 1)
        # updating it using the update method
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances from the json file depends on the cls'''
        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.json'
        else:
            file_name = 'Square.json'

        if not path.exists(file_name) and not path.isfile(file_name):
            return []

        with open(file_name, mode='r', encoding='utf-8')as file:
            data = cls.from_json_string(file.read())

        obj_list = []
        for d in data:
            obj = cls.create(**d)
            obj_list.append(obj)

        return obj_list

    # ***************** End of Class Methods *****************
