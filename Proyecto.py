# Función para verificar si es un caracter alfanumérico
def es_alfanumerico(caracter):
    return caracter.isalpha() or caracter.isdigit() or caracter == '_'

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
            i += 1

        # Comentario multilinea
        elif caracter == '/' and i + 1 < len(codigo) and codigo[i + 1] == '*':
            dentro_comentario_multilinea = True
            i += 1

        elif caracter == '*' and i + 1 < len(codigo) and codigo[i + 1] == '/':
            dentro_comentario_multilinea = False
            i += 1

        # Ignorar caracteres dentro de comentarios
        elif dentro_comentario_linea or dentro_comentario_multilinea:
            if caracter == '\n' and dentro_comentario_linea:
                dentro_comentario_linea = False

        # Identificar tokens
        elif caracter.isspace():
            if palabra_actual:
                tokens.append(palabra_actual)
                palabra_actual = ""
        elif caracter in ['(', ')', '{', '}']:
            tokens.append(caracter)
        elif caracter in ['+', '-', '*', '/', '%', '=', '!', '<', '>']:
            tokens.append(caracter)
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
                while i < len(codigo) and es_alfanumerico(codigo[i]):
                    palabra_actual += codigo[i]
                    i += 1
                tokens.append(palabra_actual)
                palabra_actual = ""
            else:
                i += 1

        i += 1

    return tokens

# Ejemplo de código
codigo_ejemplo = '''
/*EsteArchivoEsDeFacil_Lectura_Para_el_Aut%mata*/

if ( numero >= 17.34 ) {
	dato = 25..18
	print ( "Hola_Mundo" )
	}

//Otro_Comentario
	
while ( dato != hola && valor <. 5 ) { x = dato - numero }
'''

tokens_identificados = identificar_tokens(codigo_ejemplo)
print(tokens_identificados)
