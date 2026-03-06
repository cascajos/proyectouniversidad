def generar_ranking(self,grado):
    ranking = sorted(
        grado.admitidos + grado.lista_espera,
        key=lambda est: est.calcular_nota_admision(grado),
        reverse=True
    )
    return ranking
def generar_estadistica(self):
    total= len(self.solicitudes)
    asignadas = sum(1 for s in self.solicitudes if s.estado =="asignada")
    print (f"Solicitudes totales: {total}")
    print(f"solicitudes asignadas:{asignadas}")
    print(f"Tasa de éxito: {asignadas/total*100:.2f}%")