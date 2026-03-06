def mostrar_resumen(self): #este es el metodo para mostrar el resumen de la solicitud
    print("\n" + "=" * 60)
    print(f"Datos aportados a la administración y situación de solicitud:")
    print("=" * 60)
    print(f"Estudiante: {self.estudiante.nombre}")
    print(f"DNI: {self.estudiante.dni}")
    print(f"Nota de acceso: {self.estudiante.nota_acceso:.2f}")
    print(f"Estado: {self.estado}")
    print("\nPreferencias:")
    print("-" * 60)
    
    for i, (grado, prioridad, nota) in enumerate(self.preferencias, 1):
        estado = "✓ ADMITIDO" if grado == self.grado_asignado else "⏳ Pendiente"
        print(f"{i}. {grado.nombre} ({grado.universidad})")
        print(f"   Prioridad: {prioridad} | Nota: {nota:.2f}")
        print(f"   {estado}")
    
    if self.grado_asignado:
        print("-" * 60)
        print(f"Admisión aprobada en: {self.grado_asignado.nombre}")
    
    print("=" * 60)