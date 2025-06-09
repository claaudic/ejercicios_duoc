print ("¿Cual de los siguentes animales vive debajo del agua?")
print ("1.Perro")
print ("2.Cocodrilo")
print ("3.Conejo")
print ("4.Tiburon")
respuesta = input().lower() #input es para leer un valor ingresado por teclado
#debe estar siempre asignado a una variable (input)
puntaje = 0 
if respuesta == "cocodrilo":
    puntaje = puntaje + 0.5 # es lo mismo ... puntaje += 0.5
else:  ## puedes usar elif respuesta == "tiburon":
    if respuesta == "tiburon":
        puntaje =+ 1.0

print(f"Obtuviste {puntaje} puntos")



#print solo muestra algo 
#input () lee un valor ingresado por teclado y opcionalmente 
#puede mostrar un texto ""