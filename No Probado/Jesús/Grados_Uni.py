import random

# 1. Clase para registrar las Universidades
'''class Universidad:
    def __init__(self, nombre, ciudad, tipo):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tipo = tipo  # "Publica" o "Privada"
        
    def __str__(self):
        return f"{self.nombre} ({self.ciudad} - {self.tipo})" '''

# 2. Clase para registrar los Grados (en singular es mejor practica)
class Grado:
    def __init__(self, nombre, universidad, plazas, nota_de_corte, rama):
        self.nombre = nombre
        self.universidad = universidad  # Aqui guardaremos un objeto Universidad
        self.rama = rama
        self.plazas = plazas
        self.nota_de_corte = nota_de_corte
        self.ponderaciones = {}  # Diccionario vacio para guardar las asignaturas y su peso

    # Metodo para definir ponderaciones (ej: Matematicas -> 1.5)
    def definir_ponderacion(self, asignatura, peso):
        self.ponderaciones[asignatura] = peso
        print(f"Ponderacion guardada: {asignatura} vale x{peso} en {self.nombre}.")

    # Metodo para calcular la nota de un alumno concreto para este grado
    def calcular_nota_admision(self, nota_base, notas_especificas):
        nota_final = nota_base
        # Calculamos los extras segun las ponderaciones
        for asignatura, nota in notas_especificas.items():
            if asignatura in self.ponderaciones:
                # Multiplicamos la nota por su peso (ej: 9.0 * 1.5)
                nota_final += nota * self.ponderaciones[asignatura]
        
        # Limitamos la nota maxima a 14 (o el tope que useis en vuestro sistema)
        nota_final = min(nota_final, 14.0)
        return round(nota_final, 2)

    # Metodo para actualizar la nota de corte simulando la demanda
    def actualizar_nota_corte(self, demanda_alta):
        if demanda_alta:
            # Si hay mucha demanda, la nota sube un poco (entre 0.1 y 0.5)
            subida = random.uniform(0.1, 0.5)
            self.nota_de_corte = min(14.0, self.nota_de_corte + subida)
            print(f"La demanda ha subido la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")
        else:
            # Si hay poca demanda, baja (entre 0.1 y 0.5)
            bajada = random.uniform(0.1, 0.5)
            self.nota_de_corte = max(5.0, self.nota_de_corte - bajada)
            print(f"La demanda ha bajado la nota de {self.nombre} a {round(self.nota_de_corte, 2)}")

    # Metodo para matricular alumnos y restar plazas
    def matricular_alumno(self):
        if self.plazas > 0:
            self.plazas -= 1
            print(f"Alumno matriculado con éxito. Plazas restantes en {self.nombre}: {self.plazas}")
        else:
            print(f"Lo siento, no quedan plazas en {self.nombre}.")

# 3. Funcion Principal para probar todo
'''def main():
    # Creamos una universidad
    ups = Universidad("Universidad Pontificia", "Salamanca", "Privada")
    
    # Creamos el grado pasandole la universidad
    mu = Grado("Ingenieria Informatica", ups, 20, 9.5, "Ingenieria")
    
    print(f"--- Sistema del Grado: {mu.nombre} en {mu.universidad.nombre} ---")
    
    # Probamos las ponderaciones
    mu.definir_ponderacion("Matematicas", 1.5)
    mu.definir_ponderacion("Fisica", 2.0)
    
    # Simulamos un alumno con nota base de 7.5 y sus notas en la fase especifica
    notas_alumno = {"Matematicas": 8.0, "Fisica": 7.0, "Quimica": 6.0}
    nota_alumno = mu.calcular_nota_admision(7.5, notas_alumno)
    print(f"\nLa nota de admision del alumno calculada es: {nota_alumno}")
    
    # Comprobamos si entra
    if nota_alumno >= mu.nota_de_corte:
        print("El alumno ha sido admitido!")
        mu.matricular_alumno()
    else:
        print("El alumno no alcanza la nota de corte.")
        
    # Simulamos que pasa con la nota de corte al año siguiente
    print("\n--- Actualizacion de notas por demanda ---")
    mu.actualizar_nota_corte(demanda_alta=True)

if __name__ == "__main__":
    main()  '''