#!/usr/bin/python3
'''task 1 module'''


def write_file(filename="", text=""):
    '''writes a string to  file overwrites if exist'''
    with open(filename, mode='w', encoding='utf-8') as f:
        len = f.write(text)

    return len
