#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for tests"""

    def test_maxAtTheEnd(self):
        """Test a list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_maxAtTheBeginning(self):
        """Test a list"""
        result = max_integer([4, 2, 3, 1])
        self.assertEqual(result, 4)

    def test_maxAtTheMiddle(self):
        """Test a list"""
        result = max_integer([1, 2, 4, 1])
        self.assertEqual(result, 4)

    def test_oneNegativeNumber(self):
        """Test a list"""
        result = max_integer([1, -8, 4, 1])
        self.assertEqual(result, 4)

    def test_onlyNegativeNumber(self):
        """Test a list"""
        result = max_integer([-11, -8, -24, -1])
        self.assertEqual(result, -1)

    def test_oneElementInTheList(self):
        """Test a list"""
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_noElementsInTheList(self):
        """Test a list"""
        result = max_integer([])
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
