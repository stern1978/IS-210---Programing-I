#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 01."""


# Import Python libs
import unittest
import mock

class Lesson04Task01TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 01.
    """

    def test_raw_input(self):
        """
        Tests that the input values are stored into the correct variables.
        """
        values = ['The Ministry of Funny Walks']
        with mock.patch('__builtin__.raw_input',  side_effect=values):
            import task_01
            self.assertEqual(task_01.MY_ANSWER, values[0])


if __name__ == '__main__':
    unittest.main()
