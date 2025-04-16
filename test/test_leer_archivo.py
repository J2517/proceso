import unittest
import os
from control_inscripcion import ControlInscripcion

class TestLeerArchivo(unittest.TestCase):

    def setUp(self):
        self.ruta_base = os.path.join(os.path.dirname(__file__), "../archivos")

    def test_archivo_correcto(self):
        ruta = os.path.join(self.ruta_base, "correcto.csv")
        control = ControlInscripcion()
        control.leer_archivo(ruta)

        self.assertEqual(len(control.estudiantes), 5)
        self.assertEqual(len(control.inscripciones), 5)

    def test_columnas_desordenadas(self):
        ruta = os.path.join(self.ruta_base, "columnas_desordenadas.csv")
        control = ControlInscripcion()

        with self.assertRaises(ValueError):
            control.leer_archivo(ruta)

    def test_archivo_json(self):
        ruta = os.path.join(self.ruta_base, "archivo.json")
        control = ControlInscripcion()

        with self.assertRaises(Exception):  # Puede ser csv.Error u otra
            control.leer_archivo(ruta)

    def test_archivo_vacio(self):
        ruta = os.path.join(self.ruta_base, "vacio.csv")
        control = ControlInscripcion()

        control.leer_archivo(ruta)
        self.assertEqual(len(control.estudiantes), 0)
        self.assertEqual(len(control.inscripciones), 0)

    def test_linea_invalida(self):
        ruta = os.path.join(self.ruta_base, "linea_invalida.csv")
        control = ControlInscripcion()

        with self.assertRaises(ValueError):
            control.leer_archivo(ruta)

    def test_lineas_duplicadas(self):
        ruta = os.path.join(self.ruta_base, "duplicadas.csv")
        control = ControlInscripcion()

        control.leer_archivo(ruta)
        self.assertEqual(len(control.estudiantes), 1)
        self.assertEqual(len(control.inscripciones), 2)

    def test_campos_vacios(self):
        ruta = os.path.join(self.ruta_base, "campos_vacios.csv")
        control = ControlInscripcion()

        with self.assertRaises(ValueError):
            control.leer_archivo(ruta)

    def test_estudiante_con_dos_materias(self):
        ruta = os.path.join(self.ruta_base, "dos_materias.csv")
        control = ControlInscripcion()

        control.leer_archivo(ruta)
        self.assertEqual(len(control.estudiantes), 2)
        self.assertEqual(len(control.inscripciones), 3)

if __name__ == '__main__':
    unittest.main()

