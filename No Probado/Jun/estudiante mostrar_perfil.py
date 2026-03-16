def mostrar_perfil(self):
        print("------Perfil------")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.DNI}")
        print("Notas EBAU:")
        for asignatura,notas in self.notas_evau.items():#Enseña todas las notas de la evau
            print(f"  - {asignatura}: {notas}")
        print(f"Nota Bachillerato: {self.nota_bachillerato}")