#!/usr/bin/python3
for i in range(10):
    for n in range(i, 10):
        if n != i and (i != 8 or n != 9):
            print("{}{}, ".format(i, n), end="")
        elif i == 8 and n == 9:
            print("{}{}".format(i, n))
