#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for j in range(0, len(row)):
            if j == len(row) - 1:
                print(row[j])
            else:
                print(row[j], end=" ")
