turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
	"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def turistas_por_pais(pais):
    nombres_turistas = []
    for lista in turistas.values():
        if pais.lower() == lista[1].lower():
            nombres_turistas.append(lista[0])
    if len(nombres_turistas) == 0:
        print("No hay turistas en ese pais")
    else:
        print(nombres_turistas)

def turistas_por_mes(mes):
    contador = 0
    # for clave, turista in turistas.items(): => recorrer clave y valor
    # for clave in turistas.keys(): => recorrer clave 
    for turista in turistas.values(): # recorrer valores
        fecha = turista[2]
        mes2 = int(fecha.split("-")[1])
        if mes == mes2:
            contador = contador + 1
    return round(contador/len(turistas)*100, 1)
    
#porcentaje = turistas_por_mes(3)
#print(porcentaje)
def eliminar_turista():
    eliminar= input("Ingrese nombre del turista a eliminar: ").lower()
    clave_eliminar = None
    for clave,turista in turistas.items():
        if eliminar == turista[0].lower():
            clave_eliminar = clave
    turistas.pop(clave_eliminar)

def menu_principal():
    while True:
        try:
            print("\n----- Menú -----")
            print("1.Turistas por pais")
            print("2.Turistas por mes")
            print("3.Eliminar turista")
            print("4.Salir")
            opcion = int(input("Seleccione una opcíon: "))
    
            if opcion == 1:
                pais_a_buscar = input("Ingrese pais a buscar: ")
                turistas_por_pais(pais_a_buscar)
            elif opcion == 2:
                while True: 
                    try:
                        mes_a_buscar = int(input("Ingrese mes a buscar: "))
                        if mes_a_buscar >= 1 and mes_a_buscar <= 12:
                            turistas_por_mes(mes_a_buscar)
                            break
                        else:
                            print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                    except ValueError:
                        print("Datos no validos")
            elif opcion == 3:
                eliminar_turista()
            elif opcion == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opcion entre 1 y 4")
        except ValueError:
            print("Opcion no valida")
menu_principal()