#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module lets you know if you have too many kittens."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Returns a bool result for argumnets.

    Args:
        kittens (int): Number of kittens.
        litterboxes (int): Number of litterboxes.
        catfood (bool): Is there catfood.

    Returns:
        bool: True or False that there are too many cats.

    Examples:

        >>> too_many_kittens(100, 1, True)
        True
    """
    return not (litterboxes >= kittens and catfood)
