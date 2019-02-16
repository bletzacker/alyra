#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tools

class Value :

    def __init__(self,tx) :
        self.label = "  Value :"
        self.isVarInt = False
        self.isRaw = False
        self.isReverse = True
        self.length = 8
        self.format = '<Q' # little-endian integer 8 bytes
        self.value = tools.value(self,tx)

    def __str__ (self) :
        return f"{self.label} {self.value}"
