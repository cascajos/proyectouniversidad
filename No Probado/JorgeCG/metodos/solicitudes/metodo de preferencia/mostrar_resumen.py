def mostrar_resumen(self): #Esto muestra el resumen de los resultados asi, mas cuqui
    for grado, prioridad, nota_admision in self.preferencias:
        print(f"Prioridad {prioridad}: {grado.nombre}")
        print(f"Nota de admisión: {nota_admision:.2f}")