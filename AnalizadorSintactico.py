# -*- coding: utf-8 -*-
#@author: Lalo Valle

# Importacion del módulo de la implementación de yacc en python
import ply.yacc as yacc

from Programa import *
import Recursos as recursos

# Lista de nombres de los tokens
# Necesario para la generacion del parser
tokens = recursos.tokens
parser = None


programa = Programa.programa()

precedence = (
	('left', '+', '-'),
	('left', '*', '/'),
	('left', 'MENOSUNARIO'),
	('right', '^')
)

def p_lista(p):
	'''
	lista 	: vacio
			| lista SALTOLINEA
			| lista expresion termino
	'''
	try:
		p[0] = p[(1 if len(p) == 3 else 2)]
		if len(p) == 4:
			programa.agregarInstrucciones('print','STOP')
	except: pass

def p_lista_error(p):
	''' lista : lista error termino '''
	recursos.imprimirError('ErrorSintaxis','Error de sintaxis en la regla lista. Expresión erronea')
	# Se agotan los token
	while True:
		if not parser.token(): break


def p_asignacion(p):
	''' asignacion 	: VARIABLE '=' expresion
					| INDEFINIDA '=' expresion
	'''
	p[0] = p[3]
	programa.agregarInstrucciones('varpush',p[1],'asignacion')
	pass


def p_expresion_reducciones(p):
	'''
	expresion 	: NUMERO
				| CONSTANTE
	'''
	p[0] = p[1]
	programa.agregarInstrucciones('constpush',p[1])

def p_expresion_variable(p):
	'''	expresion 	: VARIABLE 
					| INDEFINIDA
	'''
	p[0] = p[1]
	programa.agregarInstrucciones('varpush',p[1])

def p_expresion_asignacion(p):
	''' expresion : asignacion '''
	p[0] = p[1]

def p_expresion_operaciones(p):
	''' 
	expresion 	: FUNCION '(' expresion ')'
				| expresion '+' expresion
				| expresion '-' expresion
				| expresion '*' expresion
				| expresion '/' expresion
				| expresion '^' expresion
	'''
	if len(p) == 4: # Operaciones binarias
		operador = p[2]
		if operador == '+': programa.agregarInstrucciones('suma')
		elif operador == '-': programa.agregarInstrucciones('resta')
		elif operador == '*': programa.agregarInstrucciones('multiplicacion')
		elif operador == '/': programa.agregarInstrucciones('division')
		else: programa.agregarInstrucciones('potencia')
	else:  # Funciones
		programa.agregarInstrucciones('funcion',p[1])

def p_expresion_modificaciones(p):
	''' 
	expresion 	: '(' expresion ')'
				| '-' expresion %prec MENOSUNARIO
	'''
	if p[1] == '(': p[0] = p[2]
	else: programa.agregarInstrucciones('negacion')

def p_vacio(p):
	''' vacio : '''
	pass

def p_termino(p):
	'''termino  : vacio
				| ';' '''
	pass

def p_error(p):
	if p:
		recursos.imprimirError('ErrorSintaxis','Error en el token {}'.format(p.type))
		# Descarta el token y prosigue con el proceso
		parser.errok()
	else:
		recursos.imprimirError('Error','Fin del entrada')


"""
	Funciones
	>>>>>>>>>
"""

def construir():
	global parser
	parser = yacc.yacc()

def analizarCadena(cadena):
	global parser
	resultado = parser.parse(cadena)
	resultado = 'Análisis valido'
	return resultado