#!/usr/bin/python3
""" divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """

    checkMatrixConditions(matrix, div)
    # return list(map(lambda l: list(map(lambda x: x / div, l)), matrix))
    return [list(map(lambda x: round(x / div, 2), listInMatrix))
            for listInMatrix in matrix]


def checkMatrixConditions(matrix, div):
    """ Checks if all conditions for the matrix are met"""

    # Check if matrix is a list
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    # Check if every member of the list is a list, and compares lengths
    prevLen = len(matrix[0])
    for listInMatrix in matrix:
        if not isinstance(listInMatrix, list):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
        if len(listInMatrix) != prevLen:
            raise TypeError("Each row of the matrix must have the same size")
        prevLen = len(listInMatrix)
        # Check if every element of the list of the list is an int or a float
        for j in listInMatrix:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    # Check for div conditions
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
