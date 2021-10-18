#!/usr/bin/python3
'''rectangle Module / task 2
'''
from .base import Base


class Rectangle(Base):
    '''Rectangle Class that inherits
    from Base Class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle object.
        Args:
            width (int): The width of this rectangle.
            height (int): The height of this rectangle.
            x (int): The horizontal position of this rectangle.
            y (int): The vertical position of this rectangle.
            id (int): The id of this rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''retrieves the __width attribute value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the new value to the __width attribute
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''retrieves the __height attribute value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the new value to the __height attribute
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''retrieves the __x attribute value
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets the new value to the __x attribute
        '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''retrieves the __y attribute value
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets the new value to the __y attribute
        '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the rectangle area
        Returns:
            the calculation result "the area"
        '''
        return self.width * self.height

    def display(self):
        '''prints the rectangle instance with the # character'''
        buffer = [' ' * self.x + '#' * self.width for h in range(self.height)]
        print('\n' * self.y + '\n'.join(buffer))

    def update(self, *args, **kwargs):
        '''Updates the instance attributes from
        the arguments passed in a strict order
        or from the kwargs
        '''
        i = 0
        attributes = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for attr in attributes:
                if i > len(args) - 1:
                    break
                setattr(self, attr, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle instance'''
        return {
                'id': self.id,
                'x': self.x,
                'y': self.y,
                'width': self.width,
                'height': self.height
                }

    def __str__(self):
        '''returns the string representation fo the instance'''
        fh = '[Rectangle] ({:d}) {:d}/{:d}'.format(self.id, self.x, self.y)
        sh = ' - {:d}/{:d}'.format(self.width, self.height)
        return fh + sh
