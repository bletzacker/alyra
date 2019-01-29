# -*- coding: utf-8 -*-

def palindrome(string):
    str = string
    str = ''.join(str.split())
    for i in range(int(len(string)/2)) :
        if str[i] != str[len(str)-1-i] :
            return print(string + " n'est pas un palindrome.")
    return print(string + " est un palindrome.")

palindrome("ressasser")
palindrome("alyra")
palindrome("ESOPE RESTE ICI ET SE REPOSE")
