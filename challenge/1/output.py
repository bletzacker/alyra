#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import value
import script_pubKey_size
import script_pubKey

class Output () :

    def __init__(self,tx) :
        self.value = value.Value(tx)
        self.script_pubKey_size = script_pubKey_size.ScriptPubKeySize(tx)
        self.script_pubKey = script_pubKey.ScriptPubKey(tx,self)

    def __str__ (self) :
        print(self.value)
        print(self.script_pubKey_size)
        print(self.script_pubKey)
        return ""
