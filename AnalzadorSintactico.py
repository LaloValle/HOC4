# -*- coding: utf-8 -*-
#@author: Lalo Valle

# Importacion del módulo de la implementación de yacc en python
import ply.yacc as yacc
import Recursos as recursos

# Lista de nombres de los tokens
# Necesario para la generacion del parser
tokens = recursos.tokens
parser = None

"""
	Reglas gramaticales
	>>>>>>>>>>>>>>>>>>>
"""

precedence = (
	('left', 'MAS', 'MENOS'),
	('left', 'MULTIPLICACION', 'DIVISION'),
	('left', 'MENOSUNARIO'),
	('right', 'POTENCIA')
)

def p_lista(p):
	'''
	lista 	: vacio
			| lista SALTOLINEA
			| lista asignacion ;
			| lista expresion ;
	'''
	try:
		p[0] = p[(1 if len(p) == 3 else 2)]
		if len(p) == 4:
			print('\x1b[0;m'+'HOC3 >> ',p[2])
	except: pass

def p_lista_error(p):
	''' lista : lista error termino '''
	recursos.mostrarError('ErrorSintaxis','Error de sintaxis en la regla lista. Expresión erronea')
	# Se agotan los token
	while True:
		if not parser.token(): break

def p_asignacion(p):
	''' asignacion : VARIABLE IGUAL expresion'''
	p[0] = variables[p[1]] = p[3]

def p_expresion_reducciones(p):
	'''
	expresion 	: NUMERO
				| CONSTANTE
				| asignacion
	'''
	p[0] = p[1]

def p_expresion_variable(p):
	''' expresion : VARIABLE '''
	if p[1] not in variables:
		recursos.mostrarError('ErrorVariable','Error en utilización de variable no definida \'{}\''.format(p[1]))
		raise SyntaxError
	else: p[0] = variables[p[1]]

def p_expresion_operaciones(p):
	''' 
	expresion 	: FUNCION AGRUPADORIZQ expresion AGRUPADORDER
				| expresion + expresion
				| expresion - expresion
				| expresion * expresion
				| expresion / expresion
				| expresion ^ expresion %prec POTENCIA
	'''
	if len(p) == 4:
		# Operaciones binarias
		operador = p[2]
		if   operador == '+': p[0] = p[1] + p[3]
		elif operador == '-': p[0] = p[1] - p[3]
		elif operador == '*': p[0] = p[1] * p[3]
		elif operador == '/': 
			if p[3] == 0:
				recursos.mostrarError('DivisorZero','Se trata de dividir entre 0')
				raise SyntaxError
			else: p[0] = p[1] / p[3]
		else: p[0] = p[1] ** p[3]

	else:
		# Funciones
		p[0] = p[1](p[3])

def p_expresion_asignaciones(p):
	''' 
	expresion 	: AGRUPADORIZQ expresion AGRUPADORDER
				| MENOS expresion %prec MENOSUNARIO
	'''
	p[0] = p[2] * (-1 if p[1] == '-' else 1)


def p_vacio(p):
	''' vacio : '''
	pass

def p_termino(p):
	'''termino  : vacio
				| ;'''
	pass

def p_error(p):
	if p:
		recursos.mostrarError('ErrorSintaxis','Error en el token'.format(p.type))
		# Descarta el token y prosigue con el proceso
		parser.errok()
	else:
		recursos.mostrarError('Error','Fin del entrada')

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
	return resultado