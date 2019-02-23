#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Exercice 2.1.7
"""
import datetime

def bloc_reward(height) :
    """
        function bloc_reward(height)
    """
    return 50 / (2 ** (height // 210000))

def total_bitcoin(height) :
    """
        function total_bitcoin(height)
    """
    total_bitcoin = 0
    for i in range(height // 210000 + 1) :
        total_bitcoin += min(210000,height+1) * (50 / (2 ** (i)))
        height -= 210000
    return total_bitcoin

def state_bitcoin(year, month=1, day=1, hour=0, minute=0, second=0) :
    """
        function state_bitcoin(year, month=1, day=1, hour=0, minute=0, second=0)
    """
    t = datetime.datetime(year, month, day, hour, minute, second)
    t0 = datetime.datetime(2019, 2, 23, 9, 34, 19) # bloc 564295
    delta = datetime.timedelta(minutes=10) # moyenne de 10 mn
    height = (t-t0) // delta + 564295
    return bloc_reward(height), total_bitcoin(height)

print(state_bitcoin(2100))
# En 2100, la récompense sera de 1192 satoshis pour un volume de bitoins en
# circulation d'environ 20 999 997 soit plus de 99,99998 % du volume total.
