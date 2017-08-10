# -*- coding: utf-8 -*-
from cola import *
class Moto:
    def __init__(self, nombre, codigo, placa):
        self.nombre=nombre
        self.codigo=codigo
        self.placa=placa

def main():
    cola = Cola()
    moto0 = Moto("Juan","2012020","ky1c")
    moto1 = Moto("Steven","2012021","ol1i")
    moto2 = Moto("Rigo","2012022","po2c")
    moto3 = Moto("Nairo","2012023","ñe4a")
    moto4 = Moto("Sebas","2012024","ol9a")
    moto5 = Moto("Alejo","2012025","ue1o")
    moto6 = Moto("Sergio","2012026","as3s")
    moto7 = Moto("Winner","2012027","qw3r")
    moto8 = Moto("Eminem","2012028","ci3n")

    cola.encolar(moto1)
    cola.encolar(moto0)
    cola.encolar(moto2)
    cola.encolar(moto3)
    cola.encolar(moto4)
    cola.encolar(moto5)
    cola.encolar(moto6)

    cola.mostrar()
    while cola.es_vacia() == True:
        moto = cola.desencolar()
        print "Nombre: " + moto.nombre +"  Codigo: "+moto.codigo+"  Placas: "+moto.placa


if __name__ == "__main__":
    main()
