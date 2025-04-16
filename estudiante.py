class Estudiante:
    def __init__(self, cedula_estudiante: str, nombre_estudiante: str):
        self.cedula_estudiante = cedula_estudiante
        self.nombre_estudiante = nombre_estudiante

    def get_nombre_estudiante(self):
        return self.nombre_estudiante
