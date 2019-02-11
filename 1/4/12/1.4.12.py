#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 1.4.12
"""

import secrets
import hashlib
import time
import statistics

def hash_function(size):

    """
        function hash(size)
    """

    key = secrets.token_bytes(size//8)

    if size == 224:
        condensat = hashlib.sha3_224(key).digest()

    if size == 256:
        condensat = hashlib.sha3_256(key).digest()

    if size == 384:
        condensat = hashlib.sha3_384(key).digest()

    if size == 512:
        condensat = hashlib.sha3_512(key).digest()

    return condensat


def recherche_debut(motif, size):

    """
        function recherche_debut(motif,size)
    """

    t_initial = time.time()
    i = 0
    while hash_function(size)[:len(motif)] != motif:
        i += 1
    return time.time() - t_initial


def test():

    """
        function test()

        Calcul d'un temps moyen comme estimateur sans biais pour une même taille
        (sinon problématique des fluctuations aléatoires)
    """

    for size in (224, 256, 384, 512):
        i = 100
        temps_moyen = statistics.mean([recherche_debut(b'\x00\x00', size) for _ in range(i)])
        print("Longueur Chaîne :", len(b'\x00\x00'), "Taille :", size,
              "Temps moyen (s) :", temps_moyen)

    size = 256
    i = 100
    temps_moyen = statistics.mean([recherche_debut(b'\x00', size) for _ in range(i)])
    print("Longueur Chaîne :", len(b'\x00'), "Taille :", size,
          "Temps moyen (s) :", temps_moyen)

    i = 100
    temps_moyen = statistics.mean([recherche_debut(b'\x00\x00', size) for _ in range(i)])
    print("Longueur Chaîne :", len(b'\x00\x00'), "Taille :", size,
          "Temps moyen (s) :", temps_moyen)

    i = 1
#    temps_moyen = statistics.mean([recherche_debut(b'\x00\x00\x00', size) for _ in range(i)])
#    print("Longueur Chaîne :", len(b'\x00\x00\x00'), "Taille :", size,
#          "Temps moyen (s) :", temps_moyen)


test()

# Temps approximatif pour obtenir les résultats :
# environ 2mn et supérieur à 5 mn avec le motif b'\x00\x00\x00'
#
# Conclusion : La complexité est nettement supérieure pour la longueur du motif
# à chercher et presque indépendante de la fonction de hachage utilisée,
# c'est-à-dire de la taille du condensat.
# Nous retrouvons la complexité exponentielle en fonction de la longueur
# du motif recherché en début de chaîne, ici en imposant une cible plus petite
# avec des b'\x00 en début de chaîne.
