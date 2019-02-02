#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CourbeElliptique:
    def __init__(self, a, b) :
        self.a = a
        self.b = b
        if 4*a**3+27*b**2 == 0 :
            raise ValueError('y^2 = x^3 + {}x + {} n\'est pas une courbe valide'.format(self.a, self.b))

    def __eq__(self, other) :
        return (self.a, self.b) == (other.a, other.b)

    def testPoint(self,x, y) :
         return True if y**2 == x**3 + self.a * x + self.b else False

    def __str__(self) :
        return 'y^2 = x^3 + {}x + {}'.format(self.a, self.b)

c1 = CourbeElliptique (0,7)
print("c1 : ",c1)
c2 = CourbeElliptique (2,4)
print("c2 : ",c2)
c3 = CourbeElliptique (2,4)
print("c3 : ",c3)
c4 = CourbeElliptique (0,1)
print("c4 : ",c4)
c5 = CourbeElliptique (0,1)

print("Equivalence de c1 et c2 : ", c1 == c2)
print("Equivalence de c2 et c3 : ", c2 == c3)

print("Appartenance du point (2,16) à c4 : ", c4.testPoint(2,16))
print("Appartenance du point (0,-1) à c4 : ", c4.testPoint(0,-1))
