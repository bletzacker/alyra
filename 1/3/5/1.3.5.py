#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import hashlib
import base58

def sha256(key) :
    return hashlib.sha256(key).digest()

def ripemd160(key) :
    hash = hashlib.new('ripemd160')
    hash.update(key)
    return hash.digest()

class Bitcoin_address :
    def __init__(self,key) :
        hash = b'\x00' + ripemd160(sha256(key))
        checksum = sha256(sha256(hash)).hex()
        hash = hash.hex()
        hash += checksum[:8]
        self.bitcoin_address = base58.b58encode(hash)

    def __str__(self) :
        return '{}'.format(self.bitcoin_address.decode("utf-8"))

key = random.getrandbits(256).to_bytes(32, 'big')
print(Bitcoin_address(key))
