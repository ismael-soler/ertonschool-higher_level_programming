#!/usr/bin/python3
"""Module"""


import unittest
from models.base import Base


class testsNumber0(unittest.TestCase):
    """Test of Base() for assigning
    automatically an ID exists"""

    def setUp(self):
        self.base1 = Base()

    def test_0(self):
        self.assertEqual(self.base1.id, 1)

    def test_1(self):
        self.assertEqual(self.base1.id, 2)

    def test_2(self):
        self.assertEqual(self.base1.id, 3)

    def test_3(self):
        self.assertEqual(self.base1.id, 4)

    def test_4(self):
        self.assertEqual(self.base1.id, 5)

    def test_5(self):
        self.assertEqual(self.base1.id, 6)


class testsNumber1(unittest.TestCase):
    """Tests number 1"""

    def setUp(self):
        self.base1 = Base(89)

    def test_1(self):
        self.assertEqual(self.base1.id, 89)

    def test_2(self):
        self.assertEqual(Base().to_json_string(None), '[]')

    def test_3(self):
        self.assertEqual(Base().to_json_string([]), '[]')

    def test_4(self):
        self.assertEqual(Base().to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_5(self):
        self.assertEqual(Base().from_json_string(None), [])

    def test_6(self):
        self.assertEqual(Base().from_json_string("[]"), [])

    def test_7(self):
        self.assertEqual(Base().from_json_string(
            '[{ "id": 89 }]'), [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
