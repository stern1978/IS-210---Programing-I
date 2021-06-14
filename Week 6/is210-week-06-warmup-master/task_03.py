#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 imports data and removes and replaces the last item in DIRECTIONS"""


import data

DIRECTIONS = data.DIRECTIONS

DIRECTIONS = DIRECTIONS[:-1] + ('West',)
