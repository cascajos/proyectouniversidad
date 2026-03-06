def calcular_probabilidades(self): #este es el método para calcular la probabilidad de entrada a grado de preferencia
    print("\n" + "=" * 60)
    print("ANÁLISIS DE PROBABILIDADES")
    print("=" * 60)
    
    for grado, prioridad, nota in self.preferencias:
        if nota > grado.nota_corte + 0.5:
            probabilidad = "ALTA (>80%)"
            simbolo = "✓✓✓"
        elif nota > grado.nota_corte:
            probabilidad = "MEDIA (40-80%)"
            simbolo = "~~"
        else:
            probabilidad = "BAJA (<20%)"
            simbolo = "✗✗✗"
        
        print(f"\n{prioridad}. {grado.nombre} - {grado.universidad}")
        print(f"   Tu nota: {nota:.2f} | Nota corte: {grado.nota_corte:.2f}")
        print(f"   Probabilidad: {probabilidad} {simbolo}")