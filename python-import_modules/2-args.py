#!/usr/bin/python3

from ast import arg


if __name__ == "__main__":
    from sys import argv


    argCount = len(argv) - 1

    if (argCount == 0):
        print("{} arguments.".format(argCount))
    else:
        print("{} arguments:".format(argCount))

    for i in range(1, argCount + 1):
        print("{}: {}".format(i, argv[i]))