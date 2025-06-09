suma = 0
while True:
    try:
        cantidad = int(input(f"Ingrese la cantidad de triangulos a calcular\n - "))
        for i in range (cantidad):
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                break
            while True:
                base_triangulo = float (input("Ingrese la base del triangulo\n- "))
                if base_triangulo <= 0:
                    print("Debe ingresar valores numéricos válidos")
                    break
                while True:
                    altura_triangulo = float (input("Ingrese la altura del triangulo\n- "))
                    if altura_triangulo <= 0:
                        print("Debe ingresar valores numéricos válidos")
                    break
            area_triangulo = (base_triangulo * altura_triangulo)/2
            suma = area_triangulo + suma
    except ValueError:
        print("Debe ingresar valores numéricos válidos.")

    print(f"La suma total de las áreas es: {suma}")
    break