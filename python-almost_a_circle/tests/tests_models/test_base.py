#!/usr/bin/python3
""" It tests the Base class """

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ Unittest for base class """

    def test_autoId(self):
        """
        It tests the auto-incrementing id functionality of the Base class
        """
        myInstance = Base()
        self.assertEqual(myInstance.id, 1)
        myInstance2 = Base()
        self.assertEqual(myInstance2.id, 2)
        myInstance3 = Base(89)
        self.assertEqual(myInstance3.id, 89)

    def test_JsonToString(self):
        """
        It tests the to_json_string function of the Base class.
        """
        aux = Base.to_json_string(None)
        self.assertEqual(aux, '[]')
        aux = Base.to_json_string([])
        self.assertEqual(aux, '[]')
        aux = Base.to_json_string([{'id': 12}])
        self.assertEqual(aux, '[{"id": 12}]')

    def test_FromJsonToString(self):
        """
        It tests the from_json_string function.
        """
        aux = Base.from_json_string(None)
        self.assertEqual(aux, [])
        aux = Base.from_json_string("[]")
        self.assertEqual(aux, [])
        aux = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(aux, [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
