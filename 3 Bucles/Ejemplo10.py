monto = float(input("¿Qué cantidad desea invertir? "))
interes = float(input("¿Cual es el interés porcentual anual? "))
anios = int(input("¿Cuántos años?"))
for i in range(anios):
    monto *= 1 + interes / 100 
    print("Capital después de " + str(i+1) + " años: " + str(round(monto, 2)))