#!/usr/bin/python3
"""creates class Square."""


class Square:
    """ Square class defined
        Attributes:
            size (int): Size of square
            position (tuple): position of space and new lines
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes
        Args:
            size (int): size
            postion(tuple): postion
        Returns:
            None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """getter of size
        Returns:
            size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size
        args:
            value (int): size of square.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter of position.
        Returns:
            position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position.
        args:
            value (tuple): position.
        """
        if type(value) != tuple or type(value[0]) != int or type(value[1]) != int or value[0] < 0 or value[1] < 0 or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns Square surface.
        Returns:
            Square surface.
        """
        return self.__size * self.__size

    def my_print(self):
        """print a square.
        Returns:
            None.
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
