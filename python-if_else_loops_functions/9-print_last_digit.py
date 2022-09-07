#!/usr/bin/python3
from asyncio.windows_events import NULL


def print_last_digit(number):
    if (number >= 48 and number <= 57):
        numberStr = repr(number)
        print("{}".format(numberStr[-1]), end="")
        return (numberStr[-1])
    return
