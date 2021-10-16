#!/usr/bin/python3
'''UnitTesting  the base module'''


import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
import pycodestyle
import os
import inspect
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''this class for testing the Rectangle class'''

    def test_pep_style(self):
        '''testing pycodestyle in Rectangle class'''
        style = pycodestyle.StyleGuide()
        check = style.check_files(
            [os.path.abspath(inspect.getsourcefile(Rectangle))])
        self.assertEqual(check.total_errors, 0,
                         'PEP8 style errors: %d' % check.total_errors)

    def test_init_Rectangle_obj_1(self):
        '''creating an instance of the class Rectangle with out passing the id
        only height and width
        '''
        obj = Rectangle(5, 8)
        self.assertEqual(obj.id, 2)

    def test_init_Rectangle_obj_2(self):
        '''creating an instance of the class Rectangle with specifying
        the id and height and width
        '''
        obj = Rectangle(5, 8, id=124)
        self.assertEqual(obj.id, 124)

    def test_init_Rectangle_obj_full(self):
        '''creating a rectangle bject the right way'''
        obj = Rectangle(5, 2, 0, 0, 12)
        self.assertEqual(obj.height, 2)  # height
        self.assertEqual(obj.width, 5)  # width
        self.assertEqual(obj.x, 0)  # x
        self.assertEqual(obj.y, 0)  # y
        self.assertEqual(obj.id, 12)  # id
        self.assertEqual(obj.area(), 10)  # area
        buf = StringIO()
        with redirect_stdout(buf):
            obj.display()
        self.assertEqual(buf.getvalue(), '#####\n#####\n')  # display
        obj.update(13, 4, 1, 1, 1)  # update using non named args
        self.assertEqual(obj.height, 1)  # height
        self.assertEqual(obj.width, 4)  # width
        self.assertEqual(obj.x, 1)  # x
        self.assertEqual(obj.y, 1)  # y
        self.assertEqual(obj.id, 13)  # id
        self.assertEqual(obj.area(), 4)  # area
        obj.update(
                    id=15,
                    width=6,
                    height=3,
                    x=2,
                    y=2
                    )  # update using named args
        self.assertEqual(obj.height, 3)  # height
        self.assertEqual(obj.width, 6)  # width
        self.assertEqual(obj.x, 2)  # x
        self.assertEqual(obj.y, 2)  # y
        self.assertEqual(obj.id, 15)  # id
        self.assertEqual(obj.area(), 18)  # area

    def test_rectangle_to_dictionary(self):
        '''test the to_dictionary method in the rectangle class'''
        obj = Rectangle(3, 2, 0, 0, 25)
        self.assertEqual(obj.to_dictionary(), {
                                            'id': 25,
                                            'x': 0,
                                            'y': 0,
                                            'width': 3,
                                            'height': 2
                                            })

    def test_rectangle_setters(self):
        '''test setters in the rectangle class'''
        with self.assertRaises(TypeError):  # width TypeError
            obj = Rectangle('2', 5, 0, 0)
        with self.assertRaises(ValueError):  # width ValueError
            obj = Rectangle(0, 5, 0, 0)

        with self.assertRaises(TypeError):  # height TypeError
            obj = Rectangle(2, '5', 0, 0)
        with self.assertRaises(ValueError):  # height ValueError
            obj = Rectangle(2, 0, 0, 0)

        with self.assertRaises(TypeError):  # x TypeError
            obj = Rectangle(1, 5, '0', 0)
        with self.assertRaises(ValueError):  # x ValueError
            obj = Rectangle(1, 5, -10, 0)

        with self.assertRaises(TypeError):  # y TypeError
            obj = Rectangle(2, 5, 0, '0')
        with self.assertRaises(ValueError):  # y ValueError
            obj = Rectangle(1, 5, 0, -2)

    def test_printing_rectangle_obj(self):
        '''testing the __str__ method in the class rectangle'''
        obj = Rectangle(1, 1, 2, 2, 10)
        buf = StringIO()
        with redirect_stdout(buf):
            print(obj)
            self.assertEqual(buf.getvalue(), '[Rectangle] (10) 2/2 - 1/1\n')
