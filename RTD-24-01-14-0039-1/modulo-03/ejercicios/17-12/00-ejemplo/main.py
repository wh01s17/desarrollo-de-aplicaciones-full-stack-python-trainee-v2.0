"""
✅ Ejercicio 2: Analizador de Notas con Estadísticas

Escribe un programa que permita ingresar las notas de estudiantes y luego calcular estadísticas.
Crear una función ingresar_notas() que:
Pida notas entre 1.0 y 7.0 hasta que el usuario escriba "fin".
Devuelva la lista de notas.
Crear una función calcular_estadisticas(notas) que retorne un diccionario con:
Promedio
Nota mínima
Nota máxima
Cantidad de notas sobre 5.0
Crear una función mostrar_estadisticas(info) que imprima los resultados de manera ordenada.
El programa principal debe ejecutar estas funciones.
"""
import ingreso_datos
from calculos import calcular_estadisticas


notas = []

while True:

    opcion = input('Escribe fin si deseras salir o enter para continuar: ')

    if opcion == 'fin':
        break
    
    ingreso_datos.ingreso_notas(notas)


reporte = calcular_estadisticas(notas)

print(f"""
Promedio: {reporte['promedio']}
Nota mínima: {reporte['n_min']}
Nota máxima: {reporte['n_max']}
Cantidad de notas sobre 5.0: {reporte['sobre_5']}
""")






