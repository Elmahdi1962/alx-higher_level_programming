#!/usr/bin/python3
'''UnitTesting  the base module'''


import unittest
import pycodestyle
import os
import inspect
from models.base import Base


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
        self.assertEqual(obj.id, 1)

    def test_init_base_obj_2(self):
        '''creating an instance of the class Base with specifying the id'''
        obj = Base(123)
        self.assertEqual(obj.id, 123)
