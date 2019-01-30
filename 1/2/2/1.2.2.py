#!/usr/bin/env python3
# -*- coding: utf-8 -*-

transactions = [(2000,13000),(6000,9000),(800,2000),(700,1500),(1200,3500),(1000,2800),(1300,5000),(600,1500)]
tailles = [transaction[0] for transaction in transactions]
pourboires = [transaction[1] for transaction in transactions]

n = len(transactions)
combinaisons_sous_contrainte = []
maximum = 0

for i in range(0,(2**n-1)+1) :

    combinaison = bin(i)[2:].zfill(n)
    combinaison = list("".join(combinaison.split()))
    combinaison = list(map(lambda x: int(x), combinaison))

    if sum(indice * taille for indice, taille in zip(combinaison,tailles)) <= 6000 :
        combinaisons_sous_contrainte.append(combinaison)
        tmp = sum(indice * pourboire for indice, pourboire in zip(combinaison,pourboires))
        if tmp > maximum :
            maximum = tmp

print("Le pourboire maximum est " + str(maximum) + " obtenu pour :")
for combinaison in combinaisons_sous_contrainte :
    if sum(indice * pourboire for indice, pourboire in zip(combinaison,pourboires)) == maximum :
        print(combinaison)
print("\navec pour exemple de lecture : [1, 0, 1, 0, 1, 0, 1, 1] qui signifie que les transactions 1,3,5,7 et 8 sont à inclure.")

# Il s'agit du problème du sac à dos dont les algorithmes optimisés sont disponibles par exemple sur : https://www.supinfo.com/cours/2ADS/chapitres/05-programmation-dynamique

# L'algorithme par approche exhaustive a une complexité en O(2^n) (l'ajout d'une nouvelle transaction multplie par 2 tous les précédentes possibilités). Il s'agit d'une complexité exponentielle.
