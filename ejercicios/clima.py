temperatura = float (input("Ingrese la temperatura en grados Celsius "))
lluvia = input ("¿Esta lloviendo? ").lower()

if temperatura < 0 and lluvia == "si":
    print ("Clima peligroso: nieve y lluvia") 
elif temperatura < 0:
    print ("Muy frio,pero seco")
elif temperatura >= 0 and temperatura <= 20 and lluvia == "si":
    print ("Frio y lluvioso")
elif temperatura >= 0 and temperatura <= 20 :
    print("Frio moderado")
elif temperatura >20 and lluvia == "si":
    print("Calido pero con lluvia") 
else:
    print("Buen clima para salir")