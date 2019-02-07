#!/usr/bin/env python3
# -*- coding: utf-8 -*-

byte = 2

def position(pos,size_field) :
    return pos + size_field * byte

def set_raw(self,pos,tx) :
    d = pos
    f = position(d,self.length)
    self.raw = tx.raw[d:f]
    return f

def set_raw_count(self,pos,tx) :
    pos = set_raw(self,pos+2,tx)
    self.decimal = int(self.raw[::-1],16)
    return pos

def varint(self,pos,tx) :
    if tx.raw[pos:pos+2] == "fd" :
        self.length = 2
        return set_raw_count(self,pos,tx)
    elif tx.raw[pos:pos+2] == "fe" :
        self.length = 4
        return set_raw_count(self,pos,tx)
    elif tx.raw[pos:pos+2] == "ff" :
        self.length = 8
        return set_raw_count(self,pos,tx)
    else :
        self.length = 1
        p = set_raw(self,pos,tx)
        self.decimal = int(self.raw,16)
        return p
