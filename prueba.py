from AnalizadorLexico import *
import AnalizadorSintactico as sintactico
from Programa import *

lexico = AnalizadorLexico()
lexico.construir()

sintactico.construir()

cadena = input('Cadena>> ')
print(lexico.analizarCadena(cadena))
sintactico.analizarCadena(cadena)
print(Programa.programa()._programa)