#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest


# Import user libs
import task_01


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""


    def test_grade_data(self):
        """Tests that the GRADE_DATA constant has the correct keys/values"""

        data = {
            'Luke Skywalker': {
                'math': 'B',
                'etiquette': 'B+',
                'grammar': 'B',
                'gym': 'A',
            },
            'Han Solo': {
                'math': 'A-',
                'etiquette': 'C-',
                'grammar': 'B',
                'gym': 'B',
            },
            'C-3PO': {
                'math': 'C',
                'etiquette': 'A+',
                'grammar': 'A',
                'gym': 'F',
            },
        }

        self.assertEqual(task_01.GRADE_DATA, data)


if __name__ == '__main__':
    unittest.main()
