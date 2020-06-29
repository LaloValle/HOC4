import PySimpleGUI as sg

from AnalizadorLexico import *
import AnalizadorSintactico as sintactico
import Recursos as recursos

sg.theme('GreenTan')  # No gray windows please!
btnLexico = 'Analizar léxicamente'
btnSintactico = 'Analizar sintácticamente'
txtInput= 'Caja de texto entrada'
txtLex = 'Caja de texto Lex'
txtSin = 'Caja de texto Sintac'

""" Analizador léxico y sintáctico """
lexico = AnalizadorLexico()
lexico.construir()
sintactico.construir()

# STEP 1 define the layout
layout = [
		[sg.Text('Cadena a analizar léxicamente')],
		[
		sg.Multiline(key=txtInput, default_text='', size=(50, 10), pad=(0,0)),#entrada
		],
		[
		sg.Multiline(key=txtLex, default_text='', size=(50, 20)),#análisis lex
        sg.Multiline(key=txtSin, default_text='', size=(20, 20)) #análisis sin
        ],
		[sg.Button(btnLexico), sg.Button(btnSintactico, pad=( (100,0), (0,0) )   )]
        ]

#STEP 2 - create the window
window = sg.Window('My new window', layout, grab_anywhere=True)

# STEP3 - the event loop
while True:
	event, values = window.read()   # Read the event that happened and the values dictionary
	if event == sg.WIN_CLOSED:     # If user closed window with X or if user clicked "Exit" button then exit
		break
	if event == btnLexico:
		window[txtLex]('')
		tokens = lexico.analizarCadena(window[txtInput].get())
		for token in tokens:
			window[txtLex].Update(value=token, append=True)

	elif event == btnSintactico:
		window[txtSin]('')
		try:
			s = window[txtInput].get()
		except EOFError:
			continue
		if not s:
			continue
		else:
			resultado = sintactico.analizarCadena(s)
			resultado = resultado + '\n'
			window[txtSin].Update(value=resultado, append=True)
			
window.close()