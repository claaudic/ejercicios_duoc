numeros = [1,2,3,4,5]
numeros1 = [1,24,3,5,5,3,54,5,4,54,5,4,5,45,5]
numeros2 = [1,2,5,5,5,45,5,43,5,34,5,435,43,5,435,43,5,43,3,4,5]
def suma_numeros(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

resultado1 = suma_numeros(numeros)
resultado2 = suma_numeros(numeros1)
resultado3 = suma_numeros(numeros2)
print(resultado1, resultado1, resultado3)
