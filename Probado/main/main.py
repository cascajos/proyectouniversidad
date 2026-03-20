# main.py (versión actualizada para pedir opcionales)

from Estudiante import Estudiante
from metodosuniversidadfinal import LISTA_UNIVERSIDADES, añadir_grado, buscar_grado

def menu_principal():
    print("\n" + "="*40)
    print("   SISTEMA DE ACCESO UNIVERSITARIO")
    print("="*40)
    print("1. Calcular nota de acceso")
    print("2. Buscar grados disponibles")
    print("3. Salir")
    print("="*40)

def calcular_nota():
    print("\n=== CÁLCULO DE NOTA DE ACCESO ===")
    nombre = input("Nombre: ")
    DNI = input("DNI: ")
    nota_bachillerato = float(input("Nota media de Bachillerato: "))
    
    # Fase obligatoria (4 asignaturas)
    print("\n--- FASE OBLIGATORIA ---")
    print("Introduce las notas de las 4 asignaturas obligatorias:")
    notas_evau = {}
    for i in range(4):
        asignatura = input(f"Asignatura {i+1}: ")
        nota = float(input(f"Nota de {asignatura}: "))
        notas_evau[asignatura] = nota
    
    # Fase opcional (2 asignaturas)
    print("\n--- FASE OPCIONAL ---")
    print("Introduce las notas de 2 asignaturas opcionales (ponderan 0.2 cada una):")
    for i in range(2):
        asignatura = input(f"Asignatura opcional {i+1}: ")
        nota = float(input(f"Nota de {asignatura}: "))
        notas_evau[asignatura] = nota
    
    estudiante = Estudiante(nombre, DNI, nota_bachillerato, notas_evau, 0)
    estudiante.calcular_nota_acceso()
    estudiante.mostrar_perfil(estudiante.nota_acceso)

def buscar_grados():
    print("\n=== BÚSQUEDA DE GRADOS ===")
    grado = añadir_grado()
    buscar_grado(LISTA_UNIVERSIDADES, grado)

# Programa principal
while True:
    menu_principal()
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "1":
        calcular_nota()
    elif opcion == "2":
        buscar_grados()
    elif opcion == "3":
        print("\n¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Intenta de nuevo.")