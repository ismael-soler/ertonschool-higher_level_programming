#!/usr/bin/python3

for numA in range(0, 9):
    for numB in range(numA + 1, 10):
        if (numA == 8 and numB == 9):
            print("{}{}".format(numA, numB))
        else:
            print("{}{}".format(numA, numB), end=", ")