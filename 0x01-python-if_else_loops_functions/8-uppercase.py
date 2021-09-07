#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        char = ord(i)
        if ord('a') <= char <= ord('z'):
            char = char - 32
        new_str += chr(char)
    print("{}".format(new_str))
