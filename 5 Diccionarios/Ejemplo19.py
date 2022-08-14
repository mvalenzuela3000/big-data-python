divisas = { 'Dollar':'$','Euro':'€', 'Boliviano':'Bs.'}
divisa = input("Introduce una divisa: ")
print(divisas.get(divisa.title(), "La divisa no está."))