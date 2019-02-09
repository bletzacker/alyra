#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def palindrome(string) :
    string = ''.join(string.split())
    if string == string[::-1] :
        print(string + " est un palindrome.")
        return True
    else :
        print(string + " n'est pas un palindrome.")
        return False

palindrome("ressasser")
palindrome("alyra")
palindrome("ESOPE RESTE ICI ET SE REPOSE")
