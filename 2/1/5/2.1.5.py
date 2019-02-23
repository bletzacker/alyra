#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Exercice 2.1.5
"""

def bloc_reward(height) :
    """
        function bloc_reward(height)
    """
    return 50 / (2 ** (height // 210000))

print(bloc_reward(564282))
