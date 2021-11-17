#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    lst = reversed(my_list)
    for int in lst:
        print("{:d}".format(int))
