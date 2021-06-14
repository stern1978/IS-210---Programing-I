#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Funky math module."""

DATA = {
    1:10,
    2:20,
    3:30,
    4:40,
    5:50,
    6:60,
    7:70,
    8:80,
    9:90,
    10:100
    }

def iter_dict_funky_sum(DATA):
    funk = 0
    for key, value in DATA.iteritems():
        funk += value - key

    return funk
