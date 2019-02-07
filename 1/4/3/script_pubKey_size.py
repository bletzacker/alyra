#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools import varint

class ScriptPubKeySize :

    def __init__(self) :
        self.label = "  ScriptPubKey Size :"
        self.isVarInt = True
        self.length = None
        self.raw = None
        self.decimal = None

    def __str__ (self) :
        return f"{self.label} {self.raw}"

    def parcours(self,pos,tx) :
        return varint(self,pos,tx)
