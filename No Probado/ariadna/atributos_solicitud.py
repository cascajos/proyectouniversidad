class Solicitud :
    def __init__(self,estudiante,fase="ordinaria", estado="pendiente",grado_asignado=None):
        self.estudiante = estudiante
        self.preferencias=[]
        self.fase= fase
        self.estado = estado
        self.grado_asignado = grado_asignado