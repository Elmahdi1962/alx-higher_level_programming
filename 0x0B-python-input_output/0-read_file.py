#!/usr/bin/python3
'''module for task 0'''


def read_file(filename=""):
    '''reads a file in utf-8 encoding'''
    with open(filename, encoding='utf-8') as f:
        txt = f.read()
    print(txt, end='')
