#!/usr/bin/python3
""" returns an object (Python data structure) represented by a JSON string """
import json


def from_json_string(my_str):
    """ main """
    if my_str is not None:
        return json.loads(my_str)
    return
