#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 2.1.2
"""

def bits2target(bits):
    """
    function bits2target(bits)
    """
    bits = bytes.fromhex(bits)
    return bits[:1], bits[1:]

def target2int(coefficient, exposant):
    """
    target2int(coefficient, exposant)
    """
    target = coefficient + (int.from_bytes(exposant, 'big') - 3) * b'\x00'
    return int.from_bytes(target, 'big')

def calculer_difficulte(target):
    """
        calculer_difficulte(target)
    """
    targetmax = 0xffff * 2**208
    return targetmax / target


exposant, coefficient = bits2target("1c0ae493")
target = target2int(coefficient, exposant)
print(calculer_difficulte(target))
