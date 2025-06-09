sueldo = int (input("Ingrese el monto de su sueldo "))
deudas = int (input("Ingrese monto de sus deudas "))

if sueldo > 1_000_000 and deudas < 500_000:
    print("Credito Aprobado")
elif (sueldo >= 700_000 and sueldo <= 1_000_000) and deudas < 300_000:
    print("Evalucion manual")
else:
    print("Credito Rechazado")