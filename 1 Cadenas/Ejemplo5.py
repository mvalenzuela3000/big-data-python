producto = input('Introduzca el nombre del producto: ')
precio = float(input('Introduzca el precio unitario: '))
unidades = int(input('Introduzca el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}Bs. = {total:11.2f}Bs.'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))