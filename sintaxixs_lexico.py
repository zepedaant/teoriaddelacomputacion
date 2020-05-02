import ply.lex as lex

tokens = (
    "numero"
    "suma"
    )
t_numero = r'([0-9]+)'
t_suma = r'(\+)'

def  t_error(t):
    print "Error: simbolo ilegal'%s' en linea '%s'"
    t.lexer.skip(1)

lexer = lex.lex()

def prueba (entrada):
    lexer.input(entrada)
    while true:
        token = lexer.token()
        if not token:
            break
        print token

while true:
    entrada = raw.input('entrada:')
    prueba(entrada)
