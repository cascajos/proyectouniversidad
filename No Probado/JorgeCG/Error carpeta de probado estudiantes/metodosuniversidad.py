class Universidad:
    def __init__(self, nombre, ciudad, tipo, grados):
        self.nombre = nombre
        self.ciudad=ciudad
        self.tipo=tipo
        self.grados=grados
    
#Mostramos cómo se estructurarán los datos almacenados de las universidades
def mostrar_ofertas(self):
    grados_formateados= ", ".join(self.grados)
    return f"Universidad: {self.nombre} ({self.tipo}) - Ciudad: {self.ciudad}\nGrados: {grados_formateados}\n"

def buscar_grado(lista_universidades):
    grado_buscado = input("Introduce el grado que desees buscar: ").strip()
    ciudades_encontradas = []
    for uni in lista_universidades:
        # Normalizamos a minúsculas para facilitar la búsqueda
        if grado_buscado.lower() in [g.lower() for g in uni.grados]:
            ciudades_encontradas.append(uni.ciudad)

        if ciudades_encontradas:
            print(f"\nTu grado está disponible en: {', '.join(ciudades_encontradas)}")
        else:
            print("\nLo sentimos, tu grado no está disponible en nuestras universidades.")
def main():
    #Añadimos la lista con todas las universidades disponibles
    lista_universidades= []
    Universidad(nombre="UBU", ciudad="Burgos", tipo="Pública", grados=["Ingeniería Informática","Derecho","Medicina","Criminología","Farmacéutica","Ingeniería eléctrica","Ingeniería robótica","Física","Matemáticas","Artes","Historia de España","Lengua Castellana","Filosofía"])
    Universidad(nombre="UPM", ciudad="Madrid", tipo="Pública", grados=["Astronomía","Enfermería","Criminología","Derecho","Geología","Ingeniería Informática","Aviación","Arquitectura","Historia de España","Filosofía","Medicina","Robótica"])
    Universidad(nombre="EHU", ciudad="Bilbao", tipo="Pública", grados=["Derecho","Farmacia","Ingeniería Electrónica","Mecánica","Matemáticas","Arte","Biología","Ingeniería Informática","Criminología","Economía"])
    Universidad(nombre="UPSAL", ciudad="Salamanca", tipo="Privada", grados=["Física","Medicina","Ingeniería Informática","Matemáticas","Derecho","Robótica","Geología","Filosofía","Criminología","Aviación"])
    Universidad(nombre="UHU", ciudad="Huelva", tipo="Pública", grados=["Ingeniería Mecánica","Farmacia","Biología","Lengua","Filosofía","Ingeniería Informática","Química","Historia de España","Matemáticas","Artes","Psicología","Artes","Física"])
    #Ahora se mostrarán todas las ofertas que el estudiante quiera
    for uni in lista_universidades:
        print(uni.mostrar_ofertas())

    buscar_grado(lista_universidades)
    #Se acaba el programa
    if __name__=="__main__":
        main()
