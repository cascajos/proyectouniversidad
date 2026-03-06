class Equipo:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.jugadores = []
    
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print(f"{jugador.nombre} añadido al {self.nombre}")
    
    def mostrar_jugadores(self):
        for i, jugador in enumerate(self.jugadores, 1):
            print(f"  {i}. {jugador.nombre} ({jugador.edad} años, {jugador.posicion})")
    
    def informacion_equipo(self):
        print(f"\nEquipo: {self.nombre}")
        print(f"Ciudad: {self.ciudad}")
        print("Jugadores:")
        self.mostrar_jugadores()