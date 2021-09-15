#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return dict(filter(lambda item: False if item[1] == value else True,
                a_dictionary.items()))
