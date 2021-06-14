#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 04."""


# Import Python libs
import unittest
import mock
import __builtin__

class Lesson04Task04TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 04.

    """

    def test_str_length(self):
        """
        Tests that correct output is captured for a string.

        This test will test both long and short strings.
        """
        with mock.patch('__builtin__.raw_input') as mocked:
            mocked.side_effect = ['a'] 
            import task_04
            self.assertEqual(task_04.LONGSTR, 'short')

            mocked.side_effect = ['a' * 100]
            task_04 = reload(task_04)
            self.assertEqual(task_04.LONGSTR, 'long')


if __name__ == '__main__':
    unittest.main()
