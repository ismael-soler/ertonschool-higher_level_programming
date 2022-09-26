#!/usr/bin/python3
"""" returns if the object is an instance of a  class """


def inherits_from(obj, a_class):
    """ checks the condition"""
    return isinstance(type(obj), a_class) or type(obj) is a_class
