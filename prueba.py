from AnalizadorLexico import *
import AnalizadorSintactico as sintactico
from Programa import *

lexico = AnalizadorLexico()
lexico.construir()

sintactico.construir()

while True:

	cadena = input('Cadena>> ')
	if cadena == 'exit': break
	print('\n>>>>>>>>>>>>>>>>>>>>\n')
	sintactico.analizarCadena(cadena)
	print(Programa.programa()._programa)
	#print('Inicia la interpretacion:\n')

	Programa.programa().ejecutar()

	Programa.programa().reiniciarPrograma()