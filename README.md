# proceso

comando para ejecutar pruebas: 
python -m unittest discover -s test


comando para ejecutar pruebas individuales: 
// para las de test_leer_archivo //
python -m unittest test.test_leer_archivo.TestLeerArchivo.test_archivo_correcto

// para las de  test_calcular_materias_por_estudiante //
python -m unittest test.test_calcular_materias_por_estudiante.TestControlInscripcion.test_tres_estudiantes_con_materias_diferentes

