#!/usr/bin/python3
""" Write a new class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle child of BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return self.__width * self.__height
