#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def chiffreCesar(string, decalage) :
    chars = [char for char in string]
    return print(''.join(list(map(lambda char: chr(ord(char) + decalage), chars))))

chiffreCesar("abc", 1)
