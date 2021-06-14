#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 02."""


# Import Python libs
import unittest
import mock
import random

class Lesson04Task02TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 02.

    """

    def test_raw_input_converted(self):
        """
        Tests that the input values are converted into the correct data type.

        A random integer is passed to the input to simulate this effect.
        """
        values = [random.randint(-999, 999)]
        with mock.patch('__builtin__.raw_input',  side_effect=values):
            import task_02
            self.assertEqual(task_02.MY_INTEGER, values[0])


if __name__ == '__main__':
    unittest.main()
