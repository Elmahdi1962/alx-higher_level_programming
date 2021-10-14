#!/usr/bin/python3
'''square Module / task 10'''


from .rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization of the instance'''
        super().__init__(size, size, x, y, id)

    # ********** Magic Methods Section **********

    def __str__(self):
        '''returns the string representation of the instance'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    # ********** End of Magic Methods Section **********
