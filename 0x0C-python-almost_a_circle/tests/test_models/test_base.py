#!/usr/bin/python3
'''UnitTesting  the base module'''


import unittest
import pycodestyle
import os
import inspect
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''this class for testing the base class'''

    def test_pep_style(self):
        '''testing pycodestyle in class Base'''
        style = pycodestyle.StyleGuide()
        check = style.check_files(
            [os.path.abspath(inspect.getsourcefile(Base))])
        self.assertEqual(check.total_errors, 0,
                         'PEP8 style errors: %d' % check.total_errors)

    def test_init_base_obj_1(self):
        '''creating an instance of the class Base with out passing the id'''
        obj = Base()
        obj2 = Base()
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj2.id, 6)

    def test_init_base_obj_2(self):
        '''creating an instance of the class Base with specifying the id'''
        obj = Base(123)
        self.assertEqual(obj.id, 123)

    def test_saving_to_file_empty_list(self):
        """Test saving emplty list and loading from empty file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_saving_to_file_None(self):
        """
        Test passing the save_to_file method None and load it
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))


    def test_to_json_string_AND_from_json_string_rec(self):
        '''test the to_json_string and from_json_string methods with the Rectangle class'''
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_to_json_string_AND_from_json_string_sqr(self):
        '''test the to_json_string and from_json_string methods with the Square class'''
        list_input = [
            {'id': 99, 'size': 10},
            {'id': 9, 'size': 1}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_save_to_file_AND_load_from_file(self):
        '''testing save_to_file and load_from_file methods'''
        # testing for the rectangle class
        r1 = Rectangle(5, 3)
        r2 = Rectangle(6, 2)
        list_rectangles_input = [r1, r2]

        # save a file and check f the file is created and is a file
        Rectangle.save_to_file(list_rectangles_input)
        self.assertTrue(os.path.isfile('Rectangle.json'))
        # check if the file is fnot empty
        with open('Rectangle.json', 'r') as f:
            r_total = sum(1 for _ in f)
        self.assertGreater(r_total, 0)

        # load data from the rectangle json file
        list_rectangles_output = Rectangle.load_from_file()
        #check if the objects in the lists are rectangles
        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

        # now testing for the square class-----------
        s1 = Square(5, 1, 1)
        s2 = Square(2, 2, 2)
        list_squares_input = [s1, s2]

        # save data to file and check if created and is a file
        Square.save_to_file(list_squares_input)
        self.assertTrue(os.path.isfile('Square.json'))

        # check if file is not empty
        with open('Square.json', 'r') as f:
            s_total = sum(1 for _ in f)
        self.assertGreater(s_total, 0)

        # load data from the square json file
        list_squares_output = Square.load_from_file()

        # check if lists have square objects
        for square in list_squares_input:
            self.assertIsInstance(square, Square)

        for square in list_squares_output:
            self.assertIsInstance(square, Square)

    def test_create(self):
            '''Tests the create method of the Base class.
            '''
            polygon = Base.create(**{
                'id': '89',
            })
            self.assertIsNone(polygon)
            # region Rectangle
            polygon = Rectangle.create(**{
                'id': '89', 'width': 3, 'height': 5,
                'x': 8, 'y': 16
            })
            self.assertEqual(polygon.id, '89')
            self.assertEqual(polygon.width, 3)
            self.assertEqual(polygon.height, 5)
            self.assertEqual(polygon.x, 8)
            self.assertEqual(polygon.y, 16)
            polygon = Rectangle.create(**{
                'id': None, 'width': 3, 'height': 5,
                'x': 8, 'y': 16, 'foo': 23
            })
            self.assertEqual(polygon.id, None)
            self.assertEqual(polygon.width, 3)
            self.assertEqual(polygon.height, 5)
            self.assertEqual(polygon.x, 8)
            self.assertEqual(polygon.y, 16)
            with self.assertRaises(AttributeError):
                print(polygon.foo)
            # endregion
            # region Square
            polygon = Square.create(**{
                'id': '89', 'width': 3, 'height': 5,
                'size': 15, 'x': 8, 'y': 16
            })
            self.assertEqual(polygon.id, '89')
            self.assertEqual(polygon.size, 15)
            self.assertEqual(polygon.x, 8)
            self.assertEqual(polygon.y, 16)
            polygon = Square.create(**{
                'id': None, 'width': 13, 'height': 25,
                'x': 8, 'y': 16, 'foo': 34
            })
            self.assertEqual(polygon.id, None)
            self.assertNotEqual(polygon.size, 13)
            self.assertNotEqual(polygon.width, 13)
            self.assertNotEqual(polygon.height, 25)
            self.assertEqual(polygon.size, polygon.width)
            self.assertEqual(polygon.size, polygon.height)
            self.assertEqual(polygon.x, 8)
            self.assertEqual(polygon.y, 16)
            with self.assertRaises(AttributeError):
                print(polygon.foo)
            # endregion

class Test_Base_csv_file_save_load(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual('id,size,x,y\n', f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual('id,size,x,y\n', f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class Test_Base_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)
