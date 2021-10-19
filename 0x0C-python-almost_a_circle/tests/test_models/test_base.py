#!/usr/bin/python3
'''UnitTesting  the base module'''


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''this class for testing the base class'''

    def test_init(self):
        '''creating an instance of the class Base with out passing the id'''
        obj = Base().id
        self.assertEqual(obj + 1, Base().id)
