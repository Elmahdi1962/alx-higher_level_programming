#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = [0 for i in my_list]
    for idx, val in enumerate(my_list):
        if val == search:
            new_list[idx] = replace
        else:
            new_list[idx] = val
    return new_list
