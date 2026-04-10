class Solicitud:
    def __init__(self, estudiante, fase="ordinaria", estado="pendiente", grado_asignado=None):
        self.estudiante = estudiante
        self.preferencias = []
        self.fase = fase
        self.estado = estado
        self.grado_asignado = grado_asignado

    def agregar_preferencia(self, grado, prioridad):
        nota_admision = grado.calcular_nota_admision(self.estudiante)
        self.preferencias.append([grado, prioridad, nota_admision])

    def ordenar_preferencias(self):
        self.preferencias.sort(key=lambda x: x[1])  # por prioridad
        print("-------- Preferencias por orden --------")
        for grado, prioridad, nota in self.preferencias:
            print(f"Prioridad: {prioridad}, Grado: {grado.nombre}, Nota: {nota:.2f}")

    def calcular_probabilidades(self):
        print("\n" + "=" * 60)
        print("ANÁLISIS DE PROBABILIDADES")
        print("=" * 60)
        for grado, prioridad, nota in self.preferencias:
            if nota > grado.nota_de_corte + 0.5:
                prob = "ALTA (>80%)"
                simb = "✓✓✓"
            elif nota > grado.nota_de_corte:
                prob = "MEDIA (40-80%)"
                simb = "~~~"
            else:
                prob = "BAJA (<20%)"
                simb = "✗✗✗"
            print(f"\n{prioridad}. {grado.nombre} - {grado.universidad.nombre}")
            print(f"   Tu nota: {nota:.2f} | Corte: {grado.nota_de_corte:.2f}")
            print(f"   Probabilidad: {prob} {simb}")

    def mostrar_resumen(self):
        print("\n" + "=" * 60)
        print("RESUMEN DE SOLICITUD")
        print("=" * 60)
        print(f"Estudiante: {self.estudiante.nombre} ({self.estudiante.DNI})")
        print(f"Nota acceso: {self.estudiante.nota_acceso:.2f}")
        print(f"Estado: {self.estado}")
        print("\nPreferencias:")
        for i, (grado, prioridad, nota) in enumerate(self.preferencias, 1):
            asignado = "✓ ADMITIDO" if grado == self.grado_asignado else "⏳ Pendiente"
            print(f"{i}. {grado.nombre} ({grado.universidad.nombre}) - Prioridad {prioridad} - Nota {nota:.2f} {asignado}")
        if self.grado_asignado:
            print(f"\nAdmitido en: {self.grado_asignado.nombre}")
        print("=" * 60)