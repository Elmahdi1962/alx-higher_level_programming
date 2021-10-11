#!/usr/bin/python3
'''module for task 1'''


class MyList(list):
    def print_sorted(self):
        newl = []
        for e in sorted(self):
            newl.append(e)
        print(newl)
