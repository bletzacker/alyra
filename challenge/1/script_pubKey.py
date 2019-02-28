#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tools
import weakref

class ScriptPubKey :

    def __init__(self,tx,parent) :
        self.parent = weakref.ref(parent) # https://stackoverflow.com/a/10791613
        self.label = "  ScriptPubKey :"
        self.isVarInt = False
        self.isRaw = True
        self.isReverse = False
        self.length = parent.script_pubKey_size.value
        self.value = tools.value(self,tx)

    def __str__ (self) :
        return f"{self.label} {self.value}"
