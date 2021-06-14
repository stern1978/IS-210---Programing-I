#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module explains the use of for loop and slicing of tuples"""


def flip_keys(to_flip):
    """This function iterates on tuple and flips its inner elements

    Args:
        to_flip (tuple): The input tuple.

    Returns:
        tuple: The inner elements are flipped and tuple is returned

    Examples:

        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    count = 0
    for ele in to_flip:
        to_flip[count] = ele[::-1]
        count += 1
    return to_flip
