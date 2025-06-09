lista_de_usuario = []
lista_de_contrasena = []
while True:
    print("-----------------------")
    print("1.- Inicio sesión")
    print("2.- Registro usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    opcion = int(input("Seleccione una opcion \n -"))
    
    if opcion == 4:
        print("Saliendo...")
        break
    elif opcion == 1:
        usuario = input("Ingrese su usuario\n -")
        contrasena = input("Ingrese su contraseña \n -")
        if usuario in lista_de_usuario:
            posicion = lista_de_usuario.index(usuario)
            contrasena_registro = lista_de_contrasena[posicion]
            print(contrasena_registro)
            if contrasena == contrasena_registro:
                print("Inicio de sesion correcto")
            else:
                print("Contraseña incorrecta")
        else:
            print("El usuario que ingreso no existe!")
    elif opcion == 2:
        usuario = input("Ingrese nombre de usuario \n -")
        if usuario in lista_de_usuario:
            print("El usuario ya existe")
            continue
        contrasena = input("Ingrese contraseña de usuario \n -")
        lista_de_usuario.append(usuario)
        lista_de_contrasena.append(contrasena)
        print("Usuario creado con exito!")
    elif opcion == 3:
        usuario_para_eliminar = input("Ingrese el usuario que desea eliminar \n -")
        if usuario_para_eliminar in lista_de_usuario:
            posicion = lista_de_usuario.index(usuario_para_eliminar)
            contrasena_para_eliminar = lista_de_contrasena[posicion]
            lista_de_usuario.remove(usuario_para_eliminar)
            lista_de_contrasena.remove(contrasena_para_eliminar)
        else:
            print("El usuario que ingreso no existe")
    else:
        print("La opcion que ingreso no es valida")
