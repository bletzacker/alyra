#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 1.4.13
"""
import secrets
import hashlib
import time
import statistics

def hash_complexity(message_hash_size):

    """
        function hash_complexity(message_hash_size)
    """

    key = secrets.token_bytes(message_hash_size//8)
    t_initial = time.time()
    hashlib.sha3_256(key).digest()
    return time.time() - t_initial

def test():

    """
        function test()
    """

    for power in range(8, 20):
        message_hash_size = 2**power
        i = 100
        temps_moyen = statistics.mean([hash_complexity(message_hash_size) for _ in range(i)])
        print("Taille :", message_hash_size, "Temps moyen (10**-6 s) :", temps_moyen*10**6)

test()

# Quelle est la complexité de rechercher un hash en modifiant le nonce ?
#
# Sa complexité est constante compte-tenu de la taille fixe
# du champ "nonce" (4 octets). Cependant, ce champs est trop court pour
# permettre d’atteindre un hash inférieur à la cible.
#
# Quelle est cette complexité en modifiant le ScriptSig de la transaction
# Coinbase ?
#
# Utiliser le champ libre (sur maximum 100 octets) ScriptSig de la transaction
# coinbase permet d'atteindre la cible. Cependant, notre étude montre
# une multiplication par 2 du temps en fonction de la taille de la clé pour
# le calcul du hash donc une complexité exponentielle pour l'utilisation
# du champ ScriptSig.
