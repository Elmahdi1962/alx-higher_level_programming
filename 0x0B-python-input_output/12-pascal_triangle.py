#!/usr/bin/python3
'''task 12 module'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''
    if n <= 0:
        return list()

    tr = []
    for line in range(0, n):
        # Every line has number of
        # integers equal to line
        # number
        tmp = []
        for i in range(0, line + 1):
            tmp.append(magic(line, i))
        tr.append(tmp)
    return tr


def magic(n, k):
    '''magic function that does some magic'''
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
