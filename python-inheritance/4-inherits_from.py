#!/usr/bin/python3
"""" returns if the object is an instance of a  class """


def inherits_from(obj, a_class):
    """ checks the condition"""
    return type(obj) is not a_class
