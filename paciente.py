class Paciente:
    def __init__(self, id_paciente, nombre, dni, fecha_nacimiento):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def consultar_historia(self):
        return f"Consultando historia clinica del paciente {self.nombre}"
