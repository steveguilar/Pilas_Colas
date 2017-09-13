

class Nodo():
    
    def __init__(self,val,i = None,d = None):
        self.valor = val
        self.izq = i
        self.der = d

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == '=':
        valor = evaluar(arbol.izq)
        Tabla.variables[arbol.der.valor] = valor
            return valor
        if Tabla.variables.has(arbol.valor) == True:
		return Tabla.variables[arbol.valor]
	elif Tabla.variables in (arbol.valor) == False:
		return int(arbol.valor)
