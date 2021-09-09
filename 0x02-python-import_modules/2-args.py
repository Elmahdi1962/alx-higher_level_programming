#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv) < 3:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg == sys.argv[0]:
                continue
            print("{}: {}".format(i, arg))
            i += 1
