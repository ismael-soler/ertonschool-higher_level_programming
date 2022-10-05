#!/usr/bin/python3
"""
Unittest for base
"""

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ Unittest for base class """

    def test_autoId(self):
        """
        It tests the auto-incrementing of the id attribute of the Base class.
        """
        myInstance = Base()
        self.assertEqual(myInstance.id, 1)
        myInstance2 = Base()
        self.assertEqual(myInstance2.id, 2)

    def test_passedId(self):
        """
        Test that the id of an instance of Base is equal to the id passed in.
        """
        myInstance = Base(89)
        self.assertEqual(myInstance.id, 89)

    def test_JsonToString(self):
        """
        It checks if the function to_json_string returns an empty list
        if the argument is None.
        """
        aux = Base.to_json_string(None)
        self.assertEqual(aux, '[]')
        aux = Base.to_json_string([])
        self.assertEqual(aux, '[]')
        aux = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(aux, '[{"id": 12}]')

if __name__ == '__main__':
    unittest.main()
