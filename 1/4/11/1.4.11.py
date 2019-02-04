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
    i = 100 # Calcul d'un temps moyen comme estimateur sans biais pour une même taille (sinon problématique des fluctuations aléatoires)
    temps_moyen = statistics.mean([rechercheDebut("AA",size) for _ in range(i)])
    print("Longueur Chaîne :",len("AA"),"Taille :",size,"Temps moyen (s) :", temps_moyen)

size = 10

i = 10 # Calcul d'un temps moyen comme estimateur sans biais pour une même taille (sinon problématique des fluctuations aléatoires)
temps_moyen = statistics.mean([rechercheDebut("A",size) for _ in range(i)])
print("Longueur Chaîne :",len("A"),"Taille :",size,"Temps moyen (s) :", temps_moyen)

i = 10 # Calcul d'un temps moyen comme estimateur sans biais pour une même taille (sinon problématique des fluctuations aléatoires)
temps_moyen = statistics.mean([rechercheDebut("AA",size) for _ in range(i)])
print("Longueur Chaîne :",len("AA"),"Taille :",size,"Temps moyen (s) :", temps_moyen)

i = 10 # Calcul d'un temps moyen comme estimateur sans biais pour une même taille (sinon problématique des fluctuations aléatoires)
temps_moyen = statistics.mean([rechercheDebut("AAA",size) for _ in range(i)])
print("Longueur Chaîne :",len("AAA"),"Taille :",size,"Temps moyen (s) :", temps_moyen)

i = 10 # Calcul d'un temps moyen comme estimateur sans biais pour une même taille (sinon problématique des fluctuations aléatoires)
temps_moyen = statistics.mean([rechercheDebut("AAAA",size) for _ in range(i)])
print("Longueur Chaîne :",len("AAAA"),"Taille :",size,"Temps moyen (s) :", temps_moyen)

# Temps approximatif pour obtenir les résultats : 2 mn
# Conclusion : La complexité est nettement supérieure pour la longueur du motif à chercher par rapport à la taille n.
# Nous retrouvons la complexité exponentielle en fonction de la longueur du motif recherché en début de chaîne
