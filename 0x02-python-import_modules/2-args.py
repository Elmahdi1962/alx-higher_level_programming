#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = 1
    argc = len(sys.argv) - i
    print('{:d} argument{:s}{:s}'.format(
        argc, 's' * (argc != 1),
        ':' if argc > 0 else '.'
        ))
    for arg in sys.argv[i:]:
        print('{:d}: {:s}'.format(i, arg))
        i += 1
