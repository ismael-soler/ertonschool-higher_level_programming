#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):

    def test_Rectangle(self):
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)
        self.assertEqual(type(Rectangle(1, 2, 3)), Rectangle)
        self.assertEqual(type(Rectangle(1, 2, 3, 4)), Rectangle)
