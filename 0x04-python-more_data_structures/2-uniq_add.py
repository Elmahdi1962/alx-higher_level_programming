#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    list = set(my_list)
    result = 0
    for n in list:
        result += n
    return result
