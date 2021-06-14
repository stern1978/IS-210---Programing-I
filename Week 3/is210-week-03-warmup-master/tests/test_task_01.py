#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 01."""


# Import Python libs
import unittest

# Import student file
import task_01


class L03T01TestCase(unittest.TestCase):
    """
    Test cases for lesson 03 task 01.

    """

    def test_raven(self):
        """
        Tests that the RAVEN constant value is 'Nevermore!'
        """
        self.assertEqual(task_01.RAVEN, 'Nevermore!')


if __name__ == '__main__':
    unittest.main()
