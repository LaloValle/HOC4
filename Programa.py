# -*- coding: utf-8 -*-
#@author: Lalo Valle

import Recursos as recursos

class Interprete:

	def __init__(self):
		self._indicePila = 0  # Indice de la siguiente casilla disponible
		self._pila = []  # Pila utilizada en la ejecución del intérprete

	def push(self,dato):
		if type(dato) != Dato:
			recursos.imprimirError('ErrorDato','Solo pueden ser ingresados elementos instancia de la clase Dato a la pila del interprete')
		else: self._pila.append(dato)

	def pop(self):
		return self._pila.pop()



class Dato():

	tipoDato = [
		'constante',
		'variable',
		'funcion',
		'indefinida'
	]

	def __init__(self,valor,tipo,nombre=''):
		self.nombre = nombre  # Utilizado en el nombre de las variables o indefinidas
		self.valor = valor  # Campo que puede tomar un valor numérico, cadena, o función
		self.tipo = tipo if tipo in Dato.tipoDato else None



class Programa():

	def __init__(self):  # Constructor privado
		self.reiniciarPrograma()

		self._interprete = Interprete()


	def agregarInstrucciones(self,*instrucciones):  # Agrega un número indefinido de instrucciones al programa
		auxIndicePrograma = int(self._indicePrograma)

		for instruccion in instrucciones:
			if instruccion in recursos.tipoInstruccion: instruccion = recursos.tipoInstruccion[instruccion]
			self._programa.append(instruccion)
			self._indicePrograma += 1

		return auxIndicePrograma

	def ejecutar(self):
		if self._programa:
			while self._programa[self._contadorPrograma]:
				print('Contador: ', self._contadorPrograma)
				self._contadorPrograma += 1
				print('Instruccion: ',self._programa[self._contadorPrograma - 1])
				self._programa[self._contadorPrograma - 1]()

				print('Pila: ',self._interprete._pila)


	def reiniciarPrograma(self):
		self._indicePrograma = 0  # Indice de la siguiente casilla disponible
		self._contadorPrograma = 0  # Indice actual de las instrucciones durante la interpretación

		self._programa = []  # Lista de instrucciones


	instancia = None

	def programa():  # Método estático para el manejo de una única instancia de la clase Programa
		if not Programa.instancia:
			Programa.instancia = Programa()
		return Programa.instancia



	""" Instrucciones representadas por funciones """

	def constpush(self):  # Introduce una constante en la pila del interprete
		constante = Dato(self._programa[self._contadorPrograma],'constante')
		self._interprete.push(constante)
		self._contadorPrograma += 1
	
	def varpush(self):  # Introduce el nombre de una variable en la pila del interprete
		variable = Dato(recursos.variables[self._programa[self._contadorPrograma]],'variable',self._programa[self._contadorPrograma])
		self._interprete.push(variable)
		self._contadorPrograma += 1

	def evaluacion(self):  # Evaluación de una variable en la pila del interprete
		variable = self._interprete.pop()
		if variable.tipo == 'indefinida': recursos.imprimirError('ErrorVariable','No se puede realizar la evaluacion de una variable indefinida')
		variable.valor = recursos.variables[variable.nombre]
		self._interprete.push(variable)

	def suma(self):
		n2 = self._interprete.pop()
		n1 = self._interprete.pop()
		res = Dato(n1.valor + n2.valor,'constante')
		self._interprete.push(res)

	def resta(self):
		n2 = self._interprete.pop()
		n1 = self._interprete.pop()
		res = Dato(n1.valor - n2.valor,'constante')
		self._interprete.push(res)

	def multiplicacion(self):
		n2 = self._interprete.pop()
		n1 = self._interprete.pop()
		res = Dato(n1.valor * n2.valor,'constante')
		self._interprete.push(res)

	def division(self):
		n2 = self._interprete.pop()
		n1 = self._interprete.pop()
		if n2.valor == 0: 
			recursos.imprimirError('DivisorCero','No se puede realizar la división entre 0')
		else:
			res = Dato(n1.valor / n2.valor,'constante')
		self._interprete.push(res)

	def potencia(self):
		n2 = self._interprete.pop()
		n1 = self._interprete.pop()
		res = Dato(n1.valor ** n2.valor,'constante')
		self._interprete.push(res)

	def negacion(self):
		n = self._interprete.pop()
		n.valor *= -1
		self._interprete.push(n)

	def asignacion(self):
		variable = self._interprete.pop()
		expresion = self._interprete.pop()

		if variable.tipo != 'variable' and variable.tipo != 'indefinida': recursos.imprimirError('ErrorVariable','No se puede realizar la asignación a un no variable')

		recursos.variables[variable.nombre] = expresion.valor
		variable.valor = expresion.valor
		variable.tipo = 'variable'
		self._interprete.push(expresion)

	def funcion(self):
		parametro = self._interprete.pop()
		parametro.valor = self._programa[self._contadorPrograma](parametro.valor)
		self._interprete.push(parametro)
		self._contadorPrograma += 1

	def print(self):
		dato = self._interprete.pop()
		cadena = dato.valor
		recursos.imprimirResultado(cadena)