n = int(input("Ingrese un numero entero: "))
if n >= 1 and n <= 100:
    if n % 2 == 0:
        print("par")
    else:
        n % 2 != 0
        print ("impar")
else:
    print("invalido")
    
