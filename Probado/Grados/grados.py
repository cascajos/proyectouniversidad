import random

import sys
import os

ruta_estudiante = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Estudiante'))
sys.path.append(ruta_estudiante)

from Estudiante import Estudiante

ruta_universidad = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metodosuniversidafinal'))
sys.path.append(ruta_universidad)
from metodosuniversidadfinal import Universidad

#IMPORTANTE. HACE FALTA TAMBIÉN IMPORT DE ESTUDIANTE Y DE UNIVERSIDADES. Como todo estará luego integrado en la misma carpeta del main del programa, entonces se puede hacer con un simple from ... import ...

# 1. Clase para registrar los Grados (en singular es mejor practica)
class Grado:
    def __init__(self, nombre, universidad, plazas, nota_de_corte, rama, admitidos, lista_espera):
        self.nombre = nombre
        self.universidad = universidad  # Aqui guardaremos un objeto Universidad
        self.rama = rama
        self.plazas = plazas
        self.nota_de_corte = nota_de_corte
        self.ponderaciones = {}  # Diccionario vacio para guardar las asignaturas y su peso
        self.admitidos = {} # Diccionario vacío para guardar los estudiantes que entren en el grado junto a su nota de admisión.
        self.lista_espera = {} # Diccionario vacío para guardar los estudiantes que pretenden entrar al grado junto a su nota de admisión.

    # Metodo para definir ponderaciones (0.1 o 0.2)
    def definir_ponderacion(self, asignatura, peso):
        self.ponderaciones[asignatura] = peso
        print(f"Ponderacion guardada: {asignatura} vale x{peso} en {self.nombre}.")

    # Metodo para calcular la nota de un alumno concreto para este grado
    def calcular_nota_admision(self, alumno):
        nota_final = alumno.nota_acceso # Establecemos como nota base la nota de acceso del alumno.
        ponderaciones_notas = [] # Lista vacía a la que añadiremos todas las ponderaciones.
        for asignatura in alumno.notas_evau: # Escogemos las asignaturas que ha cursado el alumno.
            if asignatura in self.ponderaciones: # Comprobamos si esa asignatura pondera.
                if alumno.notas_evau[asignatura] >= 4: # La asignatura solo añade a nota si supera en un 4 //// x0.2 -> (0.8,2) / x0.1 -> (0.4,1)
                    ponderaciones_notas.append(alumno.notas_evau[asignatura] * self.ponderaciones[asignatura]) # Añadimos a la lista.
        ponderaciones_notas_finales = sorted(ponderaciones_notas) # Ordenamos la lista de menor a mayor.
        nota_final += ponderaciones_notas_finales[-1] + ponderaciones_notas_finales [-2] # Añadimos a la nota final las dos últimas (es decir, las dos mayores) ponderaciones. En caso de no haber ponderaciones, será por defecto 0
        self.lista_espera[alumno] = nota_final # Añadimos al alumno a lista de espera porque hay que meterlo en algún lado.
        return round(nota_final, 2)

    # Metodo para actualizar la nota de corte simulando la demanda
    def actualizar_nota_corte(self, demanda_alta):
        if demanda_alta: # Si hay mucha demanda, la nota sube un poco (entre 0.1 y 0.5)
            subida = random.uniform(0.1, 0.5)
            self.nota_de_corte = min(14.0, self.nota_de_corte + subida)
            print(f"La demanda ha subido la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")
        else: # Si hay poca demanda, baja (entre 0.1 y 0.5)
            bajada = random.uniform(0.1, 0.5)
            self.nota_de_corte = max(5.0, self.nota_de_corte - bajada)
            print(f"La demanda ha bajado la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")

    # Metodo para matricular alumnos y restar plazas
    def matricular_alumno(self,alumno):
        print("\n" + "=" * 60)
        print(f"La nota del alumno es {self.lista_espera[alumno]}. La nota de corte es {self.nota_de_corte}.")
        if self.plazas > 0:
            if self.lista_espera[alumno] >= self.nota_de_corte:
                self.plazas -= 1
                print(f"El alumno {alumno.nombre} ha sido matriculado con éxito. Plazas restantes en {self.nombre}: {self.plazas}")
                self.admitidos[alumno] = self.lista_espera[alumno]
                del self.lista_espera[alumno]
            else:
                print(f"Lo siento, {alumno.nombre} no alcanza la nota de corte de {self.nombre}")
        else:
            print(f"Lo siento, no quedan plazas en {self.nombre}.")
        print("=" * 60)
            

# 2. Funcion Principal para probar todo
def main():
    # Creamos una universidad

    universidad1 = Universidad("UBU", "Burgos", "Pública", ["Ingeniería Informática","Derecho","Medicina","Criminología","Farmacéutica","Ingeniería eléctrica", "Ingeniería robótica","Física","Matemáticas","Artes","Historia de España","Lengua Castellana","Filosofía"])
    universidad2 = Universidad("UPM", "Madrid", "Pública", ["Astronomía","Enfermería","Criminología","Derecho","Geología","Ingeniería Informática","Aviación", "Arquitectura","Historia de España","Filosofía","Medicina","Robótica"])
    universidad3 = Universidad("UPV", "Bilbao", "Pública", ["Derecho","Farmacia","Ingeniería Electrónica","Mecánica","Matemáticas","Arte","Biología", "Ingeniería Informática","Criminología","Economía"])
    universidad4 = Universidad("USAL", "Salamanca", "Pública", ["Física","Medicina","Ingeniería Informática","Matemáticas","Derecho","Robótica", "Geología","Filosofía","Criminología","Aviación"])
    universidad5 = Universidad("UHU", "Huelva", "Pública", ["Ingeniería Mecánica","Farmacia","Biología","Lengua","Filosofía","Ingeniería Informática", "Química","Historia de España","Matemáticas","Artes","Psicología","Física"])

    grado1_1 = Grado("Ingeniería Informática", universidad1, 80, 8.5, "Ingeniería", {}, {})
    grado1_2 = Grado("Derecho", universidad1, 100, 7.2, "Ciencias Sociales", {}, {})
    grado1_3 = Grado("Medicina", universidad1, 120, 12.5, "Ciencias de la Salud", {}, {})
    grado1_4 = Grado("Criminología", universidad1, 60, 9.0, "Ciencias Sociales", {}, {})
    grado1_5 = Grado("Farmacéutica", universidad1, 90, 10.8, "Ciencias de la Salud", {}, {})
    grado1_6 = Grado("Ingeniería Eléctrica", universidad1, 70, 7.8, "Ingeniería", {}, {})
    grado1_7 = Grado("Ingeniería Robótica", universidad1, 60, 9.5, "Ingeniería", {}, {})
    grado1_8 = Grado("Física", universidad1, 50, 9.2, "Ciencias", {}, {})
    grado1_9 = Grado("Matemáticas", universidad1, 60, 9.0, "Ciencias", {}, {})
    grado1_10 = Grado("Artes", universidad1, 40, 6.5, "Artes y Humanidades", {}, {})
    grado1_11 = Grado("Historia de España", universidad1, 50, 6.8, "Artes y Humanidades", {}, {})
    grado1_12 = Grado("Lengua Castellana", universidad1, 50, 6.7, "Artes y Humanidades", {}, {})
    grado1_13 = Grado("Filosofía", universidad1, 40, 6.3, "Artes y Humanidades", {}, {})

    grado2_1 = Grado("Astronomía", universidad2, 40, 10.5, "Ciencias", {}, {})
    grado2_2 = Grado("Enfermería", universidad2, 90, 10.2, "Ciencias de la Salud", {}, {})
    grado2_3 = Grado("Criminología", universidad2, 70, 9.3, "Ciencias Sociales", {}, {})
    grado2_4 = Grado("Derecho", universidad2, 120, 8.0, "Ciencias Sociales", {}, {})
    grado2_5 = Grado("Geología", universidad2, 50, 7.5, "Ciencias", {}, {})
    grado2_6 = Grado("Ingeniería Informática", universidad2, 100, 10.8, "Ingeniería", {}, {})
    grado2_7 = Grado("Aviación", universidad2, 60, 11.5, "Ingeniería", {}, {})
    grado2_8 = Grado("Arquitectura", universidad2, 80, 10.0, "Ingeniería", {}, {})
    grado2_9 = Grado("Historia de España", universidad2, 60, 7.0, "Artes y Humanidades", {}, {})
    grado2_10 = Grado("Filosofía", universidad2, 50, 6.5, "Artes y Humanidades", {}, {})
    grado2_11 = Grado("Medicina", universidad2, 150, 13.0, "Ciencias de la Salud", {}, {})
    grado2_12 = Grado("Robótica", universidad2, 60, 11.2, "Ingeniería", {}, {})

    grado3_1 = Grado("Derecho", universidad3, 90, 7.5, "Ciencias Sociales", {}, {})
    grado3_2 = Grado("Farmacia", universidad3, 80, 10.5, "Ciencias de la Salud", {}, {})
    grado3_3 = Grado("Ingeniería Electrónica", universidad3, 70, 8.2, "Ingeniería", {}, {})
    grado3_4 = Grado("Mecánica", universidad3, 80, 8.0, "Ingeniería", {}, {})
    grado3_5 = Grado("Matemáticas", universidad3, 60, 9.1, "Ciencias", {}, {})
    grado3_6 = Grado("Arte", universidad3, 50, 6.8, "Artes y Humanidades", {}, {})
    grado3_7 = Grado("Biología", universidad3, 70, 9.5, "Ciencias", {}, {})
    grado3_8 = Grado("Ingeniería Informática", universidad3, 90, 10.2, "Ingeniería", {}, {})
    grado3_9 = Grado("Criminología", universidad3, 60, 9.0, "Ciencias Sociales", {}, {})
    grado3_10 = Grado("Economía", universidad3, 100, 7.8, "Ciencias Sociales", {}, {})

    grado4_1 = Grado("Física", universidad4, 50, 9.3, "Ciencias", {}, {})
    grado4_2 = Grado("Medicina", universidad4, 140, 12.8, "Ciencias de la Salud", {}, {})
    grado4_3 = Grado("Ingeniería Informática", universidad4, 80, 9.8, "Ingeniería", {}, {})
    grado4_4 = Grado("Matemáticas", universidad4, 60, 9.0, "Ciencias", {}, {})
    grado4_5 = Grado("Derecho", universidad4, 100, 7.4, "Ciencias Sociales", {}, {})
    grado4_6 = Grado("Robótica", universidad4, 50, 10.5, "Ingeniería", {}, {})
    grado4_7 = Grado("Geología", universidad4, 40, 7.2, "Ciencias", {}, {})
    grado4_8 = Grado("Filosofía", universidad4, 50, 6.4, "Artes y Humanidades", {}, {})
    grado4_9 = Grado("Criminología", universidad4, 60, 9.1, "Ciencias Sociales", {}, {})
    grado4_10 = Grado("Aviación", universidad4, 50, 11.0, "Ingeniería", {}, {})

    grado5_1 = Grado("Ingeniería Mecánica", universidad5, 70, 7.9, "Ingeniería", {}, {})
    grado5_2 = Grado("Farmacia", universidad5, 80, 10.3, "Ciencias de la Salud", {}, {})
    grado5_3 = Grado("Biología", universidad5, 60, 9.2, "Ciencias", {}, {})
    grado5_4 = Grado("Lengua", universidad5, 50, 6.6, "Artes y Humanidades", {}, {})
    grado5_5 = Grado("Filosofía", universidad5, 40, 6.2, "Artes y Humanidades", {}, {})
    grado5_6 = Grado("Ingeniería Informática", universidad5, 80, 9.5, "Ingeniería", {}, {})
    grado5_7 = Grado("Química", universidad5, 60, 9.0, "Ciencias", {}, {})
    grado5_8 = Grado("Historia de España", universidad5, 50, 6.7, "Artes y Humanidades", {}, {})
    grado5_9 = Grado("Matemáticas", universidad5, 60, 8.8, "Ciencias", {}, {})
    grado5_10 = Grado("Artes", universidad5, 40, 6.5, "Artes y Humanidades", {}, {})
    grado5_11 = Grado("Psicología", universidad5, 90, 10.0, "Ciencias de la Salud", {}, {})
    grado5_12 = Grado("Física", universidad5, 50, 9.1, "Ciencias", {}, {})

    grado1_1.definir_ponderacion("Matemáticas", 0.2)
    grado1_1.definir_ponderacion("Física", 0.2)
    grado1_1.definir_ponderacion("Tecnología Industrial II", 0.1)

    grado1_2.definir_ponderacion("Historia", 0.2)
    grado1_2.definir_ponderacion("Lengua Castellana y Literatura", 0.2)

    grado1_3.definir_ponderacion("Biología", 0.2)
    grado1_3.definir_ponderacion("Química", 0.2)
    grado1_3.definir_ponderacion("Matemáticas", 0.1)

    grado1_4.definir_ponderacion("Historia", 0.2)
    grado1_4.definir_ponderacion("Matemáticas", 0.1)

    grado1_5.definir_ponderacion("Química", 0.2)
    grado1_5.definir_ponderacion("Biología", 0.2)

    grado1_6.definir_ponderacion("Matemáticas", 0.2)
    grado1_6.definir_ponderacion("Física", 0.2)

    grado1_7.definir_ponderacion("Matemáticas", 0.2)
    grado1_7.definir_ponderacion("Física", 0.2)
    grado1_7.definir_ponderacion("Tecnología Industrial II", 0.1)

    grado1_8.definir_ponderacion("Matemáticas", 0.2)
    grado1_8.definir_ponderacion("Física", 0.2)

    grado1_9.definir_ponderacion("Matemáticas", 0.2)
    grado1_9.definir_ponderacion("Física", 0.1)

    grado1_10.definir_ponderacion("Historia del Arte", 0.2)
    grado1_10.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado1_11.definir_ponderacion("Historia", 0.2)
    grado1_11.definir_ponderacion("Lengua Castellana y Literatura", 0.2)

    grado1_12.definir_ponderacion("Lengua Castellana y Literatura", 0.2)
    grado1_12.definir_ponderacion("Latín", 0.2)

    grado1_13.definir_ponderacion("Historia", 0.2)
    grado1_13.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    #---

    grado2_1.definir_ponderacion("Matemáticas", 0.2)
    grado2_1.definir_ponderacion("Física", 0.2)

    grado2_2.definir_ponderacion("Biología", 0.2)
    grado2_2.definir_ponderacion("Química", 0.2)

    grado2_3.definir_ponderacion("Historia", 0.2)
    grado2_3.definir_ponderacion("Matemáticas", 0.1)

    grado2_4.definir_ponderacion("Historia", 0.2)
    grado2_4.definir_ponderacion("Lengua Castellana y Literatura", 0.2)

    grado2_5.definir_ponderacion("Geología", 0.2)
    grado2_5.definir_ponderacion("Química", 0.1)

    grado2_6.definir_ponderacion("Matemáticas", 0.2)
    grado2_6.definir_ponderacion("Física", 0.2)

    grado2_7.definir_ponderacion("Matemáticas", 0.2)
    grado2_7.definir_ponderacion("Física", 0.2)

    grado2_8.definir_ponderacion("Matemáticas", 0.2)
    grado2_8.definir_ponderacion("Dibujo Técnico II", 0.2)

    grado2_9.definir_ponderacion("Historia", 0.2)
    grado2_9.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado2_10.definir_ponderacion("Historia", 0.2)
    grado2_10.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado2_11.definir_ponderacion("Biología", 0.2)
    grado2_11.definir_ponderacion("Química", 0.2)

    grado2_12.definir_ponderacion("Matemáticas", 0.2)
    grado2_12.definir_ponderacion("Física", 0.2)

    #---

    grado3_1.definir_ponderacion("Historia", 0.2)
    grado3_1.definir_ponderacion("Lengua Castellana y Literatura", 0.2)

    grado3_2.definir_ponderacion("Química", 0.2)
    grado3_2.definir_ponderacion("Biología", 0.2)

    grado3_3.definir_ponderacion("Matemáticas", 0.2)
    grado3_3.definir_ponderacion("Física", 0.2)

    grado3_4.definir_ponderacion("Matemáticas", 0.2)
    grado3_4.definir_ponderacion("Física", 0.2)

    grado3_5.definir_ponderacion("Matemáticas", 0.2)
    grado3_5.definir_ponderacion("Física", 0.1)

    grado3_6.definir_ponderacion("Historia del Arte", 0.2)
    grado3_6.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado3_7.definir_ponderacion("Biología", 0.2)
    grado3_7.definir_ponderacion("Química", 0.1)

    grado3_8.definir_ponderacion("Matemáticas", 0.2)
    grado3_8.definir_ponderacion("Física", 0.2)

    grado3_9.definir_ponderacion("Historia", 0.2)
    grado3_9.definir_ponderacion("Matemáticas Aplicadas", 0.1)

    grado3_10.definir_ponderacion("Matemáticas", 0.2)
    grado3_10.definir_ponderacion("Economía", 0.2)

    #---

    grado4_1.definir_ponderacion("Matemáticas", 0.2)
    grado4_1.definir_ponderacion("Física", 0.2)

    grado4_2.definir_ponderacion("Biología", 0.2)
    grado4_2.definir_ponderacion("Química", 0.2)

    grado4_3.definir_ponderacion("Matemáticas", 0.2)
    grado4_3.definir_ponderacion("Física", 0.2)

    grado4_4.definir_ponderacion("Matemáticas", 0.2)
    grado4_4.definir_ponderacion("Física", 0.1)

    grado4_5.definir_ponderacion("Historia", 0.2)
    grado4_5.definir_ponderacion("Lengua Castellana y Literatura", 0.2)

    grado4_6.definir_ponderacion("Matemáticas", 0.2)
    grado4_6.definir_ponderacion("Física", 0.2)

    grado4_7.definir_ponderacion("Geología", 0.2)
    grado4_7.definir_ponderacion("Química", 0.1)

    grado4_8.definir_ponderacion("Historia", 0.2)
    grado4_8.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado4_9.definir_ponderacion("Historia", 0.2)
    grado4_9.definir_ponderacion("Matemáticas", 0.1)

    grado4_10.definir_ponderacion("Matemáticas", 0.2)
    grado4_10.definir_ponderacion("Física", 0.2)

    #---

    grado5_1.definir_ponderacion("Matemáticas", 0.2)
    grado5_1.definir_ponderacion("Física", 0.2)
    
    grado5_2.definir_ponderacion("Química", 0.2)
    grado5_2.definir_ponderacion("Biología", 0.2)

    grado5_3.definir_ponderacion("Biología", 0.2)
    grado5_3.definir_ponderacion("Química", 0.1)

    grado5_4.definir_ponderacion("Lengua Castellana y Literatura", 0.2)
    grado5_4.definir_ponderacion("Historia", 0.1)

    grado5_5.definir_ponderacion("Historia", 0.2)
    grado5_5.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado5_6.definir_ponderacion("Matemáticas", 0.2)
    grado5_6.definir_ponderacion("Física", 0.2)

    grado5_7.definir_ponderacion("Química", 0.2)
    grado5_7.definir_ponderacion("Matemáticas", 0.1)

    grado5_8.definir_ponderacion("Historia", 0.2)
    grado5_8.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado5_9.definir_ponderacion("Matemáticas", 0.2)
    grado5_9.definir_ponderacion("Física", 0.1)

    grado5_10.definir_ponderacion("Historia del Arte", 0.2)
    grado5_10.definir_ponderacion("Lengua Castellana y Literatura", 0.1)

    grado5_11.definir_ponderacion("Biología", 0.2)
    grado5_11.definir_ponderacion("Química", 0.2)

    grado5_12.definir_ponderacion("Matemáticas", 0.2)
    grado5_12.definir_ponderacion("Física", 0.2)

    '''ups = Universidad("Universidad Pontificia", "Salamanca", "Privada")
    
    # Creamos el grado pasandole la universidad
    mu = Grado("Ingenieria Informatica", ups, 20, 9.5, ["Ingeniería","Informática","Ciencias"],{},{})

    notas_manolo = {
        "Lengua y Literatura Española": 0,
        "Historia de España / Filosofía": 0,
        "Primera Lengua Extranjera": 0,
        "Matemáticas (Ciencias / Sociales)": 0,
        "Física": 0,
        "Química": 0,
        "Tecnología e Ingeniería II": 0
    }

    notas_manolo["Lengua y Literatura Española"] = float(input("> Introduzca su nota en PAU troncal, asignatura Lengua y Literatura Española: "))
    notas_manolo["Historia de España / Filosofía"] = float(input("> Introduzca su nota en PAU troncal, asignatura Historia de España o Historia de la Filosofía: "))
    notas_manolo["Primera Lengua Extranjera"] = float(input("> Introduzca su nota en PAU troncal, asignatura Primera Lengua Extranjera: "))
    notas_manolo["Matemáticas (Ciencias / Sociales)"] = float(input("> Introduzca su nota en PAU troncal, asignatura Matemáticas (Ciencias o Sociales): "))

    if "s" == input(">>> ¿Ha cursado el alumno la asignatura específica Física? En caso afirmativo, responda 's': "):
        notas_manolo["Física"] = float(input(">>> Introduzca su nota en PAU específica, asignatura Física: "))
    if "s" == input(">>> ¿Ha cursado el alumno la asignatura específica Química? En caso afirmativo, responda 's': "):
        notas_manolo["Química"] = float(input(">>> Introduzca su nota en PAU específica, asignatura Química: "))
    if "s" == input(">>> ¿Ha cursado el alumno la asignatura específica Tecnología e Ingeniería II? En caso afirmativo, responda 's': "):
        notas_manolo["Tecnología e Ingeniería II"] = float(input(">>> Introduzca su nota en PAU específica, asignatura Tecnología e Ingeniería II: "))

    Manolo = Estudiante("Manolo Manolero Manoluzo","12345678X",7.5,notas_manolo,0)
    Manolo.calcular_nota_acceso()
    
    print(f"--- Sistema del Grado: {mu.nombre} en {mu.universidad.nombre} ---")
    
    mu.definir_ponderacion("Matemáticas (Ciencias / Sociales)", 0.2) #Se definen las ponderaciones para el grado mu.
    mu.definir_ponderacion("Tecnología e Ingeniería II", 0.2)
    mu.definir_ponderacion("Física", 0.1) #Importante, el nombre debe estar bien escrito. Cuidado con tildes y mayúsculas.
    
    nota_alumno = mu.calcular_nota_admision(Manolo)
    print(f"\nLa nota de admision del alumno calculada es: {nota_alumno}") #Esto podría ir dentro del método sin problema.
    
    mu.matricular_alumno(Manolo) # Intentamos matricular al alumno.

    # Simulamos que pasa con la nota de corte al año siguiente
    print("\n--- Actualizacion de notas por demanda ---")
    mu.actualizar_nota_corte(demanda_alta = True)'''

if __name__ == "__main__":
    main()
