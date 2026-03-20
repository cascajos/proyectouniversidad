# main.py

from Estudiante import Estudiante
from metodosuniversidadfinal import Universidad, añadir_grado, buscar_grado

# ========== INPUTS PARA ESTUDIANTE ==========
print("=== REGISTRO DE ESTUDIANTE ===")
nombre = input("Nombre: ")
DNI = input("DNI: ")
nota_bachillerato = float(input("Nota media de Bachillerato: "))

print("\nIntroduce las notas de las 4 asignaturas obligatorias de la EVAU:")
notas_evau = {}
for i in range(4):
    asignatura = input(f"Asignatura {i+1}: ")
    nota = float(input(f"Nota de {asignatura}: "))
    notas_evau[asignatura] = nota

# Crear estudiante y calcular nota de acceso
estudiante = Estudiante(nombre, DNI, nota_bachillerato, notas_evau, 0)
estudiante.calcular_nota_acceso()
estudiante.mostrar_perfil(estudiante.nota_acceso)

# ========== INPUTS PARA UNIVERSIDADES (las universidades ya están creadas en el otro archivo) ==========
print("\n=== BÚSQUEDA DE GRADOS ===")
grado = añadir_grado()

# Las universidades están en metodosuniversidadfinal, necesitas importarlas o crearlas aquí
# Si las universidades están en el otro archivo, tendrás que crearlas también aquí
# o modificar el otro archivo para exportar la lista.