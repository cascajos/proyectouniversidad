import random
from metodosuniversidadfinal import LISTA_UNIVERSIDADES

# He mantenido la clase de grado prácticamente intacta
class Grado:
    def __init__(self, nombre, universidad, plazas, nota_de_corte, rama):
        self.nombre = nombre
        self.universidad = universidad
        self.rama = rama
        self.plazas = plazas
        self.nota_de_corte = nota_de_corte
        self.ponderaciones = {}
        self.admitidos = {}
        self.lista_espera = {}

    def definir_ponderacion(self, asignatura, peso):
        self.ponderaciones[asignatura] = peso

    def calcular_nota_admision(self, alumno):
        nota_final = alumno.nota_acceso
        ponderaciones_usadas = []
        for asignatura, nota in alumno.notas_evau.items():
            if asignatura in self.ponderaciones and nota >= 4:
              ponderaciones_usadas.append(nota * self.ponderaciones[asignatura])
        ponderaciones_usadas.sort()
        if len(ponderaciones_usadas) >= 2:
            nota_final += ponderaciones_usadas[-1] + ponderaciones_usadas[-2]
        elif len(ponderaciones_usadas) == 1:
            nota_final += ponderaciones_usadas[-1]
        self.lista_espera[alumno] = nota_final
        return round(nota_final, 2)

    def matricular_alumno(self, alumno):
        nota_alumno = self.lista_espera.get(alumno, 0)
        if self.plazas > 0 and nota_alumno >= self.nota_de_corte:
            self.plazas -= 1
            self.admitidos[alumno] = nota_alumno
            if alumno in self.lista_espera:
                del self.lista_espera[alumno]
            return True
        return False

    def actualizar_nota_corte(self, demanda_alta):
        if demanda_alta:
            self.nota_de_corte = min(14.0, self.nota_de_corte + random.uniform(0.1, 0.5))
        else:
            self.nota_de_corte = max(5.0, self.nota_de_corte - random.uniform(0.1, 0.5))


# He creado un apéndice en el archivo de universidades, y en este def accedo a el, depues he asignado a cada uno de los grados ya anteriormente especificados la información
# Faltante necesaria para el calculo de la admisión en dicho grado (las notas son relativamente aleatorias)

def buscar_universidad_por_nombre(nombre):
    for uni in LISTA_UNIVERSIDADES:
        if uni.nombre == nombre:
            return uni
    return None

# Diccionario para almacenar todos los grados
TODOS_GRADOS = []

# --- Universidad de Burgos (UBU) ---
ubu = buscar_universidad_por_nombre("UBU")
if ubu:
    g = Grado("Ingeniería Informática", ubu, plazas=200, nota_de_corte=10.5, rama="Ingeniería")
    g.definir_ponderacion("Matematicas", 0.2)
    g.definir_ponderacion("Fisica", 0.1)
    TODOS_GRADOS.append(g)

    g = Grado("Derecho", ubu, plazas=150, nota_de_corte=9.2, rama="Sociales")
    g.definir_ponderacion("Lengua", 0.2)
    g.definir_ponderacion("Historia/Filosofia", 0.1)
    TODOS_GRADOS.append(g)

    g = Grado("Medicina", ubu, plazas=100, nota_de_corte=12.8, rama="Ciencias Salud")
    g.definir_ponderacion("Biologia", 0.2)
    g.definir_ponderacion("Quimica", 0.2)
    TODOS_GRADOS.append(g)

# --- Universidad Politécnica de Madrid (UPM) ---
upm = buscar_universidad_por_nombre("UPM")
if upm:
    g = Grado("Ingeniería Informática", upm, plazas=350, nota_de_corte=12.5, rama="Ingeniería")
    g.definir_ponderacion("Matematicas", 0.2)
    g.definir_ponderacion("Fisica", 0.1)
    TODOS_GRADOS.append(g)

    g = Grado("Ingeniería Aeroespacial", upm, plazas=200, nota_de_corte=13.2, rama="Ingeniería")
    g.definir_ponderacion("Matematicas", 0.2)
    g.definir_ponderacion("Fisica", 0.2)
    TODOS_GRADOS.append(g)

    g = Grado("Arquitectura", upm, plazas=300, nota_de_corte=12.8, rama="Arquitectura")
    g.definir_ponderacion("Matematicas", 0.2)
    g.definir_ponderacion("Dibujo Técnico", 0.1)
    TODOS_GRADOS.append(g)

# --- Universidad del País Vasco (UPV) ---
upv = buscar_universidad_por_nombre("UPV")
if upv:
    g = Grado("Ingeniería Informática", upv, plazas=250, nota_de_corte=11.0, rama="Ingeniería")
    g.definir_ponderacion("Matematicas", 0.2)
    g.definir_ponderacion("Fisica", 0.1)
    TODOS_GRADOS.append(g)

    g = Grado("Economía", upv, plazas=180, nota_de_corte=10.2, rama="Sociales")
    g.definir_ponderacion("Matematicas CCSS", 0.2)
    g.definir_ponderacion("Economía", 0.2)
    TODOS_GRADOS.append(g)

# --- Universidad de Salamanca (USAL) ---
usal = buscar_universidad_por_nombre("USAL")
if usal:
    g = Grado("Medicina", usal, plazas=220, nota_de_corte=13.1, rama="Ciencias Salud")
    g.definir_ponderacion("Biologia", 0.2)
    g.definir_ponderacion("Quimica", 0.2)
    TODOS_GRADOS.append(g)

    g = Grado("Ingeniería Informática", usal, plazas=180, nota_de_corte=11.2, rama="Ingeniería")
    g.definir_ponderacion("Matematicas", 0.2)
    TODOS_GRADOS.append(g)

    g = Grado("Biotecnología", usal, plazas=80, nota_de_corte=12.5, rama="Ciencias")
    g.definir_ponderacion("Biologia", 0.2)
    g.definir_ponderacion("Quimica", 0.1)
    TODOS_GRADOS.append(g)

# --- Universidad de Huelva (UHU) ---
uhu = buscar_universidad_por_nombre("UHU")
if uhu:
    g = Grado("Ingeniería Informática", uhu, plazas=150, nota_de_corte=9.8, rama="Ingeniería")
    g.definir_ponderacion("Matematicas", 0.2)
    TODOS_GRADOS.append(g)

    g = Grado("Psicología", uhu, plazas=120, nota_de_corte=10.5, rama="Ciencias Salud")
    g.definir_ponderacion("Biologia", 0.2)
    TODOS_GRADOS.append(g)

if usal:
    g = Grado("Física", usal, plazas=100, nota_de_corte=11.0, rama="Ciencias")
    g.definir_ponderacion("Matematicas", 0.2)
    g.definir_ponderacion("Fisica", 0.2)
    TODOS_GRADOS.append(g)

    g = Grado("Matemáticas", usal, plazas=90, nota_de_corte=10.8, rama="Ciencias")
    g.definir_ponderacion("Matematicas", 0.2)
    TODOS_GRADOS.append(g)


LISTA_GRADOS = TODOS_GRADOS