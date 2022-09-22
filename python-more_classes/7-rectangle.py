#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ defines the rectangle """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initiates init """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        return

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return self.height * 2 + (self.width) * 2

    def __str__(self):
        """ returns a string """
        newString = ""
        if self.width != 0:
            for i in range(self.height):
                newString += str(self.print_symbol) * self.width
                if i != self.height - 1:
                    newString += "\n"

        return newString

    def __repr__(self):
        """ returns a string """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """ prints goodbye message """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
