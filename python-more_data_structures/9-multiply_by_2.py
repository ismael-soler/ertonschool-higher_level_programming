#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return a_dictionary

    newDictionary = a_dictionary.copy()
    for key in newDictionary.keys():
        newDictionary[key] = newDictionary[key]*2

    return newDictionary
