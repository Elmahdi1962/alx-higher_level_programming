#!/usr/bin/python3
"""Module for matrix Calculations"""


def matrix_divided(matrix, div):
    '''This function devides all elements of a matrix
    args:
        matrix (list): list of lists of integers/floats
        div (int): integer or float
    returns:
        a new matrix
    '''
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    fst_lst_len = len(matrix[0])
    new_matrix = list()

    for lst in matrix:
        if len(lst) != fst_lst_len:
            raise TypeError('Each row of the matrix must have the same size')

        new_list = list()

        for e in lst:
            if type(e) is not int and type(e) is not float:
                raise TypeError(
                    'matrix must be a matrix(list of lists) of integers/floats'
                    )
            new_list.append(round(e / div, 2))

        new_matrix.append(new_list)

    return new_matrix
