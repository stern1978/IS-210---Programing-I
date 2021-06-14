#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'
LENINPUT = 'long'

# You code goes here
if len(MYINPUT) > MAX_LENGTH:
    LONGSTR = LENINPUT

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
