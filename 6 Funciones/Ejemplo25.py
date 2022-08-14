def cuadrado(lista):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    lista: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista lista.
    """
    listaCuadrados = []
    for i in lista:
        listaCuadrados.append(i**2)
    return listaCuadrados

print(cuadrado([1, 2, 3, 4, 5]))