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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    #  height Property
    @property
    def height(self):
        '''retrieves the __height attribute value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the new value to the __height attribute'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    #  x Property
    @property
    def x(self):
        '''retrieves the __x attribute value'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets the new value to the __x attribute'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    #  y Property
    @property
    def y(self):
        '''retrieves the __y attribute value'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets the new value to the __y attribute'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
