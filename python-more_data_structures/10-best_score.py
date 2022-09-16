#!/usr/bin/python3
from curses import keyname


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    biggestValue = 0
    biggestKey = ""
    for key in a_dictionary.keys():
        if a_dictionary[key] > biggestValue:
            biggestValue = a_dictionary[key]
            biggestKey = key

    return biggestKey
