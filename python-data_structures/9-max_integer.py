#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        return None
    currentBigger = 0
    for i in my_list:
        if i > currentBigger:
            currentBigger = i
    return currentBigger
