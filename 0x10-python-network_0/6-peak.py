#!/usr/bin/python3
# O(log(n))
def find_peak3(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not isinstance(list_of_integers, list) or len(list_of_integers) == 0:
        return None
    n = len(list_of_integers)
    mid = n // 2
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[0:mid - 1])
    elif mid + 1 < n and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:n])
    elif mid > 0 and list_of_integers[mid] == list_of_integers[mid - 1]:
        if n % 2 == 0:
            return find_peak(list_of_integers[0:mid])
        else:
            return find_peak(list_of_integers[mid:n])
    else:
        return list_of_integers[mid]
