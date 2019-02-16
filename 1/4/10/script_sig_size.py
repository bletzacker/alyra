#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tools

class ScriptSigSize :

    def __init__(self,tx) :
        self.label = "  ScriptSig Size (bytes) :"
        self.isVarInt = True
        self.isRaw = False
        self.length = 1
        self.format = 'B'
        self.value = tools.value(self,tx)

    def __str__ (self) :
        return f"{self.label} {self.value}"
