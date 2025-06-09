total_puntos = 0
while True:
    try:
        cantidad_de_productos = int(input("Indique la cantidad de productos que lleva\n -> "))
        if cantidad_de_productos > 0:
            break
        else:
            print("Debe ingresar un número entero positivo")
    except ValueError:
        print("Dato ingresado no es válido. Intente nuevamente")

for i in range(1, cantidad_de_productos + 1,3):
    #range donde tu quieres empezar, por defecto es 0
    print(i)
    total_puntos = total_puntos + i

print(f"El total de puntos obtenidos por la compra es: {total_puntos}")
