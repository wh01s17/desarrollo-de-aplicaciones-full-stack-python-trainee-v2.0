import registros


def menu():
    print("""
1. Registrar paciente
2. Registrar atención
3. Ver pacientes registrados
4. Ver resumen de atenciones
5. Salir""")


def pacientes_registrados(pacientes: dict):
    for k, v in pacientes.items():
        print(f"""
---------------------------
rut pacinte: {k}
Nombra pacinte: {v["nombre"]}
--------------------------""")


def resumen_atenciones(atenciones: dict):
    print(f"""
- Total de atenciones registradas: {len(atenciones)}
- Monto total recaudado: {sum([int(atencion["costo_atencion"]) for atencion in atenciones])}
- Total recaudado por tipo de atención: {registros.total_por_atencion(atenciones)} """)
