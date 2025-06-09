import math

x = float (input("X: "))
resultado = 0
indice = 0
print("Coeficientes:")
while True:
    coeficiente = input()
    if coeficiente == "Fin":
        break
    resultado = resultado + float(coeficiente) * math.pow(x, indice) # math.pow(variable, elevado a q)
    indice = indice + 1
    
print(f"p (x) = {round(resultado, 2)}")