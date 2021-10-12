#!/usr/bin/python3
'''task 2 module'''


def append_write(filename="", text=""):
    '''appends text to a file'''
    with open(filename, mode='a', encoding='utf-8') as f:
        len = f.write(text)
    return len
