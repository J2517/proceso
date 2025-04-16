from control_inscripcion import ControlInscripcion

if __name__ == "__main__":
    ruta = input("Ingrese la ruta del archivo CSV: ")
    control = ControlInscripcion()
    control.leer_archivo(ruta)
    control.calcular_materias_por_estudiante()
