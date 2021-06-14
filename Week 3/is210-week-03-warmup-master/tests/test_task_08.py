#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 08."""


# Import Python libs
import unittest

# Import student file
import task_08


class L03T08TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 08.
    """

    def test_cat(self):
        """
        Tests that the KLAXON variable has the correct value.
        """
        cat = 'A long-tailed cat in a room full of rockin\' chairs.'
        self.assertEqual(task_08.NERVOUS_AS, cat)


if __name__ == '__main__':
    unittest.main()
