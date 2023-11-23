# def q22(codigo, posicion, buffer,valores):
# 	if posicion < len(codigo):
# 		caracter = codigo[posicion]
# 		if caracter.isspace():
# 			valores['Números Decimales'].append(buffer)
# 			q0(codigo, posicion + 1,valores)

#		 else:
#		 	qerror(codigo, posicion, buffer,valores)
			
# 	return valores



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
		elif caracter in ['+', '-', '*', '%','/']:
			q13(codigo, posicion + 1, caracter, valores)
		elif caracter == '&':
			q11(codigo, posicion + 1, caracter, valores)
		elif caracter == '|':
			q10(codigo, posicion + 1, caracter, valores)
		elif caracter == '!':
			q6(codigo, posicion + 1, caracter, valores)
		elif caracter in ['<','>']:
			q7(codigo, posicion + 1, caracter, valores)
		elif caracter == '=':
			q5(codigo, posicion + 1, caracter, valores)
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
			valores['Operadores Lógicos'].append(buffer)
			q0(codigo, posicion + 1,valores)
		elif caracter == '/':
			buffer += caracter
			q16(codigo, posicion + 1,buffer,valores)
		elif caracter == '*':
			buffer += caracter
			q17(codigo, posicion + 1,buffer,valores)
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
29.5 29 25555 2
/a * - * 
2.48
print a i switch
//hola_como_estas int
{ } { { case } } /*
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


resultados = q0(codigo_ejemplo,0,valores)

for tipo, cantidad in resultados.items():
    print(f'{tipo} : {cantidad}')
