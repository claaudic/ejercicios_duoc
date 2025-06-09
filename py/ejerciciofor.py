cantidad_bultos = int (input("Ingrese la cantidad de bulto \n"))
peso = 0
liviana = 0
normal = 0
cantidad_liviano = 0
cantidad_normal = 0
for i in range (cantidad_bultos):
    while True:
        try:
            peso = float (input(f"Ingrese el peso {i+1}:"))
            if peso >= 1 and peso <= 5:
                liviana = int (1000 + liviana)
                cantidad_liviano = cantidad_liviano + 1
                #print(liviana)
                break
            elif peso >= 6 and peso <= 10:
                normal = int (2000 + normal)
                cantidad_normal = cantidad_normal + 1
                #print(normal)
                break
        except ValueError as error:
             print ("Se ingresaron datos no válidos")
total_pagar = liviana + normal
if cantidad_liviano >0:
    print(f"{cantidad_liviano} Bulto liviano ${liviana}")
if cantidad_normal > 0:
    print(f"{cantidad_normal} Bulto normal ${normal}")
print(f"Valor total a pagar {total_pagar}")       