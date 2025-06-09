año_actual= int (input("¿En que año estamos?: "))
año_cualquiera= int (input("Escriba un año cualquiera: "))

if año_actual == año_cualquiera:
    print ("¡Son el mismo año!")
elif año_actual > año_cualquiera:
    resta = año_actual - año_cualquiera
    if resta == 1:
        print(f"Desde el {año_cualquiera} han pasado {resta} año ")
    else:
        print(f"Desde el {año_cualquiera} han pasado {resta} años ")
elif año_actual < año_cualquiera:
    resta = año_cualquiera - año_actual
    if resta == 1:
         print (f"Para llegar al año {año_cualquiera} falta {resta} año")
    else:
        print (f"Para llegar al año {año_cualquiera} falta {resta} años")
else:
    resta = año_cualquiera - año_actual
    print (f"Para llegar al año {año_cualquiera} faltan {resta} ")
