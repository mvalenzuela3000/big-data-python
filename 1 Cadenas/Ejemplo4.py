monto = input("Introduzca el monto de la venta con dos decimales:  ")
fecha = input("Introduzca la fecha de la venta en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesanio = fecha[fecha.find('/')+1:]
mes = mesanio[:mesanio.find('/')]
año = mesanio[mesanio.find('/')+1:]
print(monto[:monto.find('.')], 'Bolivianos y', monto[monto.find('.')+1:], 'centavos.')
print('Día', dia)
print('Mes', mes)
print('Año', año)