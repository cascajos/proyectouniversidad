from Solicitud import Solicitud
from Estudiante import Estudiante
from grados import Grado

class SistemaAdmision:
    def __init__(self):
        self.solicitudes = []
        self.grados = []
        self.estudiantes = []

    def procesar_admisiones(self):
        for solicitud in self.solicitudes:
            for grado, prioridad, nota in solicitud.preferencias:
                if grado.plazas > 0 and nota >= grado.nota_de_corte:
                    grado.matricular_alumno(solicitud.estudiante)
                    solicitud.grado_asignado = grado
                    solicitud.estado = "admitido"
                    break
                else:
                    solicitud.estado = "no admitido"

    def asignar_plazas(self):
        self.procesar_admisiones()

    def generar_ranking(self, grado):
        todos = list(grado.admitidos.items()) + list(grado.lista_espera.items())
        ranking = sorted(todos, key=lambda x: x[1], reverse=True)
        return ranking

    def generar_estadistica(self):
        total = len(self.solicitudes)
        admitidas = sum(1 for s in self.solicitudes if s.estado == "admitido")
        print(f"Solicitudes totales: {total}")
        print(f"Solicitudes admitidas: {admitidas}")
        if total > 0:
            print(f"Tasa de éxito: {admitidas/total*100:.2f}%")
        else:
            print("No hay solicitudes.")

    def simular_escenarios(self):
        print("Simulación de escenarios no implementada aún.")