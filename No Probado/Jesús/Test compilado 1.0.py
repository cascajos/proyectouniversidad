import random

# ==========================================
# CLASE UNIVERSIDAD
# ==========================================
class Universidad:
    def __init__(self, nombre, ciudad, tipo):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tipo = tipo  # "Pública" o "Privada"
        self.grados = []  # Lista vacía que guardará objetos de la clase Grado 
        
    def agregar_grado(self, grado):
        self.grados.append(grado)
        
    def mostrar_oferta(self):
        print(f"\n--- Oferta académica de {self.nombre} ({self.ciudad}) ---")
        for grado in self.grados:
            print(f"- {grado.nombre} (Plazas: {grado.plazas}, Corte: {grado.nota_de_corte})")

    def __str__(self):
        return f"{self.nombre} ({self.ciudad} - {self.tipo})" 

# ==========================================
# CLASE GRADO
# ==========================================
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
        print(f"✅ Ponderación guardada: {asignatura} vale x{peso} en {self.nombre}.")

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
            print(f"📈 La demanda ha subido la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")
        else:
            bajada = random.uniform(0.1, 0.5)
            self.nota_de_corte = max(5.0, self.nota_de_corte - bajada)
            print(f"📉 La demanda ha bajado la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")

    def matricular_alumno(self, estudiante):
        if self.plazas > 0:
            self.plazas -= 1
            self.admitidos.append(estudiante)
            print(f"🎉 {estudiante.nombre} matriculado/a con éxito en {self.nombre}. Plazas restantes: {self.plazas}")
        else:
            print(f"❌ Lo siento, no quedan plazas en {self.nombre}.")
            self.lista_espera.append(estudiante)

# ==========================================
# CLASE ESTUDIANTE
# ==========================================
class Estudiante:
    def __init__(self, nombre, DNI, nota_bachillerato, notas_evau):
        self.nombre = nombre
        self.DNI = DNI
        self.nota_bachillerato = nota_bachillerato
        self.notas_evau = notas_evau
        self.nota_acceso = 0.0 # Se inicializa a 0 hasta que se calcule

    def calcular_nota_acceso(self):
        suma_pau = 0
        # OJO: Asumimos que las 4 primeras notas del diccionario son la fase obligatoria
        notas_pau_obligatoria = dict(list(self.notas_evau.items())[0:4]) 
        
        print(f"\nCalculando nota de acceso para {self.nombre}:")
        print("Notas fase obligatoria PAU:")
        for asignatura, nota in notas_pau_obligatoria.items(): 
            print(f"> {asignatura}: {nota}")
            suma_pau += nota

        media_pau = suma_pau / 4 
        self.nota_acceso = round((self.nota_bachillerato * 0.6) + (media_pau * 0.4), 3) 
        print(f"Tu nota de acceso a la universidad es: {self.nota_acceso}")
        return self.nota_acceso

    def calcular_nota_admision(self, grado):
        # Este método delega el cálculo real al grado, pasándole la nota base y todas las notas de la EVAU
        # Primero nos aseguramos de tener la nota de acceso calculada
        if self.nota_acceso == 0.0:
            self.calcular_nota_acceso()
            
        nota_admision = grado.calcular_nota_admision(self.nota_acceso, self.notas_evau)
        return nota_admision

    def mostrar_perfil(self):
        print("\n------ Perfil del Estudiante ------")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.DNI}")
        print(f"Nota Bachillerato: {self.nota_bachillerato}")
        print("Notas EBAU:")
        for asignatura, notas in self.notas_evau.items():
            print(f"  - {asignatura}: {notas}")
        print(f"Nota de Acceso: {self.nota_acceso}")
        print("-----------------------------------")

# ==========================================
# CLASE SOLICITUD (Boceto con los métodos de tus compañeros)
# ==========================================
class Solicitud:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.preferencias = []

    def agregar_preferencia(self, grado, prioridad):
        nota = self.estudiante.calcular_nota_admision(grado) 
        lista = [grado.nombre, nota, prioridad] # Guardamos el nombre del grado para que se imprima bonito
        self.preferencias.append(lista)

    def ordenar_preferencias(self):
        self.preferencias.sort(key=lambda x: x[2]) 
        print(f"\n-------- Preferencias de {self.estudiante.nombre} --------")
        for i in range(len(self.preferencias)): 
            print(f"Prioridad: {self.preferencias[i][2]}, Grado: {self.preferencias[i][0]}, Nota de admisión: {self.preferencias[i][1]}")


# ==========================================
# FUNCIÓN PRINCIPAL (PRUEBAS)
# ==========================================
def main():
    # 1. Creamos la Universidad y el Grado
    upm = Universidad("UPM", "Madrid", "Pública")
    grado_robotica = Grado("Robótica", upm, 40, 12.1, "Ingeniería")
    upm.agregar_grado(grado_robotica)
    
    # 2. Definimos las ponderaciones del grado
    print("--- Configurando Grados ---")
    grado_robotica.definir_ponderacion("Matemáticas II", 0.2)
    grado_robotica.definir_ponderacion("Física", 0.2)

    # 3. Creamos un estudiante con sus notas (las 4 primeras son la fase obligatoria)
    notas_manolo = {
        "Lengua y Literatura Española": 8.5,
        "Historia de España": 7.5,
        "Inglés": 10.0,
        "Matemáticas II": 10.0, # Hasta aquí la fase obligatoria
        "Física": 8.5,          # Fase específica
        "Química": 5.0          # Fase específica
    }
    manolo = Estudiante("Manolo Manolo", "12345678X", 9.7, notas_manolo)
    
    # 4. Mostramos su perfil
    manolo.mostrar_perfil()

    # 5. Calculamos su nota de acceso y luego la de admisión para Robótica
    manolo.calcular_nota_acceso()
    nota_admision_manolo = manolo.calcular_nota_admision(grado_robotica)
    
    print(f"\n🤖 Nota de admisión de {manolo.nombre} para {grado_robotica.nombre}: {nota_admision_manolo}")

    # 6. Comprobamos si entra y lo matriculamos
    print("\n--- Proceso de Matriculación ---")
    if nota_admision_manolo >= grado_robotica.nota_de_corte:
        grado_robotica.matricular_alumno(manolo)
    else:
        print(f"❌ {manolo.nombre} no alcanza la nota de corte ({grado_robotica.nota_de_corte}).")

    # 7. Simulamos el año siguiente
    print("\n--- Actualización de notas por demanda (Año siguiente) ---")
    grado_robotica.actualizar_nota_corte(demanda_alta=True)
    
    # 8. Prueba rápida de la clase Solicitud
    print("\n--- Probando Sistema de Solicitudes ---")
    solicitud_manolo = Solicitud(manolo)
    solicitud_manolo.agregar_preferencia(grado_robotica, prioridad=1)
    solicitud_manolo.ordenar_preferencias()

if __name__ == "__main__":
    main()