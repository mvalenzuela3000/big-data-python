frutas = {'Plátano':2.50, 'Manzana':3.20, 'Pera':4.50, 'Naranja':0.50}
fruta = input('¿Qué fruta desea? ').title()
peso = float(input('¿Cuántos kilos requiere? '))
if fruta in frutas:
    print(peso, ' kilos de', fruta, ' cuestan ', frutas[fruta]*peso, ' Bs.')
else: 
    print("Lo sentimos, la fruta ", fruta, " no está disponible.")