#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 2.1.1
"""

def calculer_difficulte(target):
    """
        calculer_difficulte(target)
    """
    targetmax = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
    return targetmax / target

print(calculer_difficulte(1147152896345386682952518188670047452875537662186691235300769792000))
