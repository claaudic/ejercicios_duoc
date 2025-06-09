genero = input("Ingrese su genero: ")
destino = input("Ingrese su destino (NORTE o SUR) ")
edad = int (input("Ingrese su edad: "))
valor= int (input("Ingrese el valor del pasaje $: "))
maleta = int (input("Ingrese la cantidad de maleta "))

if genero == "masculino" and destino =="norte":
    print ("Cliente NO tiene descuento para este viaje")
    print (f"porcentaje de descuento es : 0%")
    descuento = 0
    print (f"monto de descuento {descuento}") 
    print(f"valor pasaje con descuento = $ {valor} ")
    if maleta > 1:
        maleta_no_gratis = maleta - 1 
        precio_maleta = maleta_no_gratis*5000
        print (f"monto por traslado de maleta = $ {precio_maleta}")
        valor_final = valor + precio_maleta 
        print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
    else:
        print (f"valor pasaje final y traslado de maletas = $ {valor}")
else:
    if genero == "masculino" and destino == "sur" and edad < 25:
        print (f"porcentaje de descuento es : 10%")
        descuento = int (valor* 0.10) 
        print (f"monto de descuento {descuento}") 
        resta = valor - descuento
        print(f"valor pasaje con descuento = $ {resta} ")
        if maleta > 1:
            maleta_no_gratis = maleta - 1 
            precio_maleta = maleta_no_gratis*5000
            print (f"monto por traslado de maleta = $ {precio_maleta}")
            valor_final = valor + precio_maleta 
            print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
        else:
            print (f"valor pasaje final y traslado de maletas = $ {resta}")
    elif genero == "masculino" and destino == "sur" and edad >= 25 and edad <= 64:
        print (f"porcentaje de descuento es : 20%")
        descuento = int (valor* 0.20) 
        print (f"monto de descuento {descuento}") 
        resta = valor - descuento
        print(f"valor pasaje con descuento = $ {resta} ")
        if  maleta > 1:
            maleta_no_gratis = maleta - 1 
            precio_maleta = maleta_no_gratis*5000
            print (f"monto por traslado de maleta = $ {precio_maleta}")
            valor_final = valor + precio_maleta 
            print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
        else:
            print (f"valor pasaje final y traslado de maletas = $ {resta}")
    else:
        print (f"porcentaje de descuento es : 30%")
        descuento = int (valor* 0.30) 
        print (f"monto de descuento {descuento}") 
        resta = valor - descuento
        print(f"valor pasaje con descuento = $ {resta} ")
        if maleta > 1:
            maleta_no_gratis = maleta - 1 
            precio_maleta = maleta_no_gratis*5000
            print (f"monto por traslado de maleta = $ {precio_maleta}")
            valor_final = resta + precio_maleta 
            print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
        else:
            print (f"valor pasaje final y traslado de maletas = $ {resta}")
if genero == "femenino" and destino =="sur":
    print ("Cliente NO tiene descuento para este viaje")
    print (f"porcentaje de descuento es : 0%")
    descuento = 0
    print (f"monto de descuento {descuento}") 
    print(f"valor pasaje con descuento = $ {resta} ")
    if maleta > 1:
        maleta_no_gratis = maleta - 1 
        precio_maleta = maleta_no_gratis*5000
        print (f"monto por traslado de maleta = $ {precio_maleta}")
        valor_final = valor + precio_maleta 
        print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
    else:
        print (f"valor pasaje final y traslado de maletas = $ {resta}")
else:
    if genero == "femenino" and destino == "norte" and edad < 25:
        print (f"porcentaje de descuento es : 5%")
        descuento = int (valor* 0.05) 
        print (f"monto de descuento {descuento}") 
        resta = valor - descuento
        print(f"valor pasaje con descuento = $ {resta} ")
        if maleta > 1:
            maleta_no_gratis = maleta - 1 
            precio_maleta = maleta_no_gratis*5000
            print (f"monto por traslado de maleta = $ {precio_maleta}")
            valor_final = resta + precio_maleta 
            print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
        else: 
            print (f"valor pasaje final y traslado de maletas = $ {resta}")
    elif genero == "femenino" and destino == "norte" and edad >= 25 and edad <= 64:
        print (f"porcentaje de descuento es : 15%")
        descuento = int (valor* 0.15) 
        print (f"monto de descuento {descuento}") 
        resta = valor - descuento
        print(f"valor pasaje con descuento = $ {resta} ")
        if maleta > 1:
            maleta_no_gratis = maleta - 1 
            precio_maleta = maleta_no_gratis*5000
            print (f"monto por traslado de maleta = $ {precio_maleta}")
            valor_final = resta + precio_maleta 
            print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
        else:
            print (f"valor pasaje final y traslado de maletas = $ {resta}")
    else:
        print (f"porcentaje de descuento es : 25%")
        descuento = int (valor* 0.25) 
        print (f"monto de descuento {descuento}") 
        resta = valor - descuento
        print(f"valor pasaje con descuento = $ {resta} ")
        if maleta > 1:
            maleta_no_gratis = maleta - 1 
            precio_maleta = maleta_no_gratis*5000
            print (f"monto por traslado de maleta = $ {precio_maleta}")
            valor_final = resta + precio_maleta 
            print (f"valor pasaje final y traslado de maletas = $ {valor_final}")
        else:
            print (f"valor pasaje final y traslado de maletas = $ {resta}")
