#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    argCount = len(argv)

    totalSum = 0
    for i in range(1, argCount):
        totalSum += int(argv[i])

    print("{}".format(totalSum))
