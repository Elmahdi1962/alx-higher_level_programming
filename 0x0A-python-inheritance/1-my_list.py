#!/usr/bin/python3
'''module for task 1'''


class MyList(list):
    '''class that derives from list class'''

    def print_sorted(self):
        '''function that prints the list sorted way ascending'''
        l = list.copy(self)
        list.sort(l)
        print(l)
