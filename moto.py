# -*- coding: utf-8 -*-
from cola import *
class Moto:
    def __init__(self, nombre, codigo, placa):
        self.nombre=nombre
        self.codigo=codigo
        self.placa=placa


cola = Cola()
cola.encolar(Moto("Juan","2012020","ky1c"))
cola.encolar(Moto("Steven","2012021","ol1i"))
cola.encolar(Moto("Rigo","2012022","po2c"))
cola.encolar(Moto("Winner","2012027","qw3r"))
cola.encolar(Moto("Nairo","2012023","ñe4a"))
cola.encolar(Moto("Sebas","2012024","ol9a"))
cola.encolar(Moto("Sergio","2012026","as3s"))
cola.mostrar()
while cola.es_vacia() != True:
    print cola.desencolar().placa

print "No hay más elementos en la Cola" , cola.es_vacia()
