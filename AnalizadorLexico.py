# -*- coding: utf-8 -*-
#@author: Lalo Valle

# Importacion del módulo de la implementación de lex en python
import ply.lex as lex
import Recursos as recursos

class AnalizadorLexico(object):

	tokens = recursos.tokens  # Lista de nombres de los tokens

	literals = [
		'+', '-',
		'*','/',
		'^'
		'=',
		';',
		'(','{',
		')','}'
	]

	""" 
		EXPRESIONES REGULARES DE LOS TOKENS 
		>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	"""

	t_ignore = ' \t' # Ignora espacios y tabuladores
	
	def t_SALTOLINEA(self,t):
		r'\n'
		self.lineas += 1
		return t

	def t_NUMERO(self,t):
		r'\d+(\.\d+)?'
		if t.value.find('.') == -1 : t.value = int(t.value)
		else: t.value = float(t.value)
		return t

	def t_VARIABLE(self,t):
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
	def t_CONSTANTE(self,t):
		r'[πΓφ]'
		t.type = 'CONSTANTE'
		t.value = recursos.constantes[t.value]
		if recursos._lex:
			recursos.agregarTokenTabla(t)
		return t

	def t_error(self,t):
		recursos.mostrarError('ErrorLexico','No se ha reconocido el caracter {} en la línea {}, posición {}'.format(t.value[0],t.lineno,t.lexpos))
		t.lexer.skip(1) 	# Salta la ejecución al lexema siguiente



	"""	
		MÉTODOS
		>>>>>>>
	"""
	def __init__(self):
		self.lexico = None
		self.lineas = 1

	def construir(self, **kwargs):
		self.lexico = lex.lex(object=self,**kwargs)

	def analizarCadena(self,cadena):
		self.lexico.input(cadena)
		recursos.mostrarTokens(self.lexico)

	def asignarLineas(self,t):
		t.lineno = self.lineas

	def reiniciarLineas(self):
		self.lineas = 1