#!/usr/bin/python3
""" creates an object from a "JSON file" """
import json


def load_from_json_file(filename):
    """ main """
    with open(filename, 'r', encoding='utf-8') as new_obj:
        return json.load(new_obj)
