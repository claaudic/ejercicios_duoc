ingreso_anual = float (input ("Ingrese ingreso anual "))
impuesto = float (0)
if ingreso_anual > 0 and ingreso_anual < 10_000_000:
    impuesto = 0
    print (f"Impuesto: {impuesto}") 
    print(f"Ingreso neto {ingreso_anual}")
elif ingreso_anual > 10_000_001 and ingreso_anual < 25_000_000:
    impuesto = int(ingreso_anual *0.10)
    resta = ingreso_anual - impuesto
    print (f"Impuesto {impuesto}")
    print (f"Ingreso neto: {resta}")
elif ingreso_anual > 25_000_001 and ingreso_anual < 50_000_000:
    impuesto = int(ingreso_anual *0.20)
    resta = ingreso_anual - impuesto
    print (f"Impuesto {impuesto}")
    print (f"Ingreso neto: {resta}")
else: 
    impuesto = int(ingreso_anual *0.30)
    resta = ingreso_anual - impuesto
    print (f"Impuesto {impuesto}")
    print (f"Ingreso neto: {resta}")

