#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def frequences(string) :
    chars = [char for char in string]
    occurence = {}
    for char in chars :
        if occurence.get(char) :
            occurence[char] +=  1
        else :
            occurence[char] = 1
    print(occurence)

frequences("Etre contesté, c’est être constaté")
