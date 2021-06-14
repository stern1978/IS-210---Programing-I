#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for checking produce."""

import produce

TOMATO = produce.Produce()
EGGPLANT = produce.Produce(1311210802)

TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT_EXPIRES = produce.Produce.get_expiration(EGGPLANT)
