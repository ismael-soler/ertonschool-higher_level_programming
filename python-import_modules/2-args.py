#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argCount = len(argv) - 1

# PRINTING FIRST LINE
    if (argCount == 0):
        print("{} arguments.".format(argCount))
    elif (argCount == 0 or argCount != 1):
        print("{} arguments:".format(argCount))
    else:
        print("{} argument:".format(argCount))

# PRINTING ARGUMENTS
    for i in range(1, argCount + 1):
        print("{}: {}".format(i, argv[i]))
