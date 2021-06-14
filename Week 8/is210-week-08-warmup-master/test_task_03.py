#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 02."""


# Import Python libs
import unittest
import task_03

class Lesson04Task03TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 03.
    """

    def test_sacrifice(self):
        """
        Tests the value of the ``SACRIFICE`` variable.
        """
        self.assertTrue(task_03.SACRIFICE)


if __name__ == '__main__':
    unittest.main()
