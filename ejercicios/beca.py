nota_promedio= float (input ("Ingrese nota promedio: "))
ingreso_familar = int (input("Ingrese ingreso mensual: "))

if nota_promedio >= 1.0 and nota_promedio < 5.0:
    print("No cumple con la nota minima")
elif nota_promedio >= 5.0 and nota_promedio <= 7.0 and ingreso_familar >= 0 and ingreso_familar <= 500_000:
    print("Beca completa")
elif nota_promedio >=5.0 and nota_promedio <= 7.0 and ingreso_familar >= 500_000 and ingreso_familar <= 1_000_000:
    print ("Beca parcial")
elif  nota_promedio >= 5.0 and nota_promedio <= 7.0 and ingreso_familar > 1000000:
    print("Sin beca por ingreso alto")
else:
    print("invalido")