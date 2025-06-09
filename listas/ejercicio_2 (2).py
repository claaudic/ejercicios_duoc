nombres = []
apellidos = []
for i in range (3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)
    apellido = input(f"Ingrese el apellido {i+1}: ")
    apellidos.append(apellido)
largo_lista = len(nombres)
for i in range (largo_lista):
    print(f"Nombres  y apellido : {nombres[i]} {apellidos[i]}")
nombres.sort()