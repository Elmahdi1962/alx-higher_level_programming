#!/usr/bin/python3
def remove_char_at(str, n):
    new = str[:n] + str[n + 1:]
    return new
