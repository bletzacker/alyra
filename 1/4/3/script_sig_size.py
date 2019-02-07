#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools import varint

class ScriptSigSize :

    def __init__(self) :
        self.label = "  ScriptSig Size :"
        self.isVarInt = True
        self.length = 1
        self.raw = None
        self.decimal = None

    def __str__ (self) :
        return f"{self.label} {self.raw}"

    def parcours(self,pos,tx) :
        return varint(self,pos,tx)
