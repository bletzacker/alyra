#!/usr/bin/env python3
# -*- coding : utf-8 -*-

class Noeud :
    def __init__(self, v) :
        self.gauche = None
        self.droit = None
        self.valeur = v

    def rechercher(self, val) :
        if (self.valeur == val) :
            return "La valeur " + str(val) + " appartient à l'arbre."
        elif self.valeur > val :
            if self.gauche :
                return self.gauche.rechercher(val)
            else :
                return "La valeur " + str(val) + " n'appartient pas à l'arbre."
        else :
            if self.droit :
                return self.droit.rechercher(val)
            else :
                return "La valeur " + str(val) + " n'appartient pas à l'arbre."

    def infixe(self) :
        if self :
            if self.gauche :
                self.gauche.infixe()
            print(str(self.valeur))
            if self.droit :
                self.droit.infixe()

class Arbre :
    def __init__(self) :
        self.racine = None

    def ajouter(self, val) :
        if(self.racine == None) :
            self.racine = Noeud(val)
        else :
            self._ajouter(val, self.racine)

    def _ajouter(self, val, nd) :
        if(val < nd.valeur  ) :
            if(nd.gauche is not None) :
                self._ajouter(val, nd.gauche)
            else :
                nd.gauche = Noeud(val)
        else :
            if(nd.droit is not None) :
                self._ajouter(val, nd.droit)
            else :
                nd.droit = Noeud(val)

    def rechercher(self, val) :
        if self.racine :
            return self.racine.rechercher(val)
        else :
            return False

    def infixe(self) :
        if self.racine is not None :
            self.racine.infixe()

    def supprimer(self, val) :
        # Cas de l'arbre vide
        if self.racine is None :
            return False

        # Cas de val dans le noeud racine
        elif self.racine.valeur == val :
            if self.racine.gauche is None and self.racine.droit is None :
                self.racine = None
            elif self.racine.gauche and self.racine.droit is None :
                self.racine = self.racine.gauche
            elif self.racine.gauche is None and self.racine.droit :
                self.racine = self.racine.droit
            elif self.racine.gauche and self.racine.droit :
                noeudParent = self.racine
                noeud = self.racine.droit
                while noeud.gauche :
                    noeudParent = noeud
                    noeud = noeud.gauche

                self.racine.valeur = noeud.valeur
                if noeud.droit :
                    if noeudParent.valeur > noeud.valeur :
                        noeudParent.gauche = noeud.droit
                    elif noeudParent.valeur < noeud.valeur :
                        noeudParent.droit = noeud.droit
                else :
                    if noeud.valeur < noeudParent.valeur :
                        noeudParent.gauche = None
                    else :
                        noeudParent.droit = None

            return True

        parent = None
        node = self.racine

        # Détermination du noeud à supprimmer
        while node and node.valeur != val :
            parent = node
            if val < node.valeur :
                node = node.gauche
            elif val > node.valeur :
                node = node.droit

        # Cas 1 de l'absence de val dans l'arbre
        if node is None or node.valeur != val :
            return False

        # Cas 2 du noeud sans enfant
        elif node.gauche is None and node.droit is None :
            if val < parent.valeur :
                parent.gauche = None
            else :
                parent.droit = None
            return True

        # Cas 3 du noeud avec seulement 1 enfant à gauche
        elif node.gauche and node.droit is None :
            if val < parent.valeur :
                parent.gauche = node.gauche
            else :
                parent.droit = node.gauche
            return True

        # Cas 4 du noeud avec seulement 1 enfant à droite
        elif node.gauche is None and node.droit :
            if val < parent.valeur :
                parent.gauche = node.droit
            else :
                parent.droit = node.droit
            return True

        # Cas 5 du noeud avec 2 enfants
        else :
            noeudParent = node
            noeud = node.droit
            while noeud.gauche :
                noeudParent = noeud
                noeud = noeud.gauche

            node.valeur = noeud.valeur
            if noeud.droit :
                if noeudParent.valeur > noeud.valeur :
                    noeudParent.gauche = noeud.droit
                elif noeudParent.valeur < noeud.valeur :
                    noeudParent.droit = noeud.droit
            else :
                if noeud.valeur < noeudParent.valeur :
                    noeudParent.gauche = None
                else :
                    noeudParent.droit = None

arbre = Arbre()
arbre.ajouter(15)
arbre.ajouter(8)
arbre.ajouter(17)
arbre.ajouter(5)
arbre.infixe()
print(arbre.rechercher(8))
print(arbre.rechercher(9))
arbre.supprimer(8)
arbre.infixe()
