#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple blood pressure readings as a string."""

BP_INPUT = int(raw_input('What is your blood pressure? '))
BP_STATUS = []

if BP_INPUT <= 89:
    BP_STATUS = 'Low'
elif BP_INPUT <= 119:
    BP_STATUS = 'Ideal'
elif BP_INPUT <= 139:
    BP_STATUS = 'Warning'
elif BP_INPUT <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

STATUS = 'Your status is currently: {}'.format(BP_STATUS)
print STATUS
