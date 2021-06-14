#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a fibonacci sequence"""


def fibonacci(maxint):
    """Returns a fibonacci squence.

    Args:
        maxint (int): Upper limit of the fibonacci sequence. 

    Returns:
        output (list): A list of numbers in the fibonacci sequence up to maxint. 

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>> fibonacci(100)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    curnum, lastnum = 0, 1
    output = []
    while curnum < maxint:
        output.append(curnum)
        curnum, lastnum = lastnum, lastnum + curnum
    return output
