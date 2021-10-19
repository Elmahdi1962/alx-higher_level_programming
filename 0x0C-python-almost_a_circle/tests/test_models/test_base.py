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

    def test_init(self):
        '''creating an instance of the class Base with out passing the id'''
        obj = Base()
        obj2 = Base()
        self.assertEqual(Base().id, 7)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj2.id, 6)
