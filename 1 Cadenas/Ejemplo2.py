frase = input("Introduzca alguna frase: ")
vocal = input("Introduzca una vocal en minúscula:  ")
print(frase[::-1])
print(frase.replace(vocal, vocal.upper()))