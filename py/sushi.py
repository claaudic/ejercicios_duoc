Monto = 0 
Monto_a_pagar = 0 
descuento = 0
cantidad_Pikachu = 0
cantidad_Otaku = 0
cantidad_Pulpo = 0
cantidad_Anguila = 0
while True:
    try:
        Pikachu_Roll = 4500
        Otaku_Roll = 5000
        Pulpo_Venenoso_Roll = 5200
        Anguila_Eléctrica_Roll = 4800
        print("---Bienvenid○@s a Sushi puki---")
        print("1. Pikachu Roll")
        print("2. Otaku Roll")
        print("3. Pulpo Venenoso Roll")
        print("4. Anguila Eléctrica Roll")
        print("5. Finalizar compra")
        
        op = int (input("Seleccione una opcion: "))
        if op == 1:
            while True:
                try:
                    cantidad= int (input(f"Selecione cuantos Pikachu Roll desea añadir: "))
                    if cantidad <= 0:
                        print("La cantidad no puede ser 0!")
                    else:
                        Monto = Monto + Pikachu_Roll * cantidad
                        cantidad_Pikachu = cantidad + cantidad_Pikachu 
                        print("Agregaste rolls pikachu a tu orden")
                        break
                    print(Monto)
                except ValueError:
                    print("La opcion seleccionada es invalida")
        elif op == 2:  
                while True:
                    try:
                        cantidad= int (input(f"Selecione cuantos Otaku Roll desea añadir: "))
                        if cantidad <= 0:
                            print("La cantidad no puede ser 0!")
                        else:
                            precio = Otaku_Roll * cantidad 
                            Monto = Monto + precio
                            cantidad_Otaku = cantidad_Otaku + cantidad
                            print("Agregaste rolls Otaku a tu orden")
                            break
                        print(Monto)
                    except ValueError:
                        print("La opcion seleccionada es invalida")
        elif op == 3:
                while True:
                    try:
                        cantidad= int (input(f"Selecione cuantos Pulpo Venenoso Roll desea añadir: "))
                        if cantidad <= 0:
                            print("La cantidad no puede ser 0!")
                        else:
                            Monto = Monto + Pulpo_Venenoso_Roll * cantidad 
                            cantidad_Pulpo = cantidad_Pulpo + cantidad
                            print("Agregaste rolls Pulpo a tu orden")
                            break
                        print(Monto)
                    except ValueError:
                        print("La opcion seleccionada es invalida")
        elif op == 4:
                 while True:
                    try:
                        cantidad= int (input(f"Selecione cuantos Anguila Eléctrica Roll desea añadir: "))
                        if cantidad <= 0:
                            print("La cantidad no puede ser 0!")
                        else:
                            Monto = Monto + Anguila_Eléctrica_Roll * cantidad
                            cantidad_Anguila = cantidad_Anguila + cantidad 
                            print("Agregaste rolls Anguila a tu orden")
                            break
                        print(Monto)
                    except ValueError:
                        print("La opcion seleccionada es invalida")
        elif op == 5:
            posee_codigo = input("Posee un código de descuento? Si/No -> " ).lower()
            if posee_codigo == "si":
                codigo = input("Ingrese el codigo de descuento..")
                while codigo != "soyotaku":
                    try:
                        print("El codigo no es valido!")
                        codigo = input("Ingresa el codigo nuevamente, para volver al menu escriba \"x\"")
                        if codigo == "x":
                            break
                    except ValueError:
                        print("La opcion seleccionada es invalida")
                if codigo == "x":
                    continue ## el continue omite todo lo que sigue despues y continua con la iteracion (pasa al siguiente paso desde el inicio)
                if codigo == "soyotaku":
                    descuento = Monto * 0.10
                    Monto_a_pagar = Monto - descuento  
                    print("Descuento aplicado!")
                # FIN PROGRAMA
                total_produtos = cantidad_Pikachu + cantidad_Otaku + cantidad_Pulpo + cantidad_Anguila
                print("***********************")
                print(f"TOTAL DE PRODUCTOS: {total_produtos}")
                print("***********************")
                print(f"Pikachu Roll: {cantidad_Pikachu}")  
                print(f"Otaku Roll: {cantidad_Otaku}")  
                print(f"Pulpo Venenoso Roll {cantidad_Pulpo}") 
                print(f"Anguila Elétrica Roll: {cantidad_Anguila}")
                print("***********************")
                print(f"Subtotal por pagar:{Monto}")
                print(f"Descuento por código:{descuento}")
                print(F"TOTAL: {Monto_a_pagar}")
        else:
            print("La opcion seleccionada es invalida")        
            print("Intente nuevamente")
    except ValueError:
        print("La opcion seleccionada es invalida")