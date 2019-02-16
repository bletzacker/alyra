#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tools

class Locktime :

    def __init__(self,tx) :
        self.label = "Locktime :"
        self.isVarInt = False
        self.isRaw = False
        self.isReverse = True
        self.length = 4
        self.format = '<I' # little-endian integer 4 bytes
        self.value = tools.value(self,tx)

    def __str__ (self) :
        return f"{self.label} {self.value}"
