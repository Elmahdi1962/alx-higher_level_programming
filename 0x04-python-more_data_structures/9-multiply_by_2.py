#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    return dict(map(lambda item: (item[0], item[1] * 2), a_dictionary.items()))
