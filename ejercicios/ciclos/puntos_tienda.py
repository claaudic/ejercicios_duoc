
total_puntos = 0
while True:
    try:
        cantidad_de_productos = int (input ("Indique la cantidad de produtos que lleva\n -> "))
        if cantidad_de_productos > 0:
            break
        else:
            print("Debe ingresar un numero positivo")
    except ValueError:
        print ("Debe ingresar un numero entero")
        
for i in range(cantidad_de_productos):
    i = i+1
    total_puntos = total_puntos + i 
    # total_puntos = total_puntos + i + 1 otra forma 
print(f"El total de puntos obtenidos por la compra es: {total_puntos}")
        
        
    


