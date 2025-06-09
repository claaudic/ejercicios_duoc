while True:
    try:
        print ("---- Menu ----")
        print ("Opcion 1")
        print ("Opcion 2")
        print ("Opcion 3")
        print ("Opcion 4")
        op = int (input("seleccione una opcion\n"))
        
        # OPCION INCORRECTA
        if not (op >= 1 and op <= 4):
            # Validacion opcion incorrecta
            print ("OPCION INVALIDA")
        # FIN OPCION INCORRECTA
        
        # OPCION SALIDA
        if op == 4:
            print ("saliendo")
        # FIN OPCION SALIDA
        
        # inicio opcion 1
        if op == 1:
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
            print ("seleccionaste opcion 1..")
        # FIN OPCION UNO
        
        # inicio opcion 2
        if op == 2:
            print ("seleccionaste opcion 2..")
            
        # FIN OPCION UNO
        
        # inicio opcion 1
        if op == 3:
            print ("seleccionaste opcion 3...")
            
        # FIN OPCION UNO
    except ValueError:
        print("opcion invalida") 
        
        
              Monto_a_pagar = Monto - descuento  
            print(f"Pikachu Roll: {cantidad_Pikachu}")  
            print(f"Otaku Roll: {cantidad_Otaku}")  
            print(f"Pulpo Venenoso Roll {cantidad_Pulpo}") 
            print(f"Anguila Elétrica Roll: {cantidad_Anguila}")