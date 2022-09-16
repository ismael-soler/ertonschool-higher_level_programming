#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    i = 0
    totalSum = 0
    for i in range(0, len(roman_string)):
        # Get value of the first symbol
        firstSymbol = value(roman_string[i])
        if (i + 1 < len(roman_string)):
            # Get value of the second symbol
            secondSymbol = value(roman_string[i + 1])
            # Compare both symbols
            if firstSymbol >= secondSymbol:
                totalSum += firstSymbol
            else:
                totalSum += secondSymbol - firstSymbol
        else:
            totalSum += firstSymbol

    return totalSum


def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
