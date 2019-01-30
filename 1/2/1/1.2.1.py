#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factorielle_iterative(n) :
    factorielle = 1
    nombre_operation = 0
    for i in range(2,n+1) :
        factorielle = i * factorielle
        nombre_operation +=1
    print("Nombre d'opérations : " + str(nombre_operation))
    return factorielle

def factorielle_recursive(n) :
    if n == 0 :
        return 1
    else :
        return n * factorielle_recursive(n-1)

for n in range(4) :
    print("Pour n = " + str(n) + " :")
    print("La factorielle calculée par un algorithme itératif de " + str(n) + " est " + str(factorielle_iterative(n)))
    print("La factorielle calculée par un algorithme récursif de " + str(n) + " est " + str(factorielle_recursive(n)) + "\n")


# Cas particulier pour n = 0 :
# 0! = 1  par définition donc 0 opération à effectuer

# Pour n >= 1, il y a n-1 opérations à effectuer. Complexité linéaire en O(n).
