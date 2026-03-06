import random

class Partido:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = 0
        self.goles_visitante = 0
        self.finalizado = False
    
    def jugar_partido(self):
        self.goles_local = random.randint(0, 5)
        self.goles_visitante = random.randint(0, 5)
        self.finalizado = True
    
    def mostrar_resultado(self):
        print(f"\nPartido: {self.equipo_local.nombre} vs {self.equipo_visitante.nombre}")
        print(f"Resultado: {self.equipo_local.nombre} {self.goles_local} - {self.goles_visitante} {self.equipo_visitante.nombre}")
        print(f"Ganador: {self.obtener_ganador()}")
    
    def obtener_ganador(self):
        if self.goles_local > self.goles_visitante:
            return self.equipo_local.nombre
        elif self.goles_visitante > self.goles_local:
            return self.equipo_visitante.nombre
        else:
            return "Empate"