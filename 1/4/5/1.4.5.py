#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def pile_vide() :
    return []

def empiler(data,p) :
    p.append(data)
    return p

def depiler(p) :
    return p.pop()

def sommet(p) :
    return p[-1]

def calculatrice_NPI(expression) :

    chars = expression.split(" ")
    p = pile_vide()

    for char in chars :
        if char.isdigit() :
            empiler(float(char),p)
        else :
            resultat = {
            '+' : lambda x,y : y + x,
            '-' : lambda x,y : y - x,
            '*' : lambda x,y : y * x,
            '/' : lambda x,y : y / x
            }[char](depiler(p),depiler(p))
            empiler(resultat,p)

    return sommet(p)

expression ="21 7 / 4 2 / -" # = 1
print("L'évaluation de + " + expression + " est :", calculatrice_NPI(expression))
