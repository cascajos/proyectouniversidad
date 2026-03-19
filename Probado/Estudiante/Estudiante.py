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

    def mostrar_perfil(self,nota_acceso):
        print("------Perfil------")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.DNI}")
        print("Notas EBAU:")
        for asignatura,notas in self.notas_evau.items():
            print(f"  - {asignatura}: {notas}")
        print(f"Nota Bachillerato: {self.nota_bachillerato}")
        print(f"Nota de acceso: {nota_acceso}")