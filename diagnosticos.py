#Modulo de diagnosticos

import datos
import pacientes


def diagnosticar(email_medico):
    print("--- DIAGNOSTICO DE PACIENTE ---")
    identificacion = input("Numero de identificacion del paciente: ")

    if not pacientes.existe_paciente(identificacion):
        print("Error: el paciente no esta registrado")
    else:
        fecha = input("Fecha de la consulta (DD/MM/AAAA): ")

        sintomas = []
        print("Registre los sintomas del paciente")
        while True:
            sintoma = input("Sintoma: ")
            sintomas.append(sintoma)
            respuesta = input("¿Desea agregar otro sintoma? (s/n): ")
            if respuesta == "n" or respuesta == "N":
                break

        diagnostico = input("Diagnostico: ")

        medicamentos = []
        total_medicamentos = int(input("Cuantos medicamentos va a prescribir: "))
        contador = 0
        while contador < total_medicamentos:
            print("Medicamento", contador + 1)
            nombre = input("Nombre del medicamento: ")
            cantidad = int(input("Cantidad: "))
            dosis = input("Dosis diaria: ")
            tiempo = int(input("Tiempo de aplicacion (dias): "))

            medicamento = {
                "medicamento": nombre,
                "cantidad": cantidad,
                "dosis": dosis,
                "tiempo": tiempo
            }
            medicamentos.append(medicamento)
            contador = contador + 1

        clinica = datos.cargar("clinica.json")
        usuarios = clinica["usuarios"]
        nombres_medico = ""
        apellidos_medico = ""
        for i in range(len(usuarios)):
            if usuarios[i]["email"] == email_medico:
                nombres_medico = usuarios[i]["nombres"]
                apellidos_medico = usuarios[i]["apellidos"]

        prescripcion = {
            "fecha": fecha,
            "paciente": identificacion,
            "medico_email": email_medico,
            "medico_nombres": nombres_medico,
            "medico_apellidos": apellidos_medico,
            "sintomas": sintomas,
            "diagnostico": diagnostico,
            "medicamentos": medicamentos
        }

        lista = datos.cargar("prescripciones.json")
        lista.append(prescripcion)
        datos.guardar("prescripciones.json", lista)
        print("Diagnostico y prescripcion guardados con exito")
