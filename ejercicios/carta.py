from random import randint

numero_random = randint (1,3)

posicion = int (input("Elige una posicion (1-3) "))
if posicion >=1 and posicion <= 3:
    if numero_random == posicion:
     print("¡Ganaste! Encontraste el As." )
    else:
        print (f"Perdiste. El As estaba en la posicion {numero_random}") 
else:
    print ("Numero fuera del rango ")
        