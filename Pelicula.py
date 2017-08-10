# -*- coding: cp1252 -*-
class Pelicula:
    def __init__(self,ano,genero,actor):
        self.ano=ano
        self.genero=genero
        self.actor=actor
        self.items=[]

pelicula1=Pelicula('1993','drama','felipe')

     def apilar(self):
        self.items.append(pelicula1)
        
print apilar(pelicula1)
