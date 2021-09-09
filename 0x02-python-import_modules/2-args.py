#!/usr/bin/python3
import sys


def main(argv):

    if len(argv) - 1 == 0:
        print("0 arguments.")
    elif len(argv) - 1 == 1:
        print("{:d} argument:".format(len(argv) - 1))
        print("{:d}: {}".format(len(argv) - 1, argv[1]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for i, x in enumerate(argv[1:], 1):
            print("{:d}: {}".format(i, x))

if __name__ == "__main__":
    import sys
