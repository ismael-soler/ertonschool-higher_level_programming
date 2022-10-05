#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

if __name__ == '__main__':
    unittest.main()
