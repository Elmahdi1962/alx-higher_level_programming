#!/usr/bin/python3
'''module for task 1'''


class MyList(list):
    """class utilizing list class"""

    def print_sorted(self):
        """print sorted list"""
        res = list.copy(self)
        list.sort(res)
        print(res)
