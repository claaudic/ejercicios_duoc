from random import randint

limete_inferior = int(input( "Ingrese limete inferior: "))
limete_superior = int(input( "Ingrese limete superior: "))

numero = randint(limete_inferior,limete_superior)
# PRIMER INTENTO
primer_intento = input("Intenta adivinar ")
if numero == primer_intento: # GANE
    print("Felicidades, adivino en el primer intento")
elif numero > primer_intento:
    print ("el numero es mayor")
elif numero < primer_intento:
    print ("el numero es menor")

# SEGUNDO INTENTO
segundo_intento = int (input("Intenta denuevo "))
if numero == segundo_intento: # GANE
    print("Felicidades, adivino en el segundo intento")
elif numero > segundo_intento:
    print ("El numero es mayor") 
    print("Te dare una pista")
    print(f"El numero que buscas esta mas cerca de {segundo_intento} que de {primer_intento}")
elif numero < segundo_intento:
    print ("El numero es menor")
    print("Te dare una pista")
    print(f"El numero que buscas esta mas cerca de {primer_intento} que de {segundo_intento}")

ultimo_intento = int (input("Intente la ultima vez "))
if numero == ultimo_intento: # GANE
    print("felicidades, ganaste en el ultimo intento")
else:
    print("Perdiste")
    print("El numero era:", numero)