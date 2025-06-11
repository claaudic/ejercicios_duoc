def validar_lista_numeros():
    lista_valida = []
    # def "nombre de la funcion"(van los argumento es como una variable siempre van separados por comas)
    while True:
        try:
            lista_numeros = input("Ingrese numeros enteros separados por espacio: ")
            lista = lista_numeros.split(" ")
            for i in lista:
                n = int(i)
                lista_valida.append(n)
            return lista_valida
        except ValueError:
            #lista_valida = []
            lista_valida.clear()
            print("Datos ingresados no validos")
lista_valida = validar_lista_numeros() 
print(lista_valida)
lista_pares=[]
lista_impares=[]
for i in lista_valida:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print(f"Numeros pares: {lista_pares}")
print(f"Numeros impares: {lista_impares}")