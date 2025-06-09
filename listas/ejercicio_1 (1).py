#ejercicio 1
nombre_largo = None
nombres = []
for i in range (3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)
nombre_largo = nombres[0] 
for nombre in nombres:
    if len(nombre)> len(nombre_largo):
        nombre_largo = nombre
print(f"El nombre largo es {nombre_largo}")
max(nombres, key=len)