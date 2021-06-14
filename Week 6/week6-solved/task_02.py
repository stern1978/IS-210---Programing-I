#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module explains the use of functions used for list manipulation"""

import data


BALLETS = data.BALLETS
print BALLETS
del BALLETS[11]
BALLETS[1] = 'Swan Lake'
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])
print BALLETS, len(BALLETS)
