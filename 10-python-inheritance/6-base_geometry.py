#!/usr/bin/python3
""" Write an empty class BaseGeometry"""


class BaseGeometry():
    """ Base Geometry """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        as