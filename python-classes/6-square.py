#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Init class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                if self.__position[0] > 0:
                    for i in range(self.__position[0]):
                        print(end="_")
                for i in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
