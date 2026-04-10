from Estudiante import Estudiante
from metodosuniversidadfinal import LISTA_UNIVERSIDADES, añadir_grado, buscar_grado
from grados import LISTA_GRADOS
from Solicitud import Solicitud
from claseadmisionfinal import SistemaAdmision

sistema = SistemaAdmision()
sistema.grados = LISTA_GRADOS

def registrar_estudiante():
    print("\n--- REGISTRO DE ESTUDIANTE ---")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    nota_bach = float(input("Nota media de Bachillerato: "))

    print("\nIntroduce las notas de las asignaturas TRONCALES (0-10):")
    troncales = ["Lengua", "Historia/Filosofia", "Ingles", "Matematicas"]
    notas = {}
    for asig in troncales:
        nota = float(input(f"{asig}: "))
        notas[asig] = nota

    print("\nAsignaturas OPCIONALES (hasta 2, puedes dejar vacío):")
    opciones = ["Fisica", "Quimica", "Biologia", "Dibujo Técnico", "Economía", "Matematicas CCSS", "Tecnología"]
    for i in range(2):
        asig = input(f"Opción {i+1} (de {opciones} o Enter para saltar): ").strip()
        if asig == "":
            break
        if asig in opciones:
            nota = float(input(f"Nota en {asig}: "))
            notas[asig] = nota
        else:
            print("Asignatura no reconocida, se omite.")

    estudiante = Estudiante(nombre, dni, nota_bach, notas, 0)
    estudiante.calcular_nota_acceso()
    sistema.estudiantes.append(estudiante)
    print("Estudiante registrado.")
    return estudiante

def crear_solicitud():
    if not sistema.estudiantes:
        print("Primero registra al estudiante.")
        return
    dni = input("DNI del estudiante: ")
    estudiante = next((e for e in sistema.estudiantes if e.DNI == dni), None)
    if not estudiante:
        print("No encontrado.")
        return

    solicitud = Solicitud(estudiante)
    print("\nGrados disponibles:")
    for i, grado in enumerate(LISTA_GRADOS):
        print(f"{i+1}. {grado.nombre} - {grado.universidad.nombre} (Corte: {grado.nota_de_corte})")

    while True:
        op = input("Número del grado a añadir (0 para terminar): ")
        if op == "0":
            break
        try:
            idx = int(op) - 1
            if 0 <= idx < len(LISTA_GRADOS):
                grado = LISTA_GRADOS[idx]
                prioridad = len(solicitud.preferencias) + 1
                solicitud.agregar_preferencia(grado, prioridad)
                print(f"Añadido: {grado.nombre} (prioridad {prioridad})")
            else:
                print("Número inválido.")
        except ValueError:
            print("Introduce un número.")

    if solicitud.preferencias:
        sistema.solicitudes.append(solicitud)
        solicitud.calcular_probabilidades()
        solicitud.mostrar_resumen()
    else:
        print("No se añadió ninguna preferencia.")

def procesar_admision():
    if not sistema.solicitudes:
        print("No hay solicitudes.")
        return
    sistema.procesar_admisiones()
    print("Admisión procesada.")
    for s in sistema.solicitudes:
        if s.grado_asignado:
            print(f"{s.estudiante.nombre} admitido en {s.grado_asignado.nombre}")
        else:
            print(f"{s.estudiante.nombre} no admitido.")

def mostrar_estadisticas():
    sistema.generar_estadistica()

def menu():
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE ACCESO UNIVERSITARIO")
        print("1. Registrar estudiante")
        print("2. Buscar grados (por nombre)")
        print("3. Crear solicitud")
        print("4. Procesar admisión")
        print("5. Ver estadísticas")
        print("6. Salir")
        op = input("Elige: ")

        if op == "1":
            registrar_estudiante()
        elif op == "2":
            grado = añadir_grado()
            buscar_grado(LISTA_UNIVERSIDADES, grado)
        elif op == "3":
            crear_solicitud()
        elif op == "4":
            procesar_admision()
        elif op == "5":
            mostrar_estadisticas()
        elif op == "6":
            print("Adiós")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()