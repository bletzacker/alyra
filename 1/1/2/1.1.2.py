#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Utilisation d'un algorithme de recherche par dichotomie itératif

def saisie_utilisateur() :
    notIntegerBetweenOneAndHundred = True
    while notIntegerBetweenOneAndHundred :
        solution = input("Saisir un nombre entre 1 et 100 : ")
        if solution.isdigit() :
            solution = int(solution)
            if min <= solution <= max :
                notIntegerBetweenOneAndHundred = False
                return solution

def verifie(estimation,solution) :
    if estimation == solution :
        return True
    else :
        return False

def recherche(solution) :
    a = min
    b = max
    estimation = 0
    i = 0
    while not verifie(estimation,solution):
        estimation = int((a+b)/2)
        if solution > estimation :
            a = estimation + 1
        else :
            b = estimation - 1
        i+=1
    print("\nJ'ai trouvé en " + str(i) + " itérations. Le nombre saisi est : " + str(estimation))

min = 1
max = 100
solution = saisie_utilisateur()
recherche(solution)
