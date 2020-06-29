# -*- coding: utf-8 -*-
#@author: Lalo Valle

import Recursos as recursos

class Instruccion():

class Programa():

	def __init__(self,interprete):
		self._indicePrograma = 0  # Indice de la siguiente casilla disponible
		self._contadorPrograma = 0  # Indice actual de las instrucciones durante la interpretación

		self._programa = []  # Lista de instrucciones

		self._interprete = Interprete()

	def agregarInstruccion(self,*instrucciones):  # Agrega un número indefinido de instrucciones al programa
		auxIndicePrograma = int(self._indicePrograma)

		for instruccion in instrucciones:
			if type(instruccion) == Instruccion:
				self._programa.append(instruccion)
				self._indicePrograma += 1
			else: recursos.imprimirError('InstrucciónInvalida','El elemento instrucción para ser ingresado a la lista del programa debe ser de la clase \'Instruccion\'')

		return auxIndicePrograma

	def constpush(self):



	"""
		CLASE INTERPRETE
		>>>>>>>>>>>>>>>>
	"""
	
	class Interprete:

		def __init__(self):
			self._indicePila = 0  # Indice de la siguiente casilla disponible

			self._pila = []  # Pila utilizada en la ejecución del intérprete