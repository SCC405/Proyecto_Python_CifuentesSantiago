import datos


def reporte_carga_medicos():
    clinica = datos.cargar("clinica.json")
    diagnosticos = datos.cargar("prescripciones.json")

    medicos = []
    for i in range(len(clinica["usuarios"])):
        u = clinica["usuarios"][i]
        if u["rol"] == "medico":
            total = 0
            sintomas = 0
            medicamentos = 0
            pacientes = []

            for j in range(len(diagnosticos)):
                d = diagnosticos[j]
                if d["medico_email"] == u["email"]:
                    total = total + 1
                    sintomas = sintomas + len(d["sintomas"])
                    medicamentos = medicamentos + len(d["medicamentos"])
                    if d["paciente"] not in pacientes:
                        pacientes.append(d["paciente"])

            if total > 0:
                promedio_sintomas = round(sintomas / total, 1)
                promedio_medicamentos = round(medicamentos / total, 1)
            else:
                promedio_sintomas = 0
                promedio_medicamentos = 0

            medicos.append({
                "id_medico": u["identificacion"],
                "nombre_completo": u["nombres"] + " " + u["apellidos"],
                "total_diagnosticos": total,
                "pacientes_distintos": len(pacientes),
                "promedio_sintomas_por_consulta": promedio_sintomas,
                "promedio_medicamentos_por_consulta": promedio_medicamentos
            })

    if len(medicos) == 0:
        print("No hay medicos registrados")
        return

    for i in range(len(medicos)):
        for j in range(len(medicos) - 1 - i):
            if medicos[j]["total_diagnosticos"] < medicos[j + 1]["total_diagnosticos"]:
                temporal = medicos[j]
                medicos[j] = medicos[j + 1]
                medicos[j + 1] = temporal

    mas_pacientes = 0
    for i in range(len(medicos)):
        if medicos[i]["pacientes_distintos"] > medicos[mas_pacientes]["pacientes_distintos"]:
            mas_pacientes = i

    reporte = {
        "medicos": medicos,
        "resumen": {
            "mayor_numero_diagnosticos": medicos[0]["nombre_completo"],
            "mayor_numero_pacientes": medicos[mas_pacientes]["nombre_completo"],
            "menor_carga": medicos[len(medicos) - 1]["nombre_completo"]
        }
    }

    for i in range(len(medicos)):
        print(medicos[i]["nombre_completo"], "-> diagnosticos:", medicos[i]["total_diagnosticos"], "pacientes:", medicos[i]["pacientes_distintos"])
    print("Mayor numero de diagnosticos:", reporte["resumen"]["mayor_numero_diagnosticos"])
    print("Mayor numero de pacientes:", reporte["resumen"]["mayor_numero_pacientes"])
    print("Menor carga:", reporte["resumen"]["menor_carga"])

    datos.guardar("reporte_carga_medicos.json", reporte)
    print("Reporte guardado en reporte_carga_medicos.json")
