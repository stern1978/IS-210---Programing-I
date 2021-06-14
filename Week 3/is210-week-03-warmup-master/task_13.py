#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports values from task 13 to test equality.

.. hint::

    You can access task_12 data in the following example type:

.. code:: python

    print task_12.FLOATVAL
"""

import task_12

T12 = task_12

FRAC_DEC_EQUAL = (T12.DECVAL == T12.FRACTVAL)

DEC_FLOAT_INEAQUAL = (T12.DECVAL != T12.FLOATVAL)
