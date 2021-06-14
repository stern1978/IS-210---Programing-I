#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Corrects bands list in data module """

import data

CORRECTED = data.BANDS.copy()

CORRECTED.update({
    'Dylan': {
        'Bob Dylan': ['vocals', 'guitar', 'harmonica']}
    })

CORRECTED['Van Halen']['Sammy Hagar'] = CORRECTED['Van Halen'].pop('David Lee Roth')
