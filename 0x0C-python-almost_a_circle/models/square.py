#!/usr/bin/python3
'''square Module / task 10'''


from .rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization of the instance'''
        super().__init__(size, size, x, y, id)

    # ********** Getters and Setters Section ***********

    @property
    def size(self):
        '''retrieves the size => width attribute'''
        return self.width

    @size.setter
    def size(self, value):
        '''sets the new vale to the size attribute => width and height'''
        self.width = value
        self.height = value

    # ********** End of Getters and Setters Section ****

    # ********** Instance Methods Section **************

    def update(self, *args, **kwargs):
        '''Updates the instance attributes from
        the arguments passed in a strict order
        or from the kwargs
        '''
        i = 0
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for attr in attributes:
                if i > len(args) - 1:
                    break
                setattr(self, attr, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # ********** End of Instace Methods Section ********

    # ********** Magic Methods Section *****************

    def __str__(self):
        '''returns the string representation of the instance'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    # ********** End of Magic Methods Section **********
