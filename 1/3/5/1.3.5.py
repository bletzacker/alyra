#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import hashlib
import base58

def sha256(bstring) :
    return hashlib.sha256(str.encode(bstring)).hexdigest()

def ripemd160(bstring) :
    hash = hashlib.new('ripemd160')
    hash.update((str.encode(bstring)))
    return hash.hexdigest()

class Bitcoin_address :
    def __init__(self,key) :
        hash = ripemd160(sha256(str(key)))
        hash = '0x00' + hash
        checksum = sha256(sha256(hash))
        hash = hash + checksum[:8]
        self.bitcoin_address = base58.b58encode(hash)

    def __str__(self) :
        return '{}'.format(self.bitcoin_address.decode("utf-8"))

key = random.random()
print(Bitcoin_address(key))
