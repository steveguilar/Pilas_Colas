import ply.lex as lex
import os

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

def entradaArchivo(ubicacionFichero):
    e = ''
    with open(ubicacionFichero) as file:
        for linea in file:
            e = e + linea
            print e
            return e
	    
entrada = entradaArchivo("C:\Users\HOME\Desktop\holi.txt")

lex.input(entrada)
while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)
