class Medico:
    def __init__(self, id_medico, nombre, especialidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad

    def ver_agenda(self):
        return f"Mostrando agenda de citas del Dr. {self.nombre}"
