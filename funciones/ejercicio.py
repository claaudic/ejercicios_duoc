lista1 = [8,4,6,7,7,7]
lista2= [1,6,8,9,0,3,4,7]
numero = 7
def devolver_numero (lista,numero):
    repeticion = 0
    for i in lista:
        if i == numero:
           repeticion = repeticion +1
    return repeticion

resultado = devolver_numero(lista1,numero)
resultado2 = devolver_numero(lista2,6)
print(f"El numero {numero} aparece {resultado} ")
print(f"El numero {6} aparece {resultado2} ")