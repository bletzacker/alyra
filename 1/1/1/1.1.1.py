#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

target = random.randint(1, 100)
notFound = True

print("J'ai tiré aléatoirement un nombre entre 1 et 100 que je vous propose de retrouver.\n")

while notFound:

    notIntegerBetweenOneAndHundred = True
    while notIntegerBetweenOneAndHundred :
        proposal = input("Entrez votre proposition sous la forme d'un entier entre 1 et 100 : ")
        if proposal.isdigit() :
            proposal = int(proposal)
            if 1 <= proposal <= 100 :
                notIntegerBetweenOneAndHundred = False

    difference = proposal - target

    if difference == 0 :
        print("Bravo ! Vous avez trouvé le nombre que j'ai tiré aléatoirement.\n")
        notFound = False
    else :
        if difference > 0 :
            print("Mon nombre est inférieur.")
        else :
            print("Mon nombre est supérieur.")

        if abs(difference) <= 5 :
            print("De plus, votre proposition est très proche, moins de 5 unités d'écart.\n")
        elif abs(difference) <= 10 :
            print("De plus, Votre proposition est proche, entre 6 et 10 unités d'écart.\n")
        else :
            print("De plus, votre proposition est éloignée de plus de 10 unités.\n")
