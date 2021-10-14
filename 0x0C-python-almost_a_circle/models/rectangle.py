#!/usr/bin/python3
'''rectangle Module / task 2'''

from .base import Base


class Rectangle(Base):
    '''Rectangle Class that inherits from Base Class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    #  width Property
    @property
    def width(self):
        '''retrieves the __width attribute value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the new value to the __width attribute'''
        self.__width = value

    #  height Property
    @property
    def height(self):
        '''retrieves the __height attribute value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the new value to the __height attribute'''
        self.__height = value

    #  x Property
    @property
    def x(self):
        '''retrieves the __x attribute value'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets the new value to the __x attribute'''
        self.__x = value

    #  y Property
    @property
    def y(self):
        '''retrieves the __y attribute value'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets the new value to the __y attribute'''
        self.__y = value
