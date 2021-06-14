#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    try:
        return var1[var2]
    except LookupError:
        print "Warning: Your index/key dosen't exist"
        return var1
