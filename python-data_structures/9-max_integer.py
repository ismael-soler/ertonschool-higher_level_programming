#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    currentBigger = 0
    for i in my_list:
        if i > currentBigger:
            currentBigger = i
    if currentBigger == 0:
        return -1
    return currentBigger
