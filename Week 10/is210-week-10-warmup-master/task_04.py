#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Adds a band and amends another."""

import data

data.BANDS.update({
    'Buckingham Nicks': {
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine']}
    })

data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])
