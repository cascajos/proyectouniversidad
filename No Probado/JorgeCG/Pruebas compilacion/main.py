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


class Universidad:
    def __init__(self, nombre, ciudad, tipo, grados):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tipo = tipo
        self.grados = grados

    def mostrar_ofertas(self):
        grados_formateados = ", ".join(self.grados)
        return f"Universidad: {self.nombre} ({self.tipo}) - Ciudad: {self.ciudad}\nGrados: {grados_formateados}\n"

def añadir_grado():
    return input("Introduce el grado que desees buscar, sin errores ortográficos: ").strip()

def buscar_grado(lista_universidades, grado_buscado):
    ciudades_encontradas = []

    for uni in lista_universidades:
        if grado_buscado in uni.grados:
            ciudades_encontradas.append(uni.ciudad)

    if ciudades_encontradas:
        print(f"Tu grado ({grado_buscado}) está disponible en: {', '.join(ciudades_encontradas)}")
    else:
        print(f"Lo sentimos, el grado '{grado_buscado}' no está disponible en nuestras universidades.")

# ========== DATOS EXPORTADOS ==========
universidad1 = Universidad("UBU", "Burgos", "Pública", ["Ingeniería Informática","Derecho","Medicina","Criminología","Farmacéutica","Ingeniería eléctrica", "Ingeniería robótica","Física","Matemáticas","Artes","Historia de España","Lengua Castellana","Filosofía"])
universidad2 = Universidad("UPM", "Madrid", "Pública", ["Astronomía","Enfermería","Criminología","Derecho","Geología","Ingeniería Informática","Aviación", "Arquitectura","Historia de España","Filosofía","Medicina","Robótica"])
universidad3 = Universidad("EHU", "Bilbao", "Pública", ["Derecho","Farmacia","Ingeniería Electrónica","Mecánica","Matemáticas","Arte","Biología", "Ingeniería Informática","Criminología","Economía"])
universidad4 = Universidad("UPSAL", "Salamanca", "Privada", ["Física","Medicina","Ingeniería Informática","Matemáticas","Derecho","Robótica", "Geología","Filosofía","Criminología","Aviación"])
universidad5 = Universidad("UHU", "Huelva", "Pública", ["Ingeniería Mecánica","Farmacia","Biología","Lengua","Filosofía","Ingeniería Informática", "Química","Historia de España","Matemáticas","Artes","Psicología","Física"])

LISTA_UNIVERSIDADES = [universidad1, universidad2, universidad3, universidad4, universidad5]

def main():
    for uni in LISTA_UNIVERSIDADES:
        print(uni.mostrar_ofertas())
    grado = añadir_grado()
    buscar_grado(LISTA_UNIVERSIDADES, grado)

if __name__ == "__main__":
    main()




def menu_principal():
    print("\n" + "="*40)
    print("   SISTEMA DE ACCESO UNIVERSITARIO")
    print("="*40)
    print("1. Calcular nota de acceso")
    print("2. Buscar grados disponibles")
    print("3. Salir")
    print("="*40)

def calcular_nota():
    print("\n=== CÁLCULO DE NOTA DE ACCESO ===")
    nombre = input("Nombre: ")
    DNI = input("DNI: ")
    nota_bachillerato = float(input("Nota media de Bachillerato: "))
    
    # Fase obligatoria (4 asignaturas)
    print("\n--- FASE OBLIGATORIA ---")
    print("Introduce las notas de las 4 asignaturas obligatorias:")
    notas_evau = {}
    for i in range(4):
        asignatura = input(f"Asignatura {i+1}: ")
        nota = float(input(f"Nota de {asignatura}: "))
        notas_evau[asignatura] = nota
    
    # Fase opcional (2 asignaturas)
    print("\n--- FASE OPCIONAL ---")
    print("Introduce las notas de 2 asignaturas opcionales (ponderan 0.2 cada una):")
    for i in range(2):
        asignatura = input(f"Asignatura opcional {i+1}: ")
        nota = float(input(f"Nota de {asignatura}: "))
        notas_evau[asignatura] = nota
    
    estudiante = Estudiante(nombre, DNI, nota_bachillerato, notas_evau, 0)
    estudiante.calcular_nota_acceso()
    estudiante.mostrar_perfil(estudiante.nota_acceso)

def buscar_grados():
    print("\n=== BÚSQUEDA DE GRADOS ===")
    grado = añadir_grado()
    buscar_grado(LISTA_UNIVERSIDADES, grado)

# Programa principal
while True:
    menu_principal()
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "1":
        calcular_nota()
    elif opcion == "2":
        buscar_grados()
    elif opcion == "3":
        print("\n¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Intenta de nuevo.")



