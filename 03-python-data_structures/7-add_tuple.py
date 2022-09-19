#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 1:
        newATuple = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        newATuple = (0, 0)
    else:
        newATuple = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 1:
        newBTuple = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        newBTuple = (0, 0)
    else:
        newBTuple = (tuple_b[0], tuple_b[1])

    tupleSum = ((newATuple[0] + newBTuple[0]), (newATuple[1] + newBTuple[1]))
    return (tupleSum)
