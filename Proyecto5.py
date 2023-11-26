import tkinter as tk
from tkinter import filedialog

def q0(codigo, posicion,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			q0(codigo, posicion + 1, valores)
		elif caracter.isdigit():
			q24(codigo, posicion + 1, caracter, valores)
		elif caracter in ['(',')']:
			q22(codigo, posicion + 1, caracter, valores)
		elif caracter in ['{','}']:
			q20(codigo, posicion + 1, caracter, valores)
		elif caracter.isalpha():
			q1(codigo, posicion + 1, caracter, valores)
		elif caracter in ['+', '*', '%']:
			q13(codigo, posicion + 1, caracter, valores)
		elif caracter == '/':
			q13_1(codigo, posicion + 1, caracter, valores)
		elif caracter == '&':
			q11(codigo, posicion + 1, caracter, valores)
		elif caracter == '|':
			q10(codigo, posicion + 1, caracter, valores)
		elif caracter == '!':
			q7(codigo, posicion + 1, caracter, valores)
		elif caracter in ['<','>']:
			q6(codigo, posicion + 1, caracter, valores)
		elif caracter == '=':
			q5(codigo, posicion + 1, caracter, valores)
		elif caracter == '"':
			q26(codigo, posicion + 1, caracter, valores)
		elif caracter == '-':
			q28(codigo, posicion + 1, caracter, valores)
	return valores
	

def q24(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isdigit():
			buffer += caracter
			q24(codigo, posicion + 1,buffer,valores)
		elif caracter == '.':
			buffer += caracter
			q25(codigo, posicion + 1, buffer,valores)
		elif caracter.isspace():
			valores['Número Enteros'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)

	return valores
		


def q25(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isdigit():
			buffer += caracter
			q25(codigo,posicion + 1, buffer, valores)
		elif caracter.isspace():
			valores['Números Decimales'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q22(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Paréntesis'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q20(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Llaves'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)			 
	return valores

def q1(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isalpha() or caracter == '_':
			buffer += caracter
			q1(codigo, posicion + 1, buffer,valores)
		elif caracter.isspace():
			# buffer += caracter
			if buffer in ['if', 'else', 'switch', 'case', 'default', 'for', 'while', 'break', 'int', 'String', 'double', 'char', 'print']:
				q2(codigo, posicion+1,buffer,valores)
			else:
				valores['Identificadores'].append(buffer)
				q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)	
	return valores

def q2(codigo, posicion, buffer,valores):
	valores['Palabras reservadas'].append(buffer)
	q0(codigo, posicion,valores)
	return valores

def q13(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Operadores Aritméticos'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q13_1(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Operadores Aritméticos'].append(buffer)
			q0(codigo, posicion + 1,valores)
		elif caracter == '/':
			buffer += caracter
			q16(codigo, posicion + 1,buffer,valores)
		elif caracter == '*':
			buffer += caracter
			q14(codigo, posicion + 1,buffer,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q16(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Comentario de Línea'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			buffer += caracter
			q16(codigo, posicion + 1, buffer,valores)
	return valores

def q14(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			qerror(codigo, posicion, buffer,valores)
		elif caracter == '*':
			buffer += caracter
			q15(codigo, posicion + 1, buffer,valores)
		else:
			buffer += caracter
			q14(codigo, posicion + 1, buffer,valores)
		return valores

def q15(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			qerror(codigo, posicion, buffer,valores)
		elif caracter == '/':
			buffer += caracter
			q17(codigo, posicion+1, buffer,valores)
		else:
			buffer += caracter
			q14(codigo, posicion+1, buffer,valores)

def q17(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Comentario Multilínea'].append(buffer)
			q0(codigo, posicion,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
		return valores

def q11(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			qerror(codigo, posicion, buffer,valores)
		elif caracter == '&':
			buffer += caracter
			q9(codigo, posicion+1, buffer,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
		return valores

def q11(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			qerror(codigo, posicion, buffer,valores)
		elif caracter == '&':
			buffer += caracter
			q9(codigo, posicion+1, buffer,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
		return valores

def q10(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			qerror(codigo, posicion, buffer,valores)
		elif caracter == '|':
			buffer += caracter
			q9(codigo, posicion+1, buffer,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
		return valores

def	q9(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Operadores Lógicos'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q6(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter == '=':
			buffer += caracter
			q8(codigo, posicion+1, buffer,valores)
		elif caracter.isspace():
			valores['Operadores Relacionales'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q8(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Operadores Relacionales'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q7(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter == '=':
			buffer += caracter
			q8(codigo, posicion+1, buffer,valores)
		elif caracter.isspace():
			valores['Operadores Lógicos'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q5(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Asignaciones'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores

def q26(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			qerror(codigo, posicion, buffer,valores)
		elif caracter == '"':
			buffer += caracter
			q27(codigo, posicion + 1, buffer,valores)
		else:
			buffer += caracter
			q26(codigo, posicion + 1, buffer,valores)
	return valores

def q27(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Cadena de Caracteres'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores



def q28(codigo, posicion, buffer,valores):
	if posicion < len(codigo):
		caracter = codigo[posicion]
		if caracter.isdigit():
			buffer += caracter
			q24(codigo, posicion + 1, buffer,valores)
		elif caracter.isspace():
			valores['Operadores Aritméticos'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			qerror(codigo, posicion, buffer,valores)
	return valores
		


def qerror(codigo, posicion, buffer,valores):
	if posicion < len (codigo):
		caracter = codigo[posicion]
		if caracter.isspace():
			valores['Errores'].append(buffer)
			q0(codigo, posicion + 1,valores)
		else:
			buffer += caracter
			qerror(codigo, posicion + 1, buffer,valores)
	return valores

codigo_ejemplo = '''
/*EsteArchivoEsDeFacil_Lectura_Para_el_Aut%mata*/

if ( numero >= 17.34 ) {
	dato = 25..18
	print ( "Hola_Mundo" )
	}

//Otro_Comentario
	
while ( dato != hola && valor <. 5 ) { x = dato - numero }
'''
valores = {
	'Palabras reservadas': [],
	'Identificadores': [],
	'Operadores Relacionales': [],
	'Operadores Lógicos': [],
	'Operadores Aritméticos': [],
	'Asignaciones': [],
	'Número Enteros': [],
	'Números Decimales': [],
	'Cadena de Caracteres': [],
	'Comentario Multilínea': [],
	'Comentario de Línea': [],
	'Paréntesis': [],
	'Llaves': [],
	'Errores': []
}


def reiniciar_valores():
    global valores
    valores = {
        'Palabras reservadas': [],
        'Identificadores': [],
        'Operadores Relacionales': [],
        'Operadores Lógicos': [],
        'Operadores Aritméticos': [],
        'Asignaciones': [],
        'Número Enteros': [],
        'Números Decimales': [],
        'Cadena de Caracteres': [],
        'Comentario Multilínea': [],
        'Comentario de Línea': [],
        'Paréntesis': [],
        'Llaves': [],
        'Errores': []
    }

def seleccionar_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            contenido = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, contenido)

def procesar_codigo():
	result_text.config(state=tk.NORMAL)
	result_text.delete("1.0", tk.END)

	reiniciar_valores()

	codigo = text_area.get("1.0", tk.END)
	resultados = q0(codigo, 0, valores)
	print(resultados)
	for tipo, valores_tipo in resultados.items():
		result_text.insert(tk.END, f'{tipo} : {len(valores_tipo)}\n')
		result_text.insert(tk.END, f'Valores de {tipo}: {valores[tipo]}\n\n')    
	result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Proyecto de Automatas")

text_area = tk.Text(root, height=20, width=100)
text_area.pack()

select_file_button = tk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo)
select_file_button.pack()

process_button = tk.Button(root, text="Procesar Código", command=procesar_codigo)
process_button.pack()

result_text = tk.Text(root, height=20, width=100)
result_text.pack()


root.mainloop()