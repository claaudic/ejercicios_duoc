nombre = input("Ingrese su nombre completo\n").lower()
letra_b = input("Ingrese una letra para buscar\n").lower()
repeticion = 0     
print(f"Cantidad de caracteres {len(nombre)}.")

for letra in nombre:
    if letra_b == letra:
        repeticion = repeticion + 1
         
if repeticion > 0:
    print(f"La letra {letra_b} aparece {repeticion} veces en el nombre.")
else:
    print(f"La letra {letra_b} no aparece en el nombre.")