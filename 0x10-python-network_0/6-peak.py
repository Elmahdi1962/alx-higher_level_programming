#!/usr/bin/python3
'''task 6 module'''


def find_peak(list_of_integers):
    '''finds a peak in a list of unsorted integers'''
    last_peak = None
    for idx, n in enumerate(list_of_integers):
        if idx > 0 and idx < len(list_of_integers) - 1:
            if n > list_of_integers[idx + 1]:
                if n > list_of_integers[idx - 1]:
                    return n
            elif n == list_of_integers[idx + 1]:
                if n == list_of_integers[idx - 1]:
                    if last_peak is not None and last_peak < n:
                        last_peak = n
                    elif last_peak is None:
                        last_peak = n
    if last_peak is not None:
        return last_peak
    return None
