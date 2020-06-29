# -*- coding: utf-8 -*-
#@author: Lalo Valle

# Importacion del módulo de la implementación de lex en python
import ply.lex as lex
import Recursos as recursos

resultado_lexema = []

tokens = recursos.tokens  # Lista de nombres de los tokens

literals = ['+','-',
	'*','/',
	'^','=',
	';','(',
	'{',')','}'
]

""" 
	EXPRESIONES REGULARES DE LOS TOKENS 
	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
t_ignore = ' \t' # Ignora espacios y tabuladores
	
def t_SALTOLINEA(t):
	r'\n'
	return t

def t_NUMERO(t):
	r'\d+(\.\d+)?'
	if t.value.find('.') == -1 : t.value = int(t.value)
	else: t.value = float(t.value)
	return t

def t_VARIABLE(t):
	r'[_a-zA-Z_][\w]*'
	if t.value in recursos.funciones: # Identificación de funciones
		t.type = 'FUNCION'
		t.value = recursos.funciones[t.value]
	elif t.value in recursos.constantes: # Identificación de constantes
		t.type = 'CONSTANTE'
		t.value = recursos.constantes[t.value]
	else: # Identificación de variables(definidas e indefinidas)
		if t.value in recursos.variables: t.type = 'VARIABLE'
		else: t.type = 'INDEFINIDA'
	return t


# Dado que las constantes tiene caracteres como letras griegas no basta con identificacion de alfanuméricos
def t_CONSTANTE(t):
	r'[πΓφ]'
	t.type = 'CONSTANTE'
	t.value = recursos.constantes[t.value]
	if recursos._lex:
		recursos.agregarTokenTabla(t)
	return t

def t_error( t):
	global resultado_lexema
	estado = "** Token no valido en la Linea {:4}\n Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
	resultado_lexema.append(estado)
	t.lexer.skip(1)

	"""	
		MÉTODOS
		>>>>>>>
	"""

def prueba(data):
	global resultado_lexema
	analizador = lex.lex()
	analizador.input(data)

	resultado_lexema.clear()
	while True:
		tok = analizador.token()
		if not tok:
			break
		# print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
		estado = "\nTipo " + str(tok.type) + " Lexema " + str(tok.value) + " Posicion " + str(tok.lexpos)
		resultado_lexema.append(estado)
	return resultado_lexema
   