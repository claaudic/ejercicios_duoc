while True:
    try:
        print("1. Opcion 1")
        print("2. Opcion 2")
        print("4. Opcion 3")
        print("4. Opcion 4")
        print("5. Opcion 5")
        print("6. Opcion salida")
        
        op = int(input("Ingrese una opcion"))
        
        if op == 1:
            print("opcion 1")   
        elif op == 2:
            print("opcion 2")
        elif op == 3:
            print("opcion 3")
        elif op == 4:
            print("opcion 4")
        elif op == 5:
            print("opcion 5")
        elif op == 6:
            print("opcion 6")
            break
        else:
            print("Opcion invalida")
    except ValueError:
        print("opcion invalida ")