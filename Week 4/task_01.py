#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Returns argument('s) entered in a string.

    Args:
        wink (str): Word that will be entered in the return string.
        numwink (int, optional): Number of times to repeat.  Default: 2

    Returns:
        str: wink arg is concatenated in to the retstr string

    Examples:

        >>> know_what_i_mean('wink ')
        'Know what I mean? wink wink, nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
