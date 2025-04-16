import csv
from collections import defaultdict
from estudiante import Estudiante
from inscripcion import Inscripcion

class ControlInscripcion:
    def __init__(self):
        self.estudiantes = {}
        self.inscripciones = []

    def leer_archivo(self, ruta_archivo):
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                cedula, nombre, codigo_materia, _ = fila  # ignoramos el nombre de la materia
                if cedula not in self.estudiantes:
                    self.estudiantes[cedula] = Estudiante(cedula, nombre)
                self.inscripciones.append(Inscripcion(cedula, codigo_materia))

    def calcular_materias_por_estudiante(self):
        materias_por_estudiante = defaultdict(set)
        for inscripcion in self.inscripciones:
            materias_por_estudiante[inscripcion.cedula_estudiante].add(inscripcion.codigo_materia)

        for cedula, materias in materias_por_estudiante.items():
            nombre = self.estudiantes[cedula].get_nombre_estudiante()
            print(f"{nombre}: {len(materias)} materias")
