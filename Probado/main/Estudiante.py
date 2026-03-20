class Estudiante:
    def __init__(self, nombre, DNI, nota_bachillerato, notas_evau, nota_acceso):
        self.nombre = nombre
        self.DNI = DNI
        self.nota_bachillerato = nota_bachillerato
        self.notas_evau = notas_evau
        self.nota_acceso = nota_acceso

    def calcular_nota_acceso(self):
        # Calcular media de las 4 obligatorias
        notas_obligatorias = dict(list(self.notas_evau.items())[0:4])
        suma_obligatorias = 0
        
        print("Notas fase obligatoria:")
        for asignatura, nota in notas_obligatorias.items():
            print(f"> {asignatura}: {nota}")
            suma_obligatorias += nota
        
        media_obligatorias = suma_obligatorias / 4
        
        # Calcular fase opcional (2 asignaturas)
        # Si hay más de 4 notas, las siguientes son las opcionales
        if len(self.notas_evau) > 4:
            notas_opcionales = dict(list(self.notas_evau.items())[4:6])
            suma_opcionales = 0
            
            print("\nNotas fase opcional (ponderan 0.2 cada una):")
            for asignatura, nota in notas_opcionales.items():
                print(f"> {asignatura}: {nota}")
                suma_opcionales += nota * 0.2  # Cada opcional suma hasta 2 puntos
            
            nota_fase_opcional = suma_opcionales
        else:
            nota_fase_opcional = 0
            print("\nNo se han introducido asignaturas opcionales.")
        
        # Nota de acceso: 60% bachillerato + 40% media obligatorias + opcionales (máximo 14)
        self.nota_acceso = (self.nota_bachillerato * 0.6) + (media_obligatorias * 0.4) + nota_fase_opcional
        
        # Limitar a 14 puntos máximo
        if self.nota_acceso > 14:
            self.nota_acceso = 14
        
        print(f"\nTu nota de acceso a la universidad es: {self.nota_acceso:.2f} / 14")
        return self.nota_acceso

    def mostrar_perfil(self, nota_acceso):
        print("\n------ PERFIL DEL ESTUDIANTE ------")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.DNI}")
        print("\nNotas EBAU:")
        for asignatura, notas in self.notas_evau.items():
            print(f"  - {asignatura}: {notas}")
        print(f"\nNota Bachillerato: {self.nota_bachillerato}")
        print(f"Nota de acceso: {nota_acceso:.2f} / 14")