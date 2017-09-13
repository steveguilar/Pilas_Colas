from arbolUno import *
from pila import *

def leerExpresion():
	expresion = raw_input('Ingrese la expresion:')

	listaExpresion = expresion.split(' ')
	return listaCaracteres

def crearArbol(lista, pila):
        if lista != []
                if lista[i] in "+-*/=":
                        der = pila.desapilar()
                        izq = pila.desapilar()
                        pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
                else:
                        pila.apilar(Nodo(lista[i], None, None))
        return pila.desapilar()

def imprimirArbolPostfijo(arbol):
        if arbol != None:
                imprimirArbolPostfijo(arbol.izq)
                imprimirArbolPostfijo(arbol.der)
                print arbol.valor               

while True:
        opcion = raw_input('ingrese expresion postfija, Y para continuar N para detenerse: (Y/N)')
        if opcion == 'Y':
                cadena = leerExpresion()
                pila = Pila()
                nodo = crearArbol(cadena, pila)
                print "Resultado operacion: " , evaluar(nodo)
        if opcion == 'N':
                break
