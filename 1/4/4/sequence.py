#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools import set_raw

class Sequence :

    def __init__(self) :
        self.label = "  Sequence (reverse byte order) :"
        self.isVarInt = False
        self.length = 4
        self.raw = None

    def __str__ (self) :
        return f"{self.label} {self.raw}"

    def parcours(self,pos,tx) :
        return set_raw(self,pos,tx)
