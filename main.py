

import usuarios
import pacientes
import diagnosticos
import historia
import reportes

print("===== CLINICA ACME =====")

while True:
    email = input("Usuario (e-mail): ")
    contrasena = input("Contraseña: ")

    if usuarios.login(email, contrasena):
        break
    elif usuarios.existe_usuario(email):
        print("Contraseña incorrecta, intente de nuevo")
    else:
        print("El usuario no existe, intente de nuevo")

print("Bienvenido al sistema")

while True:

    print("""
    1. Registrar usuario
    2. Registrar paciente
    3. Diagnosticar paciente
    4. Historia clinica
    5. Reporte de carga de medicos
    6. Salir
    """)

    try:
        opcion = int(input("Digite una opcion: "))
    except ValueError:
        opcion = 0

    if opcion == 1:
        usuarios.registrar_usuario()
    elif opcion == 2:
        pacientes.registrar_paciente()
    elif opcion == 3:
        diagnosticos.diagnosticar(email)
    elif opcion == 4:
        historia.historia_clinica()
    elif opcion == 5:
        reportes.reporte_carga_medicos()
    elif opcion == 6:
        break
    else:
        print("Error digite de nuevo")

print("Gracias por usar el sistema")
