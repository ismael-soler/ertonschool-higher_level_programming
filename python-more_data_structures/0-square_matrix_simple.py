#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return

    newMatrix = []
    for i in range(0, len(matrix)):
        squareNum = list(map(lambda x: x*x, matrix[i]))
        newMatrix.append(squareNum)
    return newMatrix
