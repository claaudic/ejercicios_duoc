pais = input("Ingrese su pais ")
peso = float (input("Ingrese el peso del paquete "))
total = 0
if pais == "chile":
    total = peso * 5
elif pais == "argentina":
    total = peso * 7
elif pais == "mexico":
    total = peso * 10
print(f"costo base: {total}")
if peso > 20:
    print ("sobrecargo por tamaño: $ 50")
    total = total + 50
print(f"total: {total}")