#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return

    counter = 0
    try:
        for i in range(0, x):
            intCondition = isinstance(my_list[i], int)
            if intCondition is True:
                print("{:d}".format(my_list[i]), end="")
                counter += 1

    except IndexError:
        raise IndexError
    else:
        print()
        return counter
