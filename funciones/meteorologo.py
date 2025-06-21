temperaturas = {} # guarda el siguiente formato Ciudad:{T1,T2,T3}
def agregar_temperatura():
    ciudad = input("Ingrese la ciudad: ").title() #deja la primera en mayúscula
    try:
        temp = float(input("Ingrese la temperatura: "))
        if ciudad not in temperaturas: # si la ciudad no esta creada en el diccionario, la agregara
            temperaturas[ciudad] = [] # inicial  vina []
        temperaturas[ciudad].append(temp) #ahora aqui la agrega busca vina y agrega ejemplo: {vina:14}
        print("Temperatura ha sido guardada")
    except ValueError:
        print("Ingrese número valido")
        
        
def consultar_estadisticas():
    ciudad = input("Ingrese la ciudad: ").title()
    if ciudad in temperaturas:
        datos = temperaturas[ciudad] # entrega los valores de la llave cuidad ejemplo: {vina:[temp1,temp2,temp3]}
        print(f"\n Estadistica de {ciudad}")
        print(f"- Promedio:{sum(datos)/len(datos):2f}") #entrega 2 decimales 2.23
        print(f" -Máxima: {max(datos)}")
        print(f" -Minima: {min(datos)}")
    else:
        print("La cuidad no está creada")

def ver_cuidades ():
    if temperaturas:
        print("Ciudades registradas: ")
        for ciudad in temperaturas:
            print(f"{ciudad}")
    else:
        print("No hay ciudades registradas")
        
def menu_principal():
    while True:
        print("\n----- Menú -----")
        print("1.- Agregar temperatura")
        print("2.- Consultar estadística")
        print("3.- Ver ciudades")
        print("4.- Salir del programa")
        
        opcion = input("Seleccione una opcíon: ")   
        
        if opcion == "1":
            agregar_temperatura()
        elif opcion == "2":
            consultar_estadisticas()
        elif opcion == "3":
            ver_cuidades()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcíon no valida")

menu_principal()