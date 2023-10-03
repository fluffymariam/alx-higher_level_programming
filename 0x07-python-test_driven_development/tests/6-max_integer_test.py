#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test max_integer with regular list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test max_integer with empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test max_integer with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test max_integer with mixed numbers."""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_float_numbers(self):
        """Test max_integer with float numbers."""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.1]), 4.1)
        self.assertEqual(max_integer([-1.5, -2.7, -3.9, -4.1]), -1.5)

    def test_single_element_list(self):
        """Test max_integer with single element list."""
        self.assertEqual(max_integer([42]), 42)


if __name__ == '__main__':
    unittest.main()
