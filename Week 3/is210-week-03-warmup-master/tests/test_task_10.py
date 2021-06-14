#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 10."""


# Import Python libs
import unittest

# Import student file
import task_10


class L03T10TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 10.
    """

    film = ('Dr. Strangelove Or: How I Learned To Stop Worrying And Love '
            'The Bomb')

    def test_movie(self):
        """
        Tests that the original MOVIE variable is unaltered.
        """
        self.assertEqual(task_10.MOVIE, self.film.lower())

    def test_entitled(self):
        """
        Tests that the ENTITLED variable is in titlecase.
        """
        self.assertEqual(task_10.ENTITLED, self.film)


if __name__ == '__main__':
    unittest.main()
