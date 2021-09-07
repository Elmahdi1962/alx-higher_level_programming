#!/usr/bin/python3
def uppercase(str):
    string = [0] * len(str)
    for i in range(len(str)):
        if ord(str[i]) > 96:
            string[i] = chr(ord(str[i]) - 32)
        else:
            string[i] = str[i]
        if i != len(str) - 1:
            print("{}".format(string[i]), end="")
    print("{}".format(string[i]))
