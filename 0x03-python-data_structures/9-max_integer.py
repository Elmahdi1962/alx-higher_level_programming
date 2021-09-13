#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1 or my_list is None:
        return None
    big = my_list[0]
    for int in my_list:
        if int > big:
            big = int
    return big
