#!/usr/bin/python3

'''module for shapes'''


class Rectangle:
    '''class for rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initiation of object'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        r1 = rect_1.width * rect_1.height
        r2 = rect_2.width * rect_2.height
        return (rect_1 if r1 > r2 or r1 == r2 else rect_2)

    @classmethod
    def square(cls, size=0):
        '''creates new instance with height and width == size'''
        return cls(size, size)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            hashes = "{}".format(self.print_symbol) * self.__width
            return '\n'.join(hashes for h in range(self.__height))

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
