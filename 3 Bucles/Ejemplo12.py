frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))