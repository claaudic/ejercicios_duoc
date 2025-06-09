while True:
    try:
        print("-- Menu Principal --")
        print("1.- Ver mi saldo ")
        print("2.- Retirar Dinero")
        print("3.- Salir")
        opcion = int (input("Ingrese una opcion \n"))
        if opcion == 1:
            print("Tiene un saldo de 500.000")
            opcion_dos = int (input("Presione 1 para volver atras o 2 para salir \n"))
            if opcion_dos == 2:
                print("Cierre de sesion exitoso, adios")
                break
        if opcion == 2:
            print("Transferencia realizada")
            opcion_dos = int (input("Presione 1 para volver atras o 2 para salir \n"))
            if opcion_dos == 2:
                print("Cierre de sesion exitoso, adios")
                break
        if opcion == 3:
            print("Cierre de sesion exitoso, adios")
            break
    except ValueError as error:
        print("Datos invalidos")