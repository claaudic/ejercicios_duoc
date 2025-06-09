impuesto = 0
renta_liquida = 0
ingreso_anual = 0
gasto_anuales = 0
while True:

    try:
        print("---- MENÚ IMPUESTO A LA RENTA ----")
        print("1. Ingresar datos del contribuyente")
        print("2. Calcular impuesto")
        print("3. Mostrar resumen")
        print("4. Borrar datos")
        print("5. Salir")
        op = int(input("Seleccione una opcion \n -"))
        if op == 1:
            while True:
                nombre_completo = input("Ingrese su nombre \n - ")
                if nombre_completo == "":
                    print("Debe ingresar su nombre completo!")
                else:
                    print("Datos ingresados correctamente!")
                    break
            while True:
                try:
                    ingreso_anual = int (input("Introduzca su ingreso anual\n - "))
                    if ingreso_anual <= 0:
                        print("El ingreso anual no puede ser 0")
                    else:
                        print("Datos ingresados correctamente!")
                        break
                except ValueError:
                    print("Datos invalidos")
            while True:
                try:
                    gasto_anuales = int (input("Introduzca sus gastos anuales aceptados por el SII\n - "))
                    if gasto_anuales > ingreso_anual:
                        print("Los gastos anuales no pueden superar el ingreso anual bruto")
                    else:
                        print("Datos ingresados correctamente!")
                        break
                except ValueError:
                        print("Datos invalidos")
        elif op == 2:
            if ingreso_anual == 0 or gasto_anuales == 0:
                print("Debe ingresar datos primero (opción 1)")
                continue
            renta_liquida = ingreso_anual - gasto_anuales
            if renta_liquida > 0 and renta_liquida  <= 8_000_000:
                print("Impuesto 0%")
            elif renta_liquida >= 8_000_001 and renta_liquida <= 20_000_000:
                print("Impuesto del 10%")
                impuesto = renta_liquida * 0.10
            elif renta_liquida >= 20_000_000 and renta_liquida <= 40_000_000:
                print("Impuesto del 20%")
                impuesto = renta_liquida * 0.20
            elif renta_liquida >= 40_000_000:
                print("Impuesto del 30%")
                impuesto = renta_liquida * 0.30
        elif op == 3:
            if nombre_completo == "" or ingreso_anual ==0:
                print("Debe ingresar datos primero (opción 1)")
                continue
            if renta_liquida == 0 or impuesto == 0:
                print("Debe revisar el calculo del impuesto primero (opción 2)")
                continue

            print(f"Contributente {nombre_completo}")
            print(f"Ingreso brutos:{ingreso_anual}")  
            print(f"Gastos aceptados:{gasto_anuales}")  
            print(f"Renta liquida:{renta_liquida}")
            print(f"Impuesto estimado:{impuesto:.0f}")
        elif op == 4:
            nombre_completo = ""  
            ingreso_anual = 0
            gasto_anuales = 0
            print("Datos eliminados correctamente")        
        elif op == 5:
            print("Adios..Que tenga buen dia!")
            break
        else:
            print("La opcion elegida no es valida")        
    except ValueError:
        print("La opcion es invalida!")