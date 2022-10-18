#!/usr/bin/python3
""" New class based on rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square child of Rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ new area method, returns the area"""
        return self.__size * self.__size

    def __str__(self):
        """ prints the dimensions """
        return super().__str__()

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
