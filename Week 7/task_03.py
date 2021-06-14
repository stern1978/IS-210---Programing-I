#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides"""


import data
import decimal

def lexicographics(to_analyze):
    """Returns largest, smallest and average number of words per line of text.

    Args:
        to_analyze (str): Text to be input. 

    Returns:
        longest (int): Number of words in longest sentance.
        shortest (int): Number of words in shortest sentance.
        avglen (dec): Average number of words per sentance

    Examples:
        lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    output = [s.strip().split() for s in to_analyze.splitlines()]
    longest = len(max(output, key=len))
    shortest = len(min(output, key=len))
    avglen = avglen = decimal.Decimal(len(to_analyze.split())) / len(to_analyze.split('\n'))
    return longest, shortest, avglen
