#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import witness_size
import witness_value

class Witness () :

    def __init__(self,tx) :
        self.witness_size = witness_size.WitnessSize(tx)
        self.witness_value = witness_value.WitnessValue(tx,self)

    def __str__ (self) :
        print(self.witness_size)
        print(self.witness_value)
        return ""
