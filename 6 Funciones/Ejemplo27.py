def funcion_palabras(oracion):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        oracion: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase oracion.
    '''
    palabras = oracion.split()
    longitudes = map(len, palabras)
    return dict(zip(palabras, longitudes))

print(funcion_palabras('Bienvenido a la materia de Big Data con python'))