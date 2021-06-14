#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 03."""


# Import Python libs
import unittest

# Import student file
import task_03


class L03T03TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 03.
    """

    def test_will_robinson(self):
        """
        Tests that the will robinson constant value is unchanged.
        """
        willval = 'Danger Will Robinson!'
        self.assertEqual(task_03.WILL_ROBINSON, willval)

    def test_klaxon(self):
        """
        Tests that the KLAXON variable has the correct value.
        """
        self.assertEqual(task_03.KLAXON, 'Danger ')


if __name__ == '__main__':
    unittest.main()
