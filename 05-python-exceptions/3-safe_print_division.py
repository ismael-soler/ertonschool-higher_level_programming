#!/usr/bin/python3
def safe_print_division(a, b):
    if a is None or b is None:
        return

    toReturn = 0
    try:
        divResult = a/b
        toReturn = divResult

    except ZeroDivisionError:
        toReturn = None

    finally:
        print("Inside result: {}".format(toReturn))

    return toReturn
