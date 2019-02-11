#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 1.1.1
    Utilisation d'un algorithme de recherche par dichotomie itératif
"""

def saisie_utilisateur(borne_min, borne_max):

    """
        function
    """

    not_integer_between_one_and_hundred = True
    while not_integer_between_one_and_hundred:
        solution = input("Saisir un nombre entre 1 et 100 : ")
        if solution.isdigit():
            solution = int(solution)
            if borne_min <= solution <= borne_max:
                not_integer_between_one_and_hundred = False
                return solution

def verifie(estimation, solution):

    """
        function
    """

    return bool(estimation == solution)

def recherche(solution, borne_min, borne_max):

    """
        function
    """

    estimation = 0
    i = 0
    while not verifie(estimation, solution):
        estimation = int((borne_min+borne_max)/2)
        if solution > estimation:
            borne_min = estimation + 1
        else:
            borne_max = estimation - 1
        i += 1
    print("\nJ'ai trouvé en " + str(i) + " itérations. Le nombre saisi est : " + str(estimation))

def dichotomie():

    """
        function
    """

    borne_min = 1
    borne_max = 100
    solution = saisie_utilisateur(borne_min, borne_max)
    recherche(solution, borne_min, borne_max)

dichotomie()
