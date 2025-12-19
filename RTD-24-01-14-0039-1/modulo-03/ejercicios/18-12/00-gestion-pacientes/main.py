"""
Ejercicio 1: Sistema de Gestión de Pacientes y Atenciones
Contexto:
Un centro de salud comunitario necesita un sistema simple en consola para registrar pacientes y llevar el control de sus atenciones.
Cada paciente se identifica mediante su RUT.

Objetivo:
Desarrollar una aplicación en Python que permita registrar pacientes, validar su RUT, ingresar atenciones y
visualizar un resumen general.

Requerimientos funcionales:
1. El sistema debe mostrar el siguiente menú:
   1. Registrar paciente
   2. Registrar atención
   3. Ver pacientes registrados
   4. Ver resumen de atenciones
   5. Salir

2. Registrar paciente:
- Solicitar nombre completo
- Solicitar RUT (formato 12345678-9)
- Validar que el RUT tenga formato correcto (no es obligatorio validar dígito verificador)
- No permitir RUT duplicados
- Guardar pacientes en un diccionario usando el RUT como clave

3. Registrar atención:
- Solicitar RUT del paciente
- Validar que el paciente exista
- Solicitar tipo de atención (ej: kinesiología, medicina, enfermería)
- Solicitar costo de la atención (número positivo)
- Guardar las atenciones en una lista de diccionarios

4. Resumen de atenciones:
- Total de atenciones registradas
- Monto total recaudado
- Total recaudado por tipo de atención


Desafío adicional (opcional):
- Mostrar el paciente con mayor gasto acumulado

"""

import mensajes
import registros


pacientes = {}
atenciones = []

while True:
    mensajes.menu()
    opcion = input(">>> ")

    if opcion == "1":
        registros.registrar_paciente(pacientes)

    elif opcion == "2":
        registros.registrar_atencion(atenciones, pacientes)

    elif opcion == "3":
        mensajes.pacientes_registrados(pacientes)

    elif opcion == "4":
        mensajes.resumen_atenciones(atenciones)

    elif opcion == "5":
        break

    else:
        print("Ingresa una opcion correcta!!!")
