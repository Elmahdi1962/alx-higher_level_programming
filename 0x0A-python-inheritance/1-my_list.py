#!/usr/bin/python3
'''module for task 1'''


class MyList(list):
    '''class that derives from list class'''

    def __init__(self):
        '''Initialization of the subclass'''
        super()
        pass

    def print_sorted(self):
        '''function that prints the list sorted way ascending'''
        nl = list.copy(self)
        list.sort(nl)
        print(nl)
