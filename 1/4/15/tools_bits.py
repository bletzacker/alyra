#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercice 1.4.14
"""

def bits2target(bits):
    """
    function bits2target(bits)
    """
    bits = bytes.fromhex(bits)
    return bits[:1], bits[1:]

def cible_atteinte(coefficient, exposant, hexstr_hash):
    """
    cible_atteinte(coefficient, exposant, hexstr_hash)
    """
    hash_to_test = bytes.fromhex(hexstr_hash)
    target = coefficient + int.from_bytes(exposant, 'big') * b'\x00'
    return int.from_bytes(hash_to_test, 'big') < int.from_bytes(target, 'big')
