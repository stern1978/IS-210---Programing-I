#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 04."""


# Import Python libs
import unittest


# Import user libs
import task_04
import data


class Task04TestCase(unittest.TestCase):
    """Task 04 tests"""

    def setUp(self):
        self.bucknicks = {
            'Lindsey Buckingham': ['guitar', 'vocals'],
            'Stevie Nicks': ['vocals', 'tambourine']
        }
        self.mac = {
            'Mick Fleetwood': ['drums'],
            'John McVie': ['bass'],
            'Christine McVie': ['vocals', 'piano', 'keyboards'],
            'Lindsey Buckingham': ['guitar', 'vocals'],
            'Stevie Nicks': ['vocals', 'tambourine'],
        }


    def test_buckingham_nicks(self):
        """Tests that the Buckingham Nicks key exists."""
        self.assertEqual(data.BANDS['Buckingham Nicks'], self.bucknicks)


    def test_fleetwood(self):
        """Tests that Fleetwood Mac has added the Nicks membership."""
        self.assertEqual(data.BANDS['Fleetwood Mac'], self.mac)


if __name__ == '__main__':
    unittest.main()
