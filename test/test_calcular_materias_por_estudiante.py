import unittest
from control_inscripcion import ControlInscripcion
from io import StringIO
from unittest.mock import patch
import tempfile
import os


class TestControlInscripcion(unittest.TestCase):

    def crear_archivo_temporal(self, contenido):
        temp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', newline='')
        temp.write(contenido)
        temp.close()
        return temp.name

    def eliminar_archivo(self, ruta):
        if os.path.exists(ruta):
            os.remove(ruta)

    def test_tres_estudiantes_con_materias_diferentes(self):
        contenido = """1234567,Lulú López,1040,Cálculo
        9876534,Pepito Pérez,1050,Física
        4567766,Calvin Clein,1060,Administración"""
        ruta = self.crear_archivo_temporal(contenido)
        
        control = ControlInscripcion()
        control.leer_archivo(ruta)

        with patch('sys.stdout', new_callable=StringIO) as salida:
            control.calcular_materias_por_estudiante()
            resultado = salida.getvalue().strip().split("\n")
            self.assertIn("Lulú López: 1 materias", resultado)
            self.assertIn("Pepito Pérez: 1 materias", resultado)
            self.assertIn("Calvin Clein: 1 materias", resultado)

        self.eliminar_archivo(ruta)

    def test_archivo_vacio(self):
        ruta = self.crear_archivo_temporal("")
        control = ControlInscripcion()
        control.leer_archivo(ruta)

        with patch('sys.stdout', new_callable=StringIO) as salida:
            control.calcular_materias_por_estudiante()
            self.assertEqual(salida.getvalue().strip(), "")

        self.eliminar_archivo(ruta)

    def test_un_estudiante_con_dos_materias(self):
        contenido = """1234567,Lulú López,1040,Cálculo
        9876534,Pepito Pérez,1050,Física
        1234567,Lulú López,1060,Administración"""
        ruta = self.crear_archivo_temporal(contenido)

        control = ControlInscripcion()
        control.leer_archivo(ruta)

        with patch('sys.stdout', new_callable=StringIO) as salida:
            control.calcular_materias_por_estudiante()
            resultado = salida.getvalue().strip().split("\n")
            self.assertIn("Lulú López: 2 materias", resultado)
            self.assertIn("Pepito Pérez: 1 materias", resultado)

        self.eliminar_archivo(ruta)

    def test_dos_estudiantes_mismo_nombre_diferente_cedula(self):
        contenido = """1234567,Alex Martínez,1040,Cálculo
        9876534,Alex Martínez,1050,Física"""
        ruta = self.crear_archivo_temporal(contenido)

        control = ControlInscripcion()
        control.leer_archivo(ruta)

        with patch('sys.stdout', new_callable=StringIO) as salida:
            control.calcular_materias_por_estudiante()
            resultado = salida.getvalue().strip().split("\n")
            self.assertEqual(sorted(resultado), sorted([
                "Alex Martínez: 1 materias",
                "Alex Martínez: 1 materias"
            ]))

        self.eliminar_archivo(ruta)

if __name__ == '__main__':
    unittest.main()
