#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 05."""

# Import Python libs
import unittest
import mock
import random


class Lesson04Task05TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 05.

    """

    def test_blood_pressure_status(self):
        """
        Tests that the correct ``BP_STATUS`` is returned.'

        This test will try random numbers in each of the target ranges.
        """
        levels = {'low': [-256, 89],
                  'ideal': [90, 119],
                  'warning': [120, 139],
                  'high': [140, 159],
                  'emergency': [160, 256]
        }

        for key, value in levels.iteritems():
            systolic = random.randint(value[0], value[1])
            with mock.patch('__builtin__.raw_input', side_effect=[systolic]):
                try:
                    task_05 = reload(task_05)
                except NameError:
                    import task_05
                self.assertEqual(task_05.BP_STATUS.lower(), key)


if __name__ == '__main__':
    unittest.main()
