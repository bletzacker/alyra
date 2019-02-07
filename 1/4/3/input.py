#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import txid
import vout
import script_sig_size
import script_sig
import sequence

class Input () :

    def __init__(self) :
        self.txid = txid.Txid()
        self.vout = vout.Vout()
        self.scriptSigSize = script_sig_size.ScriptSigSize()
        self.scriptSig = script_sig.ScriptSig()
        self.sequence = sequence.Sequence()

    def __str__ (self) :
        print(self.txid)
        print(self.vout)
        print(self.scriptSigSize)
        print(self.scriptSig)
        print(self.sequence)
        return ""

    
