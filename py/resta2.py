num1 = 0
num2 = 0

# aqui se guarda en una variable num, int indica de tipo entero y input es para leer
num1 = int(input ("Ingrese un numero para restar\n"))

num2 = int(input("Ingrese otro numero para restar\n"))

resta = num1 - num2
# esto sirve para mostrar una salida, f es format, es decir reemplazar  por valores de mis variales el texto mostrado {}
print(f"El resultado de la resta entre {num1} y {num2} es: {resta}")