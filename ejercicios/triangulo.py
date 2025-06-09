longitud_1 = int (input ("Ingrese una lado 1 (Triangulo)"))
longitud_2 = int (input ("Ingrese una lado 2 (Triangulo)"))
longitud_3 = int (input ("Ingrese una lado 3 (Triangulo)"))


if longitud_1 + longitud_2 > longitud_3 and longitud_3 + longitud_2 > longitud_1 and longitud_3 + longitud_1 > longitud_2:
    if longitud_1 == longitud_2 == longitud_3:
        print ("Triangulo Equilatero")
    elif longitud_1 == longitud_2 or longitud_3 == longitud_1 or longitud_2 == longitud_3:
        print("Triangulo Isósles")
    elif longitud_1 != longitud_2 != longitud_3:
        print ("Escaleno")
else:
    print("No es posible construir un triangulo")