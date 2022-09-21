#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for tests"""

    def maxAtTheEnd(self):
        """Test a list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def maxAtTheBeginning(self):
        """Test a list"""
        result = max_integer([4, 2, 3, 1])
        self.assertEqual(result, 4)

    def maxAtTheMiddle(self):
        """Test a list"""
        result = max_integer([1, 2, 4, 1])
        self.assertEqual(result, 4)

    def oneNegativeNumber(self):
        """Test a list"""
        result = max_integer([1, -8, 4, 1])
        self.assertEqual(result, 4)

    def onlyNegativeNumber(self):
        """Test a list"""
        result = max_integer([-11, -8, -24, -1])
        self.assertEqual(result, -1)

    def oneElementInTheList(self):
        """Test a list"""
        result = max_integer([1])
        self.assertEqual(result, 1)

    def oneElementInTheList(self):
        """Test a list"""
        result = max_integer([])
        self.assertEqual(result, "")
