#!/usr/bin/python3
def raise_exception_msg(message=""):
    if message is None:
        return

    print(message, end="")
    raise NameError
