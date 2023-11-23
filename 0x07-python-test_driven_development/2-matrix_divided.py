#!/usr/bin/python3
"""
This module composed by a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        Divides all elments of a matrix.

        Args:
            matrix: matrix elements
            div: divide number

        Returns:
            New divided matrix
        
        Raises:
             TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero
    """
    row_len = 0
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_msg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(error_msg)
        if row_len and len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        
        for item in row:
            if not type(item) in (int, float):
                raise TypeError(error_msg)
        row_len = len(row)
    div_matrix = list(map(lambda row: list(map(lambda element: round(element / div, 2), row)), matrix))
    return (div_matrix)
