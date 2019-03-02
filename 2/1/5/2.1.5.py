#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Exercice 2.1.5
"""
import math

def bloc_reward(height) :
    """
        function bloc_reward(height)
    """
    return math.floor((50 / (2 ** (height // 210000)) * 10**8))

print(str(bloc_reward(2100001)*10**(-8))+' BTC')
