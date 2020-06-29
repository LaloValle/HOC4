# -*- coding: utf-8 -*-
#@author: Lalo Valle

import math

""" Lista de nombre de los tokens """
tokens = [
	'MAS',
	'MENOS',
	'MULTIPLICACION',
	'DIVISION',
	'IGUAL',
	'NUMERO',
	'POTENCIA',
	'PARENTESISIZQ',
	'LLAVEIZQ',
	'PARENTESISDER',
	'LLAVEDER',
	'SALTOLINEA',
	'INDEFINIDA',
	'VARIABLE',
	'FUNCION',
	'CONSTANTE',
]



"""
	RECURSOS MATEMÁTICOS
	>>>>>>>>>>>>>>>>>>>>
"""
"""
	Funciones con validación de dominio
"""
def Log(x):
	try: return math.log(x)
	except Error: 
		mostrarError('ErrorLog :',Error)
		raise SyntaxError
	return None

def Log10(x):
	try: return math.log10(x)
	except Error: 
		mostrarError('ErrorLog10 :',Error)
		raise SyntaxError
	return None

def Exp(x):
	try: return math.exp(x)
	except Error: 
		mostrarError('ErrorExp :',Error)
		raise SyntaxError
	return None

def Sqrt(x):
	try: return math.sqrt(x)
	except Error: 
		mostrarError('ErrorSqrt',Error)
		raise SyntaxError
	return None

""" Diccionario de constantes matemáticas y su valor """
constantes = {
	'π':math.pi, 'PI':math.pi,
	'e':math.e, 'E':math.e,
	'Γ':0.57721566490153286060 , 'GAMMA':0.57721566490153286060,
	'DEG':57.29577951308232087680,
	'φ':1.6180339887498948482, 'PHI':1.6180339887498948482
}

""" Diccionario de funciones matemáticas y la referencia a la función """
funciones = {
	'sin':math.sin, 'cos':math.cos, 'tan':math.tan,
	'log':Log, 'log10':Log10,
	'exp':Exp,
	'sqrt':Sqrt,
	'abs':math.fabs,
	'int':int
}

variables = {}  # Diccionario que almacena el nombre(key) y valor(value) de las variables



"""
	MENSAJES CONSOLA
	>>>>>>>>>>>>>>>>
"""

def imprimirError(tipo,mensaje):
	print('\x1b[0;m'+'\x1b[3;31m'+'{} : {}'.format(tipo,mensaje)+'\x1b[0;m')

def imprimirNotificacion(mensaje):
	print('\x1b[1;33m'+'\n--- %s ---\n',mensaje)

def imprimirResultado(resultado):
	print('\x1b[0;m'+'HOC3 >> %s'+'\x1b[0;m',resultado)



"""
	REGLAS GRAMATICALES
	>>>>>>>>>>>>>>>>>>>

	lista 		: vacio
				| lista SALTOLINEA
				| lista asignacion termino
				| lista expresion termino
				| lista error termino

	asignacion 	: VARIABLE = expresion

	expresion 	: NUMERO
				| VARIABLE
				| CONSTANTE
				| asignacion
				| FUNCION AGRUPADORIZQ expresion AGRUPADORDER
				| expresion + expresion
				| expresion - expresion
				| expresion * expresion
				| expresion / expresion
				| expresion POTENCIA expresion %prec POTENCIA
				| AGRUPADORIZQ expresion AGRUPADORDER
				| - expresion %prec MENOSUNARIO

	vacio 		:

	termino 	: vacio
				| SALTOLINEA

"""