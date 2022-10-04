#!/usr/bin/python3
"""Module"""


import unittest
from models.square import Square


class AllTests(unittest.TestCase):
    def test_0(self):
        self.s1 = Square(75, 62)
        self.s1.update()
        self.assertEqual(self.s1.id, 22)
        self.s1.update(89)
        self.assertEqual(self.s1.id, 89)
        self.s1.update(89, 1)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 1)

    def test_1(self):
        self.s2 = Square(1)
        self.assertEqual(self.s2.id, 23)
        self.assertEqual(self.s2.size, 1)
        self.s3 = Square(1, 2)
        self.assertEqual(self.s3.id, 24)
        self.s4 = Square(1, 2, 3)
        self.assertEqual(self.s4.id, 25)
        self.s4 = Square(1, 2, 3, 4)
        self.assertEqual(self.s4.id, 4)
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)
        self.s5 = Square(2)
        self.assertEqual(self.s5.__str__(), '[Square] (26) 0/0 - 2')
        self.assertEqual(self.s5.to_dictionary(), {
                         'id': 26, 'size': 2, 'x': 0, 'y': 0})


class TestCreate(unittest.TestCase):
    def test_0(self):
        self.s6 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(self.s6.size, 1)
        self.assertEqual(self.s6.id, 89)


class TestFileFunctions(unittest.TestCase):
    def test_0(self):
        self.s = Square(3)
        self.assertEqual(self.s.save_to_file(None), '[]')
        self.assertEqual(Square.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
