cuentas={}       #:P

def validar_sexo(sexo):
    if sexo.upper() not in ["M", "F"]:
        print("Debe ingresar M o F solamente. Intente de nuevo.")
        return False
    return True



def ingresar_usuario():
    while True:
        usuario=input("Ingrese nombre de usuario: ")
        if usuario in cuentas:
            print("Usuario ya existe. Intente otro.")
            continue
        else:
            while True:
                sexo=input("Ingrese sexo: ")
                if validar_sexo(sexo):
                    break
            while True:
                contraseña=input("Ingresa contraseña: ").strip()
                if len(contraseña)!=8:
                    print("Contraseña no válida. Intente otra.")
                    continue
                else:
                    cuentas[usuario]={"usuario":usuario,"sexo":sexo,"contraseña":contraseña}
                print("Usuario registrado con exito!!")
                return False



def buscar_usuario():
    usuario=input("Ingrese usuario a buscar: ")
    if usuario in cuentas:
        datos=cuentas[usuario]
        print(f"El sexo del usuario es {datos['sexo']} y la contraseña es: {datos['contraseña']}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario():
    usuario=input("Ingrese usuario a buscar: ")
    if usuario in cuentas:
        del cuentas[usuario]
        print("Usuario eliminado con éxito!")
    else:
        print("No se pudo eliminar usuario.")



while True:
    print("""
MENÚ PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
""")
    opcion=input("Selecciona una opción: ")
    match opcion:
        case "1":
            ingresar_usuario()
        case "2":
            buscar_usuario()
        case "3":
            eliminar_usuario()
        case "4":
            print("Programa terminado...")
            break
        case _:
            print("Debe ingresar una opción válida!!")