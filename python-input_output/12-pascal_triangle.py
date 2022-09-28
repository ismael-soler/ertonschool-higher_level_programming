#!/usr/bin/python3
""" returns a list of list of integers representing the Pascal's triangle """


def pascal_triangle(n):
    """ creates the triangle """
    if n <= 0:
        return []

    triangle = []
    triangle.append([1])
    firstLoop = True
    for i in range(1, n):
        triangle.append([1])
        for j in range(1, i + 1):
            try:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            except IndexError:
                triangle[i].append(1)
                continue

    return triangle
