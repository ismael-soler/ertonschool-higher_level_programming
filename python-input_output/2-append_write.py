#!/usr/bin/python3
""" appends a string to a text file (UTF8)  """


def write_file(filename="", text=""):
    """ writes to the file """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
