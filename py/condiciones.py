# LEER DOS NUMEROS DECIMALES, Y SUMAR SI EL PRIMER NUMERO ES MAYOR AL SEGUNDO Y MULTIPLICAR EN CASO CONTRARIO
 
num1 = float(input("Ingrese un numero decimal \n") )

num2 = float(input("Ingrese un numero decimal\n") )

if num1 > num2: 
    suma = num1 + num2
    print (f"El resultado de la suma entre {num1} y {num2} es; {suma}")
else:
    multiplicar = num1 * num2
    print (f"El resultado de la multiplicacion entre {num1} y {num2} es; {multiplicar}")