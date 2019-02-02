#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import egcd

def pgcd(a,b) :
    while b :
        r = a % b
        a,b = b,r
    return a

def rsa_generation_key(p,q) :
    n = p * q
    phi_n = (p-1)*(q-1)
    c = random.randint(2, phi_n-1)
    while pgcd(c,phi_n) != 1 :
        c = random.randint(2, phi_n-1)
    d = egcd.egcd(c,phi_n)[1]
    if d <= 0 :
        d = d % phi_n
    rsa_pub = (n,c)
    rsa_pri = (n,d)
    print ("La clef public est rsa_pub : ",rsa_pub)
    print ("La clef privé est rsa_pri : ",rsa_pri )
    return (rsa_pub,rsa_pri)

def rsa_chiffrement(rsa_pub,M) :
    (n,c) = rsa_pub
    return (M**c) % n

def rsa_dechiffrement(rsa_pri,C) :
    (n,d) = rsa_pri
    return (C**d) % n

p = 107
q = 71

rsa = rsa_generation_key(p,q)
rsa_pub = rsa[0]
rsa_pri = rsa[1]

M = 37
print("Message initial : ",M)
C = rsa_chiffrement(rsa_pub,M)
print("Message chiffré : ",C)
print("Message déchiffré : ", rsa_dechiffrement(rsa_pri,C))

# Principales fragilités de mon programme :
# - nécessité de générer aléatoirement de très grands nombres premiers
# - nécessité d'utiliser un algorithme d'exponentiation rapide pour M**c et C**d
