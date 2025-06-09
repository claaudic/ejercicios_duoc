print("Opciones de menú")
print("Opcion 1.- Validar si es par o impar")
print("Opcion 2.- Sumar números primos y no primos")
print("Opcion 3.- Salir del programa")
numero = 0

op = int(input("Ingrese una opcion \n -> "))
while op != 3:
    try:
        if op == 1:
            numero= int(input("Ingrese un numero \n -> "))
            if numero % 2 == 0:
                print(f"El numero {numero} es par")
            else:
                print(f"El numero {numero} no es")  
            op = int(input("Nuevamente ingrese una opcion (3.- para salir)\n -> "))
    except ValueError:
           print("Usted ingreso un valor malo!!")
    if op == 2:
        suma = 0
        suma_no_primos= 0 
        suma_primos= 0
        cantidad= int(input("Ingrese la cantidad de numeros \n -> "))
        for i in range (1,cantidad + 1):
            while True:
                try:
                    numeros = int(input(f"Numero {i} -> "))
                    contador = 0
                    for l in  range (1,numeros + 1):
                        #print("mostrando l",l)
                        if numeros % l == 0:
                            contador = contador + 1
                    #print(contador)
                    if contador == 2:
                        #print("es")
                        suma_primos = suma_primos + numeros
                    else:
                        #print("no es")
                        suma_no_primos = suma_no_primos + numeros
                    break
                except ValueError:
                    print("Usted ingreso un valor malo!!")
        print(f"La suma de primos es {suma_primos} y de no primos es {suma_no_primos}")
        op = int(input("Nuevamente ingrese una opcion (3.- para salir)\n -> "))
if op == 3:
        print("Saliendo del programa...")
   
  
