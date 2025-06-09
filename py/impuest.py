ingreso_anual = int (input("Digite su ingreso anual"))
impuesto= 0
if ingreso_anual < 10000:
    impuesto = 0
elif ingreso_anual >= 10000 and ingreso_anual <= 20000:
    impuesto = (ingreso_anual- 10000) * 0.10
elif ingreso_anual >= 20000 and ingreso_anual <= 50000:
    impuesto = 10000 * 0.10 + (ingreso_anual - 10000) * 0.20
else:
    impuesto = 10000 * 0.10 + 30000 * 0.2 + (ingreso_anual - 40000) * 0.30
print(int(impuesto))