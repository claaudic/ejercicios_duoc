

def numeros_pares (lista):
    nueva_lista = []
    for i in lista:
        if i % 2 == 0:
            nueva_lista.append(i)
    return nueva_lista

lista1 = [1,2,3,4,5,6,7,8,9,10,11,12]
lista2 = [1,3,5,7]
resultado = numeros_pares(lista1)
resultado2 = numeros_pares(lista2)
print(resultado)
print(resultado2)


    