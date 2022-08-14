a = (1, -1, 2)
b = (1, 2, -3)
producto = 0
for i in range(len(a)):
    producto += a[i]*b[i]
print("El producto escalar de los vectores " + str(a) + " y " + str(b) + " es " + str(producto)) 