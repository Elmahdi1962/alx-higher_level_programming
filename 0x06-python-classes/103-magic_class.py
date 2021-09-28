#!/usr/bin/python
import math
"""defining magic class"""





class MagicClass:
    def __init__(self, radius):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.radius = None

    def area(self):
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        return self.__radius * (2 * math.pi)
