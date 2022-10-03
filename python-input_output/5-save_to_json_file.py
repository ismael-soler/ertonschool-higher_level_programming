#!/usr/bin/python3
""" writes an Object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ main """
    if my_obj is None:
        return
    with open(filename, "w", encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
