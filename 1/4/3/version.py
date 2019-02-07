#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools import set_raw

class Version :

    def __init__(self) :
        self.label = "Version (reverse byte order) :"
        self.isVarInt = False
        self.length = 4
        self.raw = None

    def __str__ (self) :
        return f"{self.label} {self.raw}"

    def parcours(self,f,raw) :
        return set_raw(self,f,raw)
