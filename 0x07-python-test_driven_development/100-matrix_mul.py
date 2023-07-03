#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(mat_a, mat_b):
    """Return the matrix resulting of
    the multiplication of m_a and m_b."""

    if type(mat_a) is not list:
        raise TypeError("mat_a must be a list")
    if type(mat_b) is not list:
        raise TypeError("mat_b must be a list")

    for x in mat_a:
        if type(x) is not list:
            raise TypeError("mat_a must be a list of lists")
    for x in mat_b:
        if type(x) is not list:
            raise TypeError("mat_b must be a list of lists")

    if mat_a == [] or mat_a == [[]]:
        raise ValueError("mat_a can't be empty")
    if mat_b == [] or mat_b == [[]]:
        raise ValueError("mat_b can't be empty")

    for row in mat_a:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("mat_a should contain only integers or floats")
    for row in mat_b:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("mat_b should contain only integers or floats")

    row_len = []
    for row in mat_a:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
            raise TypeError("each row of mat_a must should be of the same size")
    row_len = []
    for row in mat_b:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
            raise TypeError("each row of mat_b must should be of the same size")

    a_col = 0
    for col in mat_a[0]:
        a_col += 1
    b_row = 0
    for row in mat_b:
        b_row += 1

    if a_col != b_row:
        raise ValueError("mat_a and mat_b can't be multiplied")

    result = [[0 for x in range(len(mat_b[0]))] for y in range(len(mat_a))]

    for i in range(len(mat_a)):
        for j in range(len(mat_b[0])):
            for k in range(len(mat_b)):
                result[i][j] += mat_a[i][k] * mat_b[k][j]

    return result
