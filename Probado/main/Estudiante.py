class Estudiante:
    def __init__(self, nombre, DNI, nota_bachillerato, notas_evau, nota_acceso):
        self.nombre = nombre
        self.DNI = DNI
        self.nota_bachillerato = nota_bachillerato
        self.notas_evau = notas_evau
        self.nota_acceso = nota_acceso

    def calcular_nota_acceso(self):
        troncales = ["Lengua", "Historia/Filosofia", "Ingles", "Matematicas"]
        suma = 0
        for asig in troncales:
            suma += self.notas_evau.get(asig, 0)
        media_troncales = suma / 4

        opcionales = {k:v for k,v in self.notas_evau.items() if k not in troncales}
        suma_opc = 0
        for nota in list(opcionales.values())[:2]:
            suma_opc += nota * 0.2

        self.nota_acceso = (self.nota_bachillerato * 0.6) + (media_troncales * 0.4) + suma_opc
        if self.nota_acceso > 14:
            self.nota_acceso = 14
        print(f"Nota de acceso: {self.nota_acceso:.2f}")
        return self.nota_acceso

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.DNI}")
        print("Notas EBAU:")
        for asig, nota in self.notas_evau.items():
            print(f"  {asig}: {nota}")
        print(f"Nota acceso: {self.nota_acceso:.2f}")