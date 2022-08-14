facturas = {}
cobrado = 0
pendiente = 0
opcion = ''
while opcion != 'T':
    if opcion == 'A':
        clave = input('Introduce el número de la factura: ')
        costo = float(input('Introduce el costo de la factura: '))
        facturas[clave] = costo
        pendiente += costo
    if opcion == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        costo = facturas.pop(clave, 0)
        cobrado += costo
        pendiente -= costo
    print('Cobrado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    opcion = input('¿Quiere añadir una nueva factura (A), pagarla (P) o terminar (T)? ')