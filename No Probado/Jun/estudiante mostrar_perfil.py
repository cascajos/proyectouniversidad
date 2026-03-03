def mostrar_perfil(self):
        print("------Perfil------")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.DNI}")
        print("Notas EBAU:")
        for asignatura,notas in self.notas_evau.items():
            print(f"  - {asignatura}: {notas}")
        print(f"Nota Bachillerato: {self.nota_bachillerato}")
        print(f"Notas EVAU: {self.notas_evau}")