

import datos


def existe_paciente(identificacion):
    clinica = datos.cargar("clinica.json")
    lista = clinica["pacientes"]
    for i in range(len(lista)):
        if lista[i]["identificacion"] == identificacion:
            return True
    return False


def registrar_paciente():
    print("--- REGISTRO DE PACIENTE ---")
    identificacion = input("Numero de identificacion: ")

    if existe_paciente(identificacion):
        print("Error: ya existe un paciente con esa identificacion")
    else:
        nombres = input("Nombres: ")
        apellidos = input("Apellidos: ")
        telefono = input("Numero de telefono: ")
        email = input("E-mail: ")
        direccion = input("Direccion: ")
        genero = input("Genero: ")
        estado_civil = input("Estado civil: ")

        paciente = {
            "identificacion": identificacion,
            "nombres": nombres,
            "apellidos": apellidos,
            "telefono": telefono,
            "email": email,
            "direccion": direccion,
            "genero": genero,
            "estado_civil": estado_civil
        }

        #Se carga el JSON, se agrega el paciente y se guarda otra vez
        clinica = datos.cargar("clinica.json")
        clinica["pacientes"].append(paciente)
        datos.guardar("clinica.json", clinica)
        print("Paciente registrado con exito")
