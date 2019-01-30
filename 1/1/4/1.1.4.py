#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Cercle :

    def __init__(self, rayon) :
      self.rayon = rayon

    def aire(self) :
        return math.pi*self.rayon**2

    def perimetre(self) :
        return 2*math.pi*self.rayon

cercle = Cercle(1)
print("L'aire du disque de rayon " + str(cercle.rayon) + " est " + str(cercle.aire()))
print("Le périmètre du cercle de rayon " + str(cercle.rayon) + " est " + str(cercle.perimetre()))
