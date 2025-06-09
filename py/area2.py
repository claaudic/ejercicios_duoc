suma = 0
def leer_validar(texto):
    while True:
        try:
            cantidad = int(input(texto))
            if cantidad <= 0:
                print("La cantidad no puede ser 0")
            else:
                return cantidad
        except ValueError:
            print("opcion no valida") 
cantidad = leer_validar("Ingrese la cantidad de triangulos a calcular\n - ")
for i in range(cantidad):
    base_triangulo = leer_validar("Ingrese la base del triangulo\n- ")
    altura_triangulo = leer_validar("Ingrese la altura del triangulo\n- ")
    area = (base_triangulo * altura_triangulo)/2
    suma = area + suma
print(f"La suma total de las áreas es: {suma}")
lista = ["te","amo","longito","mochi"]
print(len(lista))
for i in lista:
    print(i)