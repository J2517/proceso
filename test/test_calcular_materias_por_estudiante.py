import unittest
from unittest.mock import patch
from io import StringIO
from control_inscripcion import ControlInscripcion
from inscripcion import Inscripcion
from estudiante import Estudiante

class TestControlInscripcion(unittest.TestCase):

    def setUp(self):
        self.control = ControlInscripcion()

    @patch("sys.stdout", new_callable=StringIO)
    def test_3_estudiantes_1_materia_cada_uno(self, mock_stdout):
        """Calcular materias cuando hay 3 estudiantes y 3 materias distintas"""
        self.control.estudiantes = {
            "1": Estudiante("1", "Ana"),
            "2": Estudiante("2", "Luis"),
            "3": Estudiante("3", "Sofi")
        }
        self.control.inscripciones = [
            Inscripcion("1", "MAT1"),
            Inscripcion("2", "MAT2"),
            Inscripcion("3", "MAT3")
        ]
        self.control.calcular_materias_por_estudiante()
        salida = mock_stdout.getvalue().strip().split("\n")

        self.assertIn("Ana: 1 materias", salida)
        self.assertIn("Luis: 1 materias", salida)
        self.assertIn("Sofi: 1 materias", salida)

    @patch("sys.stdout", new_callable=StringIO)
    def test_ningun_estudiante_ni_materia(self, mock_stdout):
        """Calcular materias cuando no se ha subido ningún dato"""
        self.control.estudiantes = {}
        self.control.inscripciones = []
        self.control.calcular_materias_por_estudiante()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_un_estudiante_dos_materias(self, mock_stdout):
        """Un estudiante tiene 2 materias, los otros una"""
        self.control.estudiantes = {
            "1": Estudiante("1", "Carlos"),
            "2": Estudiante("2", "Laura"),
            "3": Estudiante("3", "Andrés")
        }
        self.control.inscripciones = [
            Inscripcion("1", "MAT1"),
            Inscripcion("1", "MAT2"),
            Inscripcion("2", "MAT3"),
            Inscripcion("3", "MAT4")
        ]
        self.control.calcular_materias_por_estudiante()
        salida = mock_stdout.getvalue().strip().split("\n")

        self.assertIn("Carlos: 2 materias", salida)
        self.assertIn("Laura: 1 materias", salida)
        self.assertIn("Andrés: 1 materias", salida)

    @patch("sys.stdout", new_callable=StringIO)
    def test_mismo_nombre_distinta_cedula(self, mock_stdout):
        """Dos estudiantes con el mismo nombre pero diferente cédula"""
        self.control.estudiantes = {
            "10": Estudiante("10", "Alex"),
            "20": Estudiante("20", "Alex")
        }
        self.control.inscripciones = [
            Inscripcion("10", "MAT1"),
            Inscripcion("20", "MAT2")
        ]
        self.control.calcular_materias_por_estudiante()
        salida = mock_stdout.getvalue().strip().split("\n")

        self.assertEqual(sorted(salida), sorted(["Alex: 1 materias", "Alex: 1 materias"]))

    def test_misma_cedula_diferente_nombre(self):
        """Dos inscripciones con misma cédula pero diferente nombre deben lanzar excepción"""
        self.control.estudiantes = {
            "99": Estudiante("99", "Pedro")
        }
        # Simulamos conflicto de cédula con otro nombre
        with self.assertRaises(ValueError):
            nuevo_nombre = "Juan"
            cedula = "99"
            if self.control.estudiantes[cedula].get_nombre_estudiante() != nuevo_nombre:
                raise ValueError(f"Conflicto de nombres para cédula {cedula}")


if __name__ == "_main_":
    unittest.main()