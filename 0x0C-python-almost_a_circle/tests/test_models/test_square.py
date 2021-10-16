#!/usr/bin/python3
'''UnitTesting  the Square module'''


import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
import pycodestyle
import os
import inspect
from models.square import Square


class TestSquare(unittest.TestCase):
    '''this class for testing the Square class'''

    def test_pep_style(self):
        '''testing pycodestyle in Square class'''
        style = pycodestyle.StyleGuide()
        check = style.check_files(
            [os.path.abspath(inspect.getsourcefile(Square))])
        self.assertEqual(check.total_errors, 0,
                         'PEP8 style errors: %d' % check.total_errors)

    def test_init_Square_obj_1(self):
        '''creating an instance of the class Square with  passing only
        the size
        '''
        obj = Square(5)
        self.assertEqual(obj.width, 5)  # width
        self.assertEqual(obj.height, 5)  # height

    def test_init_Square_obj_2(self):
        '''creating an instance of the class Square with specifying
        the id and size
        '''
        obj = Square(6, id=120)
        self.assertEqual(obj.id, 120)  # id
        self.assertEqual(obj.width, 6)  # width
        self.assertEqual(obj.height, 6)  # height
        self.assertEqual(obj.size, 6)  # size

    def test_init_Square_obj_full(self):
        '''creating a square object the right way'''
        obj = Square(5, 0, 0, 111)
        self.assertEqual(obj.height, 5)  # height
        self.assertEqual(obj.width, 5)  # width
        self.assertEqual(obj.size, 5)  # size
        self.assertEqual(obj.x, 0)  # x
        self.assertEqual(obj.y, 0)  # y
        self.assertEqual(obj.id, 111)  # id

    def test_Square_area(self):
        '''test the area method in the Square class'''
        obj = Square(5, 0, 0, 122)
        self.assertEqual(obj.area(), 25)  # area

    def test_Square_obj_update(self):
        '''testing the update function of the Square class'''
        obj = Square(5, 0, 0, 70)

        # update using non named args
        obj.update(2, 1, 1, 50)
        self.assertEqual(obj.height, 1)  # height
        self.assertEqual(obj.width, 1)  # width
        self.assertEqual(obj.size, 1)  # size
        self.assertEqual(obj.x, 1)  # x
        self.assertEqual(obj.y, 50)  # y
        self.assertEqual(obj.id, 2)  # id
        self.assertEqual(obj.area(), 1)  # area

        # update using non named args with wrong type
        with self.assertRaises(TypeError):
            obj.update(13, '1', 1, 190)

        # update using non named args with wrong value
        with self.assertRaises(ValueError):
            obj.update(13, -1, 1, 40)

        # update using named args
        obj.update(
                    id=15,
                    size=6,
                    x=2,
                    y=2
                    )
        self.assertEqual(obj.height, 6)  # height
        self.assertEqual(obj.width, 6)  # width
        self.assertEqual(obj.size, 6)  # size
        self.assertEqual(obj.x, 2)  # x
        self.assertEqual(obj.y, 2)  # y
        self.assertEqual(obj.id, 15)  # id
        self.assertEqual(obj.area(), 36)  # area

        # update using named args with wrong value
        with self.assertRaises(ValueError):
            obj.update(
                        id=15,
                        size=4,
                        x=-5,
                        y=6
                        )
        self.assertEqual(obj.height,4)  # height
        self.assertEqual(obj.width, 4)  # width
        self.assertEqual(obj.size, 4)  # size
        self.assertEqual(obj.x, 2)  # x
        self.assertEqual(obj.y, 2)  # y
        self.assertEqual(obj.id, 15)  # id
        self.assertEqual(obj.area(), 16)  # area

        # update using named args with wrong type
        with self.assertRaises(TypeError):
            obj.update(
                        id=15,
                        size=6,
                        x=5,
                        y='6'
                        )

    def test_Square_to_dictionary(self):
        '''test the to_dictionary method in the square class'''
        obj = Square(3, 0, 0, 25)
        self.assertEqual(obj.to_dictionary(), {
                                            'id': 25,
                                            'size': 3,
                                            'x': 0,
                                            'y': 0,
                                            })

    def test_Square_setters(self):
        '''test setters in the square class'''
        with self.assertRaises(TypeError):  # size / width TypeError
            obj = Square('2', 0, 0)
        with self.assertRaises(ValueError):  # size / width ValueError
            obj = Square(0, 0, 0)

        with self.assertRaises(TypeError):  # x TypeError
            obj = Square(1, '0', 0)
        with self.assertRaises(ValueError):  # x ValueError
            obj = Square(1, -10, 0)

        with self.assertRaises(TypeError):  # y TypeError
            obj = Square(2, 0, '0')
        with self.assertRaises(ValueError):  # y ValueError
            obj = Square(1, 0, -2)

    def test_printing_Square_obj(self):
        '''testing the __str__ method in the class square'''
        obj = Square(1, 2, 2, 10)
        buf = StringIO()
        with redirect_stdout(buf):
            print(obj)
            self.assertEqual(buf.getvalue(), '[Square] (10) 2/2 - 1\n')

    def test_Square_display(self):
        '''testing the display method in the Square class'''
        obj = Square(2, 2, 3, 100)
        buf = StringIO()
        with redirect_stdout(buf):
            obj.display()
        self.assertEqual(buf.getvalue(), '\n\n\n  ##\n  ##\n')  # display
