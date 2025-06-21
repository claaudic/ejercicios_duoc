def devolver_diccionarario (lista):
    diccionario = {}
    for palabra in lista:
        if palabra in diccionario:
          diccionario [palabra] = diccionario[palabra] +1
        else:
            diccionario[palabra] = 1
    return diccionario
animales = ["gato", "perro", "gato", "pájaro", "perro", "gato"]

resultado = devolver_diccionarario(animales)
print(resultado)
        
          