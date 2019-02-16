#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tools

class PreviousBlochHash :

    def __init__(self,tx) :
        self.label = "Previous Block Hash :"
        self.isVarInt = False
        self.isRaw = True
        self.isReverse = True
        self.length = 32
        self.value = tools.value(self,tx)

    def __str__ (self) :
        return f"{self.label} {self.value}"
