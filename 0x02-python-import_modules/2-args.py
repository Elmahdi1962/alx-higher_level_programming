#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) < 3:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))
    for arg in argv[1:]:
        if arg == argv[0]:
            continue
        print("{}: {}".format(i, arg))
        i += 1
