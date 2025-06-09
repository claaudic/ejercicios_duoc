num1= float (input("Escriba un numero "))
num2= float (input("Escriba otro numero "))

if num1 > num2:
    print(f"Mayor:{num1} Menor: {num2} ")
elif num1 < num2:
    print(f"Menor: {num1} Mayor: {num2}")  
else:
    print(f"Los dos numeros son iguales.")