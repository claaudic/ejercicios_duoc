while True:
    try:
        n = int (input ("Hasta que numeros pares quieres mostrar\n -> "))
        if n > 0:
            break
        else:
            print("Debe ingresar un numero positivo")
    except ValueError:
        print ("Debe ingresar un numero entero")
#for i in range (desde, hasta, incremento)
for i in range(2,n + 1,2):
    print(i)
    
