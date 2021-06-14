#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 03."""


# Import Python libs
import unittest


# Import user libs
import data
import task_03


class Task03TestCase(unittest.TestCase):
    """Task 03 tests"""


    def test_corrected_is_copy(self):
        """Tests that CORRECTED is different from the original (a copy)"""

        self.assertNotEqual(task_03.CORRECTED, data.BANDS)


    def test_dylan(self):
        """Tests CORRECT['Dylan'] values."""
        dylan = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']} 
        self.assertEqual(task_03.CORRECTED['Dylan'], dylan)


    def test_van_halen(self):
        """Tests that the van halen entry has the correct membership."""
        vh = {
            'Eddie Van Halen': ['guitar'],
            'Sammy Hagar': ['vocals'],
            'Alex Van Halen': ['drums'],
            'Michael Anthony': ['bass']
        }
        self.assertEqual(task_03.CORRECTED['Van Halen'], vh)


if __name__ == '__main__':
    unittest.main()
