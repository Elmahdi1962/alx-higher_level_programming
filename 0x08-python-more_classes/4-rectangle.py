#!/usr/bin/python3

'''module for shapes'''


class Rectangle:
    '''class for rectangle'''

    def __init__(self, width=0, height=0):
        '''Initiation of object'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets the width attr'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width attr'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''gets the height attr'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height attr'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__height * self.width

    def perimeter(self):
        '''return the perimeter of the rectangle'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            hashes = '#' * self.__width
            return '\n'.join(hashes for h in range(self.__height))

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))
