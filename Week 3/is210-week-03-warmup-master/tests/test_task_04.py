#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 04."""


# Import Python libs
import unittest

# Import student file
import task_04


class L03T04TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 04.
    """

    def test_klaxon(self):
        """
        Tests that the KLAXON variable has the correct value.
        """
        self.assertEqual(task_04.KLAXON, 'Danger ' * 5)


if __name__ == '__main__':
    unittest.main()
