#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Exercice 1.1.4
"""

import math

class Cercle:

    """
        class
    """

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):

        """
            function
        """

        return math.pi*self.rayon**2

    def perimetre(self):

        """
            function
        """

        return 2*math.pi*self.rayon

def exemple():

    """
        function
    """

    cercle = Cercle(1)
    print("L'aire du disque de rayon " + str(cercle.rayon) + " est " \
    + str(cercle.aire()))
    print("Le périmètre du cercle de rayon " + str(cercle.rayon) + " est " \
    + str(cercle.perimetre()))

exemple()
