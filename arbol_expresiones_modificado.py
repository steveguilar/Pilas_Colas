from pila import *
from arbolUno import *


listaResultado = []

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/=":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        elif lista[0].isalpha():            
            pila.apilar(Nodo(lista[0]))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "=":
        arbol.der = evaluar(arbol.izq)
        return arbol.der
    return int(arbol.valor)
    

while True:
        opcion = raw_input('Desea ingresar una expresion matematica en posfijo: (Y/EA/N)')
        if opcion == 'Y':
                exp = raw_input("ingrese la expresion en posfija: ").split(" ")
                pila = Pila()
                nodo = convertir(exp, pila)
                listaResultado.append(evaluar(pila.desapilar()))
                
        if opcion == 'EA':
                exp = raw_input("ingrese la expresion en posfija: ").split(" ")
                listaResultado.append(exp)
                pila1 = Pila()
                nodo = convertir(listaResultado, pila1)
                print "el resultado es  ", evaluar(pila1.desapilar())
                
                
        if opcion == 'N':
                for element in listaResultado:
                    print "los resultados son " + element
                break

