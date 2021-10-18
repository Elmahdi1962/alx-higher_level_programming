#!/usr/bin/python3
'''Base Module / Task 1'''


import json
import csv
import turtle
from math import sqrt
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
        """Creates the JSON representation of a list of dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: A JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if len(list_dictionaries) <= 0:
            return "[]"
        return json.JSONEncoder().encode(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns a list object of the json string
        represenation json_string
        '''
        if json_string is None or len(json_string) <= 0:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''opens a window and draws all the Rectangles and
        squares in the lists passed to it
        args:
            list_ractangles (Rectangle): list of rectangle objects
            list_squares (Square): list of square objects
        '''
        # finding the biggest width and height and number of shapes
        big_w = 0
        big_h = 0
        num_shapes = 0
        for rec in list_rectangles:
            bigt_w = rec.width if rec.width > big_w else big_w
            big_h = rec.height if rec.height > big_h else big_h
            num_shapes += 1
        for sq in list_squares:
            big_w = sq.width if sq.width > big_w else big_w
            big_h = sq.height if sq.height > big_h else big_h
            num_shapes += 1

        # calculate screen size
        per_side = sqrt(num_shapes)
        add_one = 1 if type(per_side) is float else 0
        screen_width = (int(per_side) + add_one) * big_w
        screen_height = (int(per_side) + add_one) * big_h

        # starting position of each row of drawings
        pos_w = -(screen_width / 2)
        pos_h = (screen_height / 2)

        # create turtle with name 't' and screen window and edit screen size
        window = turtle.Screen()
        window.setup(screen_width, screen_height, 0, 0)

        t = turtle.Turtle()
        turtle.bgcolor('black')
        turtle.title('Super Shape Painter XPlus Ver 1.0.0')
        # draw a border for  the screen
        b = turtle.Turtle()
        b.speed(0)
        b.hideturtle()
        b.pensize(3)
        b.color('yellow')
        b.penup()
        b.setpos(pos_w - 2, pos_h + 2)
        b.pendown()
        b.fd(screen_width + 4)
        b.right(90)
        b.fd(screen_height + 4)
        b.right(90)
        b.fd(screen_width + 4)
        b.right(90)
        b.fd(screen_height + 4)
        b.right(90)

        t.speed(10)
        t.penup()
        t.setpos(pos_w, pos_h)
        num_of_draws = 0
        for obj in list_rectangles:
            if (num_of_draws >= per_side):
                num_of_draws = 0
                t.penup()
                pos_h = pos_h - big_h
                t.setpos(pos_w, pos_h)
            obj.draw_shape(t, obj, big_w)
            num_of_draws += 1

        for obj in list_squares:
            if (num_of_draws >= per_side):
                num_of_draws = 0
                t.penup()
                pos_h = pos_h - big_h
                t.setpos(pos_w, pos_h)
            obj.draw_shape(t, obj, big_w)
            num_of_draws += 1
        t.hideturtle()
        window.exitonclick()

    # ***************** End of Static Methods *****************

    # ***************** Class Methods *****************

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.json'
        elif cls.__name__ == 'Square':
            file_name = 'Square.json'
        else:
            return

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
        # check who is calling
        if cls.__name__ == 'Base':
            return
        elif cls.__name__ == 'Square':
            # creating dummy instance
            new_obj = cls(1)
        elif cls.__name__ == 'Rectangle':
            new_obj = cls(1, 1)

        # updating it using the update method
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances from the json file depends on the cls'''
        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.json'
        elif cls.__name__ == 'Square':
            file_name = 'Square.json'
        else:
            return

        # if dosen't exist or is not a file return empty list
        if not path.exists(file_name) or not path.isfile(file_name):
            return []

        with open(file_name, mode='r', encoding='utf-8')as file:
            data = cls.from_json_string(file.read())

        obj_list = []
        for d in data:
            obj = cls.create(**d)
            obj_list.append(obj)

        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''saves a list of objects to a csv file.
        custum csv serializer
        '''
        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.csv'
        elif cls.__name__ == 'Square':
            file_name = 'Square.csv'
        else:
            return

        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []

        with open(file_name, mode='w', encoding='utf-8') as file:
            if file_name == 'Rectangle.csv':
                field_names = ['id', 'width', 'height', 'x', 'y']
            else:
                field_names = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(file, delimiter=',',
                                        fieldnames=field_names)
            csv_writer.writeheader()

            for dict in list_dicts:
                csv_writer.writerow(dict)

    @classmethod
    def load_from_file_csv(cls):
        '''loads data from csv file
        and return a list of objects depends on the filename.
        custom csv deserializer
        '''
        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.csv'
        elif cls.__name__ == 'Square':
            file_name = 'Square.csv'
        else:
            return

        list_dicts = []
        # if dosen't exist or is not a file return empty list
        if not path.exists(file_name) or not path.isfile(file_name):
            return []
        with open(file_name, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')

            for line in csv_reader:
                list_dicts.append(line)

        for i in range(len(list_dicts)):
            for key, value in list_dicts[i].items():
                try:
                    list_dicts[i][key] = int(value)
                except Exception:
                    continue

        list_objs = []
        for d in list_dicts:
            new_obj = cls.create(**d)
            list_objs.append(new_obj)

        return list_objs

    @classmethod
    def draw_shape(cls, t, obj, big_w):
        '''draw th shape of the class passed to it'''
        t.begin_fill()
        t.fillcolor('red' if cls.__name__ == 'Rectangle' else 'Blue')
        t.pendown()
        t.fd(obj.width)
        t.right(90)
        t.fd(obj.height)
        t.right(90)
        t.fd(obj.width)
        t.right(90)
        t.fd(obj.height)
        t.end_fill()
        t.right(90)
        t.penup()
        t.fd(big_w)

    # ***************** End of Class Methods *****************
