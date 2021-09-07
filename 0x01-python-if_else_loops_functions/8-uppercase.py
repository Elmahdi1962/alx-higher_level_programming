#!/usr/bin/python3
def uppercase(str):
    for char in str[:-2]:
        print("{}".format(chr(ord(char) - 32)), end="")
    print("{}".format(chr(ord(str[-1]) - 32)))
	