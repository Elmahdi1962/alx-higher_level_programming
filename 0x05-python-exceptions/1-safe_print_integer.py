#!/usr/bin/python3
def safe_print_integer(value):
    is_int = True
    try:
        if value == True or value == False:
            raise ValueError
        print("{:d}".format(value))
    except ValueError:
        is_int = False
    return is_int
