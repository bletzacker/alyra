#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools import position
import version
import input_count
import input
import output_count
import output
import locktime


class Tx :

    def __init__(self,raw) :
        self.raw = raw
        self.version = version.Version()
        self.inputCount = input_count.InputCount()
        self.inputs = []
        self.outputCount = output_count.OutputCount()
        self.outputs = []
        self.locktime = locktime.Locktime()

    def __str__ (self) :
        print(self.version)
        print(self.inputCount)
        for i in range(self.inputCount.decimal):
            print("Input :",i+1)
            print(self.inputs[i])
        if self.outputCount.decimal is not None :
            print(self.outputCount)
            for i in range(self.outputCount.decimal):
                print("Output :",i+1)
                print(self.outputs[i])
            print(self.locktime)
        return ""

    def parcours(self) :
        pos = 0
        pos = self.version.parcours(pos,self)
        pos = self.inputCount.parcours(pos,self)
        for i in range(self.inputCount.decimal) :
            self.input = input.Input()
            pos = self.input.txid.parcours(pos,self)
            pos = self.input.vout.parcours(pos,self)
            d = pos
            pos = self.input.scriptSigSize.parcours(pos,self)
            self.input.scriptSig.length = int(self.raw[d:pos],16)
            pos = self.input.scriptSig.parcours(pos,self)
            pos = self.input.sequence.parcours(pos,self)
            self.inputs.append(self.input)

        if pos != len(self.raw) :
            pos = self.outputCount.parcours(pos,self)
            for i in range(self.outputCount.decimal) :
                self.output = output.Output()
                pos = self.output.value.parcours(pos,self)
                d = pos
                pos = self.output.scriptPubKeySize.parcours(pos,self)
                self.output.scriptPubKey.length = int(self.raw[d:pos],16)
                pos = self.output.scriptPubKey.parcours(pos,self)
                self.outputs.append(self.output)

        if pos != len(self.raw) :
            pos = self.locktime.parcours(pos,self)
