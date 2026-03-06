class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
        print(f"Jugador creado: {self.nombre} - {self.equipo}")
    
    def mostrar_info(self):
        print(f"{self.nombre} ({self.edad} años, {self.posicion})")