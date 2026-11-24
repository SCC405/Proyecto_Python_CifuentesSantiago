

import datos


def historia_clinica():
    print("--- HISTORIA CLINICA ---")
    identificacion = input("Numero de identificacion del paciente: ")

    clinica = datos.cargar("clinica.json")
    lista_pacientes = clinica["pacientes"]
    encontrado = False

    for i in range(len(lista_pacientes)):
        if lista_pacientes[i]["identificacion"] == identificacion:
            encontrado = True
            paciente = lista_pacientes[i]
            print("========== DATOS DEL PACIENTE ==========")
            print("Identificacion:", paciente["identificacion"])
            print("Nombres:", paciente["nombres"])
            print("Apellidos:", paciente["apellidos"])
            print("Telefono:", paciente["telefono"])
            print("E-mail:", paciente["email"])
            print("Direccion:", paciente["direccion"])
            print("Genero:", paciente["genero"])
            print("Estado civil:", paciente["estado_civil"])

    if not encontrado:
        print("Error: el paciente no esta registrado")
    else:
        prescripciones = datos.cargar("prescripciones.json")
        consultas = 0

        for i in range(len(prescripciones)):
            if prescripciones[i]["paciente"] == identificacion:
                consultas = consultas + 1
                consulta = prescripciones[i]
                print("---------- Consulta", consultas, "----------")
                print("Fecha:", consulta["fecha"])
                print("Medico:", consulta["medico_nombres"], consulta["medico_apellidos"])

                print("Sintomas:")
                sintomas = consulta["sintomas"]
                for j in range(len(sintomas)):
                    print("  -", sintomas[j])

                print("Diagnostico:", consulta["diagnostico"])

                print("Medicamentos:")
                medicamentos = consulta["medicamentos"]
                for j in range(len(medicamentos)):
                    print("  -", medicamentos[j]["medicamento"])
                    print("    Cantidad:", medicamentos[j]["cantidad"])
                    print("    Dosis diaria:", medicamentos[j]["dosis"])
                    print("    Tiempo (dias):", medicamentos[j]["tiempo"])

        if consultas == 0:
            print("El paciente no tiene consultas registradas")
