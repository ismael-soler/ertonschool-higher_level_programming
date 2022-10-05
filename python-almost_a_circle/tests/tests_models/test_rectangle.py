#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):

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
        It tests that the __str__ method of the Rectangle class returns the correct string.
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 0/0 - 1/2")


if __name__ == '__main__':
    unittest.main()
