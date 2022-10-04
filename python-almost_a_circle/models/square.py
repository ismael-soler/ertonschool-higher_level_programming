#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """
        return (f"[Square] ({self.__id}) {self.__x}/{self.__y}" +
                f"+  - {self.__height}")
