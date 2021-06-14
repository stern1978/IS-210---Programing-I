#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 05."""


# Import Python libs
import unittest


# Import user libs
import data
import task_05


class Task05TestCase(unittest.TestCase):
    """Task 05 tests"""


    def test_logan_alias(self):
        """Tests the alias value of Logan"""
        self.assertEqual(data.SUPERHEROES['Logan']['alias'], 'Wolverine')


if __name__ == '__main__':
    unittest.main()
