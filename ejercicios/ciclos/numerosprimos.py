num= int(input("Ingrese un numero entero positivo: "))
contador = 0

for i in range (1,num + 1):
    #print(i)
    if num % i == 0:
        contador = contador + 1
#print(contador)
if contador == 2:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num}no es primo")
    
    
