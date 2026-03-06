def agregar_preferencia(self,grado,prioridad):
        nota=self.estudiante.calcular_nota_admision(grado)
        lista=[grado,nota,prioridad]
        self.preferencias.append(lista)