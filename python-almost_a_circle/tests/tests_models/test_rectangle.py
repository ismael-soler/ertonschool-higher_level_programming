#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def set_zero(self):
        Base.__nb_objects = 0

    def test_Rectangle(self):
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)
        self.assertEqual(type(Rectangle(1, 2, 3)), Rectangle)
        self.assertEqual(type(Rectangle(1, 2, 3, 4)), Rectangle)


if __name__ == '__main__':
    unittest.main()
