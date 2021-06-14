#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module shows if two values are equal"""

def defaults(my_required, my_optional=True):
    """This function determines is the two arguments match.

    Args:
        my_required (mixed): Any entry.
        my_optional (mixed, optional): Any entry. Default=True

    Returns:
        boolean: Returns True or False if Args match.

    Examples:

        >>> defaults(True)
        True
        >>> defaults(True, False)
        False
        >>> defaults(False, False)
        True
        >>> defaults(7)
        False
    """
    return my_optional is my_required
