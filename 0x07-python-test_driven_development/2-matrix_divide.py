#!/usr/bin/python3
"""Define a fucntionthat divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.

    Args:
        matrix (lists): List of list or interger or floats.
        div (int/float): the divider
    Raises:
        TypeError: if matrix contains non-numbers.
        TypeError: if matrix contains rows of different sizes.
        TypeError: if div is not int or float.
        ZeroDivisionError: if div is 0.
    Returns:
        New matris
    """

    if (not isinstance(matrix, list) or matrix ==[] or 
            not all(isinstance(row, list) for row in matrix) or 
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must ba a matrix(list of list) of"
                "interger/float")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TyperError("Each row of the matrix mest have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TyperError("div must be a number")
    if div ==0:
        reise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
