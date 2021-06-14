#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains class Dog from pet module."""

import pet

PET = pet.Pet


class Dog(PET):
    """Class of Dog from Pet class."""

    def __new__(self, has_shots=False, **kwargs):
        """Constructor for Dog class.

        Args:
            has_shots (bool, ooptional): Does dog have shots, defaults to False.
            
        Attributes:
            shots: (bool, optioinal): True or False if dog has shots.

        """
        
        self.has_shots = has_shots
        kwargs['has_shots'] = has_shots
        dict.items
        print kwargs
        return kwargs
        

        
if __name__ == '__main__':
    Dog()

