#!/usr/bin/python3
""" returns the dict description with simple data structure"""


def class_to_json(obj):
    """ main """
    return obj.__dict__
