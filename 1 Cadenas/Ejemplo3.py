email = input("Introduce tu correo electrónico: ")
dominio=input("Introduce nuevo dominio: ")
print(email[:email.find('@')] +'@' +dominio)