import random
from Alejandro.metodo_estudiante import Estudiante #Implementamos Estudiante de su archivo.
#from como_se_llame_universidad import Universidad #Por ahora, así, luego se cambia.

class Universidad:
    def __init__(self, nombre, ciudad, tipo):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tipo = tipo 
        
    def __str__(self):
        return f"{self.nombre} ({self.ciudad} - {self.tipo})"

# 2. Clase para registrar los Grados (en singular es mejor practica)
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
            

# 3. Funcion Principal para probar todo
def main():
    # Creamos una universidad
    ups = Universidad("Universidad Pontificia", "Salamanca", "Privada")
    
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
    mu.actualizar_nota_corte(demanda_alta = True)

if __name__ == "__main__":
    main()