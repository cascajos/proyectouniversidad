class Solicitud:
    def __init__(self,estudiante,fase="ordinaria", estado="pendiente",grado_asignado=None):
        self.estudiante = estudiante
        self.preferencias=[]
        self.fase= fase
        self.estado = estado
        self.grado_asignado = grado_asignado
    
    def agregar_preferencia(self,grado,prioridad):
        nota_admision=grado.calcular_nota_admision(self.estudiante)#Esta parte puede dar problemas, necesita la clase Grado y la clase Estudiante*
        lista=[grado,prioridad,nota_admision]
        self.preferencias.append(lista)

    def ordenar_preferencias(self):
        self.preferencias.sort(key=lambda x:x[2])#Chat GPT (esto basicamente ordena las preferencias)
        print("--------Preferencias por orden--------")
        for i in range(0,len(self.preferencias)):#imprime las preferencias por orden
            print(f"Prioridad: {self.preferencias[i][1]}, Grado: {(self.preferencias[i][0]).nombre}, Nota de admisión: {self.preferencias[i][2]}")
    
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
                simbolo = "~~~"
            else:
                probabilidad = "BAJA (<20%)"
                simbolo = "✗✗✗"
            
            print(f"\n{prioridad}. {grado.nombre} - {grado.universidad}")
            print(f"   Tu nota: {nota:.2f} | Nota corte: {grado.nota_corte:.2f}")
            print(f"   Probabilidad: {probabilidad} {simbolo}")

    def mostrar_resumen(self): #este es el metodo para mostrar el resumen de la solicitud
        print("\n" + "=" * 60)
        print(f"Datos aportados a la administración y situación de solicitud:")
        print("=" * 60)
        print(f"Estudiante: {self.estudiante.nombre}")
        print(f"DNI: {self.estudiante.DNI}")
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