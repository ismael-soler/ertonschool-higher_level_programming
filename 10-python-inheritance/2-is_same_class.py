#!/usr/bin/python3
""" returns some stuff"""


def is_same_class(obj, a_class):
    """checks if it's the same class"""
    if a_class == type(obj):
        return True
    else:
        return False
