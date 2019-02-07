#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools import varint

class InputCount :

    def __init__(self) :
        self.label = "varInt Input Count :"
        self.isVarInt = True
        self.length = None
        self.raw = None
        self.inputs = None
        self.decimal = None

    def __str__ (self) :
        return f"{self.label} {self.raw}"

    def parcours(self,pos,tx) :
        return varint(self,pos,tx)
