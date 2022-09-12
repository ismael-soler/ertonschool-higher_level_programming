#!/usr/bin/python3
def no_c(my_string):
    empty_string = ""
    i = 0
    for x in my_string:
        if x != 'C' and x != 'c':
            empty_string += x
    return empty_string
