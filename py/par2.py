n = int(input("Ingrese un numero entero: "))
if n >= 1 and n <= 100:
    par = n % 2 == 0
    rango1 = n >=2 and n <= 5 
    rango2= n >= 6 and n <= 20
    rango3 = n > 20 
    if par and rango1:
        print ("Not Weird")
    elif par and rango2:
        print ("Weird")
    elif par and rango3:
        print ("Not Weird")
    else:
        print("Weird")
else:
    print("no valido")
