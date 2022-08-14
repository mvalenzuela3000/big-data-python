# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria BigData.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduzca el número correspondiente al tipo de pizza que desea:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimientos\n\t2- Champiñones\n")
    ingrediente = input("Introduzca el ingrediente que desea: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimientos")
    else: 
        print("champiñones")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Chorizo\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduzca el ingrediente que desea: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("chorizo")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("carne molida")