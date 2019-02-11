#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 1.1.3
"""

def palindrome(string):

    """
        function
    """

    string = ''.join(string.split())
    if string == string[::-1]:
        answer = (string + " est un palindrome.")
    else:
        answer = (string + " n'est pas un palindrome.")
    print(answer)

palindrome("ressasser")
palindrome("alyra")
palindrome("ESOPE RESTE ICI ET SE REPOSE")
