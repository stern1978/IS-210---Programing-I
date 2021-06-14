#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

SCARFACE = LOOKS_NICE == True and EXPENSE <= MAX_EXPENSE or GET_OUT_ALIVE == False
scarface = (LOOKS_NICE and EXPENSE <= MAX_EXPENSE) or GET_OUT_ALIVE

print SCARFACE, True
print scarface, True
