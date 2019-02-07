#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import value
import script_pubKey_size
import script_pubKey

class Output () :

    def __init__(self) :
        self.value = value.Value()
        self.scriptPubKeySize = script_pubKey_size.ScriptPubKeySize()
        self.scriptPubKey = script_pubKey.ScriptPubKey()

    def __str__ (self) :
        print(self.value)
        print(self.scriptPubKeySize)
        print(self.scriptPubKey)
        return ""
