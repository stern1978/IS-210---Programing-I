#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 11."""


# Import Python libs
import unittest

# Import student file
import task_11


class L03T11TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 11.
    """

    def test_escape_string(self):
        """
        Tests that the ESCAPE_STRING variable has the correct value.
        """
        self.assertEqual(task_11.ESCAPE_STRING, '\\' + "n'" + '"')


if __name__ == '__main__':
    unittest.main()
