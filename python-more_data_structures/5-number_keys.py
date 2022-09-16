#!/usr/bin/python3
from sqlite3 import adapt


def number_keys(a_dictionary):
    if a_dictionary is None:
        return

    return len(a_dictionary)