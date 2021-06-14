#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 13."""


# Import Python libs
import unittest

# Import student file
import task_13


class L03T13TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 13.
    """

    def test_frac_dec_equal(self):
        """
        Tests that the FRACVAL and DECVAL are equal.
        """
        self.assertFalse(task_13.FRAC_DEC_EQUAL)

    def test_dec_float_inequal(self):
        """
        Tests that the DECVAL and FLOATVAL are inequal.
        """
        self.assertTrue(task_13.DEC_FLOAT_INEQUAL)


if __name__ == '__main__':
    unittest.main()
