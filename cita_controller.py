class CitaMedicaController:
    def __init__(self, db_connection):
        self.db = db_connection

    def registrar_cita(self, id_paciente, id_medico, fecha_hora, especialidad):
        if not self._validar_disponibilidad(id_medico, fecha_hora):
            raise ValueError("El medico no se encuentra disponible en el horario seleccionado.")

        query = """
            INSERT INTO cita_medica (id_paciente, id_medico, fecha_hora, especialidad, estado)
            VALUES (%s, %s, %s, %s, 'PROGRAMADA')
        """
        cursor = self.db.cursor()
        cursor.execute(query, (id_paciente, id_medico, fecha_hora, especialidad))
        self.db.commit()
        return cursor.lastrowid

    def _validar_disponibilidad(self, id_medico, fecha_hora):
        query = "SELECT COUNT(*) FROM cita_medica WHERE id_medico = %s AND fecha_hora = %s"
        cursor = self.db.cursor()
        cursor.execute(query, (id_medico, fecha_hora))
        resultado = cursor.fetchone()
        return resultado[0] == 0
