#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import version
import segwit
import input_count
import input
import output_count
import output
import witness_count
import witness
import locktime

class Tx :
    def __init__(self,tx) :
        self.version = version.Version(tx)
        self.input_count = input_count.InputCount(tx)
        if self.input_count.value == 0 :
            self.segwit = segwit.Segwit(tx)
            self.input_count = input_count.InputCount(tx)
        else:
            self.segwit = None
        self.inputs = []
        for i in range(self.input_count.value) :
            self.inputs.append(input.Input(tx))
        self.output_count = output_count.OutputCount(tx)
        self.outputs = []
        for i in range(self.output_count.value) :
            self.outputs.append(output.Output(tx))
        if self.segwit is not None :
            self.witness_count = witness_count.WitnessCount(tx)
            self.witnesss = []
            for i in range(self.witness_count.value) :
                self.witnesss.append(witness.Witness(tx))
        self.locktime = locktime.Locktime(tx)

    def __str__ (self) :
        print(self.version)
        if self.segwit is not None :
            print(self.segwit)
        print(self.input_count)
        for i in range(self.input_count.value):
            print("Input",i+1)
            print(self.inputs[i])
        if self.output_count.value is not None :
            print(self.output_count)
            for i in range(self.output_count.value):
                print("Output",i+1)
                print(self.outputs[i])
        if self.segwit is not None :
            print(self.witness_count)
            for i in range(self.witness_count.value) :
                print("Witness",i+1)
                print(self.witnesss[i])
            print(self.locktime)
        return ""
