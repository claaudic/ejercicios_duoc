quintil = int (input(" quintil "))
condicion_laboral = input ("Ingrese su condicion laboral")
edad = int (input("ingrese su edad"))

subsidio_gas= 0
if (quintil == 1 or quintil == 2) and condicion_laboral == "desempleado":
   subsidio_gas = 10000
elif (quintil == 1 or quintil == 2) and condicion_laboral == "empleado":
    subsidio_gas = 8000
elif quintil == 3  and condicion_laboral == "desempleado":
    subsidio_gas = 6000
elif quintil == 3 and condicion_laboral == "empleado":
    subsidio_gas = 4000
else:
    subsidio_gas = 1500
    