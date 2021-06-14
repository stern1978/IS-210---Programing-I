#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    pass

def get_age(birthyear):
    age = datetime.datetime.now().year - birthyear
    return age
