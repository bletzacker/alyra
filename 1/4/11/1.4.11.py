#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random
import time
import statistics

def chaineAlea(size) :
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))

def rechercheDebut(string,size) :
    t1 = time.time()
    i = 0
    while chaineAlea(size)[:len(string)] != string :
        i += 1
    return time.time() - t1

for size in range(10,110,10) :
    n = 100 # Calcul d'un temps moyen comme estimateur sans biais pour une même taille (sinon problématique des fluctuations aléatoires)
    temps_moyen = statistics.mean([rechercheDebut("AA",size) for _ in range(n)])
    print("Taille :",size,"Temps moyen (s) :", temps_moyen)
