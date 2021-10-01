#!/usr/bin/python3
'''this module do stuff to strings'''


def text_indentation(text):
    '''this function fixes text indentation
    args:
        text (str): text to fix
    returns:
        None
    '''

    if type(text) is not str:
        raise TypeError('text must be a string')

    fst_idx = 0
    for idx, char in enumerate(text):
        if char == '.' or char == '?' or char == ':':
            if (idx + 1) == len(text):
                tmp_str = text[fst_idx:]
            else:
                tmp_str = text[fst_idx:idx + 1]
            fst_idx = idx + 1
            print(tmp_str.strip())
            print()
            continue

        if idx == len(text) - 1:
            tmp_str = text[fst_idx:]
            print(tmp_str.strip())
