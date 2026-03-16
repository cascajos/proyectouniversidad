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
def añadir_grado(Universidad):
    global Grado
    
    Grado = input("Introduce el grado que desees buscar, sin errores ortográficos: ").strip()
#Ponemos toda la información necesaria de las universidades en el main
def main():
    universidad1 = Universidad(
        nombre="UBU", ciudad="Burgos", tipo="Pública", grados=["Ingeniería Informática","Derecho","Medicina","Criminología","Farmacéutica","Ingeniería eléctrica",
            "Ingeniería robótica","Física","Matemáticas","Artes","Historia de España","Lengua Castellana","Filosofía"]
    )
    universidad2 = Universidad(
        nombre="UPM", ciudad="Madrid", tipo="Pública", grados=["Astronomía","Enfermería","Criminología","Derecho","Geología","Ingeniería Informática","Aviación",
            "Arquitectura","Historia de España","Filosofía","Medicina","Robótica"]
    )
    universidad3 =Universidad(
        nombre="EHU", ciudad="Bilbao", tipo="Pública", grados=["Derecho","Farmacia","Ingeniería Electrónica","Mecánica","Matemáticas","Arte","Biología",
        "Ingeniería Informática","Criminología","Economía"]
    )
    universidad4 = Universidad(
            nombre="UPSAL", ciudad="Salamanca", tipo="Privada", grados=["Física","Medicina","Ingeniería Informática","Matemáticas","Derecho","Robótica",
        "Geología","Filosofía","Criminología","Aviación"]   
        )
    universidad5 = Universidad(
        nombre="UHU", ciudad="Huelva", tipo="Pública", grados=["Ingeniería Mecánica","Farmacia","Biología","Lengua","Filosofía","Ingeniería Informática",
        "Química","Historia de España","Matemáticas","Artes","Psicología","Artes","Física"]
    )
def buscar_grado(Universidad):
    if Grado in Universidad.grados:
        if Grado_buscado in universidad1.grados:
            lista_universidad.append(universidad1.ciudad)
    elif Grado in universidad2.grados:
        lista_universidad.append(universidad2.ciudad)  
    elif Grado in universidad3.grados:
        lista_universidad.append(universidad3.ciudad)
    elif Grado in universidad4.grados:
        lista_universidad.append(universidad4.ciudad)
    elif Grado in universidad5.grados:
        print(f"Tu grado está disponible en la/s universidad/es de {lista_universidad}")
    else:
        print("lo sentimos, tu grado no está disponible en nuestras universidades")

    for uni in lista_universidades:
        if grado_buscado in uni.grados:
            ciudades_encontradas.append(uni.ciudad)
#Creamos una lista para almacenar las universidades
    lista_universidades =[universidad1, universidad2, universidad3, universidad4, universidad5]

#Mostramos todos los datos de las universidades  
    for uni in lista_universidades:
        print(uni.mostrar_ofertas())

    buscar_grado(lista_universidades)
    
    if __name__=="__main__":
        main()