import ply.lex as lex
import sys

tokens = [ 'VARIABLE','NUMERO','MAS','MENOS','MULTIPLICACION','DIVISION', 'IGUAL' ]

t_ignore = ' \t,\n'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
archivo = open("expresiones.txt", "r")
linea = archivo.readlines()
print linea
for x in linea :
    print(x)
    lex.input(x)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)


