print("$$$$ Cajero Automatico $$$$")
print("Bienvenid@")
for i in range(1, 3 + 1):
    clave = input("Introduzca su clave (FIN para salir)\n").upper()
    
    if clave == "FIN":
        print("saliendo")
        break
    
    #print(len(clave))
    if len (clave) == 4:
        if clave == "4542":
            print("Clave correcta")
            saldo = 0
            # MENU
            while True:
                try:
                    print ("Opcion 1.-Ingresar dinero")
                    print ("Opcion 2.-Retirar dinero")
                    print ("Opcion 3.-Transferir dinero")
                    print("Opcion 4.- Consultar saldo")
                    print ("Opcion 5.-Salir")
                    op = int(input("Selecione una opcion \n -> "))
                    if op == 5:
                        print("Saliendo...")
                        break
                    if op == 1:
                        while True:
                            try:
                                ingresar_dinero = input("Monto a ingresar (FIN para volver al menu)\n -> ")
                                if ingresar_dinero == "FIN":
                                    print("Saliendo...")
                                    break
                                ingresar_dinero = int(ingresar_dinero)
                                if ingresar_dinero <= 0:
                                    print("El monto a ingresar no puede ser 0")
                                else:
                                    saldo = ingresar_dinero + saldo
                                    print(f"Ingreso exitoso! Su nuevo saldo es {saldo}")
                                    break
                            except ValueError:
                                print("Datos invalidos, Intente nuevamente")
                    if op == 2:
                        while True:
                            try:
                                retiro_dinero = int(input("Ingrese el monto a retirar (-1 para volver al menu) \n -> "))
                                if retiro_dinero == -1:
                                        print("Saliendo...")
                                        break
                                if retiro_dinero > saldo:
                                    print("El monto a retirar no puede ser superior al monto disponible!")
                                elif retiro_dinero == 0:
                                    print("El monto a retirar no puede ser 0")
                                else:
                                    saldo = saldo - retiro_dinero 
                                    print(f"Retiro exitoso! Su nuevo saldo es {saldo}")
                                    break
                            except ValueError:
                                print("Datos invalidos, Intente nuevamente")
                    if op == 3:
                        cuenta_a_transferir = (input("Ingrese el numero de la cuenta a transferir\n ->"))
                        if cuenta_a_transferir == "":
                            print("Debe ingresar algo aqui!")
                        else:
                            while True:
                                try:
                                    monto_transferir = int (input("Ingrese el monto a transferir (-1 para volver al menu)\n -> "))
                                    
                                    if monto_transferir == -1:
                                        print("Saliendo...")
                                        break
                                    if monto_transferir > saldo:
                                        print("El monto a transferir no puede ser superior al monto disponible!")
                                    elif monto_transferir == 0:
                                        print("El monto a transferir no puede ser 0")
                                    else:
                                        saldo = saldo - monto_transferir
                                        print(f"Transferencia exitosa! a destino {cuenta_a_transferir} por el monto {monto_transferir}")
                                        break
                                except: 
                                    print("Datos invalidos, Intente nuevamente")
                    if op == 4:
                        try:
                            print(f"Su saldo es {saldo}")
                        except ValueError:
                            print("La opcion eligida no es valida")
                except ValueError:
                    print("La opcion eligida no es valida")
                # FIN MENU
        else:
            if i == 3:
                print("Clave bloqueada!")
            else:
                print(f"Clave incorrecta, te quedan {3  - i} intentos")
    else:
        if i == 3:
            print("Clave bloqueada!")
        else:
            print(f"Debe introducir su clave de 4 digitos, te quedan {3  - i} intentos")
