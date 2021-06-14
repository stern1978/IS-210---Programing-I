#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 06."""


# Import Python libs
import unittest


# Import user libs
import task_06


class Task06TestCase(unittest.TestCase):
    """Task 06 tests"""


    def test_sidekicks(self):
        """Tests the value of SUPER_SIDEKICKS."""
        sk = {'Kitty Pryde': 'Lockheed', 'Bruce Wayne': 'Ace', 'Logan': None,
              'Clark Kent': 'Krypto', 'Samuel Wilson': 'Redwing'}

        self.assertEqual(task_06.SUPER_SIDEKICKS, sk)


if __name__ == '__main__':
    unittest.main()
