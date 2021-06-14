#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module changes a boolean value to a string."""


def bool_to_str(bval):
    """Returns a boolean value as a string.

    Args:
        bval (any): Value to test truthyness. 

    Returns:
        Yes or No (str): True is output as "Yes" and False is output as "No". 

    Examples:
        >>> bool_to_str(True)
        'Yes'
        
        >>> bool_to_str(False)
        'No'
        
        >>> bool_to_str('abcdefghijklmnopqrstuvwxyz')
        'Yes'
        
        >>> bool_to_str('')
        'No'
    """
    return 'Yes' if bool(bval) is True else 'No'
