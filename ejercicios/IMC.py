peso = float(input ("Ingrese su peso "))
altura = float (input("Ingrese su altura "))
edad = int(input("Ingrese su edad "))
multiplicacion = altura*altura
imm= round(peso/multiplicacion,2)
print(f"Su índice de masa corporal es:{imm}")

if imm < 22 and edad < 45:
    print("Su nivel de riesgo es bajo")
elif imm < 22 and edad >= 45:
    print("Su nivel de riesgo es medio")
elif imm >= 22 and edad < 45:
    print("Su nivel de riesgo es medio")
elif imm >= 22 and edad >= 45:
    print ("Su nivel de riesgo es alto") 