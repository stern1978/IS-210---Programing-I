#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 12."""


# Import Python libs
import unittest
from decimal import Decimal
from fractions import Fraction

# Import student file
import task_12


class L03T12TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 12.
    """

    def test_intval(self):
        """
        Tests that the intval variable has the correct value.
        """
        self.assertIs(task_12.INTVAL, 1)

    def test_floatval(self):
        """
        Tests that the floatval variable has the correct value.
        """
        self.assertEqual(task_12.FLOATVAL, 0.1)

    def test_decval(self):
        """
        Tests that the decval variable has the correct value.
        """
        self.assertEqual(task_12.DECVAL, Decimal('0.1'))

    def test_fracval(self):
        """
        Tests that the fracval variable has the correct value.
        """
        self.assertEqual(task_12.FRACVAL, Fraction(1, 10))


if __name__ == '__main__':
    unittest.main()
