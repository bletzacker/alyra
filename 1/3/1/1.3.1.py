#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def chiffreCesar(string, decalage) :
    chars = [char for char in string]
    return print(''.join(list(map(lambda char: chr((ord(char) + decalage - ord('a')) % 26 + ord('a')), chars))))

chiffreCesar("abc", -1)
chiffreCesar("xyz",3)
