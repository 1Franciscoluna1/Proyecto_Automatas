def es_alfanumerico(caracter):
    return caracter.isalpha() or caracter.isdigit() or caracter in ['_']

# Función para identificar tokens
def identificar_tokens(codigo):
    tokens = []
    palabra_actual = ""
    dentro_comentario_linea = False
    dentro_comentario_multilinea = False

    i = 0
    while i < len(codigo):
        caracter = codigo[i]

        # Comentario de línea
        if caracter == '/' and i + 1 < len(codigo) and codigo[i + 1] == '/':
            dentro_comentario_linea = True
            palabra_actual += codigo[i]
            i += 1
            palabra_actual += codigo[i]

        # Comentario multilinea
        elif caracter == '/' and i + 1 < len(codigo) and codigo[i + 1] == '*':
            dentro_comentario_multilinea = True
            palabra_actual += codigo[i]
            i += 1
            palabra_actual += codigo[i]

        elif caracter == '*' and i + 1 < len(codigo) and codigo[i + 1] == '/':
            palabra_actual += codigo[i]
            i += 1
            palabra_actual += codigo[i]
            tokens.append(palabra_actual)
            palabra_actual = ""
            dentro_comentario_multilinea = False

        # Ignorar caracteres dentro de comentarios
        elif dentro_comentario_linea or dentro_comentario_multilinea:
            if codigo[i] != '\n':
                palabra_actual += codigo[i]
            if caracter == '\n' and dentro_comentario_linea:
                # palabra_actual += codigo[i]
                tokens.append(palabra_actual)
                palabra_actual = ""
                dentro_comentario_linea = False

        # Identificar tokens
        elif caracter.isspace():
            if palabra_actual:
                tokens.append(palabra_actual)
                palabra_actual = ""
        elif caracter in ['(', ')', '{', '}']:
            tokens.append(caracter)
        elif caracter in ['+', '-', '*', '/', '%', '=']:
            tokens.append(caracter)
        elif caracter in ['!', '<', '>']:
            palabra_actual += caracter
            i += 1
            if not codigo[i].isspace():
                palabra_actual += codigo[i]
            tokens.append(palabra_actual)
            palabra_actual = ""
            # i += 1
        elif caracter in ['&', '|']:
            if i + 1 < len(codigo) and codigo[i + 1] == caracter:
                tokens.append(caracter + caracter)
                i += 1
            else:
                tokens.append(caracter)
        elif caracter == '"':
            inicio_cadena = i
            i += 1
            while i < len(codigo) and codigo[i] != '"':
                i += 1
            if i < len(codigo) and codigo[i] == '"':
                tokens.append(codigo[inicio_cadena:i + 1])
        else:
            if es_alfanumerico(caracter):
                palabra_actual += caracter
                i += 1
                while i < len(codigo) and (es_alfanumerico(codigo[i]) or codigo[i]=='.'):
                    palabra_actual += codigo[i]
                    i += 1
                tokens.append(palabra_actual)
                palabra_actual = ""
            else:
                i += 1

        i += 1

    return tokens

def contar_tokens(tokens):
    conteo = {
        'Palabras reservadas': 0,
        'Identificadores': 0,
        'Operadores Relacionales': 0,
        'Operadores Lógicos': 0,
        'Operadores Aritméticos': 0,
        'Asignaciones': 0,
        'Número Enteros': 0,
        'Números Decimales': 0,
        'Cadena de Caracteres': 0,
        'Comentario Multilínea': 0,
        'Comentario de Línea': 0,
        'Paréntesis': 0,
        'Llaves': 0,
        'Errores': 0
    }
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
    

    for token in tokens:
        if token in ['if', 'else', 'switch', 'case', 'default', 'for', 'while', 'break', 'int', 'String', 'double', 'char', 'print']:
            conteo['Palabras reservadas'] += 1
            valores['Palabras reservadas'].append(token)
        elif token[0].isalpha() and all(c.isalnum() or c == '_' for c in token):
            conteo['Identificadores'] += 1
            valores['Identificadores'].append(token)
        elif token in ['<', '<=', '>', '>=', '==', '!=']:
            conteo['Operadores Relacionales'] += 1
            valores['Operadores Relacionales'].append(token)
        elif token in ['&&', '||', '!']:
            conteo['Operadores Lógicos'] += 1
            valores['Operadores Lógicos'].append(token)
        elif token in ['+', '-', '*', '/', '%']:
            conteo['Operadores Aritméticos'] += 1
            valores['Operadores Aritméticos'].append(token)
        elif token == '=':
            conteo['Asignaciones'] += 1
            valores['Asignaciones'].append(token)
        elif token.isdigit():
            conteo['Número Enteros'] += 1
            valores['Número Enteros'].append(token)
        elif '.' in token and all(part.isdigit() for part in token.split('.')):
            conteo['Números Decimales'] += 1
            valores['Números Decimales'].append(token)
        elif token.startswith('"') and token.endswith('"'):
            conteo['Cadena de Caracteres'] += 1
            valores['Cadena de Caracteres'].append(token)
        elif token.startswith('/*') and token.endswith('*/'):
            conteo['Comentario Multilínea'] += 1
            valores['Comentario Multilínea'].append(token)
        elif token.startswith('//'):
            conteo['Comentario de Línea'] += 1
            valores['Comentario de Línea'].append(token)
        elif token in ['(', ')']:
            conteo['Paréntesis'] += 1
            valores['Paréntesis'].append(token)
        elif token in ['{', '}']:
            conteo['Llaves'] += 1
            valores['Llaves'].append(token)
        else:
            conteo['Errores'] += 1
            valores['Errores'].append(token)

    return conteo, valores

codigo_ejemplo = '''
int dat.o
double numer__o
String texto = "HolaMundo"

switch ( numero ) {
	case 5 
		if ( 3.5 >= 8 && dato < 16 ) {
		/*Esto_deberia_funcionar()*/
		/*Para_el_automata{}*/
		valor = 18 * 5
		}
	case 3
		for ( i = 0 i < 7 || j > 18 ) {
		i = i - -3.16
		}
default
	while ( num < 3 )
		break

/*Se termino

}
'''

tokens_identificados = identificar_tokens(codigo_ejemplo)
# print(tokens_identificados)
resultados, valores = contar_tokens(tokens_identificados)

for tipo, cantidad in resultados.items():
    print(f'{tipo} : {cantidad}')
    print(f'Valores de {tipo}: {valores[tipo]}')