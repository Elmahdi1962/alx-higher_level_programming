#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bgs = -1
    bgk = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > bgs:
            bgs = a_dictionary[key]
            bgk = key
    return bgk
