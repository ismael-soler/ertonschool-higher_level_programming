#!/usr/bin/python3
""" returns a list of list of integers representing the Pascal's triangle """


def pascal_triangle(n):
    """ creates the triangle """
    if n <= 0 :
        return []

    listOfLists = []
    for i in range(n):
        rowList = []
        row = pow(11, i)
        for number in str(row):
            rowList.append(int(number))
        listOfLists.append(rowList)
    return listOfLists
