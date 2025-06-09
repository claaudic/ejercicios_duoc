lista = []
cantidad = int(input("Ingrese una cantidad: "))       
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    lista.append(nombre)# Agregar un elemento al final
print(lista)
#--------------------------------------------------------------------
lista_desordenada = [7,1,3,4,2,6] #-> ejemplo [7,1,3,4,....] 
print(lista_desordenada)
lista_desordenada.sort() #-> ejemplo [1,2,3,4,....]
print(lista_desordenada)
lista_desordenada.sort(reverse=True) #-> ejemplo [7,6,5,4,3,...]
print(lista_desordenada)
#------------------------------------------------------------------
print(lista.count(input("Ingrese el nombre: "))) #COUNT(puede ir cualquier cosa) dice cuantas veces se repite un elemento
#--------------------------------------------
#Eliminar
nombre = input("Ingrese un nombre para eliminar: ")
lista.remove(nombre)
print(lista)
#----------------------------------------------
#Modificar un elemento el lista (REMPLAZAR)
nombre = input("Ingrese un nombre para modificar: ")
posicion = lista.index(nombre) #INDEX Devuelve el índice (posición) de la primera aparición de un elemento específico.
lista[posicion] = input("Ingrese un nuevo nombre: ")
print(lista)
