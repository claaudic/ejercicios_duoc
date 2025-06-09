entradas_por_comprar = 0
total_entradas = 70
while True:
    try:
        print("**** Cine Estrella ****")
        print("Bienenido al sistema de venta de entradas del Cine Estrella")
        print("1.- Ver cuántas entradas quedan.")
        print("2.- Comprar una cantidad de entradas.")
        print("3.- Salir del sistema")
        opcion = int(input("Seleccione una opcion\n - "))
        
        if opcion == 1:
            print(f"Entradas disponibles {total_entradas}")
        elif opcion == 2:
            while True:
                try:
                    entradas_por_comprar = int(input("¿Cuantas entradas desea comprar?\n - "))
                    if entradas_por_comprar > total_entradas:
                        print("Cantidad insuficientes")
                        break
                    else:
                        total_entradas = total_entradas - entradas_por_comprar
                        print(f"Compra exitosa. Quedan {total_entradas} entradas.")
                        break
                except ValueError:
                    print("La opcion elegida no es valida")
        elif opcion == 3:
            print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
            break
        else:
            print("La opcion elegida no es valida")
    except ValueError:
        print("La opcion elegida no es valida")