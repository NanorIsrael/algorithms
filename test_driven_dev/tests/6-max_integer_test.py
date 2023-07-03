#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    # test with different list values
    def test_max_integer(self):
        """Test max_integer with different list values
        """
        self.assertEqual(max_integer([2, 5, 6, 9]), 9)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([2, 5.55555]), 5.55555)
        self.assertEqual(max_integer([0, -1]), 0)
        self.assertEqual(max_integer([]), None)
    
    def test_types(self):
        """Test max_integer with different list types
        """
        # raise value errors when necessary
        self.assertRaises(TypeError, max_integer, ["1", 3])
