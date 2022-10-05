#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_Rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

if __name__ == '__main__':
    unittest.main()
