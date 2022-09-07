#!/usr/bin/python3
def print_last_digit(number):
    numberStr = repr(number)
    print("{}".format(numberStr[-1]), end="")
    return (numberStr[-1])
