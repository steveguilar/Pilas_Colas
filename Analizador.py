import ply.lex as lex
import sys



tokens = [ 'VARIABLE','NUMERO','MAS','MENOS','MULTIPLICACION','DIVISION','IGUAL','MAYOR','MENOR','MAYORoIGUAL','MENORoIGUAL','DIFERENTE','AND','OR','WHILE','THEN','IF','FOR'] 

##reserved = {
##   'if' :'IF',
##   'then':'THEN',
##   'else' : 'ELSE',
##   'while' : 'WHILE'
##}

##tokens += reserved.values()
def t_WHILE(t): r'WHILE'; return t
def t_THEN(t): r'THEN'; return t
def t_IF(t): r'IF'; return t
def t_FOR(t): r'FOR'; return t

t_ignore = ' \t,\n'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'=='
t_VARIABLE = r'\[a-zA-Z_]*'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORoIGUAL = r'>='
t_MENORoIGUAL = r'<='
t_DIFERENTE = r'!='
t_AND = r'\^'
t_OR = r'\|'


 
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

##def t_ID(t):
##    r'[a-zA-Z_][a-zA-Z0-9_]*'
##    if t.value in reserved:
##        t.type = reserved[ t.value ]
##    return t

##def t_ID(t):
##    r'\[a-zA-Z_][a-zA-Z_0-9]*'
##    t.type = reserved.get(t.value,'ID')    # Check for reserved words
##    return t

# Error handling rule
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)



lex.lex() # Build the lexer

archivo = open("expresiones.txt", "r")

linea = archivo.readlines()

print (linea)
for x in linea :
    print(x)
    lex.input(x)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)


