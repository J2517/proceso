import csv
from collections import defaultdict
from estudiante import Estudiante
from inscripcion import Inscripcion
import re

class ControlInscripcion:
    def __init__(self):
        self.estudiantes = {}
        self.inscripciones = []

    def leer_archivo(self, ruta_archivo):
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:

                # Ignorar filas con campos faltantes
                if len(fila) < 4 or not fila[0] or not fila[2]:
                    continue

                # Limpiar espacios
                cedula = fila[0].strip()
                nombre = fila[1].strip()
                codigo_materia = fila[2].strip()

                # Validar que la columna 0 sea una cédula (7 dígitos) y columna 2 un código de materia (4 dígitos)
                if not re.fullmatch(r"\d{7}", cedula) or not re.fullmatch(r"\d{4}", codigo_materia):
                    raise ValueError("Columnas en orden incorrecto")

                # Validar si ya existe la cédula con nombre diferente
                if cedula in self.estudiantes and self.estudiantes[cedula].nombre_estudiante != nombre:
                    # Eliminar estudiante e inscripciones asociadas
                    del self.estudiantes[cedula]
                    self.inscripciones = [i for i in self.inscripciones if i.cedula_estudiante != cedula]
                    raise ValueError(f"Cédula duplicada con nombre diferente: {cedula}")
            
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
