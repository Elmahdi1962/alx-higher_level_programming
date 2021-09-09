#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    res = 0
    for arg in argv[1:]:
        res += int(arg)
    print("{:d}".format(res))
