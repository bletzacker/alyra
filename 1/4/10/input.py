#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import txid
import vout
import script_sig_size
import script_sig
import sequence

class Input () :

    def __init__(self,tx) :
        self.txid = txid.Txid(tx)
        self.vout = vout.Vout(tx)
        self.script_sig_size = script_sig_size.ScriptSigSize(tx)
        self.script_sig = script_sig.ScriptSig(tx,self)
        self.sequence = sequence.Sequence(tx)

    def __str__ (self) :
        print(self.txid)
        print(self.vout)
        print(self.script_sig_size)
        print(self.script_sig)
        print(self.sequence)
        return ""
