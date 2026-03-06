from equipo import Equipo
from jugador import Jugador
from partido import Partido

print("=" * 50)
print("CREACIÓN DE EQUIPOS")
print("=" * 50)

equipo1 = Equipo("Real Madrid", "Madrid")
print(f"Equipo creado: {equipo1.nombre} ({equipo1.ciudad})")

equipo2 = Equipo("Barcelona", "Barcelona")
print(f"Equipo creado: {equipo2.nombre} ({equipo2.ciudad})")

equipo3 = Equipo("Atlético de Madrid", "Madrid")
print(f"Equipo creado: {equipo3.nombre} ({equipo3.ciudad})")

equipo4 = Equipo("Sevilla", "Sevilla")
print(f"Equipo creado: {equipo4.nombre} ({equipo4.ciudad})")

print("\n" + "=" * 50)
print("CREACIÓN DE JUGADORES")
print("=" * 50)

jugador1 = Jugador("Thibaut Courtois", 31, "portero", "Real Madrid")
equipo1.agregar_jugador(jugador1)

jugador2 = Jugador("Vinicius Jr", 23, "delantero", "Real Madrid")
equipo1.agregar_jugador(jugador2)

jugador3 = Jugador("Jude Bellingham", 20, "medio", "Real Madrid")
equipo1.agregar_jugador(jugador3)

jugador4 = Jugador("Marc-André ter Stegen", 34, "portero", "Barcelona")
equipo2.agregar_jugador(jugador4)

jugador5 = Jugador("Robert Lewandowski", 35, "delantero", "Barcelona")
equipo2.agregar_jugador(jugador5)

jugador6 = Jugador("Pedri", 21, "medio", "Barcelona")
equipo2.agregar_jugador(jugador6)

jugador7 = Jugador("Jan Oblak", 36, "portero", "Atlético de Madrid")
equipo3.agregar_jugador(jugador7)

jugador8 = Jugador("Antoine Griezmann", 35, "delantero", "Atlético de Madrid")
equipo3.agregar_jugador(jugador8)

jugador9 = Jugador("Koke", 37, "medio", "Atlético de Madrid")
equipo3.agregar_jugador(jugador9)

jugador10 = Jugador("Yassine Bounou", 35, "portero", "Sevilla")
equipo4.agregar_jugador(jugador10)

jugador11 = Jugador("Youssef En-Nesyri", 29, "delantero", "Sevilla")
equipo4.agregar_jugador(jugador11)

jugador12 = Jugador("Ivan Rakitic", 36, "medio", "Sevilla")
equipo4.agregar_jugador(jugador12)

print("\n" + "=" * 50)
print("INFORMACIÓN DE EQUIPOS")
print("=" * 50)

equipo1.informacion_equipo()
equipo2.informacion_equipo()
equipo3.informacion_equipo()
equipo4.informacion_equipo()

print("\n" + "=" * 50)
print("SIMULACIÓN DE PARTIDOS")
print("=" * 50)

partido1 = Partido(equipo1, equipo2)
partido1.jugar_partido()
partido1.mostrar_resultado()

partido2 = Partido(equipo3, equipo4)
partido2.jugar_partido()
partido2.mostrar_resultado()

partido3 = Partido(equipo2, equipo3)
partido3.jugar_partido()
partido3.mostrar_resultado()


# La simulacion de partidos ya lo he tenido que hacer con IA casi todo que no era capaz
