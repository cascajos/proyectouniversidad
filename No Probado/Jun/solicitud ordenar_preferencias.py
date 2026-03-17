def ordenar_preferencias(self):
    self.preferencias.sort(key=lambda x:x[2])#Chat GPT (esto basicamente ordena las preferencias)
    print("--------Preferencias por orden--------")
    for i in range(0,len(self.preferencias)):#imprime las preferencias por orden
        print(f"Prioridad: {self.preferencias[i][2]}, Grado: {self.preferencias[i][0]}, Nota de admisión: {self.preferencias[i][1]}")