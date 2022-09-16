#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        return
    condition = False

    try:
        print("{:d}".format(value))
        condition = True

    except:
        condition = False


    return condition
