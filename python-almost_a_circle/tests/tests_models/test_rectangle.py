#!/usr/bin/python3

import os
import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


class RectangleTest(unittest.TestCase):

    def set_zero(self):
        """ Sets to 0 the instance counter of base """
        Base._Base__nb_objects = 0

    def test_Rectangle(self):
        """
        Test that the Rectangle class is created correctly.
        """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_IntValue(self):
        """
        If the input is not an integer, raise a TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_PositiveValues(self):
        """
        If the width or height is less than or equal to zero,
        raise a ValueError.
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_Area(self):
        """
        Test that the area of a rectangle.
        """
        auxRectangle = Rectangle(1, 2)
        self.assertEqual(auxRectangle.area(), 2)

    def test_str(self):
        """
        It tests that the __str__ method of the Rectangle class returns
        the correct string.
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 0/0 - 1/2")

    def test_Display(self):
        """
        It tests the display function of the Rectangle class.
        """
        # Creating a temporary output.
        temp_out = StringIO()
        # Redirecting the output to a temporary output.
        sys.stdout = temp_out
        r1 = Rectangle(2, 2)
        r1.display()
        self.assertEqual(temp_out.getvalue(), "##\n##\n")

        temp_out2 = StringIO()
        sys.stdout = temp_out2
        r2 = Rectangle(2, 2, 1)
        r2.display()
        self.assertEqual(temp_out2.getvalue(), " ##\n ##\n")

        temp_out3 = StringIO()
        sys.stdout = temp_out3
        r3 = Rectangle(2, 2, 1, 1)
        r3.display()
        self.assertEqual(temp_out3.getvalue(), "\n ##\n ##\n")

    def test_ToDictionary(self):
        """
        It test the class method to_dictionary
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r1.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1})

    def test_Update(self):
        """
        It tests updating the Rectangle class
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/1 - 1/1")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/1 - 2/1")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/1 - 2/3")

    def test_Create(self):
        """
        `test_Create` creates a rectangle with an id of 89 and then checks that the id of the rectangle is
        89
        """
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)


class RectangleSaveToFileNone(unittest.TestCase):
    def test_None(self):
        r1 = Rectangle.save_to_file(None)
        with open("Rectangle.json") as tempFile:
            self.assertEqual('[]', tempFile.read())


class RectangleSaveToFile(unittest.TestCase):
    def test_NoList(self):
        r2 = Rectangle.save_to_file([])
        with open("Rectangle.json") as tempFile:
            self.assertEqual('[]', tempFile.read())

    def test_List(self):
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as temporary:
            self.assertEqual(
                '[{"id": 3, "width": 1, "height": 2, "x": 0, "y": 0}]', temporary.read())


if __name__ == '__main__':
    unittest.main()
