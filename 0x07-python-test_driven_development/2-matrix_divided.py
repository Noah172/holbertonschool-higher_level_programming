#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix
>>> print(matrix_divided([[1, 2, 3], [4, 5, 6]], 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
    """
    neo = [[0, 0, 0], [0, 0, 0]]
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) > len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            neo[i][j] = float("{0:.2f}".format(value / div))
    return neo
