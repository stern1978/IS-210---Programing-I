#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 09."""


# Import Python libs
import unittest

# Import student file
import task_09


class L03T09TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 09.
    """

    def test_docstring(self):
        """
        Tests that the docstring is at least 3 lines long.
        """
        numlines = len(task_09.__doc__.splitlines())
        msg = 'Your docstring does not meet the minimum line length'
        self.assertGreaterEqual(numlines, 3, msg)


if __name__ == '__main__':
    unittest.main()
