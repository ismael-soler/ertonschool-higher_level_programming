#!/usr/bin/python3
""" returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """ main """
    if my_obj is not None:
        return json.dumps(my_obj)
    return
