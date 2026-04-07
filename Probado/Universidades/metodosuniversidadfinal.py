class Universidad:
    def __init__(self, nombre, ciudad, tipo, grados):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tipo = tipo
        self.grados = grados

# Este método debe estar indentado dentro de la clase
    def mostrar_ofertas(self):
        grados_formateados = ", ".join(self.grados)
        return f"Universidad: {self.nombre} ({self.tipo}) - Ciudad: {self.ciudad}\nGrados: {grados_formateados}\n"

def añadir_grado():
# Pedimos el grado al usuario y lo devolvemos
    return input("Introduce el grado que desees buscar, sin errores ortográficos: ").strip()

def buscar_grado(lista_universidades, grado_buscado):
    ciudades_encontradas = []

    for uni in lista_universidades:
        if grado_buscado in uni.grados:
            ciudades_encontradas.append(f"{uni.nombre} ({uni.ciudad})")
    if ciudades_encontradas:
            print(f"Tu grado ({grado_buscado}) está disponible en: {', '.join(ciudades_encontradas)}")
    else:
            print(f"Lo sentimos, el grado '{grado_buscado}' no está disponible en nuestras universidades.")
def main():
    universidad1 = Universidad("UBU", "Burgos", "Pública", ["Ingeniería Informática","Derecho","Medicina","Criminología","Farmacéutica","Ingeniería eléctrica", "Ingeniería robótica","Física","Matemáticas","Artes","Historia de España","Lengua Castellana","Filosofía"])
    universidad2 = Universidad("UPM", "Madrid", "Pública", ["Astronomía","Enfermería","Criminología","Derecho","Geología","Ingeniería Informática","Aviación", "Arquitectura","Historia de España","Filosofía","Medicina","Robótica"])
    universidad3 = Universidad("UPV", "Bilbao", "Pública", ["Derecho","Farmacia","Ingeniería Electrónica","Mecánica","Matemáticas","Arte","Biología", "Ingeniería Informática","Criminología","Economía"])
    universidad4 = Universidad("USAL", "Salamanca", "Pública", ["Física","Medicina","Ingeniería Informática","Matemáticas","Derecho","Robótica", "Geología","Filosofía","Criminología","Aviación"])
    universidad5 = Universidad("UHU", "Huelva", "Pública", ["Ingeniería Mecánica","Farmacia","Biología","Lengua","Filosofía","Ingeniería Informática", "Química","Historia de España","Matemáticas","Artes","Psicología","Física"])

    lista_universidades = [universidad1, universidad2, universidad3, universidad4, universidad5]

# Mostramos todos los datos
    for uni in lista_universidades:
        print(uni.mostrar_ofertas())

# Ejecutamos la búsqueda
    grado = añadir_grado()
    buscar_grado(lista_universidades, grado)

if __name__ == "__main__":
    main()