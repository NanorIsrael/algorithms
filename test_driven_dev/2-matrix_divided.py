#!/usr/bin/python3

"""
This module defines function that divides 
all elements of a matrix.


>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

>>> matrix_divided([[1, "2", 3], [4, 5, "6"]], 3)
Traceback (most recent call last):
    ...
TypeError: matrix value must be an integer or float
"""
def matrix_divided(matrix, div=None):
    if div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    prev_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != prev_row_length:
            raise NameError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
    return [[round((x / div), 2) for x in row] for row in matrix]