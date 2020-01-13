#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)

    def test_one_negative(self):
                self.assertEqual(max_integer([-2, 6, 8]), 8)

    def test_all_negative(self):
                self.assertEqual(max_integer([-1, -4, -5, -6]), -1)

    def test_just_none(self):
                self.assertIsNone(max_integer([None]), None)

    def test_no_input(self):
                self.assertIsNone(max_integer())

    def test_boolean(self):
                self.assertEqual(max_integer([True, False, 4, 5, 6]), 6)

    def test_neg_boolean(self):
                self.assertEqual(max_integer([-True, -False, 5, 6]), 6)

    def test_empty_list(self):
                self.assertFalse(max_integer([]))

    def test_big_number(self):
                big_num = 300000000000000000000000000000000000000000001
                self.assertEqual(max_integer([big_num, 5]),
                                 300000000000000000000000000000000000000000001)

    def test_a_string(self):
        self.assertEqual(max_integer("si"), 's')

    def test_list_of_floats(self):
        self.assertEqual(max_integer([3.8, 8.9, 6.8]), 8.9)

    def test_a_list_including_None(self):
        with self.assertRaises(TypeError):
            max_integer([4, 6, None, 9])

    def test_None_None(self):
        with self.assertRaises(TypeError):
            max_integer([None, None])

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            max_integer(-2)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            max_integer((5, 8), [4, 3, 9])

if __name__ == '__main__':
    unittest.main()
