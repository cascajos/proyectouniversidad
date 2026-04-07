import random

# Clase Grado


class Grado:

    def __init__(self, nombre, universidad, plazas, nota_de_corte, rama):

        self.nombre = nombre
        self.universidad = universidad  
        self.rama = rama
        self.plazas = plazas
        self.nota_de_corte = nota_de_corte
        self.ponderaciones = {}  
        self.admitidos = []      
        self.lista_espera = []  

    def definir_ponderacion(self, asignatura, peso):

        self.ponderaciones[asignatura] = peso
        print(f"Ponderación guardada: {asignatura} vale x{peso} en {self.nombre}.")

    def calcular_nota_admision(self, nota_base, notas_especificas):
        nota_final = nota_base
        for asignatura, nota in notas_especificas.items():
            if asignatura in self.ponderaciones:
                nota_final += nota * self.ponderaciones[asignatura]
        return round(min(nota_final, 14.0), 2)

    def actualizar_nota_corte(self, demanda_alta):
        if demanda_alta:
            subida = random.uniform(0.1, 0.5)
            self.nota_de_corte = min(14.0, self.nota_de_corte + subida)
            print(f"La demanda ha subido la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")
        else:
            bajada = random.uniform(0.1, 0.5)
            self.nota_de_corte = max(5.0, self.nota_de_corte - bajada)
            print(f"La demanda ha bajado la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")



    def matricular_alumno(self, estudiante):
        if self.plazas > 0:
            self.plazas -= 1
            self.admitidos.append(estudiante)
            print(f"{estudiante.nombre} matriculado/a con éxito en {self.nombre}. Plazas restantes: {self.plazas}")
        else:
            print(f"Lo siento, no quedan plazas en {self.nombre}.")
            self.lista_espera.append(estudiante)