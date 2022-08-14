clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nitci = input('Introduzca NIT/CI del cliente: ')
        nombre = input('Introduzca el nombre completo del cliente: ')
        direccion = input('Introduzca la dirección del cliente: ')
        telefono = input('Introduzca el teléfono del cliente: ')
        email = input('Introduzca el correo electrónico del cliente: ')
        privilegio = input('¿Es un cliente preferencial (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':privilegio=='S'}
        clientes[nitci] = cliente
    if opcion == '2':
        nitci = input('Introduzca NIT/CI del cliente: ')
        if nitci in clientes:
            del clientes[nitci]
        else:
            print('No existe el cliente con el NIT/CI', nitci)
    if opcion == '3':
        nitci = input('Introduzca NIT/CI del cliente: ')
        if nitci in clientes:
            print('NIT/CI:', nitci)
            for clave, valor in clientes[nitci].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el NIT/CI', nitci)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')