def agregar_preferencia(self,grado,prioridad):
        nota=self.estudiante.calcular_nota_admision(grado)#Calculo la nota de admisión para el grado
        lista=[grado,nota,prioridad]#Creo la lista
        self.preferencias.append(lista)#Lo añado a la lista de preferencias