#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 07."""


# Import Python libs
import unittest

# Import student file
import task_07


class L03T07TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 07.
    """

    def test_granaries(self):
        """
        Tests for the presence of a word within the WORDS string.
        """
        self.assertTrue(task_07.GRANARIES_EXIST)


if __name__ == '__main__':
    unittest.main()
