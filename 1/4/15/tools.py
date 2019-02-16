#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

def value (self,tx) :
    if self.isRaw == True and self.isReverse == True :
        return tx.read(self.length)[::-1].hex()
    elif self.isRaw == True and self.isReverse == False :
        return tx.read(self.length).hex()
    else :
        if self.isVarInt is False :
            value, = struct.unpack(self.format, tx.read(self.length))
            return value
        else :
            size, = struct.unpack(self.format, tx.read(self.length))
            if size < 0xfd :
                value = size
            if size == 0xfd :
                value, = struct.unpack('<H', tx.read(2))
            if size == 0xfe :
                value, = struct.unpack('<I', tx.read(4))
            if size == 0xff :
                value, = struct.unpack('<Q', tx.read(8))
            return value
