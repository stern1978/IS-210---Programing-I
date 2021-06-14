#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


LIST = []
NEW = []

def flip_keys(keys):
    for keys in LIST:
        NEW.append(keys[::-1])
    return NEW
