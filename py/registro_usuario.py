usuario_1 = None
usuario_2 = None
usuario_3 = None
contraseña_1 = None
contraseña_2 = None
contraseña_3 = None
while True:
    try:
        print ("--- Menu ---")
        print("1. Iniciar sesion")
        print("2. Registrar usuario")
        print("3. Salir")
        opcion = int (input("Introduzca una opcion \n - "))
        if opcion == 1:
            if usuario_1 == None and usuario_3 == None and usuario_2 == None:
                print("Primero debe registar un usuario")
                continue   
            else:
                inicio_sesion = False
                usuario_iniciar_sesion = input("Introduzca su nombre de usuario \n - ")
                contraseña_iniciar_sesion = input("Introduzca su contraseña \n - ")
                if usuario_iniciar_sesion == usuario_1 and contraseña_iniciar_sesion == contraseña_1:
                    print("Inicio de sesion correcta!")
                    inicio_sesion = True
                elif usuario_iniciar_sesion == usuario_2 and contraseña_iniciar_sesion == contraseña_2:
                    print("Inicio de sesion correcta!")
                    inicio_sesion = True
                elif usuario_iniciar_sesion == usuario_3 and contraseña_iniciar_sesion == contraseña_3:
                    print("Inicio de sesion correcta!")
                    inicio_sesion = True    
                else:
                    print("Inicio de sesion incorrecto!")
                if inicio_sesion == True:
                    while True:
                        try:
                            print(" - Menu 2 -")
                            print ("1. Realizar llamada")
                            print("2. Enviar correo electrónico")
                            print("3. Cerrar sesion")
                            seleccion = int(input("Seleccione una de las opciones \n - "))
                            if seleccion == 1:
                                numero_celular = input("Ingrese su numero de celular")
                                if len(numero_celular) == 9:#len es como un print(ksksls) len(numero)
                                    if numero_celular[0] == "9": #corchete [] obtiene un elemento del texto
                                        print("Realizando llamada..")
                                    else:
                                        print("El numero de celular debe empezar con 9")
                                else:
                                    print("El numero de celular debe tener 9 digitos")
                                        
                            elif seleccion == 2:
                                correo = input("Ingrese su correo")
                                tiene_arroba = False
                                for i in correo:
                                    if i == "@":
                                        tiene_arroba = True
                                if tiene_arroba == True:
                                    mensaje = input("Escriba el mensaje a enviar")
                                    print("Mensaje enviado...") 
                                else:
                                    print("Su correo es invalido")     
                            elif seleccion == 3:
                                print("Ha cerrado sesion!")
                                break
                            else:
                                print("selecion no valida")
                        except ValueError:
                            print("Opcion no valida")
                    
        elif opcion == 2:
                nuevo_usuario = input("Registre el nombre de usuario \n - ")
                print("Usuario creado !")
                nueva_contraseña = input("Ingrese una nueva contraseña \n - ")
                print("Contraseña creada!")
                if usuario_1 == None and contraseña_1 == None:
                    usuario_1 = nuevo_usuario
                    contraseña_1 = nueva_contraseña
                elif usuario_2 == None and contraseña_2 == None:
                    usuario_2 = nuevo_usuario
                    contraseña_2 = nueva_contraseña
                elif usuario_3 == None and contraseña_3 == None:
                    usuario_3 = nuevo_usuario
                    contraseña_3 = nueva_contraseña
                else:
                    print("No se pueden crear mas usuarios!")
        elif opcion == 3:
            print("Adios!")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Opcion no valida")