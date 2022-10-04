#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update """
        le = len(args)
        if (le > 0):
            self.id = args[0]
            if (le > 1):
                self.size = args[1]
            if (le > 2):
                self.x = args[2]
            if (le > 3):
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if (key == "id"):
                    self.id = value
                if (key == "size"):
                    self.size = value
                if (key == "x"):
                    self.x = value
                if (key == "y"):
                    self.y = value

