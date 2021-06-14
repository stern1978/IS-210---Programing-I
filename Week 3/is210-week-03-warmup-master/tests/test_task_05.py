#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 05."""


# Import Python libs
import unittest

# Import student file
import task_05


class L03T05TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 05.
    """

    def test_turtle_power(self):
        """
        Tests that the string has been correctly split.
        """
        turtles = ['Michaelangelo', 'Leonardo', 'Rafael', 'Donatello',
                   'Heroes in a half shell.']
        self.assertEqual(task_05.TURTLE_POWER, turtles)


if __name__ == '__main__':
    unittest.main()
