#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import unittest


# Import user libs
import data
import task_02


class Task02TestCase(unittest.TestCase):
    """Task 02 tests"""


    def test_nigel(self):
        """Tests the value of the NIGEL constant."""
        self.assertEqual(task_02.NIGEL,
                         data.BANDS['Spinal Tap']['Nigel Tufnel'])


    def test_band_names(self):
        """Tests the value of the BAND_NAMES constant."""
        self.assertEqual(task_02.BAND_NAMES, data.BANDS.keys())


if __name__ == '__main__':
    unittest.main()
