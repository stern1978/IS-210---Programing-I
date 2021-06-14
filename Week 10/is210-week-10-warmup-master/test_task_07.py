#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 07."""


# Import Python libs
import unittest

# Import user libs
import task_07


class Task07TestCase(unittest.TestCase):
    """Task 07 tests"""


    def my_funky_sum(self):
        funk = 0
        for key, value in task_07.DATA.iteritems():
            funk += value - key

        return funk


    def test_data_length(self):
        """Tests that the DATA constant is at least 10 items long."""
        self.assertGreaterEqual(len(task_07.DATA), 10)


    def test_funky_sum(self):
        """Tests that the DATA dictionary is correctly summed."""
        self.assertEqual(
            task_07.iter_dict_funky_sum(task_07.DATA), self.my_funky_sum()
        )


if __name__ == '__main__':
    unittest.main()
