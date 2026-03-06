class Solicitud:
    def __init__(self):
        self.preferencias=[]
    
    def agregar_preferencia(self,grado,prioridad):
        nota=self.estudiante.calcular_nota_admision(grado)
        lista=[grado,nota,prioridad]
        self.preferencias.append(lista)


    def ordenar_preferencias(self):
        self.preferencias.sort(key=lambda x:x[2])#Chat GPT (esto basicamente ordena las preferencias)
        for i in range(0,len(self.preferencias)):#imprime las preferencias por orden
            print(f"Prioridad: {self.preferencias[i][2]}, Grado: {self.preferencias[i][0]}, Nota de admisión: {self.preferencias[i][1]}")
a=Solicitud()
l=["a","b",2]
l1=["a","b",1]
l2=["a","b",3]
a.preferencias.append(l)
a.preferencias.append(l1)
a.preferencias.append(l2)
a.ordenar_preferencias()