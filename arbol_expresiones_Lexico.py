from pila import *
from arbolUno import *
import re

listaResultado = []
tipo=[]
valor=[]
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
    
def evaluarCaracteres(aux, tipo , valor):
    errores =0
    for x in aux:
        if re.match('^[-+]?[0-9]+$', x):
            tipo.append("Numero")
            valor.append(x)
            #print ("Numero")
        elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', x):
            tipo.append("Variable")
            valor.append(x)
            #print ("Letra")
        elif re.match('[-|=|+|*|/]', x):
            tipo.append("Operador")
            valor.append(x)
            #print ("Operaciones")
        else:
            tipo.append("Elemento no Permitido")
            valor.append(x)
            errores+=1
            #print ("Operaciones")
    return errores
    
def sacarTabla(tipo , valor):
        a = 0
        for m in tipo:
            print(tipo[a] + "   " + valor[a])
            a = a+1

while True:
        opcion = raw_input('Desea ingresar una expresion matematica en posfijo: (Y/EA/N)')
        if opcion == 'Y':
            exp = raw_input("ingrese la expresion en posfija: ").split(" ")
            evaluarCaracteres(exp,tipo,valor)
            sacarTabla(tipo, valor)
            pila = Pila()
            nodo = convertir(exp, pila)
            listaResultado.append(evaluar(pila.desapilar()))
                
        if opcion == 'EA':
            exp = raw_input("ingrese la expresion en posfija: ").split(" ")
            listaResultado.append(exp)
            evaluarCaracteres(exp,tipo,valor)
            sacarTabla(tipo, valor)
            pila1 = Pila()
            nodo = convertir(listaResultado, pila1)
            print "el resultado es  ", evaluar(pila1.desapilar())
                
                
        if opcion == 'N':
                for element in listaResultado:
                    print "los resultados son " + element
                break
