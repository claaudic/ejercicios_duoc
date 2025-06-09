velocidad_actual= int(input("Velocidad actual: "))
velocidad_permitida = int(input("Velocidad permitida: "))

if velocidad_actual <= velocidad_permitida:
    print("Velocidad permitida")
elif velocidad_actual - velocidad_permitida <= 10 and velocidad_actual > velocidad_permitida:
    print("Advertencia")
elif velocidad_actual- velocidad_permitida >=11 and velocidad_actual - velocidad_permitida <= 30:
    print("Multa leve")
elif velocidad_actual - velocidad_permitida > 30:
    print ("Multa grave y suspencion de licencia")
