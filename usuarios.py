#Modulo de usuarios

import datos


def login(email, contrasena):
    clinica = datos.cargar("clinica.json")
    lista = clinica["usuarios"]
    for i in range(len(lista)):
        if lista[i]["email"] == email and lista[i]["contrasena"] == contrasena:
            return True
    return False


def existe_usuario(email):
    clinica = datos.cargar("clinica.json")
    lista = clinica["usuarios"]
    for i in range(len(lista)):
        if lista[i]["email"] == email:
            return True
    return False


def registrar_usuario():
    print("--- REGISTRO DE USUARIO ---")
    identificacion = input("Numero de identificacion: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Numero de telefono: ")
    direccion = input("Direccion: ")
    email = input("E-mail corporativo: ")

    if "@acmeclinic.com" not in email:
        print("Error: el e-mail debe ser corporativo (@acmeclinic.com)")
    elif existe_usuario(email):
        print("Error: ya existe un usuario con ese e-mail")
    else:
        contrasena = input("Asigne una contraseña: ")

        usuario = {
            "identificacion": identificacion,
            "nombres": nombres,
            "apellidos": apellidos,
            "telefono": telefono,
            "email": email,
            "direccion": direccion,
            "contrasena": contrasena
        }

        clinica = datos.cargar("clinica.json")
        clinica["usuarios"].append(usuario)
        datos.guardar("clinica.json", clinica)
        print("Usuario registrado con exito")
