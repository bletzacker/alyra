#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tools

class Segwit :

    def __init__(self,tx) :
        self.label = "Segwit :"
        self.isVarInt = False
        self.isRaw = False # à vérifier
        self.isReverse = False # à vérifier
        self.length = 1
        self.format = 'B'
        self.value = tools.value(self,tx)

    def __str__ (self) :
        return f"{self.label} {self.value}"
