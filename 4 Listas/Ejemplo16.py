palabra = input("Introduzca una palabra: ")
invertido = palabra
palabra = list(palabra)
invertido = list(invertido)
invertido.reverse()
if palabra == invertido:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")