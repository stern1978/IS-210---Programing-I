#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 06."""


# Import Python libs
import unittest

# Import student file
import task_06


class L03T06TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 06.
    """

    def test_wordct(self):
        """
        Tests that the WORDCT variable to see if it correctly counted words.
        """
        self.assertEqual(task_06.WORDCT, 566316)


if __name__ == '__main__':
    unittest.main()
