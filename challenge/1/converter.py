#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import struct
import block_header
import tx
import wget

def hexadecimal2decimal(hexadecimal):
    return int.from_bytes(bytes.fromhex(hexadecimal), 'big', signed=False)
    #return int(str(hexadecimal), 16)

def decimal2hexadecimal(decimal):
    return hex(decimal)

def hexadecimal_little_endian2decimal(hexadecimal_little_endian):
    return int.from_bytes(bytes.fromhex(hexadecimal_little_endian), 'little', signed=False)

def varInt2decimal(varInt):
    varInt = io.BytesIO(bytes.fromhex(varInt))
    size, = struct.unpack('B', varInt.read(1))
    if size < 0xfd :
        value = size
    if size == 0xfd :
        value, = struct.unpack('<H', varInt.read(2))
    if size == 0xfe :
        value, = struct.unpack('<I', varInt.read(4))
    if size == 0xff :
        value, = struct.unpack('<Q', varInt.read(8))
    return value

def bits2target(bits):
    bits = bytes.fromhex(bits)
    return int.from_bytes(bits[1:] + (int.from_bytes(bits[:1], 'big') - 3) * b'\x00', 'big')

def target2difficulty(target):
    targetmax = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
    return targetmax / target

def decode_transaction(raw):
    print(tx.Tx(io.BytesIO(bytes.fromhex(raw))))

def decode_block(hash):
    url = 'http://learnmeabitcoin.com/browser/block/download.php?hash=' + hash
    raw_block = wget.download(url)
    with open(raw_block,'r') as myfile:
        raw = myfile.read()
    print(block_header.BlockHeader(io.BytesIO(bytes.fromhex(raw))))

def navigate(raw) :
    return True
