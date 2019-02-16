#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import version_block
import previous_block_hash
import merkle_root
import unix_time
import bits
import nonce
import tx_count
import tx

class BlockHeader:
    def __init__(self,block):
        self.version_block = version_block.VersionBlock(block)
        self.previous_block_hash = previous_block_hash.PreviousBlochHash(block)
        self.merkle_root = merkle_root.MerkleRoot(block)
        self.unix_time = unix_time.UnixTime(block)
        self.bits = bits.Bits(block)
        self.nonce = nonce.Nonce(block)
        self.tx_count = tx_count.TxCount(block)
        self.txs = []
        for i in range(self.tx_count.value):
            self.txs.append(tx.Tx(block))

    def __str__ (self):
        print(self.version_block)
        print(self.previous_block_hash)
        print(self.merkle_root)
        print(self.unix_time)
        print(self.bits)
        print(self.nonce)
        print(self.tx_count)
        for i in range(self.tx_count.value):
            print("Transaction",i+1)
            print(self.txs[i])
        return ""
