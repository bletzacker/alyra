#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Exercice 2.1.6
"""
import math

def total_bitcoin(height) :
    """
        function total_bitcoin(height)
    """
    total_bitcoin = 0
    for i in range(height // 210000 + 1) :
        total_bitcoin += min(210000,height+1) * math.floor((50 / (2 ** (i))) * 10**8)
        height -= 210000
    return total_bitcoin

print(str(total_bitcoin(2100001)*10**(-8))+' BTC')
