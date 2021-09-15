#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda l: map(lambda n: n * n, l), matrix))
