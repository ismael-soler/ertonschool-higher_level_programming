#!/usr/bin/python3
""" writes a string to a text file (UTF8)  """


def write_file(filename="", text=""):
    """ writes to the file """
    with open(filename, 'w', encoding='utf-8') as pepito:
        return pepito.write(text)
