#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    big = 0
    for int in my_list:
        if int > big:
            big = int
    return big
