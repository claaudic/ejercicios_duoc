numero1 = int (input ("Escriba un numero "))
numero2 = int (input ("Escriba otro numero "))
if numero1 == 0 or numero2 == 0:
    print ("Lo siento, este programa no admite valores nulos")
else:
    if numero1 < 0 or numero2 < 0:
        print ("Lo siento, este programa no admite valores negativos")
    
if numero1 > 0 and numero2 > 0:
    if numero1% numero2 == 0:
        print (f"{numero1} es multiplo de {numero2}")
    else:
        print (f"{numero1} no es multiplo {numero2}")

