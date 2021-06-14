#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""."""

import os

filepath = os.path.abspath('test.py')
newfile = 'newfile.py'

fdir =  os.path.dirname(filepath)

print (filepath, '\n', newfile, '\n', fdir, '\n')

print (os.path.join(fdir, newfile))
