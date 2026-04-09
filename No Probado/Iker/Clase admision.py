class Solicitud:
    def __init__(self, estudiante, preferencias):
        """
        estudiante: objeto estudiante
        preferencias: lista de tuplas (grado, prioridad, nota)
        """
        self.estudiante = estudiante
        self.preferencias = preferencias
        self.grado_asignado = None
        self.estado = "pendiente"

    def __repr__(self):
        return f"Solicitud({self.estudiante.nombre}, estado={self.estado}, asignado={self.grado_asignado})"


def procesar_admisiones(self):
        for solicitud in self.solicitudes:
            for grado, prioridad, nota in solicitud.preferencias:
                if grado.esta_disponible():
                    grado.agregar_admitido(solicitud.estudiante)
                    solicitud.grado_asignado = grado.nombre
                    solicitud.estado = "asignada"
                    break
def asignar_plazas(self):
        self.procesar_admisiones()
def generar_ranking(self, grado):
        ranking = sorted(
            grado.admitidos + grado.lista_espera,
            key=lambda est: est.calcular_nota_admision(grado),
            reverse=True
        )
        return ranking
def generar_estadistica(self):
        total = len(self.solicitudes)
        asignadas = sum(1 for s in self.solicitudes if s.estado == "asignada")
        print(f"Solicitudes totales: {total}")
        print(f"Solicitudes asignadas: {asignadas}")
        if total > 0:
            print(f"Tasa de éxito: {asignadas/total*100:.2f}%")
        else:
            print("Tasa de éxito: No disponible (0 solicitudes)")
def simular_escenarios(self):
        print("Simulación de escenarios no implementada aún.")

