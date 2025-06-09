texto = "HOLA MI AMORCITO".lower()
print(len(texto))
print(texto[8:len(texto)])
print(texto[5:7])

for i in range(len(texto)):
    if texto[i].upper() in ('A','E','I','O','U'):
        print(texto[i])
        
condicion = "TE AMO".lower() == "te amo" # verdadero o falso
print(condicion)

numero = int(input("Ingresa un numero"))
cumple_rango = numero > 1 and numero < 10
if cumple_rango: # numero > 1 and numero < 10
    print("esta en el rago")
else:
    print("no esta")

