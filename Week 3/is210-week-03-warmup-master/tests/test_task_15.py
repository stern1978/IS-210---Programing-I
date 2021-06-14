#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 15."""


# Import Python libs
import unittest

# Import student file
import task_15


class L03T15TestCase(unittest.TestCase):
    """
    Tests for lesson 03 task 15.
    """

    def test_not_the_question(self):
        """
        Tests that the NOT_THE_QUESTION variable has the correct value.
        """
        quest = 'The answer to life, the universe, and everything? It\'s '
        self.assertEqual(task_15.NOT_THE_QUESTION, quest)

    def test_answer(self):
        """
        Tests that the ANSWER variable has the correct value.
        """
        self.assertEqual(task_15.ANSWER, 42)

    def test_thanks_for_the_fish(self):
        """
        Tests that the thanks_for_the_fish variable has the correct value.
        """
        quest = 'The answer to life, the universe, and everything? It\'s 42'
        self.assertEqual(task_15.THANKS_FOR_THE_FISH, quest)


if __name__ == '__main__':
    unittest.main()
