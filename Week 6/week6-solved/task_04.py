#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module explains the use of arithmetic operators on tuples"""


def process_data(data):
    """This function iterates on tuple or list to calculate sum and average

    Args:
        data (mixed): The input tuple or list.

    Returns:
        tuple: It returns tuple containing sum and average.

    Examples:

        >>> process_data([1, 2, 3])
        (6, 2.0)
    """
    total = 0
    count = 0
    for item in data:
        total += item
        count += 1
    return (total, total/(count*1.0))
