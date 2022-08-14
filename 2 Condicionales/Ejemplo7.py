edad = int(input("¿Introduzca su edad? "))
ingresos = float(input("¿Cuales son tus ingresos mensuales? "))
if edad > 18 and ingresos >= 1000:
    print("Usted tiene que pagar impuestos")
else:
    print("Usted no tiene que pagar impuestos")