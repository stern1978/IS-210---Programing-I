#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 14."""


# Import Python libs
import unittest

# Import student file
import task_14


class L03T14TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 14.

    """

    def test_is_true(self):
        """
        Tests that the IS_TRUE variable exists and has the correct value.
        """
        self.assertTrue(task_14.IS_TRUE)

    def test_is_false(self):
        """
        Tests that the IS_FALSE variable exists and has the correct value.
        """
        self.assertFalse(task_14.IS_FALSE)

    def test_is_none(self):
        """
        Tests that the IS_NONE variable exists and has the correct value.
        """
        self.assertIsNone(task_14.IS_NONE)

    def test_integer_equivs(self):
        """
        Tests that the INTEGER_EQUIV variable exists and has the correct
        value.
        """
        self.assertTrue(task_14.INTEGER_EQUIV)


if __name__ == '__main__':
    unittest.main()
