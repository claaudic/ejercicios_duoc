def palabras_con_letras (lista,n):
    nueva_lista = []
    for palabra in lista:
        if len(palabra)> n:
            nueva_lista.append(palabra)
    return nueva_lista
    
palabras = ["Hola", "como", "chao", "bien", "mal", "y"]
resultado = palabras_con_letras(palabras,3)    
print(resultado)   
