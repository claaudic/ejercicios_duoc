valor_cancelar = int (input("Monto a pagar: "))
print("bolita 1")
print("bolita 2")
print("bolita 3")
print("bolita 4")
print("bolita 5")

op = int(input("Escoja una bolita: "))
descuento = 0
if op == 1:
    print("Bolita blanca")
    print("No obtuvo descuento :(")
    print(f"Valor final $: {valor_cancelar}")
elif op == 2:
    print ("Bolita verde")
    print("Obtuvo 10 % de descuento")
    descuento = valor_cancelar * 0.10 
    valor_final = valor_cancelar - descuento
    print(f"Valor final $: {valor_final}")
elif op == 3:
    print ("Bolita amarilla")
    print("Obtuvo 25 % de descuento")
    descuento = valor_cancelar * 0.25 
    valor_final = valor_cancelar - descuento
    print(f"Valor final $: {valor_final}")
elif op == 4:
    print ("Bolita azul")
    print("Obtuvo 50 % de descuento")
    descuento = valor_cancelar * 0.5
    valor_final = valor_cancelar - descuento
    print(f"Valor final $: {valor_final}")
elif op == 5:
    print ("Bolita roja")
    print("Felicidades! Obtuvo el 100 % de descuento")
    descuento = valor_cancelar * 1
    valor_final = valor_cancelar - descuento
    print(f"Valor final $: {valor_final}")
    