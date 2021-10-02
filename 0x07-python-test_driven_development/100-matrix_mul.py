#!/usr/bin/python3
'''module for marices calculations'''


def matrix_mul(m_a, m_b):
    '''this function multplies two matrices
    args:
        m_a (list of list of int or float): matrix a
        m_b (list of list of int or float): matrix b
    returns:
        a matrix result of there multiplication
    '''

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    elif type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for l in m_a:
        if type(l) is not list:
            raise TypeError('m_a must be a list of lists')
    for l in m_b:
        if type(l) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for l in m_a:
        if len(l) == 0:
            raise ValueError("m_a can't be empty")
    for l in m_b:
        if len(l) == 0:
            raise ValueError("m_b can't be empty")

    for l in m_a:
        for e in l:
            if type(e) is not int and type(e) is not float:
                raise TypeError(
                    'm_a should contain only integers or floats'
                    )

    for l in m_b:
        for e in l:
            if type(e) is not int and type(e) is not float:
                raise TypeError(
                    'm_b should contain only integers or floats'
                    )

    size = len(m_a[0])
    for l in m_a:
        if len(l) != size:
            raise TypeError(
                'each row of m_a must be of the same size'
                )

    size = len(m_b[0])
    for l in m_b:
        if len(l) != size:
            raise TypeError(
                'each row of m_b must be of the same size'
                )

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = list()
    c_size = len(m_a[0])

    for l in m_a:
        ls = []
        i = 0   # for b
        n = 0   # for a
        j = 0   # for ls
        for c in range(c_size):
            ls.append(0)
            for r in m_b:
                ls[j] += r[i] * l[n]
                n += 1
            i += 1
            n = 0
            j += 1
        new_matrix.append(ls)

    return new_matrix
