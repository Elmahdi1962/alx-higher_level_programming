#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for key in sorted(a_dictionary.keys()):
        print('{:s}: {}'.format(key, a_dictionary[key]))
