#!/usr/bin/python3
from decimal import DivisionByZero


def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is None or my_list_2 is None or list_length is None:
        return

    result = []

    for i in range(list_length):
        try:
            result.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            continue

    return result
