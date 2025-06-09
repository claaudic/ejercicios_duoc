numero1 = int (input ("Escriba un numero "))
numero2 = int (input ("Escriba otro numero "))
numero3 = int (input ("Escriba otro numero "))

if numero1 == numero2 == numero3:
    print("Ha escrito tres veces el mismo numero")
elif numero1 == numero2 and numero3 != numero1:
    print("Ha escrito uno de los numeros dos veces")
elif numero2 == numero3 and numero1 != numero2:
    print("Ha escrito uno de los numeros dos veces")
elif numero3 == numero1 and numero2 != numero3:
    print("Ha escrito uno de los numeros dos veces")
else:
    print("Los tres numeros que ha escrito son distintos")
    




















