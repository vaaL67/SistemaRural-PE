class HistoriaClinica:
    def __init__(self, id_historia, diagnostico):
        self.id_historia = id_historia
        self.diagnostico = diagnostico
        self.tratamientos = []

    def agregar_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)
