#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Shopping list."""

from data import FRUIT

shoplist = {}

def get_cost_per_item(shoplist):
    """Constructor for cost per item on shoplist.

    Args:
        shoplist (dict): List of items

    Attrubutes:
        price (dict): Items from shoplist with cost per item.
    
    """
    price = {}
    for key, value in shoplist.iteritems():
        if key in FRUIT:
            price[key] = FRUIT[key] * value
    return price
        
def get_total_cost(shoplist):
    """Constructor for total cost of shoplist.

    Args:
        shoplist (dict): List of items.

    Attributes:
        total (int): Total cost of items from shoplist.
    """
    total = sum(get_cost_per_item(shoplist).values())
    return total
    
if __name__ == '__main__':
    print get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
    print get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
