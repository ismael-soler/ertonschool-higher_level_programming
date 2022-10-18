#!/usr/bin/python3
""" rectangle """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ It returns the value of the private variable y. """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns area """
        return self.__height * self.__width

    def display(self):
        """
        The function prints a rectangle of the specified
        height and width, with the specified x and y
        coordinates
        """
        for i in range(self.__y):
            print()
        for height in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for width in range(self.width):
                if width == self.__width - 1:
                    print("#")
                else:
                    print("#", end="")

    def __str__(self):
        """ str """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " +
                f"- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        If there are arguments,
        then assign them to the appropriate attributes.
        """
        le = len(args)
        if (le > 0):
            self.id = args[0]
            if (le > 1):
                self.__width = args[1]
            if (le > 2):
                self.__height = args[2]
            if (le > 3):
                self.__x = args[3]
            if (le > 4):
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if (key == "id"):
                    self.id = value
                if (key == "width"):
                    self.__width = value
                if (key == "height"):
                    self.__height = value
                if (key == "x"):
                    self.__x = value
                if (key == "y"):
                    self.__y = value

    def to_dictionary(self):
        """
        It creates a dictionary with the attributes of the class
        """
        myDict = {}

        myDict["id"] = self.id
        myDict["width"] = self.width
        myDict["height"] = self.height
        myDict["x"] = self.x
        myDict["y"] = self.y
        return myDict
