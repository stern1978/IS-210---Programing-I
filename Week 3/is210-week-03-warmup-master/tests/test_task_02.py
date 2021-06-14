#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 02."""


# Import Python libs
import unittest

# Import student file
import task_02


class L03T02TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 02.
    """

    def test_weeks(self):
        """
        Tests that the WEEKS constant value is 52
        """
        self.assertIs(task_02.WEEKS, 52)


if __name__ == '__main__':
    unittest.main()
