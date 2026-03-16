class Estudiante:
    def __init__(self,nombre,DNI,nota_bachillerato, notas_evau, nota_acceso):
        self.nombre = nombre
        self.DNI = DNI
        self.nota_bachillerato = nota_bachillerato
        self.notas_evau = notas_evau
        self.nota_acceso = nota_acceso

    def calcular_nota_acceso(self):
        suma_pau = 0
        notas_pau_obligatoria = dict(list(self.notas_evau.items())[0:4]) #Esto selecciona solo las de la fase obligatoria, que DEBERIAN SER SIEMPRE las 4 primeras.
        print("Notas en la PAU:")

        i = 0
        for i in notas_pau_obligatoria: #Esto coge las notas de las primeras 4 asignaturas (que recuerdo, DEBEN SER LAS OBLIGATORIAS), y las suma para luego generar la media.
            print(f"> {i}: {notas_pau_obligatoria[i]}")
            suma_pau += notas_pau_obligatoria[i]

        media_pau = suma_pau/4 #Esta es la media.
        self.nota_acceso = (self.nota_bachillerato * 0.6) + (media_pau * 0.4) #Y esto la nota de acceso.
        print(f"\nTu nota de acceso a la universidad es: {self.nota_acceso}")
        return self.nota_acceso

    def calcular_nota_admision(self,grado):
        nota_admision = self.nota_acceso
        if "Física" in grado:
            nota_admision += self.notas_evau["Física"] * grado["Física"]
        if "Química" in grado:
            nota_admision += self.notas_evau["Química"] * grado["Química"]
        if "Tecnología" in grado:
            nota_admision += self.notas_evau["Tecnología"] * grado["Tecnología"]
        
        print("\n- Ponderación #1 pondera 0,2.")
        print("- Ponderación #2 pondera 0,2.")
        print("- Ponderación #3 pondera 0,1.")
        print(f"La nota de acceso para este grado es {nota_admision}")
        return nota_admision

# -------------------------------------------------------------------------------------------------------

def main():
    print()

    mi_pau = {
        "Lengua y Literatura Española": 8.5,
        "Historia de España": 7.5,
        "Inglés": 10,
        "Matemáticas II": 10,
        "Física": 6.5,
        "Química": 5
    }
    #Este diccionario es de las notas. Se explica por sí mismo. Procurad que las asignaturas de fase obligatoria sean siempre las primeras, da igual el orden.

    manolo = Estudiante("Manolo Manolo","12345678X",9.7,mi_pau,0)

    manolo.calcular_nota_acceso()
    print()
    print("=" * 50)

    ponderaciones = { #Esto es para simular el grado.
        "Física": 0.2,
        "Química": 0.1
    }

    manolo.calcular_nota_admision(ponderaciones) #Bla bla blah clase Grado por favor la necesito.
    print()

if __name__ == "__main__":
    main()