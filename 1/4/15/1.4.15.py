#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 1.4.14 (optionnel)
"""

import io
import hashlib
import block_header
import tools_bits

def hash_block_header(block_hex):
    """
    hash_block_header(block_hex)
    """
    block_header_bin = bytearray.fromhex(block_hex)[:80]
    hash_header = hashlib.sha256(hashlib.sha256(block_header_bin).digest()).digest()
    # print(hash[::-1].hex())
    # 0000000026f34d197f653c5e80cb805e40612eadb0f45d00d7ea4164a20faa33
    # pour le block 50
    return hash_header[::-1].hex()

def validation_POW(block_hex):
    """
    validationPOW(block_hex)
    """
    block = block_header.BlockHeader(io.BytesIO(bytes.fromhex(block_hex)))
    exposant, coefficient = tools_bits.bits2target(block.bits.value)
    hash_header = hash_block_header(block_hex)
    print(tools_bits.cible_atteinte(coefficient, exposant, hash_header))

validation_POW("01000000008de6ae7a37b4f26a763f4d65c5bc7feb1ad9e3ce0fff4190c067f0000000000913281db730c5cff987146330508c88cc3e642d1b9f5154854764fd547e0a54eaf26849ffff001d2e4a4c3d0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d013fffffffff0100f2052a010000004341041ada81ea00c11098d2f52c20d5aa9f5ba13f9b583fda66f2a478dd7d95a7ab615159d98b63df2e6f3ecb3ef9eda138e4587e7afd31e7f434cbb6837e17feb0c5ac00000000")
