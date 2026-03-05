def agregar_preferencia(self,grado,prioridad):

        nota_admision = self.estudiante.calcular_nota_admision(grado) #Calculo automático de nota de admision
        self.preferencias.append((grado, prioridad, nota_admision)) #Añadri a la lista por orden de prioridad