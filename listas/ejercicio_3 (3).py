lista_nombres = []
while True:
    nombre = input("Ingrese un nombre: ").lower()
    if nombre == "no":
        break
    lista_nombres.append(nombre)
nombre_corto = lista_nombres[0] 
for nombre in lista_nombres:
    if len(nombre)< len(nombre_corto):
        nombre_corto = nombre
lista_nombres.remove(nombre_corto)
print(lista_nombres)